

# SOFIA MUÑOZ - MANEJO DE EXCEPCIONES + LOGS

from abc import ABC, abstractmethod
import logging
import re

# Configuración de logging - SOFIA MUÑOZ
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)
logger = logging.getLogger(__name__)

# Excepción personalizada - SOFIA MUÑOZ
class DatoInvalidoError(Exception):
    """Excepcion para datos invalidos del sistema."""
    pass

# YULER VELASQUEZ - CLASE ABSTRACTA GENERAL

class EntidadSistema(ABC):
    """Clase abstracta general del sistema - YULER VELASQUEZ"""

    @abstractmethod
    def mostrar_info(self):
        pass


# VERONICA ORDOÑEZ - CLASE CLIENTE + VALIDACIONES

class Cliente(EntidadSistema):
    """Clase Cliente con encapsulacion y validacion de datos - VERONICA ORDOÑEZ"""

    def __init__(self, nombre, email, telefono):
        self._nombre = None
        self._email = None
        self._telefono = None

        self.nombre = nombre
        self.email = email
        self.telefono = telefono

        # Log - SOFIA MUÑOZ
        logger.info(f"Cliente creado: {self._nombre}")

    # VALIDACIONES DE NOMBRE - VERONICA ORDOÑEZ
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str) or len(valor.strip()) < 3:
            raise DatoInvalidoError("Nombre invalido: minimo 3 caracteres")
        self._nombre = valor.strip()

    # VALIDACIONES DE EMAIL - VERONICA ORDOÑEZ
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        patron = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if not isinstance(valor, str) or not re.match(patron, valor):
            raise DatoInvalidoError(f"Email invalido: {valor}")
        self._email = valor.strip()

    # VALIDACIONES DE TELEFONO - VERONICA ORDOÑEZ
    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, valor):
        if not isinstance(valor, str):
            valor = str(valor)

        if not valor.isdigit() or len(valor) < 7:
            raise DatoInvalidoError(
                "Telefono invalido: solo digitos, minimo 7"
            )
        self._telefono = valor

    def mostrar_info(self):
        return (
            f"Cliente: {self._nombre} | "
            f"Email: {self._email} | "
            f"Tel: {self._telefono}"
        )


# YULER VELASQUEZ - CLASE ABSTRACTA SERVICIO + HERENCIA

class Servicio(EntidadSistema, ABC):
    """Clase abstracta base para los servicios - YULER VELASQUEZ"""

    def __init__(self, codigo, descripcion, precio):
        self._codigo = None
        self._descripcion = None
        self._precio = None

        self.codigo = codigo
        self.descripcion = descripcion
        self.precio = precio

        # Log - SOFIA MUÑOZ
        logger.info(f"Servicio creado: {self._codigo}")

    # VALIDACIONES SERVICIO - YULER VELASQUEZ
    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, valor):
        if not isinstance(valor, str) or len(valor.strip()) == 0:
            raise DatoInvalidoError("Codigo invalido")
        self._codigo = valor.strip()

    @property
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self, valor):
        if not isinstance(valor, str) or len(valor.strip()) < 5:
            raise DatoInvalidoError("Descripcion invalida")
        self._descripcion = valor.strip()

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):
        if not isinstance(valor, (int, float)) or valor <= 0:
            raise DatoInvalidoError("Precio invalido")
        self._precio = valor

    @abstractmethod
    def calcular_costo(self, impuesto=0, descuento=0):
        pass

    def mostrar_info(self):
        return (
            f"{self._codigo} | {self._descripcion} | "
            f"Precio base: {self._precio}"
        )

# CLASE HIJA 1 - RESERVA SALAS (HERENCIA) - YULER VELASQUEZ
class ReservaSalas(Servicio):
    """Servicio para reservar salas por horas - YULER VELASQUEZ"""

    def __init__(self, codigo, descripcion, precio, horas):
        super().__init__(codigo, descripcion, precio)
        self._horas = None
        self.horas = horas

    @property
    def horas(self):
        return self._horas

    @horas.setter
    def horas(self, valor):
        if not isinstance(valor, (int, float)) or valor <= 0:
            raise DatoInvalidoError("Horas invalidas")
        self._horas = valor

    def calcular_costo(self, impuesto=0, descuento=0):
        total = self._precio * self._horas
        total += total * impuesto
        total -= total * descuento

        # Log - SOFIA MUÑOZ
        logger.info(f"Costo ReservaSalas: {total}")
        return total

# CLASE HIJA 2 - ALQUILER EQUIPOS (HERENCIA) - YULER VELASQUEZ
class AlquilerEquipos(Servicio):
    """Servicio para alquilar equipos por dias - YULER VELASQUEZ"""

    def __init__(self, codigo, descripcion, precio, dias):
        super().__init__(codigo, descripcion, precio)
        self._dias = None
        self.dias = dias

    @property
    def dias(self):
        return self._dias

    @dias.setter
    def dias(self, valor):
        if not isinstance(valor, (int, float)) or valor <= 0:
            raise DatoInvalidoError("Dias invalidos")
        self._dias = valor

    def calcular_costo(self, impuesto=0, descuento=0):
        total = self._precio * self._dias
        total += total * impuesto
        total -= total * descuento

        # Log - SOFIA MUÑOZ
        logger.info(f"Costo AlquilerEquipos: {total}")
        return total

