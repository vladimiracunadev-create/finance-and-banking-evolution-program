# Caso · El token que era un edificio y el edificio que era de otro

**Tema:** tokenización · **Parte relacionada:** 21 · **Naturaleza:** caso
sintético compuesto · **Fecha de verificación:** 2026-08-12

Ochocientos inversores compran participaciones tokenizadas de un edificio de
oficinas. El registro de la blockchain funciona perfectamente y refleja quién
tiene cada token. El registro de la propiedad del país donde está el edificio
refleja otra cosa. Este caso trata de qué registro manda.

## Hechos

```text
HECHO VERIFICADO (del expediente del caso)

  · edificio valorado en    18 000 000
  · titular registral: una sociedad
    vehículo
  · se emiten 18 000 tokens de 1 000
  · cada token representa una participación
    en la sociedad vehículo, no en el
    inmueble
  · 812 inversores, 41 de ellos con más de
    50 tokens
  · el promotor mantiene el 12 % y la
    administración de la sociedad

INCIDENCIA
  · la sociedad vehículo constituye una
    hipoteca sobre el inmueble por
    4 200 000 sin consultar a los tenedores
  · era jurídicamente válido: los estatutos
    lo permitían al administrador
```

La cadena de derechos tiene tres eslabones y solo uno estaba en la blockchain:

```text
  TOKEN  →  participación en la sociedad
         →  la sociedad es titular
         →  del inmueble

  LO QUE EL REGISTRO DISTRIBUIDO GARANTIZA
    quién tiene el token

  LO QUE NO GARANTIZA
    qué puede hacer el administrador
    de la sociedad
```

## Actores

| Actor | Qué persigue | Qué información tenía |
|---|---|---|
| Inversor minorista | Exposición al inmueble | Un folleto y una aplicación |
| Promotor administrador | Financiación y control | Los estatutos |
| Sociedad vehículo | Ser el titular | Su propia estructura |
| Prestamista hipotecario | Garantía real | El registro de la propiedad |
| Plataforma emisora | Comisión de colocación | Los tres eslabones |
| Supervisor | Que la oferta tenga régimen | El expediente, si se presentó |

## Decisiones

```text
DISEÑO
  usar sociedad vehículo
  DECISIÓN NECESARIA: el registro de la
  propiedad no reconoce tokens

DISEÑO
  estatutos que permiten al administrador
  gravar el inmueble
  DECISIÓN NO DESTACADA EN EL FOLLETO

COLOCACIÓN
  el material comercial dice
  «sé propietario de una parte del edificio»
  AFIRMACIÓN INEXACTA: se es socio de la
  sociedad que es propietaria

MES 19
  se constituye la hipoteca
  VÁLIDA Y NO COMUNICADA

MES 22
  los tenedores se enteran por el
  registro de la propiedad
```

## Riesgos

| Riesgo | Estaba presente | Se materializó |
|---|---|---|
| Distancia entre token y activo | Desde el diseño | Sí |
| Poderes del administrador | Desde los estatutos | Sí |
| Material comercial inexacto | Desde la colocación | Sí |
| Ausencia de gobierno de los tenedores | Desde el diseño | Sí |
| Iliquidez del secundario | Desde el diseño | Sí |
| Divergencia entre registros | Estructural | Sí |

## Regulación

```text
QUÉ ALCANZA

  OFERTA PÚBLICA
    ofrecer participaciones a 812 personas
    es oferta pública en la mayoría de los
    regímenes; el soporte no la excluye

  INFORMACIÓN
    los poderes del administrador y la
    posibilidad de gravar el activo son
    información material; omitirlos puede
    generar responsabilidad

  REGISTROS OFICIALES
    la titularidad de un inmueble la
    determina el registro competente; un
    registro distribuido no lo sustituye
    salvo que la ley lo prevea

LÍMITE
  depende de la jurisdicción del inmueble
  y de la de la oferta, que pueden no
  coincidir
```

## Controles

| Control | Existía | Funcionó | Qué faltaba |
|---|---|---|---|
| Sociedad vehículo | Sí | Sí | Estatutos con límites al administrador |
| Folleto | Parcial | No | Describir los tres eslabones |
| Gobierno de tenedores | No | — | Mayoría reforzada para gravar |
| Auditoría del vínculo jurídico | No | — | Dictamen sobre qué otorga el token |
| Vigilancia del registro oficial | No | — | Alerta ante cualquier carga |
| Restricción de reventa | Parcial | No | Coherente con el régimen de oferta |

El tercero es el que habría evitado el caso entero y cuesta una cláusula: **gravar
el inmueble requiere el voto de una mayoría reforzada de los tenedores.** Sin esa
cláusula, la tokenización reparte el riesgo económico sin repartir el poder.

## Resultado

```text
SITUACIÓN A LOS 22 MESES (supuestos)

  valor del inmueble        18 000 000
  hipoteca                   4 200 000
  valor neto para los socios 13 800 000
  valor por token
    13 800 000 / 18 000 =        766,67
    frente a 1 000 de emisión

  PÉRDIDA DE VALOR POR TOKEN     233,33
  PÉRDIDA AGREGADA             4 200 000

  Y ES EXACTAMENTE EL IMPORTE DE LA
  HIPOTECA: el promotor obtuvo 4,2 M de
  financiación con el patrimonio de 812
  personas que no votaron
```

## Lecciones

1. **El token vale lo que vale el eslabón más débil de la cadena de derechos**, y
   esa cadena casi nunca está en el registro distribuido.
2. **Repartir el riesgo económico sin repartir el poder produce este resultado**,
   y el remedio es una cláusula de gobierno, no una tecnología.
3. **«Sé propietario de una parte del edificio» es una afirmación inexacta** en
   casi todas las estructuras de este tipo, y su inexactitud tiene consecuencias.
4. **Los registros oficiales siguen mandando.** Vigilar el registro de la
   propiedad es un control tan necesario como vigilar la cadena.

## Preguntas

1. ¿Qué debería decir exactamente el material comercial? Redáctalo en dos frases.
2. ¿Qué mayorías exigirías para gravar, vender o refinanciar el inmueble?
3. ¿Cómo se audita el vínculo jurídico entre el token y el activo? ¿Quién lo firma?
4. Si la jurisdicción del inmueble y la de la oferta difieren, ¿qué régimen aplica
   a cada cosa?
5. ¿Qué aporta aquí la tokenización que no aportara una sociedad con 812 socios y
   un libro registro?

## Fuentes

- IOSCO (2023). *Policy Recommendations for Crypto and Digital Asset Markets*. <https://www.iosco.org/library/pubdocs/pdf/IOSCOPD747.pdf>
- UNIDROIT. *Principles on Digital Assets and Private Law*. <https://www.unidroit.org/work-in-progress/digital-assets-and-private-law/>
- OCDE. *The Tokenisation of Assets and Potential Implications for Financial Markets*. <https://www.oecd.org/finance/The-Tokenisation-of-Assets-and-Potential-Implications-for-Financial-Markets.htm>
- CMF. *Normativa sobre oferta pública de valores*. <https://www.cmfchile.cl/>
- Verificación local: caso sintético; cifras supuestas. El régimen de la oferta y el de la propiedad inmobiliaria dependen de jurisdicciones que pueden no coincidir. **Fecha de verificación: 2026-08-12.** No constituye asesoría legal ni de inversión.
