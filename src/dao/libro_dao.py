from src.db.connection import get_conn

class LibroDAO:
    def crear(self, titulo: str, autor: str, isbn: str | None, copias_totales: int) -> int:
        conn = get_conn()
        try:
            cur = conn.cursor()
            cur.execute(
                """
                INSERT INTO libros (titulo, autor, isbn, copias_totales, copias_disponibles)
                VALUES (%s, %s, %s, %s, %s)
                """,
                (titulo.strip(), autor.strip(), isbn, copias_totales, copias_totales),
            )
            conn.commit()
            return cur.lastrowid
        finally:
            conn.close()

    def listar(self) -> list[dict]:
        conn = get_conn()
        try:
            cur = conn.cursor(dictionary=True)
            cur.execute("""
                SELECT id, titulo, autor, isbn, copias_totales, copias_disponibles
                FROM libros
                ORDER BY id
            """)
            return cur.fetchall()
        finally:
            conn.close()

    def buscar(self, texto: str) -> list[dict]:
        conn = get_conn()
        try:
            cur = conn.cursor(dictionary=True)
            like = f"%{texto.strip()}%"
            cur.execute("""
                SELECT id, titulo, autor, isbn, copias_totales, copias_disponibles
                FROM libros
                WHERE titulo LIKE %s OR autor LIKE %s OR isbn LIKE %s
                ORDER BY id
            """, (like, like, like))
            return cur.fetchall()
        finally:
            conn.close()

    def actualizar_datos(self, libro_id: int, titulo: str, autor: str, isbn: str | None) -> bool:
        conn = get_conn()
        try:
            cur = conn.cursor()
            cur.execute("""
                UPDATE libros
                SET titulo=%s, autor=%s, isbn=%s
                WHERE id=%s
            """, (titulo.strip(), autor.strip(), isbn, libro_id))
            conn.commit()
            return cur.rowcount > 0
        finally:
            conn.close()

    def actualizar_copias_totales(self, libro_id: int, nuevas_totales: int) -> tuple[bool, str]:
        """
        Regla: no puedes bajar copias_totales por debajo de las copias prestadas.
        prestadas = copias_totales - copias_disponibles
        """
        conn = get_conn()
        try:
            cur = conn.cursor(dictionary=True)
            cur.execute("""
                SELECT copias_totales, copias_disponibles
                FROM libros
                WHERE id=%s
            """, (libro_id,))
            row = cur.fetchone()
            if not row:
                return False, "Libro no existe"

            tot = int(row["copias_totales"])
            disp = int(row["copias_disponibles"])
            prestadas = tot - disp

            if nuevas_totales < prestadas:
                return False, f"No se puede: hay {prestadas} copias prestadas."

            nueva_disp = nuevas_totales - prestadas

            cur2 = conn.cursor()
            cur2.execute("""
                UPDATE libros
                SET copias_totales=%s, copias_disponibles=%s
                WHERE id=%s
            """, (nuevas_totales, nueva_disp, libro_id))
            conn.commit()
            return (cur2.rowcount > 0), "Copias actualizadas"
        finally:
            conn.close()
