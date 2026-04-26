from abc import ABC, abstractmethod
from datetime import date
from enum import Enum


class TipoBeca(Enum):
    EXCELENCIA = "Excelencia"
    SOCIOECONOMICA = "Socioeconómica"
    DEPORTIVA = "Deportiva"


class EstadoPago(Enum):
    PENDIENTE = "Pendiente"
    PAGADO = "Pagado"
    VENCIDO = "Vencido"


class Persona(ABC):
    def __init__(self, rut, nombre, apellido, fecha_nacimiento):
        self._rut = rut
        self._nombre = nombre
        self._apellido = apellido
        self._fecha_nacimiento = fecha_nacimiento

    @property
    def rut(self):
        return self._rut

    @property
    def nombre_completo(self):
        return f"{self._nombre} {self._apellido}"

    @abstractmethod
    def mostrar_resumen(self):
        pass


class Estudiante(Persona):
    def __init__(self, rut, nombre, apellido, fecha_nacimiento, codigo, carrera):
        super().__init__(rut, nombre, apellido, fecha_nacimiento)
        self._codigo = codigo
        self._carrera = carrera
        self._inscripciones = []
        self.beca = None
        self._pagos = []

    @property
    def carrera(self):
        return self._carrera

    @property
    def codigo(self):
        return self._codigo

    def agregar_inscripcion(self, insc):
        self._inscripciones.append(insc)

    def obtener_inscripciones(self):
        return self._inscripciones.copy()

    def agregar_pago(self, pago):
        self._pagos.append(pago)

    def obtener_pagos(self):
        return self._pagos.copy()

    def mostrar_resumen(self):
        print(f"{self.nombre_completo} - {self.carrera}")


class Docente(Persona):
    def __init__(self, rut, nombre, apellido, fecha_nacimiento, depto):
        super().__init__(rut, nombre, apellido, fecha_nacimiento)
        self._depto = depto
        self.secciones = []

    def asignar_seccion(self, seccion):
        if seccion not in self.secciones:
            self.secciones.append(seccion)
            seccion.docente = self

    def mostrar_resumen(self):
        print(f"{self.nombre_completo} - {self._depto}")


class Beca:
    def __init__(self, tipo, porcentaje, inicio, fin):
        self.tipo = tipo
        self._porcentaje = porcentaje
        self.inicio = inicio
        self.fin = fin

    @property
    def porcentaje(self):
        return self._porcentaje

    def es_valida(self):
        return self.inicio <= date.today() <= self.fin


class Arancel:
    def __init__(self, monto_base, vencimiento):
        self._monto_base = monto_base
        self.vencimiento = vencimiento

    @property
    def monto_base(self):
        return self._monto_base

    def calcular_monto(self, beca=None):
        if beca and beca.es_valida():
            descuento = self._monto_base * (beca.porcentaje / 100)
            return round(self._monto_base - descuento, 2)
        return self._monto_base


class Pago:
    def __init__(self, estudiante, arancel):
        self._estudiante = estudiante
        self._arancel = arancel
        self._estado = EstadoPago.PENDIENTE
        self._fecha_pago = None

    @property
    def monto(self):
        return self._arancel.calcular_monto(self._estudiante.beca)

    @property
    def estado(self):
        return self._estado

    def pagar(self):
        if self._estado == EstadoPago.PENDIENTE:
            self._estado = EstadoPago.PAGADO
            self._fecha_pago = date.today()

    def verificar_vencimiento(self):
        if self._estado == EstadoPago.PENDIENTE and date.today() > self._arancel.vencimiento:
            self._estado = EstadoPago.VENCIDO

    def mostrar_detalle(self):
        beca_info = f" (beca {self._estudiante.beca.porcentaje}%)" if self._estudiante.beca else ""
        print(f"  Monto: ${self.monto:,.0f}{beca_info} | Estado: {self._estado.value}")


