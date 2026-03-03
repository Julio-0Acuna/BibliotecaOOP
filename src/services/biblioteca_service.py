from src.dao.libro_dao import LibroDAO

class BibliotecaService:
    def __init__(self):
        self.libro_dao = LibroDAO()

    def listar_libros(self) -> list[dict]:
        return self.libro_dao.listar()