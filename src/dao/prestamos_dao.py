from src.db.connection import get_conn

class PrestamoDAO:
    def prestar(self, usuario_id: int, libro_id: int) -> dict:
        conn = get_conn()
        try:
            cur = conn.cursor(dictionary=True)
            cur.callproc("sp_prestar_libro", [usuario_id, libro_id])

            result = None
            for r in cur.stored_results():
                rows = r.fetchall()
                if rows:
                    result = rows[0]
            return result or {"mensaje": "Sin respuesta", "prestamo_id": None}
        finally:
            conn.close()

    def devolver(self, prestamo_id: int) -> dict:
        conn = get_conn()
        try:
            cur = conn.cursor(dictionary=True)
            cur.callproc("sp_devolver_libro", [prestamo_id])

            result = None
            for r in cur.stored_results():
                rows = r.fetchall()
                if rows:
                    result = rows[0]
            return result or {"mensaje": "Sin respuesta"}
        finally:
            conn.close()

    def listar_activos(self) -> list[dict]:
        conn = get_conn()
        try:
            cur = conn.cursor(dictionary=True)
            cur.execute("SELECT * FROM vw_prestamos_activos ORDER BY prestamo_id DESC")
            return cur.fetchall()
        finally:
            conn.close()