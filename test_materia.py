import unittest
from materia import Profesor, Alumno, Materia
class TestMateria(unittest.TestCase):

    def setUp(self):
        self.profesor1 = Profesor("Profesor 1", "Titular", 123)
        self.profesor2 = Profesor("Profesor 2", "Adjunto", 456)
        self.alumno1 = Alumno("Alumno 1", 789)
        self.alumno2 = Alumno("Alumno 2", 1011)
        self.materia = Materia("Matemáticas", [self.profesor1, self.profesor2], [self.alumno1, self.alumno2])

    def test_constructor(self):
        self.assertEqual(self.materia.nombre, "Matemáticas")
        self.assertEqual(self.materia.profesores, [self.profesor1, self.profesor2])
        self.assertEqual(self.materia.alumnos, [self.alumno1, self.alumno2])

    def test_obtener_profesores(self):
        self.assertEqual(self.materia.obtener_profesores(), [self.profesor1, self.profesor2])

    def test_cambiar_nombre(self):
        self.materia.cambiar_nombre("Física")
        self.assertEqual(self.materia.nombre, "Física")

    def test_obtener_alumnos(self):
        self.assertEqual(self.materia.obtener_alumnos(), [self.alumno1, self.alumno2])

class TestProfesor(unittest.TestCase):

    def setUp(self):
        self.profesor = Profesor("Profesor 1", "Titular", 123)

    def test_constructor(self):
        self.assertEqual(self.profesor.nombre, "Profesor 1")
        self.assertEqual(self.profesor.cargo, "Titular")
        self.assertEqual(self.profesor.legajo, 123)

    def test_obtener_nombre(self):
        self.assertEqual(self.profesor.obtener_nombre(), "Profesor 1")

    def test_obtener_cargo(self):
        self.assertEqual(self.profesor.obtener_cargo(), "Titular")

    def test_obtener_legajo(self):
        self.assertEqual(self.profesor.obtener_legajo(), 123)

class TestAlumno(unittest.TestCase):

    def setUp(self):
        self.alumno = Alumno("Alumno 1", 789)

    def test_constructor(self):
        self.assertEqual(self.alumno.nombre, "Alumno 1")
        self.assertEqual(self.alumno.legajo, 789)

if __name__ == "__main__":
    unittest.main()