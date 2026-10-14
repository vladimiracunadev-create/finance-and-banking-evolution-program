from pathlib import Path
import sys

import pytest

sys.path.insert(0, str(Path(__file__).parents[1] / "tools"))

from sync_maintenance_issue import github_request, matching_issues, sync_issue


def test_matching_issues_excludes_pull_requests_and_sorts_by_number():
    issues = [
        {"number": 9, "title": "Monitor"},
        {"number": 3, "title": "Monitor"},
        {"number": 2, "title": "Otro"},
        {"number": 1, "title": "Monitor", "pull_request": {}},
    ]

    assert [issue["number"] for issue in matching_issues(issues, "Monitor")] == [3, 9]


def test_github_request_rejects_untrusted_hosts(monkeypatch):
    monkeypatch.setenv("GITHUB_TOKEN", "token-de-prueba")

    with pytest.raises(RuntimeError, match="api.github.com"):
        github_request("GET", "https://example.com/issues")


def test_active_monitor_updates_oldest_issue_and_closes_duplicates():
    calls = []

    def request(method, url, payload):
        calls.append((method, url, payload))
        if method == "GET":
            return [
                {"number": 8, "title": "Monitor"},
                {"number": 4, "title": "Monitor"},
            ]
        return {"number": 4}

    result = sync_issue(
        repository="owner/repo",
        title="Monitor",
        body="informe",
        active=True,
        labels=["mantenimiento"],
        request=request,
    )

    assert result == {"action": "updated", "issue": 4, "duplicates_closed": [8]}
    assert calls[1][2] == {"body": "informe", "labels": ["mantenimiento"]}
    assert calls[2][2] == {"state": "closed", "state_reason": "duplicate"}


def test_clean_monitor_closes_every_matching_issue():
    calls = []

    def request(method, url, payload):
        calls.append((method, url, payload))
        if method == "GET":
            return [{"number": 4, "title": "Monitor"}]
        return {"number": 4}

    result = sync_issue(
        repository="owner/repo",
        title="Monitor",
        body="sin fallos",
        active=False,
        labels=[],
        request=request,
    )

    assert result == {"action": "closed", "issues": [4]}
    assert calls[1][2] == {"state": "closed", "state_reason": "completed"}


def test_active_monitor_creates_issue_when_none_exists():
    calls = []

    def request(method, url, payload):
        calls.append((method, url, payload))
        if method == "GET":
            return []
        return {"number": 12}

    result = sync_issue(
        repository="owner/repo",
        title="Monitor",
        body="informe",
        active=True,
        labels=["mantenimiento", "documentacion"],
        request=request,
    )

    assert result == {"action": "created", "issue": 12}
    assert calls[1][2] == {
        "title": "Monitor",
        "body": "informe",
        "labels": ["mantenimiento", "documentacion"],
    }
