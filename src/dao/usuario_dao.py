from src.db.connection import get_conn

class UsuarioDAO:
    def crear(self, nombre: str, email: str) -> int:
        conn = get_conn()
        try:
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO usuarios (nombre, email, activo) VALUES (%s, %s, 1)",
                (nombre.strip(), email.strip().lower()),
            )
            conn.commit()
            return cur.lastrowid
        finally:
            conn.close()

    def listar(self, solo_activos: bool = True) -> list[dict]:
        conn = get_conn()
        try:
            cur = conn.cursor(dictionary=True)
            if solo_activos:
                cur.execute("SELECT id, nombre, email, activo FROM usuarios WHERE activo=1 ORDER BY id")
            else:
                cur.execute("SELECT id, nombre, email, activo FROM usuarios ORDER BY id")
            return cur.fetchall()
        finally:
            conn.close()

    def desactivar(self, usuario_id: int) -> bool:
        conn = get_conn()
        try:
            cur = conn.cursor()
            cur.execute("UPDATE usuarios SET activo=0 WHERE id=%s", (usuario_id,))
            conn.commit()
            return cur.rowcount > 0
        finally:
            conn.close()
