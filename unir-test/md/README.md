# Automatizacion de pruebas con Python - Actividad individual

Este proyecto implementa una calculadora con API REST y una bateria de pruebas automatizadas.

## 1) Que se amplio en esta actividad

Se completaron las funcionalidades pedidas en la consigna:

- Suma
- Resta
- Multiplicacion
- Division
- Potenciacion
- Raiz cuadrada
- Logaritmo base 10

Tambien se reforzo la validacion de parametros en la clase `Calculator`:

- Si un parametro no es numerico, se lanza `TypeError`.
- Si hay division por cero, se lanza `TypeError`.
- Si se intenta `sqrt` de numero negativo, se lanza `TypeError`.
- Si se intenta `log10` con valor menor o igual a 0, se lanza `TypeError`.

## 2) Archivos modificados

- `app/calc.py`
	- Se anadieron `sqrt` y `log10`.
	- Se agregaron validadores estaticos (`check_number`, `check_types`).
	- Se usa `substract` como operacion de resta.

- `app/api.py`
	- Se anadieron endpoints para todas las operaciones.
	- Se refactorizo para reutilizar logica con funciones auxiliares de operaciones binarias y unarias.

- `test/unit/calc_test.py`
	- Se agregaron pruebas de exito y error para todas las operaciones.
	- Se incluyeron pruebas para metodos estaticos.

- `test/rest/api_test.py`
	- Se agregaron pruebas API para endpoints de exito y error (HTTP 400 en casos invalidos).

## 3) Como se entendio y abordo la tarea

Pasos realizados para analizar y resolver:

1. Revisar implementacion existente (`calc.py`, `api.py`) para detectar funciones faltantes.
2. Revisar pruebas existentes (`test/unit`, `test/rest`) para detectar cobertura insuficiente.
3. Implementar funciones matematicas faltantes usando `math` donde aplica.
4. Estandarizar validaciones y errores con `TypeError`.
5. Completar endpoints REST para todas las operaciones.
6. Ampliar pruebas unitarias y API con casos de exito y fallo.
7. Generar reportes XML para entregar evidencia.

## 4) Endpoints disponibles

- `GET /calc/add/<op_1>/<op_2>`
- `GET /calc/substract/<op_1>/<op_2>`
- `GET /calc/multiply/<op_1>/<op_2>`
- `GET /calc/divide/<op_1>/<op_2>`
- `GET /calc/power/<op_1>/<op_2>`
- `GET /calc/sqrt/<op_1>`
- `GET /calc/log10/<op_1>`

## 5) Como ejecutar pruebas y generar XML

Las ejecuciones se realizaron en Ubuntu usando Docker y Makefile.

### 5.1 Preparacion comun

```bash
cd /home/ubuntu/Entornos_2/unir-test
mkdir -p results
```

### 5.2 Ejecutar pruebas unitarias y generar XML/HTML

```bash
sudo make test-unit
```

Archivos generados:

- `results/unit_result.xml`
- `results/unit_result.html`
- `results/coverage.xml`
- `results/coverage/`

### 5.3 Ejecutar pruebas API y generar XML/HTML

```bash
sudo make test-api
```

Archivos generados:

- `results/api_result.xml`
- `results/api_result.html`

### 5.4 Descargar resultados a local (Windows)

```powershell
scp -i "C:\Maestria\Entornos\test-packer-key.pem" -P 2222 -r ubuntu@ec2-98-93-254-223.compute-1.amazonaws.com:/home/ubuntu/Entornos_2/unir-test/results "C:\Maestria\Entornos\Entornos_2\unir-test"
```

## 6) Resultados obtenidos

- Unitarias: `19 passed, 15 deselected`.
- API: `14 passed, 20 deselected`.
- En ambos casos se generaron reportes XML/HTML sin fallos ni errores.

## 7) Checklist para cumplir la rubrica

- Criterio 1 (30%):
	- `Calculator` tiene todas las operaciones solicitadas.
	- API tiene endpoints de todas las operaciones.

- Criterio 2 (30%):
	- Pruebas unitarias cubren todas las operaciones.
	- Pruebas API cubren todos los endpoints principales.

- Criterio 3 (40%):
	- Cada operacion tiene casos de exito y de error.
	- API devuelve 400 en entradas invalidas.

## 8) Entrega final recomendada

Incluye en la entrega:

- Codigo actualizado.
- `results/unit_result.xml`
- `results/api_result.xml`
- Informe explicativo (puedes usar el archivo `INFORME_ACTIVIDAD.md` como base).
