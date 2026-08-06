# Modelo de amenazas del Open Finance Sandbox

Amenazas ordenadas por **impacto × probabilidad**, no por sofisticación técnica.
Es la regla de la Parte 17, clase 14: «token registrado en el log» debe ir por
encima de «ataque criptográfico al algoritmo de firma», y esa ordenación es la
correcta.

## Escala

| Impacto | Significado | Probabilidad | Significado |
|---:|---|---:|---|
| 1 | Molestia | 1 | Requiere un atacante muy capaz |
| 3 | Pérdida de datos | 3 | Requiere una condición previa |
| 4 | Pérdida de datos sensibles | 4 | Ocurre con una configuración descuidada |
| 5 | Pérdida patrimonial o suplantación | 5 | Ocurre por un error de configuración común |

## Amenazas

| # | Amenaza | I | P | Pri | Control implementado | Prueba |
|---:|---|---:|---:|---:|---|---|
| 1 | Token de acceso escrito en el registro | 5 | 5 | 25 | `_log` nunca recibe el token | `test_el_registro_no_contiene_tokens` |
| 2 | `redirect_uri` validada por prefijo | 5 | 4 | 20 | Coincidencia exacta contra el conjunto registrado | `test_redirect_uri_por_prefijo_no_pasa` |
| 3 | Reintento sin idempotencia duplica el pago | 4 | 5 | 20 | Clave obligatoria, huella canónica y bloqueo | `test_cinco_reintentos_no_duplican_el_pago` |
| 4 | Revocación que no invalida los tokens vivos | 4 | 4 | 16 | `on_revoke` invalida antes de responder | `test_revocar_invalida_los_tokens_vivos` |
| 5 | Enumeración de cuentas por diferencia de error | 4 | 4 | 16 | Respuesta idéntica para ajena e inexistente | `test_no_se_pueden_enumerar_cuentas` |
| 6 | Robo del código de autorización sin PKCE | 5 | 3 | 15 | PKCE con S256 obligatorio; `plain` rechazado | `test_authorize_sin_pkce_falla` |
| 7 | Fuga de saldo por bisección de confirmación de fondos | 4 | 3 | 12 | Límite por consentimiento y detección de patrón | `test_confirmacion_de_fondos_corta_la_biseccion` |
| 8 | Escalada de alcance: solicitado tratado como concedido | 4 | 3 | 12 | El token se emite sobre lo concedido | `test_token_acotado_al_alcance_concedido` |
| 9 | Repetición del código de autorización | 4 | 3 | 12 | Un solo uso y vida menor a 60 s | `test_codigo_de_un_solo_uso` |
| 10 | Alcance concedido que nunca se presentó al cliente | 3 | 3 | 9 | `presented_scopes` separado de `scopes` | `test_no_se_concede_un_alcance_que_no_se_presento` |
| 11 | Entrega de mercancía en «aceptado» | 4 | 2 | 8 | `is_firm` separado de `is_final` | `test_aceptado_no_es_firme` |
| 12 | Extracción masiva por página sin límite | 3 | 2 | 6 | `MAX_LIMIT` aplicado en el servidor | `test_limite_de_pagina_acotado` |
| 13 | Cursor manipulado provoca error del servidor | 2 | 3 | 6 | Se traduce a `invalid_request`, nunca a 500 | `test_cursor_invalido_da_400_no_500` |
| 14 | Dato de tercero almacenado por el agregador | 4 | 1 | 4 | Descarte en la ingesta, no en la presentación | `test_la_ingesta_descarta_los_datos_de_contraparte` |
| 15 | Error de redondeo por coma flotante | 3 | 1 | 3 | Importe como cadena decimal | `test_importes_son_cadena_decimal` |
| 16 | Transición ilegal en la máquina de estados | 3 | 1 | 3 | Tabla de transiciones cerrada | `test_transicion_ilegal_de_consentimiento` |

## Amenazas fuera de alcance del entorno

Se enumeran porque **no declararlas se leería como cobertura completa**, y esa
lectura es la que produce incidentes.

| Amenaza | Por qué queda fuera | Dónde se trata |
|---|---|---|
| Intercepción del canal | El entorno no implementa TLS | Clase 7 |
| Certificado de participante falsificado | No hay autoridad certificadora | Clase 7 |
| Participante suspendido con certificado válido | No hay directorio en tiempo real | Clase 2 |
| Denegación de servicio distribuida | No hay capa de red | Clase 13 |
| Compromiso del proveedor tecnológico | No existe esa figura en el entorno | Clases 2 y 13 |
| Manipulación del cliente por ingeniería social | Ningún control técnico la resuelve | Clase 11 |

## Cómo se mantiene

Cada amenaza nueva entra con su puntuación y su prueba. Una amenaza sin prueba
asociada es una intención, no un control: si nadie la ejecuta, nadie sabe si el
control sigue funcionando tras el siguiente cambio.

```bash
python -m pytest tests/test_open_finance_sandbox.py -q
python apps/open_finance_sandbox/conformance_tests/run.py
```
