from abc import ABC, abstractmethod
import logging
import re


logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)
logger = logging.getLogger(__name__)


class DatoInvalidoError(Exception):
    """Excepcion para datos invalidos del sistema."""


class EntidadSistema(ABC):
    """Clase abstracta general del sistema."""

    @abstractmethod
    def mostrar_info(self):
        pass


class Cliente(EntidadSistema):
    """Clase Cliente con encapsulacion y validacion de datos."""

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
        if not isinstance(valor, str) or len(valor.strip()) < 3:
            raise DatoInvalidoError("Nombre invalido: minimo 3 caracteres")
        self._nombre = valor.strip()

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        patron = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if not isinstance(valor, str) or not re.match(patron, valor):
            raise DatoInvalidoError(f"Email invalido: {valor}")
        self._email = valor.strip()

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


class Servicio(EntidadSistema, ABC):
    """Clase abstracta base para los servicios."""

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


class ReservaSalas(Servicio):
    """Servicio para reservar salas por horas."""

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

        logger.info(f"Costo ReservaSalas: {total}")
        return total


class AlquilerEquipos(Servicio):
    """Servicio para alquilar equipos por dias."""

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

        logger.info(f"Costo AlquilerEquipos: {total}")
        return total


class Asesoria(Servicio):
    """Servicio de asesoria por sesiones."""

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

        logger.info(f"Costo Asesoria: {total}")
        return total

#Sofia Muñoz
class Reserva:
    """Clase Reserva."""

    def __init__(self, cliente, servicio, duracion):
        self._cliente = cliente
        self._servicio = servicio
        self._duracion = duracion
        self._estado = "Pendiente"

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
# Sofia Muñoz
    def confirmar(self):
        if self._estado == "Cancelada":
            raise DatoInvalidoError(
                "No se puede confirmar una reserva cancelada"
            )

        self._estado = "Confirmada"
        logger.info("Reserva confirmada")
# Sofia Muñoz
    def cancelar(self):
        self._estado = "Cancelada"
        logger.info("Reserva cancelada")
# Sofia Muñoz
    def procesar_reserva(self):
        try:
            total = self._servicio.calcular_costo()
            logger.info(f"Reserva procesada correctamente. Total: {total}")
            return total
        except Exception as error:
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


def main():
    try:
        cliente1 = Cliente(
            "Camilo Velasco",
            "camilo@gmail.com",
            "3001234567"
        )

        servicio1 = ReservaSalas(
            "RS01",
            "Sala empresarial",
            50000,
            3
        )

        reserva1 = Reserva(
            cliente1,
            servicio1,
            "3 horas"
        )

        print(cliente1.mostrar_info())
        print(servicio1.mostrar_info())
        print(reserva1.mostrar_info())

        reserva1.confirmar()
        print("\nEstado actual:", reserva1.estado)

        total = reserva1.procesar_reserva()
        print(f"\nCosto final: ${total:,.0f}")

    except DatoInvalidoError as error:
        print(f"ERROR DE VALIDACION: {error}")

    except Exception as error:
        print(f"ERROR GENERAL: {error}")


if __name__ == "__main__":
    main()
