from dataclasses import dataclass

@dataclass
class Prestamo:
    id: int | None
    usuario_id: int
    libro_id: int
    devuelto: int = 0