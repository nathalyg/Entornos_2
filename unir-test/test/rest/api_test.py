import http.client
import os
import unittest
from urllib.error import HTTPError
from urllib.request import urlopen

import pytest

# Cambios de la actividad:
# - Se ampliaron pruebas API para todas las rutas de la calculadora.
# - Se cubrieron escenarios de exito y errores HTTP 400 por tipo y dominio.
# - Se valido comportamiento para divide/0, sqrt negativo y log10 en cero.

BASE_URL = os.environ.get("BASE_URL")
DEFAULT_TIMEOUT = 2  # in secs


@pytest.mark.api
class TestApi(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(BASE_URL, "URL no configurada")
        self.assertTrue(len(BASE_URL) > 8, "URL no configurada")
        self.base_url = BASE_URL.rstrip("/")

    def get_response(self, path):
        url = f"{self.base_url}{path}"
        return urlopen(url, timeout=DEFAULT_TIMEOUT)

    def get_error_response(self, path):
        url = f"{self.base_url}{path}"
        with self.assertRaises(HTTPError) as error:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        return error.exception

    def test_api_add(self):
        response = self.get_response("/calc/add/2/2")
        self.assertEqual(
            response.status, http.client.OK, "Error en la petición API de suma"
        )
        self.assertEqual("4", response.read().decode("utf-8"))

    def test_api_substract(self):
        response = self.get_response("/calc/substract/5/2")
        self.assertEqual(response.status, http.client.OK)
        self.assertEqual("3", response.read().decode("utf-8"))

    def test_api_multiply(self):
        response = self.get_response("/calc/multiply/3/2")
        self.assertEqual(response.status, http.client.OK)
        self.assertEqual("6", response.read().decode("utf-8"))

    def test_api_divide(self):
        response = self.get_response("/calc/divide/6/2")
        self.assertEqual(response.status, http.client.OK)
        self.assertEqual("3.0", response.read().decode("utf-8"))

    def test_api_power(self):
        response = self.get_response("/calc/power/2/3")
        self.assertEqual(response.status, http.client.OK)
        self.assertEqual("8", response.read().decode("utf-8"))

    def test_api_sqrt(self):
        response = self.get_response("/calc/sqrt/9")
        self.assertEqual(response.status, http.client.OK)
        self.assertEqual("3.0", response.read().decode("utf-8"))

    def test_api_log10(self):
        response = self.get_response("/calc/log10/100")
        self.assertEqual(response.status, http.client.OK)
        self.assertEqual("2.0", response.read().decode("utf-8"))

    def test_api_divide_by_zero_returns_bad_request(self):
        response = self.get_error_response("/calc/divide/6/0")
        self.assertEqual(response.status, http.client.BAD_REQUEST)

    def test_api_sqrt_negative_returns_bad_request(self):
        response = self.get_error_response("/calc/sqrt/-9")
        self.assertEqual(response.status, http.client.BAD_REQUEST)

    def test_api_log10_zero_returns_bad_request(self):
        response = self.get_error_response("/calc/log10/0")
        self.assertEqual(response.status, http.client.BAD_REQUEST)

    def test_api_add_invalid_parameter_returns_bad_request(self):
        response = self.get_error_response("/calc/add/a/2")
        self.assertEqual(response.status, http.client.BAD_REQUEST)

    def test_api_substract_invalid_parameter_returns_bad_request(self):
        response = self.get_error_response("/calc/substract/a/2")
        self.assertEqual(response.status, http.client.BAD_REQUEST)

    def test_api_multiply_invalid_parameter_returns_bad_request(self):
        response = self.get_error_response("/calc/multiply/a/2")
        self.assertEqual(response.status, http.client.BAD_REQUEST)

    def test_api_power_invalid_parameter_returns_bad_request(self):
        response = self.get_error_response("/calc/power/a/2")
        self.assertEqual(response.status, http.client.BAD_REQUEST)
