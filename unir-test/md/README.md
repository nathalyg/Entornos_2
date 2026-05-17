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

### Requisito previo (solo la primera vez)

Ejecuta estos comandos desde `C:\Maestria\Entornos\Actividad2`:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install pytest flask
```

Si ya tienes `.venv`, solo activa:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5.1 Preparacion comun para todas las pruebas

```powershell
Set-Location C:\Maestria\Entornos\Actividad2\unir-test
New-Item -ItemType Directory -Force -Path results | Out-Null
$env:PYTHONPATH='.'
```

### 5.2 Ejecutar pruebas unitarias y generar XML

```powershell
python -m pytest -m unit --junit-xml=results/unit_result.xml --ignore=test/sec/owasp_zap_test.py
```

Validar que se genero el XML:

```powershell
Get-Item .\results\unit_result.xml
Get-Content .\results\unit_result.xml -TotalCount 20
```

### 5.3 Levantar API para pruebas REST

Abre una terminal nueva y ejecuta:

```powershell
Set-Location C:\Maestria\Entornos\Actividad2\unir-test
.\.venv\Scripts\Activate.ps1
$env:PYTHONPATH='.'
$env:FLASK_APP='app/api.py'
python -m flask run --host=127.0.0.1 --port=5000
```

Prueba rapida manual (opcional, en otra terminal):

```powershell
Invoke-WebRequest -Uri http://127.0.0.1:5000/calc/add/2/2 | Select-Object -ExpandProperty Content
```

### 5.4 Ejecutar pruebas API y generar XML

En otra terminal distinta a la que levanto Flask:

```powershell
Set-Location C:\Maestria\Entornos\Actividad2\unir-test
.\.venv\Scripts\Activate.ps1
$env:PYTHONPATH='.'
$env:BASE_URL='http://127.0.0.1:5000'
python -m pytest -m api --junit-xml=results/api_result.xml --ignore=test/sec/owasp_zap_test.py
```

Validar que se genero el XML:

```powershell
Get-Item .\results\api_result.xml
Get-Content .\results\api_result.xml -TotalCount 20
```

### 5.5 Cerrar servidor API

En la terminal donde corre Flask, presiona:

```powershell
Ctrl + C
```

### 5.6 Comando rapido (resumen)

Si ya tienes entorno y dependencias, este bloque te ejecuta todo lo unitario en una sola pasada:

```powershell
Set-Location C:\Maestria\Entornos\Actividad2\unir-test
.\.venv\Scripts\Activate.ps1
New-Item -ItemType Directory -Force -Path results | Out-Null
$env:PYTHONPATH='.'
python -m pytest -m unit --junit-xml=results/unit_result.xml --ignore=test/sec/owasp_zap_test.py
```

Para API, recuerda que siempre necesitas Flask levantado en paralelo para que los tests REST pasen.

## 6) Checklist para cumplir la rubrica

- Criterio 1 (30%):
	- `Calculator` tiene todas las operaciones solicitadas.
	- API tiene endpoints de todas las operaciones.

- Criterio 2 (30%):
	- Pruebas unitarias cubren todas las operaciones.
	- Pruebas API cubren todos los endpoints principales.

- Criterio 3 (40%):
	- Cada operacion tiene casos de exito y de error.
	- API devuelve 400 en entradas invalidas.

## 7) Entrega final recomendada

Incluye en la entrega:

- Codigo actualizado.
- `results/unit_result.xml`
- `results/api_result.xml`
- Informe explicativo (puedes usar el archivo `INFORME_ACTIVIDAD.md` como base).
