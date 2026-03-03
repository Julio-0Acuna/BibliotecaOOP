from src.dao.usuario_dao import UsuarioDAO
from src.dao.libro_dao import LibroDAO
from src.dao.prestamos_dao import PrestamoDAO

class Menu:
    def __init__(self):
        self.usuario_dao = UsuarioDAO()
        self.libro_dao = LibroDAO()
        self.prestamo_dao = PrestamoDAO()

    def _leer_int(self, msg: str) -> int:
        while True:
            try:
                return int(input(msg))
            except ValueError:
                print("Debes ingresar un número.")

    def start(self):
        op = -1
        while op != 0:
            print("\n=== BIBLIOTECA OOP (Python + MySQL) ===")
            print("1) Usuarios - Crear")
            print("2) Usuarios - Listar")
            print("3) Usuarios - Desactivar")
            print("4) Libros - Crear")
            print("5) Libros - Listar")
            print("6) Libros - Buscar (titulo/autor/isbn)")
            print("7) Libros - Editar datos")
            print("8) Libros - Actualizar copias totales")
            print("9) Préstamos - Prestar libro (SP)")
            print("10) Préstamos - Devolver libro (SP)")
            print("11) Préstamos - Ver activos (vista)")
            print("0) Salir")

            op = self._leer_int("Opción: ")

            # ---- USUARIOS ----
            if op == 1:
                nombre = input("Nombre: ").strip()
                email = input("Email: ").strip()

                if nombre == "":
                    print("Nombre vacío.")
                    continue
                if "@" not in email or "." not in email:
                    print("Email inválido.")
                    continue

                try:
                    uid = self.usuario_dao.crear(nombre, email)
                    print(f"OK: usuario creado con ID {uid}")
                except Exception as e:
                    print("Error:", e)

            elif op == 2:
                solo = input("¿Solo activos? (si/no): ").strip().lower()
                solo_activos = (solo != "no")
                rows = self.usuario_dao.listar(solo_activos)
                if not rows:
                    print("No hay usuarios.")
                else:
                    for r in rows:
                        print(r)

            elif op == 3:
                uid = self._leer_int("Usuario ID a desactivar: ")
                ok = self.usuario_dao.desactivar(uid)
                print("OK: desactivado" if ok else "No existe ese usuario.")

            # ---- LIBROS ----
            elif op == 4:
                titulo = input("Título: ").strip()
                autor = input("Autor: ").strip()
                isbn = input("ISBN (opcional): ").strip()
                if isbn == "":
                    isbn = None
                copias = self._leer_int("Copias totales: ")
                if copias < 0:
                    print("Copias no puede ser negativa.")
                    continue

                try:
                    lid = self.libro_dao.crear(titulo, autor, isbn, copias)
                    print(f"OK: libro creado con ID {lid}")
                except Exception as e:
                    print("Error:", e)

            elif op == 5:
                libros = self.libro_dao.listar()
                if not libros:
                    print("No hay libros registrados.")
                else:
                    print("\n--- LIBROS ---")
                    for l in libros:
                        print(
                            f"ID: {l['id']} | {l['titulo']} - {l['autor']} "
                            f"| Disp: {l['copias_disponibles']}/{l['copias_totales']} | ISBN: {l['isbn']}"
                        )

            elif op == 6:
                texto = input("Buscar: ").strip()
                rows = self.libro_dao.buscar(texto)
                if not rows:
                    print("Sin resultados.")
                else:
                    for l in rows:
                        print(
                            f"ID: {l['id']} | {l['titulo']} - {l['autor']} "
                            f"| Disp: {l['copias_disponibles']}/{l['copias_totales']} | ISBN: {l['isbn']}"
                        )

            elif op == 7:
                lid = self._leer_int("Libro ID a editar: ")
                titulo = input("Nuevo título: ").strip()
                autor = input("Nuevo autor: ").strip()
                isbn = input("Nuevo ISBN (opcional): ").strip()
                if isbn == "":
                    isbn = None
                ok = self.libro_dao.actualizar_datos(lid, titulo, autor, isbn)
                print("OK: actualizado" if ok else "No existe ese libro.")

            elif op == 8:
                lid = self._leer_int("Libro ID: ")
                nuevas = self._leer_int("Nuevas copias totales: ")
                if nuevas < 0:
                    print("Totales no puede ser negativa.")
                    continue
                ok, msg = self.libro_dao.actualizar_copias_totales(lid, nuevas)
                print("OK:" if ok else "ERROR:", msg)

            # ---- PRESTAMOS (SP + VISTA) ----
            elif op == 9:
                uid = self._leer_int("Usuario ID: ")
                lid = self._leer_int("Libro ID: ")
                res = self.prestamo_dao.prestar(uid, lid)
                print(res)

            elif op == 10:
                pid = self._leer_int("Prestamo ID: ")
                res = self.prestamo_dao.devolver(pid)
                print(res)

            elif op == 11:
                activos = self.prestamo_dao.listar_activos()
                if not activos:
                    print("No hay préstamos activos.")
                else:
                    print("\n--- PRÉSTAMOS ACTIVOS ---")
                    for p in activos:
                        print(
                            f"Prestamo ID: {p['prestamo_id']} | "
                            f"Usuario: {p['usuario_nombre']} | "
                            f"Libro: {p['libro_titulo']} | "
                            f"Fecha: {p['fecha_prestamo']}"
                        )

            elif op == 0:
                print("Chao.")
            else:
                print("Opción inválida.")
