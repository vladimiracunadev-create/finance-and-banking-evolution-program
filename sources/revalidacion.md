# Revalidación de fuentes

Última ejecución de `scripts/refresh_sources.py`: **2026-08-20**.

Este informe lo escribe la capa de red y **no se comprueba en CI**. Un enlace
que hoy responde puede no responder mañana, y esa es exactamente la razón de
que la revalidación viva fuera de la puerta de calidad: el programa se entera
del cambio sin quedarse bloqueado por él.

## Clases con contenido normativo

Estas son las clases que declaran fecha de verificación regulatoria. Para cada una
se consultaron todos los enlaces oficiales que cita. **La fecha avanza solo cuando
todos respondieron**: si uno falló, la clase conserva la fecha anterior, porque
mover la fecha sin haber comprobado la fuente sería justo lo que aquí se evita.

| Clase | Enlaces citados | Comprobados | Fecha de verificación | Resultado |
|---|---:|---:|:---:|---|
| [01-banca-abierta-finanzas-abiertas-y-datos-abiertos.md](../modules/16-finanzas-abiertas-apis-y-economia-de-datos/classes/01-banca-abierta-finanzas-abiertas-y-datos-abiertos.md) | 5 | 5 | 2026-08-20 | ✅ revalidada |
| [02-ecosistema-participantes-y-modelos-de-implantacion.md](../modules/16-finanzas-abiertas-apis-y-economia-de-datos/classes/02-ecosistema-participantes-y-modelos-de-implantacion.md) | 5 | 5 | 2026-08-20 | ✅ revalidada |
| [03-sistema-de-finanzas-abiertas-de-chile.md](../modules/16-finanzas-abiertas-apis-y-economia-de-datos/classes/03-sistema-de-finanzas-abiertas-de-chile.md) | 5 | 5 | 2026-08-20 | ✅ revalidada |
| [04-clasificacion-calidad-y-gobierno-de-datos.md](../modules/16-finanzas-abiertas-apis-y-economia-de-datos/classes/04-clasificacion-calidad-y-gobierno-de-datos.md) | 5 | 4 | 2026-08-06 | ⚠️ 1 enlace(s) sin resolver |
| [05-consentimiento-ciclo-de-vida.md](../modules/16-finanzas-abiertas-apis-y-economia-de-datos/classes/05-consentimiento-ciclo-de-vida.md) | 5 | 5 | 2026-08-20 | ✅ revalidada |
| [06-oauth-openid-connect-y-autorizacion.md](../modules/16-finanzas-abiertas-apis-y-economia-de-datos/classes/06-oauth-openid-connect-y-autorizacion.md) | 5 | 5 | 2026-08-20 | ✅ revalidada |
| [07-financial-grade-apis-y-firma.md](../modules/16-finanzas-abiertas-apis-y-economia-de-datos/classes/07-financial-grade-apis-y-firma.md) | 5 | 5 | 2026-08-20 | ✅ revalidada |
| [08-diseno-versionado-e-idempotencia.md](../modules/16-finanzas-abiertas-apis-y-economia-de-datos/classes/08-diseno-versionado-e-idempotencia.md) | 5 | 5 | 2026-08-20 | ✅ revalidada |
| [09-apis-de-informacion-financiera.md](../modules/16-finanzas-abiertas-apis-y-economia-de-datos/classes/09-apis-de-informacion-financiera.md) | 5 | 4 | 2026-08-06 | ⚠️ 1 enlace(s) sin resolver |
| [10-iniciacion-de-pagos-y-confirmacion-de-fondos.md](../modules/16-finanzas-abiertas-apis-y-economia-de-datos/classes/10-iniciacion-de-pagos-y-confirmacion-de-fondos.md) | 5 | 5 | 2026-08-20 | ✅ revalidada |
| [11-autenticacion-reforzada-fraude-y-responsabilidad.md](../modules/16-finanzas-abiertas-apis-y-economia-de-datos/classes/11-autenticacion-reforzada-fraude-y-responsabilidad.md) | 5 | 4 | 2026-08-06 | ⚠️ 1 enlace(s) sin resolver |
| [12-privacidad-finalidad-y-portabilidad.md](../modules/16-finanzas-abiertas-apis-y-economia-de-datos/classes/12-privacidad-finalidad-y-portabilidad.md) | 5 | 4 | 2026-08-06 | ⚠️ 1 enlace(s) sin resolver |
| [13-disponibilidad-sla-y-observabilidad.md](../modules/16-finanzas-abiertas-apis-y-economia-de-datos/classes/13-disponibilidad-sla-y-observabilidad.md) | 5 | 5 | 2026-08-20 | ✅ revalidada |
| [14-proyecto-agregador-financiero-regulado.md](../modules/16-finanzas-abiertas-apis-y-economia-de-datos/classes/14-proyecto-agregador-financiero-regulado.md) | 5 | 5 | 2026-08-20 | ✅ revalidada |
| [01-que-es-un-pago-transfronterizo.md](../modules/17-pagos-transfronterizos-remesas-y-liquidacion/classes/01-que-es-un-pago-transfronterizo.md) | 5 | 4 | 2026-08-06 | ⚠️ 1 enlace(s) sin resolver |
| [02-arquitectura-de-participantes.md](../modules/17-pagos-transfronterizos-remesas-y-liquidacion/classes/02-arquitectura-de-participantes.md) | 5 | 5 | 2026-08-20 | ✅ revalidada |
| [03-corresponsalia-bancaria.md](../modules/17-pagos-transfronterizos-remesas-y-liquidacion/classes/03-corresponsalia-bancaria.md) | 5 | 5 | 2026-08-20 | ✅ revalidada |
| [04-cuentas-nostro-vostro-y-loro.md](../modules/17-pagos-transfronterizos-remesas-y-liquidacion/classes/04-cuentas-nostro-vostro-y-loro.md) | 5 | 4 | 2026-08-06 | ⚠️ 1 enlace(s) sin resolver |
| [05-mensajeria-frente-a-movimiento-de-fondos.md](../modules/17-pagos-transfronterizos-remesas-y-liquidacion/classes/05-mensajeria-frente-a-movimiento-de-fondos.md) | 5 | 4 | 2026-08-06 | ⚠️ 1 enlace(s) sin resolver |
| [06-swift-cbpr-e-iso-20022.md](../modules/17-pagos-transfronterizos-remesas-y-liquidacion/classes/06-swift-cbpr-e-iso-20022.md) | 5 | 2 | 2026-08-06 | ⚠️ 3 enlace(s) sin resolver |
| [07-compensacion-liquidacion-y-finalidad.md](../modules/17-pagos-transfronterizos-remesas-y-liquidacion/classes/07-compensacion-liquidacion-y-finalidad.md) | 5 | 5 | 2026-08-20 | ✅ revalidada |
| [08-liquidez-prefinanciacion-y-netting.md](../modules/17-pagos-transfronterizos-remesas-y-liquidacion/classes/08-liquidez-prefinanciacion-y-netting.md) | 5 | 5 | 2026-08-20 | ✅ revalidada |
| [09-fx-dentro-de-un-pago-transfronterizo.md](../modules/17-pagos-transfronterizos-remesas-y-liquidacion/classes/09-fx-dentro-de-un-pago-transfronterizo.md) | 5 | 4 | 2026-08-06 | ⚠️ 1 enlace(s) sin resolver |
| [10-remesas-y-corredores-internacionales.md](../modules/17-pagos-transfronterizos-remesas-y-liquidacion/classes/10-remesas-y-corredores-internacionales.md) | 5 | 4 | 2026-08-06 | ⚠️ 1 enlace(s) sin resolver |
| [11-pagos-empresariales-y-comercio-exterior.md](../modules/17-pagos-transfronterizos-remesas-y-liquidacion/classes/11-pagos-empresariales-y-comercio-exterior.md) | 5 | 5 | 2026-08-20 | ✅ revalidada |
| [12-aml-sanciones-y-regla-del-viaje.md](../modules/17-pagos-transfronterizos-remesas-y-liquidacion/classes/12-aml-sanciones-y-regla-del-viaje.md) | 5 | 5 | 2026-08-20 | ✅ revalidada |
| [13-interconexion-de-pagos-inmediatos.md](../modules/17-pagos-transfronterizos-remesas-y-liquidacion/classes/13-interconexion-de-pagos-inmediatos.md) | 5 | 5 | 2026-08-20 | ✅ revalidada |
| [14-stablecoins-y-pagos-internacionales.md](../modules/17-pagos-transfronterizos-remesas-y-liquidacion/classes/14-stablecoins-y-pagos-internacionales.md) | 5 | 5 | 2026-08-20 | ✅ revalidada |
| [15-payment-versus-payment-y-liquidacion-atomica.md](../modules/17-pagos-transfronterizos-remesas-y-liquidacion/classes/15-payment-versus-payment-y-liquidacion-atomica.md) | 5 | 5 | 2026-08-20 | ✅ revalidada |
| [16-proyecto-red-de-pagos-transfronterizos.md](../modules/17-pagos-transfronterizos-remesas-y-liquidacion/classes/16-proyecto-red-de-pagos-transfronterizos.md) | 5 | 4 | 2026-08-06 | ⚠️ 1 enlace(s) sin resolver |
| [01-sistemas-distribuidos-aplicados-a-finanzas.md](../modules/18-blockchain-y-dlt-para-instituciones-financieras/classes/01-sistemas-distribuidos-aplicados-a-finanzas.md) | 4 | 2 | 2026-08-06 | ⚠️ 2 enlace(s) sin resolver |
| [02-resumenes-firmas-y-arboles-de-merkle.md](../modules/18-blockchain-y-dlt-para-instituciones-financieras/classes/02-resumenes-firmas-y-arboles-de-merkle.md) | 4 | 4 | 2026-08-20 | ✅ revalidada |
| [03-claves-direcciones-y-gestion-criptografica.md](../modules/18-blockchain-y-dlt-para-instituciones-financieras/classes/03-claves-direcciones-y-gestion-criptografica.md) | 5 | 5 | 2026-08-20 | ✅ revalidada |
| [04-transacciones-bloques-nodos-y-estado.md](../modules/18-blockchain-y-dlt-para-instituciones-financieras/classes/04-transacciones-bloques-nodos-y-estado.md) | 5 | 5 | 2026-08-20 | ✅ revalidada |
| [05-mecanismos-de-consenso.md](../modules/18-blockchain-y-dlt-para-instituciones-financieras/classes/05-mecanismos-de-consenso.md) | 5 | 3 | 2026-08-06 | ⚠️ 2 enlace(s) sin resolver |
| [06-finalidad-reorganizaciones-y-tolerancia-a-fallos.md](../modules/18-blockchain-y-dlt-para-instituciones-financieras/classes/06-finalidad-reorganizaciones-y-tolerancia-a-fallos.md) | 5 | 5 | 2026-08-20 | ✅ revalidada |
| [07-redes-publicas-privadas-y-autorizadas.md](../modules/18-blockchain-y-dlt-para-instituciones-financieras/classes/07-redes-publicas-privadas-y-autorizadas.md) | 5 | 5 | 2026-08-20 | ✅ revalidada |
| [08-contratos-inteligentes.md](../modules/18-blockchain-y-dlt-para-instituciones-financieras/classes/08-contratos-inteligentes.md) | 5 | 5 | 2026-08-20 | ✅ revalidada |
| [09-oraculos.md](../modules/18-blockchain-y-dlt-para-instituciones-financieras/classes/09-oraculos.md) | 5 | 5 | 2026-08-20 | ✅ revalidada |
| [10-privacidad-y-pruebas-criptograficas.md](../modules/18-blockchain-y-dlt-para-instituciones-financieras/classes/10-privacidad-y-pruebas-criptograficas.md) | 5 | 5 | 2026-08-20 | ✅ revalidada |
| [11-interoperabilidad-y-puentes.md](../modules/18-blockchain-y-dlt-para-instituciones-financieras/classes/11-interoperabilidad-y-puentes.md) | 5 | 5 | 2026-08-20 | ✅ revalidada |
| [12-escalabilidad-capas-y-disponibilidad.md](../modules/18-blockchain-y-dlt-para-instituciones-financieras/classes/12-escalabilidad-capas-y-disponibilidad.md) | 5 | 5 | 2026-08-20 | ✅ revalidada |
| [13-gobernanza-bifurcaciones-y-recuperacion.md](../modules/18-blockchain-y-dlt-para-instituciones-financieras/classes/13-gobernanza-bifurcaciones-y-recuperacion.md) | 5 | 5 | 2026-08-20 | ✅ revalidada |
| [14-proyecto-red-financiera-autorizada.md](../modules/18-blockchain-y-dlt-para-instituciones-financieras/classes/14-proyecto-red-financiera-autorizada.md) | 5 | 5 | 2026-08-20 | ✅ revalidada |
| [01-taxonomia-de-los-activos-digitales.md](../modules/19-activos-digitales-stablecoins-y-dinero-programable/classes/01-taxonomia-de-los-activos-digitales.md) | 5 | 5 | 2026-08-20 | ✅ revalidada |
| [02-criptoactivos-no-respaldados.md](../modules/19-activos-digitales-stablecoins-y-dinero-programable/classes/02-criptoactivos-no-respaldados.md) | 4 | 4 | 2026-08-20 | ✅ revalidada |
| [03-stablecoins-tipologias-y-mecanica-de-la-paridad.md](../modules/19-activos-digitales-stablecoins-y-dinero-programable/classes/03-stablecoins-tipologias-y-mecanica-de-la-paridad.md) | 4 | 4 | 2026-08-20 | ✅ revalidada |
| [04-reservas-composicion-calidad-y-verificacion.md](../modules/19-activos-digitales-stablecoins-y-dinero-programable/classes/04-reservas-composicion-calidad-y-verificacion.md) | 5 | 5 | 2026-08-20 | ✅ revalidada |
| [05-redencion-el-derecho-el-proceso-y-la-cola.md](../modules/19-activos-digitales-stablecoins-y-dinero-programable/classes/05-redencion-el-derecho-el-proceso-y-la-cola.md) | 4 | 4 | 2026-08-20 | ✅ revalidada |
| [06-perdida-de-paridad-anatomia-de-una-corrida.md](../modules/19-activos-digitales-stablecoins-y-dinero-programable/classes/06-perdida-de-paridad-anatomia-de-una-corrida.md) | 4 | 4 | 2026-08-20 | ✅ revalidada |
| [07-stablecoins-algoritmicas-y-su-modo-de-fallo.md](../modules/19-activos-digitales-stablecoins-y-dinero-programable/classes/07-stablecoins-algoritmicas-y-su-modo-de-fallo.md) | 4 | 4 | 2026-08-20 | ✅ revalidada |
| [08-depositos-tokenizados-y-dinero-de-banco-comercial.md](../modules/19-activos-digitales-stablecoins-y-dinero-programable/classes/08-depositos-tokenizados-y-dinero-de-banco-comercial.md) | 4 | 4 | 2026-08-20 | ✅ revalidada |
| [09-dinero-electronico-el-regimen-que-ya-existia.md](../modules/19-activos-digitales-stablecoins-y-dinero-programable/classes/09-dinero-electronico-el-regimen-que-ya-existia.md) | 4 | 4 | 2026-08-20 | ✅ revalidada |
| [10-monedas-digitales-de-banco-central.md](../modules/19-activos-digitales-stablecoins-y-dinero-programable/classes/10-monedas-digitales-de-banco-central.md) | 4 | 4 | 2026-08-20 | ✅ revalidada |
| [11-dinero-programable-y-sus-limites.md](../modules/19-activos-digitales-stablecoins-y-dinero-programable/classes/11-dinero-programable-y-sus-limites.md) | 4 | 4 | 2026-08-20 | ✅ revalidada |
| [12-custodia-de-activos-digitales.md](../modules/19-activos-digitales-stablecoins-y-dinero-programable/classes/12-custodia-de-activos-digitales.md) | 4 | 4 | 2026-08-20 | ✅ revalidada |
| [13-mercado-liquidez-y-formacion-de-precio.md](../modules/19-activos-digitales-stablecoins-y-dinero-programable/classes/13-mercado-liquidez-y-formacion-de-precio.md) | 4 | 4 | 2026-08-20 | ✅ revalidada |
| [14-contagio-y-riesgo-sistemico.md](../modules/19-activos-digitales-stablecoins-y-dinero-programable/classes/14-contagio-y-riesgo-sistemico.md) | 4 | 4 | 2026-08-20 | ✅ revalidada |
| [15-contabilidad-tributacion-y-balance.md](../modules/19-activos-digitales-stablecoins-y-dinero-programable/classes/15-contabilidad-tributacion-y-balance.md) | 5 | 5 | 2026-08-20 | ✅ revalidada |
| [16-proyecto-evaluacion-de-un-activo-digital.md](../modules/19-activos-digitales-stablecoins-y-dinero-programable/classes/16-proyecto-evaluacion-de-un-activo-digital.md) | 5 | 5 | 2026-08-20 | ✅ revalidada |
| [01-que-es-y-que-no-es-tokenizar.md](../modules/20-tokenizacion-fx-onchain-y-mercados-programables/classes/01-que-es-y-que-no-es-tokenizar.md) | 4 | 4 | 2026-08-20 | ✅ revalidada |
| [02-el-registro-de-referencia.md](../modules/20-tokenizacion-fx-onchain-y-mercados-programables/classes/02-el-registro-de-referencia.md) | 4 | 4 | 2026-08-20 | ✅ revalidada |
| [03-derechos-economicos-y-politicos-del-tenedor.md](../modules/20-tokenizacion-fx-onchain-y-mercados-programables/classes/03-derechos-economicos-y-politicos-del-tenedor.md) | 4 | 3 | 2026-08-06 | ⚠️ 1 enlace(s) sin resolver |
| [04-emision-mercado-primario-tokenizado.md](../modules/20-tokenizacion-fx-onchain-y-mercados-programables/classes/04-emision-mercado-primario-tokenizado.md) | 4 | 4 | 2026-08-20 | ✅ revalidada |
| [05-ciclo-de-vida-del-instrumento.md](../modules/20-tokenizacion-fx-onchain-y-mercados-programables/classes/05-ciclo-de-vida-del-instrumento.md) | 4 | 3 | 2026-08-06 | ⚠️ 1 enlace(s) sin resolver |
| [06-mercado-secundario-y-liquidez-prometida.md](../modules/20-tokenizacion-fx-onchain-y-mercados-programables/classes/06-mercado-secundario-y-liquidez-prometida.md) | 4 | 4 | 2026-08-20 | ✅ revalidada |
| [07-fraccionamiento-y-acceso.md](../modules/20-tokenizacion-fx-onchain-y-mercados-programables/classes/07-fraccionamiento-y-acceso.md) | 4 | 4 | 2026-08-20 | ✅ revalidada |
| [08-entrega-contra-pago-atomica.md](../modules/20-tokenizacion-fx-onchain-y-mercados-programables/classes/08-entrega-contra-pago-atomica.md) | 4 | 4 | 2026-08-20 | ✅ revalidada |
| [09-custodia-de-valores-tokenizados.md](../modules/20-tokenizacion-fx-onchain-y-mercados-programables/classes/09-custodia-de-valores-tokenizados.md) | 4 | 4 | 2026-08-20 | ✅ revalidada |
| [10-el-tramo-de-dinero.md](../modules/20-tokenizacion-fx-onchain-y-mercados-programables/classes/10-el-tramo-de-dinero.md) | 4 | 4 | 2026-08-20 | ✅ revalidada |
| [11-fx-del-mercado-mayorista-al-registro.md](../modules/20-tokenizacion-fx-onchain-y-mercados-programables/classes/11-fx-del-mercado-mayorista-al-registro.md) | 4 | 4 | 2026-08-20 | ✅ revalidada |
| [12-pago-contra-pago-y-riesgo-de-liquidacion.md](../modules/20-tokenizacion-fx-onchain-y-mercados-programables/classes/12-pago-contra-pago-y-riesgo-de-liquidacion.md) | 4 | 4 | 2026-08-20 | ✅ revalidada |
| [13-creacion-de-mercado-automatizada.md](../modules/20-tokenizacion-fx-onchain-y-mercados-programables/classes/13-creacion-de-mercado-automatizada.md) | 4 | 4 | 2026-08-20 | ✅ revalidada |
| [14-colateral-y-garantias-tokenizadas.md](../modules/20-tokenizacion-fx-onchain-y-mercados-programables/classes/14-colateral-y-garantias-tokenizadas.md) | 4 | 4 | 2026-08-20 | ✅ revalidada |
| [15-interoperabilidad-entre-infraestructuras.md](../modules/20-tokenizacion-fx-onchain-y-mercados-programables/classes/15-interoperabilidad-entre-infraestructuras.md) | 4 | 4 | 2026-08-20 | ✅ revalidada |
| [16-proyecto-mercado-primario-y-secundario.md](../modules/20-tokenizacion-fx-onchain-y-mercados-programables/classes/16-proyecto-mercado-primario-y-secundario.md) | 5 | 5 | 2026-08-20 | ✅ revalidada |
| [01-el-perimetro-regulatorio.md](../modules/21-regulacion-de-mercados-financieros-digitales/classes/01-el-perimetro-regulatorio.md) | 5 | 5 | 2026-08-20 | ✅ revalidada |
| [02-misma-actividad-mismo-riesgo.md](../modules/21-regulacion-de-mercados-financieros-digitales/classes/02-misma-actividad-mismo-riesgo.md) | 4 | 4 | 2026-08-20 | ✅ revalidada |
| [03-calificacion-de-un-instrumento-digital.md](../modules/21-regulacion-de-mercados-financieros-digitales/classes/03-calificacion-de-un-instrumento-digital.md) | 5 | 5 | 2026-08-20 | ✅ revalidada |
| [04-autorizacion-registro-y-supervision.md](../modules/21-regulacion-de-mercados-financieros-digitales/classes/04-autorizacion-registro-y-supervision.md) | 5 | 5 | 2026-08-20 | ✅ revalidada |
| [05-regimen-de-emisores.md](../modules/21-regulacion-de-mercados-financieros-digitales/classes/05-regimen-de-emisores.md) | 4 | 4 | 2026-08-20 | ✅ revalidada |
| [06-proteccion-del-cliente-y-de-sus-fondos.md](../modules/21-regulacion-de-mercados-financieros-digitales/classes/06-proteccion-del-cliente-y-de-sus-fondos.md) | 4 | 4 | 2026-08-20 | ✅ revalidada |
| [07-moneda-digital-de-banco-central-marco.md](../modules/21-regulacion-de-mercados-financieros-digitales/classes/07-moneda-digital-de-banco-central-marco.md) | 4 | 4 | 2026-08-20 | ✅ revalidada |
| [08-tratamiento-prudencial-de-las-exposiciones.md](../modules/21-regulacion-de-mercados-financieros-digitales/classes/08-tratamiento-prudencial-de-las-exposiciones.md) | 4 | 4 | 2026-08-20 | ✅ revalidada |
| [09-custodia-y-segregacion-en-la-norma.md](../modules/21-regulacion-de-mercados-financieros-digitales/classes/09-custodia-y-segregacion-en-la-norma.md) | 4 | 4 | 2026-08-20 | ✅ revalidada |
| [10-infraestructuras-de-mercado-y-su-regimen.md](../modules/21-regulacion-de-mercados-financieros-digitales/classes/10-infraestructuras-de-mercado-y-su-regimen.md) | 4 | 4 | 2026-08-20 | ✅ revalidada |
| [11-conducta-de-mercado-e-integridad.md](../modules/21-regulacion-de-mercados-financieros-digitales/classes/11-conducta-de-mercado-e-integridad.md) | 4 | 4 | 2026-08-20 | ✅ revalidada |
| [12-prevencion-de-lavado-y-financiamiento.md](../modules/21-regulacion-de-mercados-financieros-digitales/classes/12-prevencion-de-lavado-y-financiamiento.md) | 4 | 3 | 2026-08-06 | ⚠️ 1 enlace(s) sin resolver |
| [13-proteccion-de-datos-y-economia-de-la-informacion.md](../modules/21-regulacion-de-mercados-financieros-digitales/classes/13-proteccion-de-datos-y-economia-de-la-informacion.md) | 4 | 4 | 2026-08-20 | ✅ revalidada |
| [14-resiliencia-operativa-y-terceros-criticos.md](../modules/21-regulacion-de-mercados-financieros-digitales/classes/14-resiliencia-operativa-y-terceros-criticos.md) | 4 | 4 | 2026-08-20 | ✅ revalidada |
| [15-estabilidad-financiera-y-vigilancia.md](../modules/21-regulacion-de-mercados-financieros-digitales/classes/15-estabilidad-financiera-y-vigilancia.md) | 4 | 4 | 2026-08-20 | ✅ revalidada |
| [16-regulacion-comparada-chile-y-el-mundo.md](../modules/21-regulacion-de-mercados-financieros-digitales/classes/16-regulacion-comparada-chile-y-el-mundo.md) | 5 | 5 | 2026-08-20 | ✅ revalidada |
| [17-mica-perimetro-activos-y-participantes.md](../modules/21-regulacion-de-mercados-financieros-digitales/classes/17-mica-perimetro-activos-y-participantes.md) | 4 | 4 | 2026-08-20 | ✅ revalidada |
| [18-mica-obligaciones-reservas-y-supervision.md](../modules/21-regulacion-de-mercados-financieros-digitales/classes/18-mica-obligaciones-reservas-y-supervision.md) | 4 | 4 | 2026-08-20 | ✅ revalidada |
| [19-regimenes-europeos-conexos.md](../modules/21-regulacion-de-mercados-financieros-digitales/classes/19-regimenes-europeos-conexos.md) | 4 | 3 | 2026-08-12 | ⚠️ 1 enlace(s) sin resolver |
| [20-el-salvador-bitcoin-chivo-y-activos-digitales.md](../modules/21-regulacion-de-mercados-financieros-digitales/classes/20-el-salvador-bitcoin-chivo-y-activos-digitales.md) | 4 | 2 | 2026-08-12 | ⚠️ 2 enlace(s) sin resolver |
| [21-espacios-de-prueba-y-regulacion-experimental.md](../modules/21-regulacion-de-mercados-financieros-digitales/classes/21-espacios-de-prueba-y-regulacion-experimental.md) | 4 | 4 | 2026-08-20 | ✅ revalidada |
| [22-proyecto-expediente-regulatorio.md](../modules/21-regulacion-de-mercados-financieros-digitales/classes/22-proyecto-expediente-regulatorio.md) | 4 | 4 | 2026-08-20 | ✅ revalidada |
| [01-alcance-y-modelo-de-negocio.md](../modules/22-proyecto-banco-digital-y-mercado-tokenizado/classes/01-alcance-y-modelo-de-negocio.md) | 4 | 4 | 2026-08-20 | ✅ revalidada |
| [02-construir-integrar-o-comprar.md](../modules/22-proyecto-banco-digital-y-mercado-tokenizado/classes/02-construir-integrar-o-comprar.md) | 4 | 4 | 2026-08-20 | ✅ revalidada |
| [03-perimetro-del-propio-proyecto.md](../modules/22-proyecto-banco-digital-y-mercado-tokenizado/classes/03-perimetro-del-propio-proyecto.md) | 4 | 4 | 2026-08-20 | ✅ revalidada |
| [04-decision-de-arquitectura-registro.md](../modules/22-proyecto-banco-digital-y-mercado-tokenizado/classes/04-decision-de-arquitectura-registro.md) | 4 | 4 | 2026-08-20 | ✅ revalidada |
| [05-decision-de-arquitectura-el-dinero.md](../modules/22-proyecto-banco-digital-y-mercado-tokenizado/classes/05-decision-de-arquitectura-el-dinero.md) | 4 | 4 | 2026-08-20 | ✅ revalidada |
| [06-decision-de-producto-que-se-ofrece.md](../modules/22-proyecto-banco-digital-y-mercado-tokenizado/classes/06-decision-de-producto-que-se-ofrece.md) | 4 | 4 | 2026-08-20 | ✅ revalidada |
| [07-el-registro-de-referencia-del-sistema.md](../modules/22-proyecto-banco-digital-y-mercado-tokenizado/classes/07-el-registro-de-referencia-del-sistema.md) | 4 | 4 | 2026-08-20 | ✅ revalidada |
| [08-interfaces-consentimiento-y-terceros.md](../modules/22-proyecto-banco-digital-y-mercado-tokenizado/classes/08-interfaces-consentimiento-y-terceros.md) | 4 | 4 | 2026-08-20 | ✅ revalidada |
| [09-custodia-y-gestion-de-claves.md](../modules/22-proyecto-banco-digital-y-mercado-tokenizado/classes/09-custodia-y-gestion-de-claves.md) | 4 | 4 | 2026-08-20 | ✅ revalidada |
| [10-liquidacion-y-sus-modos-de-fallo.md](../modules/22-proyecto-banco-digital-y-mercado-tokenizado/classes/10-liquidacion-y-sus-modos-de-fallo.md) | 4 | 4 | 2026-08-20 | ✅ revalidada |
| [11-pagos-y-conexion-con-el-exterior.md](../modules/22-proyecto-banco-digital-y-mercado-tokenizado/classes/11-pagos-y-conexion-con-el-exterior.md) | 4 | 4 | 2026-08-20 | ✅ revalidada |
| [12-ciclo-de-vida-y-operacion-diaria.md](../modules/22-proyecto-banco-digital-y-mercado-tokenizado/classes/12-ciclo-de-vida-y-operacion-diaria.md) | 4 | 4 | 2026-08-20 | ✅ revalidada |
| [13-expediente-regulatorio-del-sistema.md](../modules/22-proyecto-banco-digital-y-mercado-tokenizado/classes/13-expediente-regulatorio-del-sistema.md) | 4 | 4 | 2026-08-20 | ✅ revalidada |
| [14-modelo-de-amenazas-priorizado.md](../modules/22-proyecto-banco-digital-y-mercado-tokenizado/classes/14-modelo-de-amenazas-priorizado.md) | 4 | 4 | 2026-08-20 | ✅ revalidada |
| [15-escenario-de-tension-y-continuidad.md](../modules/22-proyecto-banco-digital-y-mercado-tokenizado/classes/15-escenario-de-tension-y-continuidad.md) | 4 | 4 | 2026-08-20 | ✅ revalidada |
| [16-resolucion-ordenada-y-salida.md](../modules/22-proyecto-banco-digital-y-mercado-tokenizado/classes/16-resolucion-ordenada-y-salida.md) | 4 | 4 | 2026-08-20 | ✅ revalidada |
| [17-lo-que-el-sistema-no-puede-hacer.md](../modules/22-proyecto-banco-digital-y-mercado-tokenizado/classes/17-lo-que-el-sistema-no-puede-hacer.md) | 4 | 4 | 2026-08-20 | ✅ revalidada |
| [18-defensa-ante-el-comite.md](../modules/22-proyecto-banco-digital-y-mercado-tokenizado/classes/18-defensa-ante-el-comite.md) | 4 | 4 | 2026-08-20 | ✅ revalidada |