class Horario:
    def __init__(self, dia, inicio, fin):
        self.dia = dia
        self.inicio = inicio
        self.fin = fin

    def hay_choque(self, otro):
        if self.dia != otro.dia:
            return False
        return not (self.fin <= otro.inicio or self.inicio >= otro.fin)

    def __str__(self):
        return f"{self.dia} {self.inicio}:00-{self.fin}:00"


class Asignatura:
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre


class Seccion:
    def __init__(self, codigo, asignatura, horario):
        self.codigo = codigo
        self.asignatura = asignatura
        self.horario = horario
        self._inscripciones = []
        self.docente = None

    def obtener_inscripciones(self):
        return self._inscripciones.copy()

    def inscribir(self, estudiante):
        for insc in estudiante.obtener_inscripciones():
            if self.horario.hay_choque(insc.seccion.horario):
                raise ValueError("Choque de horario")

        nueva = Inscripcion(estudiante, self)
        self._inscripciones.append(nueva)
        estudiante.agregar_inscripcion(nueva)

    def mostrar_lista(self):
        docente_nombre = self.docente.nombre_completo if self.docente else "Sin asignar"
        print(f"  Sección {self.codigo} | {self.asignatura.nombre} | {self.horario} | Docente: {docente_nombre}")
        for insc in self._inscripciones:
            print(f"    - {insc.estudiante.nombre_completo} [{insc.estado()}]")


class Inscripcion:
    def __init__(self, estudiante, seccion):
        self.estudiante = estudiante
        self.seccion = seccion
        self._notas = []
        self._examen = None

    def agregar_nota(self, n):
        if 1 <= n <= 7:
            self._notas.append(n)

    def registrar_examen(self, n):
        if 1 <= n <= 7:
            self._examen = n

    def final(self):
        if not self._notas or self._examen is None:
            return 0
        prom = sum(self._notas) / len(self._notas)
        return round(prom * 0.6 + self._examen * 0.4, 1)

    def estado(self):
        nf = self.final()
        if nf == 0:
            return "Pendiente"
        return "Aprobado" if nf >= 4 else "Reprobado"

    def mostrar_notas(self):
        print(f"  Notas: {self._notas} | Examen: {self._examen} | Final: {self.final()} | {self.estado()}")


# ---------- DATOS ----------

def poblar():
    ests = [
        Estudiante("1-9", "Freddy", "Caneo", date(1998, 5, 19), "A1", "Informática"),
        Estudiante("2-7", "Matias", "Vasquez", date(2002, 5, 16), "A2", "Informática")
    ]

    docs = [
        Docente("9-9", "Pablo", "Lastra", date(1980, 5, 10), "Computación"),
        Docente("8-7", "Jesus", "Pacheco", date(1975, 3, 22), "Matemáticas")
    ]

    secs = [
        Seccion("S1", Asignatura("POO", "Programación OO"), Horario("Lunes", 10, 12)),
        Seccion("S2", Asignatura("BD", "Base de Datos"), Horario("Lunes", 13, 15)),
        Seccion("S3", Asignatura("MAT", "Matemáticas"), Horario("Martes", 9, 11))
    ]

    beca_mat = Beca(TipoBeca.EXCELENCIA, 50, date(2025, 1, 1), date(2026, 12, 31))
    ests[0].beca = beca_mat

    docs[0].asignar_seccion(secs[0])
    docs[0].asignar_seccion(secs[1])
    docs[1].asignar_seccion(secs[2])

    arancel = Arancel(500000, date(2026, 6, 30))
    for e in ests:
        p = Pago(e, arancel)
        e.agregar_pago(p)

    return ests, docs, secs


# ---------- MENÚ ----------

