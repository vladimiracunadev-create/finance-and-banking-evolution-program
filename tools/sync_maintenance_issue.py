"""Mantiene un unico issue abierto por cada monitor de mantenimiento.

Los workflows programados llaman a este script con el resultado de su
comprobacion. Si hay un problema, crea o actualiza un issue y cierra duplicados;
si el problema desaparecio, cierra todos los issues abiertos con ese titulo.

Requiere ``GITHUB_TOKEN`` y ``GITHUB_REPOSITORY`` en el entorno.
"""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
from typing import Any, Callable
from urllib.error import HTTPError
from urllib.parse import urlencode, urlparse
from urllib.request import Request, urlopen


JsonRequest = Callable[[str, str, dict[str, Any] | None], Any]


def github_request(method: str, url: str, payload: dict[str, Any] | None = None) -> Any:
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        raise RuntimeError("Falta GITHUB_TOKEN")
    parsed_url = urlparse(url)
    if parsed_url.scheme != "https" or parsed_url.hostname != "api.github.com":
        raise RuntimeError("La API de issues solo admite https://api.github.com")
    data = None if payload is None else json.dumps(payload).encode("utf-8")
    request = Request(
        url,
        data=data,
        method=method,
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "X-GitHub-Api-Version": "2022-11-28",
        },
    )
    try:
        # El esquema y el host se validan antes de construir la solicitud.
        with urlopen(request, timeout=30) as response:  # nosec B310
            content = response.read()
    except HTTPError as error:
        detail = error.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"GitHub API devolvio {error.code}: {detail}") from error
    return json.loads(content) if content else None


def matching_issues(issues: list[dict[str, Any]], title: str) -> list[dict[str, Any]]:
    return sorted(
        (
            issue
            for issue in issues
            if issue.get("title") == title and "pull_request" not in issue
        ),
        key=lambda issue: int(issue["number"]),
    )


def sync_issue(
    *,
    repository: str,
    title: str,
    body: str,
    active: bool,
    labels: list[str],
    request: JsonRequest = github_request,
    api_url: str = "https://api.github.com",
) -> dict[str, Any]:
    base = f"{api_url.rstrip('/')}/repos/{repository}"
    query = urlencode({"state": "open", "per_page": 100})
    open_issues = matching_issues(request("GET", f"{base}/issues?{query}", None), title)

    if not active:
        for issue in open_issues:
            request(
                "PATCH",
                f"{base}/issues/{issue['number']}",
                {"state": "closed", "state_reason": "completed"},
            )
        return {"action": "closed", "issues": [issue["number"] for issue in open_issues]}

    if open_issues:
        primary = open_issues[0]
        request(
            "PATCH",
            f"{base}/issues/{primary['number']}",
            {"body": body, "labels": labels},
        )
        duplicates = open_issues[1:]
        for issue in duplicates:
            request(
                "PATCH",
                f"{base}/issues/{issue['number']}",
                {"state": "closed", "state_reason": "duplicate"},
            )
        return {
            "action": "updated",
            "issue": primary["number"],
            "duplicates_closed": [issue["number"] for issue in duplicates],
        }

    created = request(
        "POST",
        f"{base}/issues",
        {"title": title, "body": body, "labels": labels},
    )
    return {"action": "created", "issue": created["number"]}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--title", required=True)
    parser.add_argument("--body-file", type=Path, required=True)
    parser.add_argument(
        "--active-count",
        type=int,
        required=True,
        help="Cantidad de fallos; cero cierra el issue y un valor positivo lo mantiene.",
    )
    parser.add_argument("--label", action="append", default=[])
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repository = os.environ.get("GITHUB_REPOSITORY")
    if not repository:
        raise RuntimeError("Falta GITHUB_REPOSITORY")
    body = args.body_file.read_text(encoding="utf-8")
    result = sync_issue(
        repository=repository,
        title=args.title,
        body=body,
        active=args.active_count > 0,
        labels=args.label,
    )
    print(json.dumps(result, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