## Enlaces que no resolvieron

Ninguno de estos se ha borrado del registro. Quedan como `pendiente` con el
motivo, que es la única forma honesta de declarar un hueco.

| Entrada | Estado HTTP | Localizador |
|---|---:|---|
| annual-report-on-exchange-arrangements-and-exchange-restrictions-2023 | 403 | `https://www.imf.org/` |
| blockchain-and-distributed-ledger-technologies-vocabulario-y-marcos-de-refer | 403 | `https://www.iso.org/committee/6266604.html` |
| business-model-and-message-definitions-for-account-and-payment-information | 0 | `https://www.iso20022.org/` |
| camt-053-bank-to-customer-statement-guia-de-uso | 0 | `https://www.iso20022.org/` |
| cbpr-usage-guidelines-para-pagos-transfronterizos | 0 | `https://www.swift.com/standards/iso-20022` |
| consumer-complaint-database | 403 | `https://www.consumerfinance.gov/data-research/consumer-complaints` |
| consumer-protection-in-e-commerce-oecd-recommendation-2016 | 403 | `https://www.oecd.org/` |
| corporate-actions-message-definitions | 0 | `https://www.iso20022.org/iso-20022-message-definitions` |
| data-quality-model | 403 | `https://www.iso.org/standard/35736.html` |
| digital-disruption-in-banking-and-its-impact-on-competition-2020 | 403 | `https://www.oecd.org/competition/digital-disruption-in-banking-and-its-impact-on-competition.htm` |
| documentacion-de-la-red-y-de-sus-servicios-de-mensajeria | 0 | `https://www.swift.com/` |
| el-salvador-informes-de-consulta-del-articulo-iv-y-del-acuerdo-vigente | 403 | `https://www.imf.org/en/Countries/SLV` |
| external-code-sets-purpose-codes-y-reason-codes | 0 | `https://www.iso20022.org/catalogue-messages/additional-content-messages/external-code-sets` |
| financial-sector-assessment-program-fsap | 403 | `https://www.imf.org/en/Publications/fsap` |
| financing-smes-and-entrepreneurs-an-oecd-scoreboard-2023 | 403 | `https://www.oecd.org/industry/smes` |
| fiscal-monitor-2024 | 403 | `https://www.imf.org/en/Publications/FM` |
| g20-oecd-principles-of-corporate-governance-2023 | 403 | `https://www.oecd.org/corporate/principles-corporate-governance` |
| global-financial-stability-report-2024 | 403 | `https://www.imf.org/` |
| guidance-on-digital-identity | 403 | `https://www.fatf-gafi.org/` |
| high-level-principles-on-financial-consumer-protection-2011 | 403 | `https://www.oecd.org/finance/financial-education` |
| international-standards-on-combating-money-laundering-and-the-financing-of-t-2012 | 403 | `https://www.fatf-gafi.org/en/publications/Fatfrecommendations/Fatf-recommendations.html` |
| ley-bitcoin-y-sus-reformas | 0 | `https://www.asamblea.gob.sv/` |
| message-definitions-and-catalogue | 0 | `https://www.iso20022.org/iso-20022-message-definitions` |
| mutual-evaluations | 403 | `https://www.fatf-gafi.org/` |
| oecd-privacy-framework-2013 | 403 | `https://www.oecd.org/digital/ieconomy/privacy-guidelines.htm` |
| oecd-privacy-guidelines-2013 | 403 | `https://www.oecd.org/digital/privacy` |
| pensions-at-a-glance-2023 | 403 | `https://www.oecd.org/pensions` |
| practical-byzantine-fault-tolerance-1999 | 0 | `https://pmg.csail.mit.edu/papers/osdi99.pdf` |
| recomendacion-16-y-activos-virtuales | 403 | `https://www.fatf-gafi.org/en/topics/virtual-assets.html` |
| remittance-prices-worldwide | 403 | `https://remittanceprices.worldbank.org/` |
| resolution-concerning-statistics-of-work-employment-and-labour-underutilizat-2013 | 403 | `https://ilostat.ilo.org/` |
| the-byzantine-generals-problem-1982 | 403 | `https://dl.acm.org/doi/10.1145/357172.357176` |
| the-fatf-recommendations-2012 | 403 | `https://www.fatf-gafi.org/en/publications/Fatfrecommendations/Fatf-recommendations.html` |
| the-making-of-good-supervision-learning-to-say-no-2010 | 403 | `https://www.imf.org/external/pubs/ft/spn/2010/spn1008.pdf` |
