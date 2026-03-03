# BibliotecaOOP

BibliotecaOOP es un sistema de gestión de biblioteca desarrollado en Python aplicando Programación Orientada a Objetos (OOP) y persistencia en MySQL. El proyecto permite administrar usuarios y libros, así como gestionar préstamos y devoluciones mediante Stored Procedures, asegurando el control de stock y la integridad de los datos.

## Descripción

Este sistema de consola simula el funcionamiento básico de una biblioteca real. Está estructurado por capas (Models, DAO, UI y DB), separando la lógica de negocio del acceso a datos y de la interfaz de usuario.

El objetivo del proyecto es reforzar conceptos de arquitectura backend, conexión a bases de datos relacionales y buenas prácticas en organización de código.

## Funcionalidades

Gestión de Usuarios:
- Crear usuario
- Listar usuarios (activos o todos)
- Desactivar usuario

Gestión de Libros:
- Crear libro
- Listar libros
- Buscar libro por título, autor o ISBN
- Editar datos del libro
- Actualizar cantidad total de copias con validación de préstamos activos

Gestión de Préstamos:
- Prestar libro (Stored Procedure sp_prestar_libro)
- Devolver libro (Stored Procedure sp_devolver_libro)
- Ver préstamos activos (vista vw_prestamos_activos)
- Control automático de stock disponible

## Tecnologías Utilizadas

- Python 3
- MySQL
- MySQL Workbench
- mysql-connector-python

## Base de Datos

El sistema utiliza la base de datos llamada biblioteca_oop.

Incluye:
- Tablas: usuarios, libros, prestamos
- Vista: vw_prestamos_activos
- Stored Procedures: sp_prestar_libro y sp_devolver_libro

Los procedimientos almacenados gestionan validaciones, transacciones y actualización automática del stock disponible.

## Instalación

1. Clonar el repositorio.
2. Instalar dependencias con:
   pip install -r requirements.txt
3. Crear la base de datos ejecutando el script SQL correspondiente.
4. Configurar las credenciales en src/config.py.
5. Ejecutar el sistema desde la raíz del proyecto con:
   python -m src.main

## Estructura del Proyecto

src/
- models: clases del dominio (Usuario, Libro, Prestamo)
- dao: acceso a datos y ejecución de consultas SQL
- db: configuración y conexión a MySQL
- ui: menú de consola
- main.py: punto de entrada del sistema

## Objetivo

Proyecto académico orientado a la práctica de programación orientada a objetos, arquitectura por capas e integración con bases de datos relacionales en un entorno similar al desarrollo profesional.

Autor: Julio Acuña.
