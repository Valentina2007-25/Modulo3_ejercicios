import unittest
from ejercicio_2_Generador_Perfiles_Usuario import crear_perfil


class TestCrearPerfil(unittest.TestCase):
    """Pruebas unitarias para la función crear_perfil."""

    def test_nombre_vacio(self):
        with self.assertRaises(ValueError):
            crear_perfil("", 18, "leer")

    def test_nombre_solo_numeros(self):
        with self.assertRaises(ValueError):
            crear_perfil("12345", 18, "bailar")

    def test_nombre_con_numeros(self):
        with self.assertRaises(ValueError):
            crear_perfil("Vale123", 18, "viajar")

    def test_edad_invalida(self):
        with self.assertRaises(ValueError):
            crear_perfil("Valentina", -5, "leer")

    def test_edad_no_entero(self):
        with self.assertRaises(ValueError):
            crear_perfil("Valentina", "dieciocho", "leer")

    def test_hobby_invalido(self):
        with self.assertRaises(ValueError):
            crear_perfil("Valentina", 18, "leer", 123)

    def test_red_social_invalida(self):
        with self.assertRaises(ValueError):
            crear_perfil("Valentina", 18, "leer", instagram=123)

    def test_perfil_valido(self):
        resultado = crear_perfil("Valentina", 18, "leer", "viajar", instagram="@vale", twitter="@valetw")
        self.assertIn("Valentina", resultado)
        self.assertIn("leer", resultado)
        self.assertIn("instagram: @vale", resultado)


if __name__ == "__main__":
    unittest.main()