# CLASE HIJA 3 - ASESORIA (HERENCIA) - YULER VELASQUEZ
class Asesoria(Servicio):
    """Servicio de asesoria por sesiones - YULER VELASQUEZ"""

    def __init__(self, codigo, descripcion, precio, sesiones):
        super().__init__(codigo, descripcion, precio)
        self._sesiones = None
        self.sesiones = sesiones

    @property
    def sesiones(self):
        return self._sesiones

    @sesiones.setter
    def sesiones(self, valor):
        if not isinstance(valor, (int, float)) or valor <= 0:
            raise DatoInvalidoError("Sesiones invalidas")
        self._sesiones = valor

    def calcular_costo(self, impuesto=0, descuento=0):
        total = self._precio * self._sesiones
        total += total * impuesto
        total -= total * descuento

        # Log - SOFIA MUÑOZ
        logger.info(f"Costo Asesoria: {total}")
        return total


# EDWAR CAMILO NARVAEZ VELASCO - CLASE RESERVA + MÉTODOS

class Reserva(EntidadSistema):
    """Clase Reserva con métodos principales - EDWAR CAMILO NARVAEZ VELASCO"""

    def __init__(self, cliente, servicio, duracion):
        self._cliente = cliente
        self._servicio = servicio
        self._duracion = duracion
        self._estado = "Pendiente"

        # Log - SOFIA MUÑOZ
        logger.info("Reserva creada")

    @property
    def cliente(self):
        return self._cliente

    @property
    def servicio(self):
        return self._servicio

    @property
    def duracion(self):
        return self._duracion

    @property
    def estado(self):
        return self._estado

    # MÉTODO CONFIRMAR - EDWAR CAMILO NARVAEZ VELASCO
    def confirmar(self):
        if self._estado == "Cancelada":
            raise DatoInvalidoError(
                "No se puede confirmar una reserva cancelada"
            )

        self._estado = "Confirmada"
        # Log - SOFIA MUÑOZ
        logger.info("Reserva confirmada")

    # MÉTODO CANCELAR - EDWAR CAMILO NARVAEZ VELASCO
    def cancelar(self):
        self._estado = "Cancelada"
        # Log - SOFIA MUÑOZ
        logger.info("Reserva cancelada")

    # MÉTODO PROCESAR - EDWAR CAMILO NARVAEZ VELASCO
    def procesar_reserva(self):
        try:
            total = self._servicio.calcular_costo()
            # Log - SOFIA MUÑOZ
            logger.info(f"Reserva procesada correctamente. Total: {total}")
            return total
        except Exception as error:
            # Manejo de excepciones - SOFIA MUÑOZ
            logger.error(f"Error procesando reserva: {error}")
            raise

    def mostrar_info(self):
        return (
            "\n===== RESERVA =====\n"
            f"{self._cliente.mostrar_info()}\n"
            f"Servicio: {self._servicio.descripcion}\n"
            f"Duracion: {self._duracion}\n"
            f"Estado: {self._estado}"
        )


# TODOS  - MAIN.PY + SIMULACIÓN 10 OPERACIONES

def main():
    """Función principal con simulación de 10 operaciones - TRABAJO EN EQUIPO"""
    print("=== SIMULACIÓN SISTEMA DE RESERVAS - 10 OPERACIONES ===\n")
    
    try:
        # OPERACIÓN 1-3: Creación clientes - VERONICA ORDOÑEZ
        clientes = []
        clientes.append(Cliente("Camilo Velasco", "camilo@gmail.com", "3001234567"))
        clientes.append(Cliente("Maria Lopez", "maria@empresa.com", "3109876543"))
        clientes.append(Cliente("Juan Perez", "juan@gmail.com", "3204567890"))

        # OPERACIÓN 4-7: Creación servicios - YULER VELASQUEZ
        servicios = []
        servicios.append(ReservaSalas("RS01", "Sala empresarial", 50000, 3))
        servicios.append(AlquilerEquipos("AE01", "Proyector", 25000, 2))
        servicios.append(Asesoria("AS01", "Consultoria empresarial", 80000, 1))
        servicios.append(ReservaSalas("RS02", "Sala reuniones", 30000, 4))

        # OPERACIÓN 8-10: Reservas + métodos - EDWAR CAMILO + Integración todos
        reservas = []
        reservas.append(Reserva(clientes[0], servicios[0], "3 horas"))
        reservas.append(Reserva(clientes[1], servicios[1], "2 dias"))
        reservas.append(Reserva(clientes[2], servicios[2], "1 sesion"))

        # Procesar todas las reservas
        total_general = 0
        for i, reserva in enumerate(reservas, 1):
            print(f"\n--- OPERACIÓN {i+7} ---")
            print(reserva.mostrar_info())
            
            reserva.confirmar()
            print(f"Estado: {reserva.estado}")
            
            total = reserva.procesar_reserva()
            total_general += total
            print(f"Costo: ${total:,.0f}")
        
        print(f"\n{'='*50}")
        print(f"TOTAL GENERAL 10 OPERACIONES: ${total_general:,.0f}")
        print(f"{'='*50}")

    # MANEJO EXCEPCIONES - SOFIA MUÑOZ
    except DatoInvalidoError as error:
        print(f"❌ ERROR DE VALIDACION: {error}")
        logger.error(f"Validación fallida: {error}")
    except Exception as error:
        print(f"❌ ERROR GENERAL: {error}")
        logger.error(f"Error general: {error}")


if __name__ == "__main__":
    main()
