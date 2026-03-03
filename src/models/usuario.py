from dataclasses import dataclass

@dataclass
class Usuario:
    id: int | None
    nombre: str
    email: str
    activo: int = 1