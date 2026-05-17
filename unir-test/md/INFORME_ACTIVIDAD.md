# Informe de actividad - Automatizacion de pruebas con Python

## 1. Datos generales

- Asignatura:
- Alumno:
- Fecha:
- Repositorio base: `unir-test`

## 2. Objetivo de la actividad

Explicar como se completo la calculadora y su API, y como se amplio la bateria de pruebas para cubrir casos correctos y casos de error en pruebas unitarias y de sistema (API).

## 3. Analisis inicial

Describe aqui el estado inicial encontrado:

- Funcionalidades implementadas inicialmente.
- Funcionalidades faltantes respecto a la consigna.
- Cobertura de pruebas existente y huecos detectados.

## 4. Cambios realizados

### 4.1 Clase Calculator (`app/calc.py`)

Indica que se implemento o refactorizo:

- [ ] `add`
- [ ] `substract`
- [ ] `multiply`
- [ ] `divide`
- [ ] `power`
- [ ] `sqrt`
- [ ] `log10`
- [ ] Validaciones de tipo con `TypeError`
- [ ] Validaciones de dominio (division por cero, raiz negativa, log10 <= 0)

### 4.2 API REST (`app/api.py`)

Endpoints incorporados/verificados:

- [ ] `/calc/add/<op_1>/<op_2>`
- [ ] `/calc/substract/<op_1>/<op_2>`
- [ ] `/calc/multiply/<op_1>/<op_2>`
- [ ] `/calc/divide/<op_1>/<op_2>`
- [ ] `/calc/power/<op_1>/<op_2>`
- [ ] `/calc/sqrt/<op_1>`
- [ ] `/calc/log10/<op_1>`

Manejo de errores en API:

- [ ] Respuesta HTTP 400 para entradas invalidas.

### 4.3 Pruebas unitarias (`test/unit/calc_test.py`)

Resume los casos agregados:

- Casos de exito por cada operacion.
- Casos de error por cada operacion.
- Pruebas de metodos estaticos, si aplica.

### 4.4 Pruebas API (`test/rest/api_test.py`)

Resume los casos agregados:

- Casos de exito por endpoint.
- Casos de error (incluyendo division por cero y parametros invalidos).
- Verificacion de codigos HTTP esperados.

## 5. Ejecucion de pruebas

Comandos ejecutados (ajusta a tu entorno):

```powershell
$env:PYTHONPATH='.'
python -m pytest -m unit --junit-xml=results/unit_result.xml --ignore=test/sec/owasp_zap_test.py
```

```powershell
$env:PYTHONPATH='.'
$env:FLASK_APP='app/api.py'
python -m flask run --host=127.0.0.1 --port=5000
```

```powershell
$env:PYTHONPATH='.'
$env:BASE_URL='http://127.0.0.1:5000'
python -m pytest -m api --junit-xml=results/api_result.xml --ignore=test/sec/owasp_zap_test.py
```

## 6. Evidencias generadas

- [ ] `results/unit_result.xml`
- [ ] `results/api_result.xml`

(Adjunta tambien capturas si te las solicitan.)

## 7. Problemas encontrados y soluciones

Documenta de forma breve y concreta:

1. Problema:
   Solucion aplicada:

2. Problema:
   Solucion aplicada:

3. Problema:
   Solucion aplicada:

## 8. Verificacion de rubrica

- Criterio 1 (30%):
  - [ ] Clase Calculator completa
  - [ ] API completa

- Criterio 2 (30%):
  - [ ] Pruebas unitarias cubren todas las funciones
  - [ ] Pruebas de API cubren todas las funciones

- Criterio 3 (40%):
  - [ ] Casos de exito cubiertos
  - [ ] Casos de error cubiertos

## 9. Conclusiones

Incluye una conclusion corta:

- Que aprendiste sobre diferencia entre prueba unitaria y prueba de sistema.
- Como mejoro la calidad del codigo tras ampliar pruebas y validaciones.
- Mejoras futuras recomendadas.
