import unittest
from ejercicio_1_calculadora_IMC import calcular_imc, interpretar_imc


class TestCalculadoraIMC(unittest.TestCase):
    """Pruebas unitarias para las funciones de la Calculadora de IMC."""

    def test_calculo_imc_normal(self):
        """Prueba de cálculo normal de IMC."""
        resultado = calcular_imc(70, 1.75)
        self.assertAlmostEqual(resultado, 22.86, places=2)

    def test_calculo_imc_bajo_peso(self):
        """Prueba IMC menor a 18.5."""
        imc = calcular_imc(45, 1.70)
        categoria = interpretar_imc(imc)
        self.assertEqual(categoria, "Bajo peso")

    def test_calculo_imc_normal_categoria(self):
        """Prueba IMC normal (18.5–24.9)."""
        imc = calcular_imc(60, 1.70)
        categoria = interpretar_imc(imc)
        self.assertEqual(categoria, "Normal")

    def test_calculo_imc_sobrepeso(self):
        """Prueba IMC entre 25 y 29.9."""
        imc = calcular_imc(80, 1.75)
        categoria = interpretar_imc(imc)
        self.assertEqual(categoria, "Sobrepeso")

    def test_calculo_imc_obesidad(self):
        """Prueba IMC mayor o igual a 30."""
        imc = calcular_imc(95, 1.60)
        categoria = interpretar_imc(imc)
        self.assertEqual(categoria, "Obesidad")

    def test_altura_invalida(self):
        """Altura cero o negativa debe generar error."""
        with self.assertRaises(ZeroDivisionError):
            calcular_imc(70, 0)

    def test_tipos_invalidos(self):
        """Valores no numéricos deben causar error."""
        with self.assertRaises(TypeError):
            calcular_imc("setenta", "uno punto setenta")


if __name__ == "__main__":
    unittest.main()
