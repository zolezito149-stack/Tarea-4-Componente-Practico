# archivo: cliente.py
# Estudiante: Verónica Ordoñez
# Tarea: Clase Cliente con validaciones

import re
from excepciones import DatoInvalidoError  # lo creará el Estudiante 4
from logger import logger  # lo creará el Estudiante 4

class Cliente:
    """Clase Cliente con encapsulación y validación de datos"""
    
    def __init__(self, nombre, email, telefono):
        self._nombre = None
        self._email = None
        self._telefono = None
        
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        
        logger.info(f"Cliente creado: {self._nombre}")
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, valor):
        # Validación: no vacío y mínimo 3 caracteres
        if not valor or len(valor.strip()) < 3:
            raise DatoInvalidoError(f"Nombre inválido: mínimo 3 caracteres")
        self._nombre = valor.strip()
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, valor):
        # Validación: formato de email
        patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(patron, valor):
            raise DatoInvalidoError(f"Email inválido: {valor}")
        self._email = valor
    
    @property
    def telefono(self):
        return self._telefono
    
    @telefono.setter
    def telefono(self, valor):
        # Validación: solo dígitos y mínimo 7
        if not valor.isdigit() or len(valor) < 7:
            raise DatoInvalidoError(f"Teléfono inválido: solo dígitos, mínimo 7")
        self._telefono = valor
    
    def mostrar_info(self):
        """Retorna información del cliente"""
        return f"Cliente: {self._nombre} | Email: {self._email} | Tel: {self._telefono}"


# archivo: .python
# Estudiante: Yuler Alexander Velasquqez 
# Tarea:  Clase abstracta Servicio + herencia (ReservaSalas, AlquilerEquipos, Asesoria)
from abc import ABC, abstractmethod
from excepciones import DatoInvalidoError
from logger import logger

# ==============================
# CLASE ABSTRACTA SERVICIO
# ==============================

class Servicio(ABC):
    """Clase abstracta base para los servicios"""

    def __init__(self, codigo, descripcion, precio):
        self._codigo = None
        self._descripcion = None
        self._precio = None

        self.codigo = codigo
        self.descripcion = descripcion
        self.precio = precio

        logger.info(f"Servicio creado: {self._codigo}")

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, valor):
        if not valor or len(valor.strip()) == 0:
            raise DatoInvalidoError("Código inválido")
        self._codigo = valor.strip()

    @property
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self, valor):
        if not valor or len(valor.strip()) < 5:
            raise DatoInvalidoError("Descripción inválida")
        self._descripcion = valor.strip()

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):
        if valor <= 0:
            raise DatoInvalidoError("Precio inválido")
        self._precio = valor

    @abstractmethod
    def calcular_costo(self):
        pass

    def mostrar_info(self):
        return f"{self._codigo} | {self._descripcion} | Precio base: {self._precio}"


# ==============================
# HERENCIA 1: RESERVA DE SALAS
# ==============================

class ReservaSalas(Servicio):

    def __init__(self, codigo, descripcion, precio, horas):
        super().__init__(codigo, descripcion, precio)
        self._horas = horas

    @property
    def horas(self):
        return self._horas

    @horas.setter
    def horas(self, valor):
        if valor <= 0:
            raise DatoInvalidoError("Horas inválidas")
        self._horas = valor

    def calcular_costo(self):
        total = self._precio * self._horas
        logger.info(f"Costo ReservaSalas: {total}")
        return total


# ==============================
# HERENCIA 2: ALQUILER EQUIPOS
# ==============================

class AlquilerEquipos(Servicio):

    def __init__(self, codigo, descripcion, precio, dias):
        super().__init__(codigo, descripcion, precio)
        self._dias = dias

    @property
    def dias(self):
        return self._dias

    @dias.setter
    def dias(self, valor):
        if valor <= 0:
            raise DatoInvalidoError("Días inválidos")
        self._dias = valor

    def calcular_costo(self):
        total = self._precio * self._dias
        logger.info(f"Costo AlquilerEquipos: {total}")
        return total


# ==============================
# HERENCIA 3: ASESORIA
# ==============================

class Asesoria(Servicio):

    def __init__(self, codigo, descripcion, precio, sesiones):
        super().__init__(codigo, descripcion, precio)
        self._sesiones = sesiones

    @property
    def sesiones(self):
        return self._sesiones

    @sesiones.setter
    def sesiones(self, valor):
        if valor <= 0:
            raise DatoInvalidoError("Sesiones inválidas")
        self._sesiones = valor

    def calcular_costo(self):
        total = self._precio * self._sesiones
        logger.info(f"Costo Asesoria: {total}")
        return total
    
