
class Materia:
    def __init__(self, nombre, profesores, alumnos=None):
        self._nombre = nombre
        self._profesores = profesores
        self._alumnos = alumnos if alumnos is not None else []

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def profesores(self):
        return self._profesores

    @property
    def alumnos(self):
        return self._alumnos

    def obtener_profesores(self):
        return self._profesores

    def cambiar_nombre(self, nombre):
        self._nombre = nombre

    def obtener_alumnos(self):
        return self._alumnos

    def __repr__(self):
        return f"Materia(nombre={self._nombre}, profesores={self._profesores}, alumnos={self._alumnos})"



class Profesor:
    def __init__(self, nombre, cargo, legajo):
        self.__nombre__ = nombre
        self.__cargo__ = cargo
        self.__legajo__ = legajo

    def obtener_nombre(self):
        return self.__nombre__

    def obtener_cargo(self):
        return self.__cargo__

    def obtener_legajo(self):
        return self.__legajo__
    

class Alumno:
    def __init__(self, nombre, legajo):
        self._nombre = nombre
        self._legajo = legajo

    @property
    def nombre(self):
        return self._nombre

    @property
    def legajo(self):
        return self._legajo

    def __repr__(self):
        return f"Alumno(nombre={self._nombre}, legajo={self._legajo})"