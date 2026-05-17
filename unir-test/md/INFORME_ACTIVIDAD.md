# Informe de actividad - Automatizacion de pruebas con Python

## 1. Datos generales

- Asignatura:
- Alumno:
- Fecha: 2026-05-16
- Repositorio base: `unir-test`

## 2. Objetivo de la actividad

Explicar como se completo la calculadora y su API, y como se amplio la bateria de pruebas para cubrir casos correctos y casos de error en pruebas unitarias y de sistema (API).

## 3. Analisis inicial

Estado inicial identificado:

- El proyecto ya incluia parte de la calculadora y endpoints iniciales.
- Faltaban completar funcionalidades matematicas requeridas por la consigna.
- La cobertura de pruebas era insuficiente para demostrar todos los casos de exito y error.
- La bateria de pruebas API no validaba todos los escenarios de fallo para todas las operaciones.

## 4. Cambios realizados

### 4.1 Clase Calculator (`app/calc.py`)

- [x] `add`
- [x] `substract`
- [x] `multiply`
- [x] `divide`
- [x] `power`
- [x] `sqrt`
- [x] `log10`
- [x] Validaciones de tipo con `TypeError`
- [x] Validaciones de dominio (division por cero, raiz negativa, log10 <= 0)

Refactorizaciones realizadas:

- Se uso el modulo `math` para `sqrt` y `log10`.
- Se agregaron metodos auxiliares `check_number` y `check_types` para reutilizar validaciones.
- Se normalizo el uso de `TypeError` para entradas invalidas y errores de dominio.

### 4.2 API REST (`app/api.py`)

Endpoints incorporados/verificados:

- [x] `/calc/add/<op_1>/<op_2>`
- [x] `/calc/substract/<op_1>/<op_2>`
- [x] `/calc/multiply/<op_1>/<op_2>`
- [x] `/calc/divide/<op_1>/<op_2>`
- [x] `/calc/power/<op_1>/<op_2>`
- [x] `/calc/sqrt/<op_1>`
- [x] `/calc/log10/<op_1>`

Manejo de errores en API:

- [x] Respuesta HTTP 400 para entradas invalidas.

Implementacion adicional:

- Se agregaron funciones auxiliares para evitar duplicacion (`execute_binary_operation` y `execute_unary_operation`).
- Se valido conversion de parametros y manejo de excepciones de forma uniforme.

### 4.3 Pruebas unitarias (`test/unit/calc_test.py`)

Resume los casos agregados:

- Casos de exito por cada operacion (`add`, `substract`, `multiply`, `divide`, `power`, `sqrt`, `log10`).
- Casos de error por cada operacion (tipos invalidos y errores de dominio).
- Pruebas de metodos estaticos/auxiliares (`check_number`, `check_types`).

### 4.4 Pruebas API (`test/rest/api_test.py`)

Resume los casos agregados:

- Casos de exito por endpoint para todas las operaciones.
- Casos de error para parametros invalidos y dominio (`divide/0`, `sqrt` negativo, `log10` en 0).
- Verificacion de codigos HTTP esperados (`200` en exito y `400` en error).

## 5. Ejecucion de pruebas

Comandos ejecutados en la instancia (Ubuntu + Docker):

```bash
cd /home/ubuntu/Entornos_2/unir-test
sudo make test-unit
```

```bash
cd /home/ubuntu/Entornos_2/unir-test
sudo make test-api
```

Resultados obtenidos:

- Unitarias: `19 passed, 15 deselected`.
- API: `14 passed, 20 deselected`.
- Sin fallos ni errores en ambos conjuntos.

## 6. Evidencias generadas

- [x] `results/unit_result.xml`
- [x] `results/api_result.xml`

Evidencias adicionales generadas:

- `results/unit_result.html`
- `results/api_result.html`
- `results/coverage.xml`
- `results/coverage/`

## 7. Problemas encontrados y soluciones

1. Problema: error de permisos al ejecutar Docker (`docker.sock`).
  Solucion aplicada: ejecucion de comandos `make` con `sudo` en la instancia.

2. Problema: error en `make server` por `--network-alias` sin red definida.
  Solucion aplicada: ajuste del target `server` en `Makefile` para eliminar el alias en ejecucion standalone.

3. Problema: dificultad para ubicar el proyecto entre sesiones SSM y SSH.
  Solucion aplicada: clonacion/uso del repositorio en ruta estable de `ubuntu` (`/home/ubuntu/Entornos_2/unir-test`).

## 8. Verificacion de rubrica

- Criterio 1 (30%):
  - [x] Clase Calculator completa
  - [x] API completa

- Criterio 2 (30%):
  - [x] Pruebas unitarias cubren todas las funciones
  - [x] Pruebas de API cubren todas las funciones

- Criterio 3 (40%):
  - [x] Casos de exito cubiertos
  - [x] Casos de error cubiertos

## 9. Conclusiones

La actividad permitio diferenciar claramente entre pruebas unitarias (validan funciones aisladas en `Calculator` y `util`) y pruebas de sistema/API (validan integracion mediante HTTP y codigos de respuesta). Al ampliar validaciones y pruebas, mejoro la robustez del codigo frente a entradas invalidas y errores de dominio. Como mejora futura, se recomienda ampliar cobertura E2E y seguridad para fortalecer la calidad integral del producto.
