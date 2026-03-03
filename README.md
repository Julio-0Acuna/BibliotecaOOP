# BibliotecaOOP (Python + MySQL)

Proyecto de consola desarrollado en Python aplicando Programación Orientada a Objetos (OOP) y persistencia en MySQL.
Incluye Stored Procedures para manejar préstamos y devoluciones con control de stock.

## Funcionalidades
- Listar libros
- Prestar libro (Stored Procedure `sp_prestar_libro`)
- Devolver libro (Stored Procedure `sp_devolver_libro`)
- Ver préstamos activos (vista `vw_prestamos_activos`)
- CRUD de usuarios (DAO)

## Tecnologías
- Python 3
- MySQL (MySQL Workbench)
- mysql-connector-python

## Base de datos
1. Ejecuta el script SQL que crea la base `biblioteca_oop`, tablas, vista y procedimientos.
2. Verifica que existan:
   - Tablas: `usuarios`, `libros`, `prestamos`
   - Vista: `vw_prestamos_activos`
   - SP: `sp_prestar_libro`, `sp_devolver_libro`

## Configuración
Edita `src/config.py` con tus credenciales:
- host, user, password, database

## Instalación
```bash
pip install -r requirements.txt