def menu():
    estudiantes, docentes, secciones = poblar()

    while True:
        print("\n========== SISTEMA ACADÉMICO ==========")
        print("1. Listar estudiantes")
        print("2. Listar secciones con docentes")
        print("3. Inscribir estudiante en sección")
        print("4. Ver horarios")
        print("5. Registrar notas")
        print("6. Ver calificaciones de estudiante")
        print("7. Ver pagos de estudiante")
        print("8. Pagar arancel")
        print("9. Listar docentes")
        print("0. Salir")

        op = input("\nOpción: ")

        try:
            if op == "1":
                print()
                for i, e in enumerate(estudiantes):
                    beca_str = f"[Beca {e.beca.tipo.value}]" if e.beca else ""
                    print(f"  {i} - {e.nombre_completo} | {e.carrera} {beca_str}")

            elif op == "2":
                print()
                for s in secciones:
                    s.mostrar_lista()

            elif op == "3":
                for i, e in enumerate(estudiantes):
                    print(f"  {i} - {e.nombre_completo}")
                ei = int(input("Índice estudiante: "))
                for i, s in enumerate(secciones):
                    print(f"  {i} - {s.asignatura.nombre} ({s.horario})")
                si = int(input("Índice sección: "))
                secciones[si].inscribir(estudiantes[ei])
                print("Inscripción realizada correctamente.")

            elif op == "4":
                print()
                for s in secciones:
                    docente_str = s.docente.nombre_completo if s.docente else "Sin asignar"
                    print(f"  {s.asignatura.nombre} | {s.horario} | {docente_str}")

            elif op == "5":
                for i, e in enumerate(estudiantes):
                    print(f"  {i} - {e.nombre_completo}")
                ei = int(input("Índice estudiante: "))
                est = estudiantes[ei]
                inscs = est.obtener_inscripciones()
                if not inscs:
                    print("Sin inscripciones.")
                else:
                    for i, insc in enumerate(inscs):
                        print(f"  {i} - {insc.seccion.asignatura.nombre}")
                    ii = int(input("Índice inscripción: "))
                    insc = inscs[ii]
                    tipo = input("¿Agregar (n)ota o (e)xamen? ").strip().lower()
                    valor = float(input("Valor (1.0 - 7.0): "))
                    if tipo == "n":
                        insc.agregar_nota(valor)
                        print("Nota registrada.")
                    elif tipo == "e":
                        insc.registrar_examen(valor)
                        print("Examen registrado.")

            elif op == "6":
                for i, e in enumerate(estudiantes):
                    print(f"  {i} - {e.nombre_completo}")
                ei = int(input("Índice estudiante: "))
                est = estudiantes[ei]
                inscs = est.obtener_inscripciones()
                if not inscs:
                    print("Sin inscripciones registradas.")
                else:
                    print(f"\nCalificaciones de {est.nombre_completo}:")
                    for insc in inscs:
                        print(f"  {insc.seccion.asignatura.nombre}:")
                        insc.mostrar_notas()

            elif op == "7":
                for i, e in enumerate(estudiantes):
                    print(f"  {i} - {e.nombre_completo}")
                ei = int(input("Índice estudiante: "))
                est = estudiantes[ei]
                pagos = est.obtener_pagos()
                print(f"\nPagos de {est.nombre_completo}:")
                for p in pagos:
                    p.verificar_vencimiento()
                    p.mostrar_detalle()

            elif op == "8":
                for i, e in enumerate(estudiantes):
                    print(f"  {i} - {e.nombre_completo}")
                ei = int(input("Índice estudiante: "))
                est = estudiantes[ei]
                pagos = [p for p in est.obtener_pagos() if p.estado == EstadoPago.PENDIENTE]
                if not pagos:
                    print("Sin pagos pendientes.")
                else:
                    pagos[0].pagar()
                    print(f"Pago realizado. Monto: ${pagos[0].monto:,.0f}")

            elif op == "9":
                print()
                for i, d in enumerate(docentes):
                    secs_str = ", ".join(s.asignatura.nombre for s in d.secciones) or "Ninguna"
                    print(f"  {i} - {d.nombre_completo} | Secciones: {secs_str}")

            elif op == "0":
                print("Saliendo del sistema.")
                break

        except (IndexError, ValueError) as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    menu()