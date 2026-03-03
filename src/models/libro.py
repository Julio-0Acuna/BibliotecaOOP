from dataclasses import dataclass

@dataclass
class Libro:
    id: int | None
    titulo: str
    autor: str
    isbn: str | None
    copias_totales: int
    copias_disponibles: int