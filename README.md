# Zona Fit - Gestión de Clientes

Aplicación de consola para gestionar los clientes de un establecimiento de fitness, con operaciones CRUD (Crear, Leer, Actualizar, Eliminar) en una base de datos MySQL.

**Zona Fit** es una aplicación que permite gestionar los datos de los clientes de un gimnasio.

La tabla **Clientes** tiene los siguientes campos:
- **Nombre**
- **Apellido**
- **Membresía** (Tipo de membresía del cliente)

La aplicación es **solo de consola**, no tiene interfaz gráfica, y permite realizar las operaciones a través de la terminal.

## Instalación

### 1. Clona el repositorio
git clone https://github.com/tattaforero/Zona_Fit_CRUD.git
### 2. Instala la libreria para conexión a MySQL
pip install mysql-connector-python
### 3. Configura la base de datos MySQL
Crea la base de datos llamada zona_fit_db en MySQL.
Restaura la base de datos con el archivo Zona_Fit_DB.sql
Configura la conexión a la base de datos: Asegúrate de que los parámetros de conexión (usuario, contraseña) estén correctos en el archivo de configuración de tu proyecto.

## Uso
1. Ejecuta la aplicación
Hay 2 archivos para ejecución: app_clientes.py y app_clientes_zona_fit.py. Los 2 archivos tienen la misma función, varía la propuesta en organización del código.

2. La aplicación te mostrará un menú en consola con las siguientes opciones:

Menú:\n
    1. Listar clientes
    2. Consultar cliente por ID
    3. Crear cliente
    4. Actualizar cliente
    5. Eliminar cliente
    6. Salir

## Contribución
Si deseas contribuir al proyecto, sigue estos pasos:

Haz un fork del repositorio.
Crea una nueva rama (git checkout -b nombre-de-la-rama).
Realiza tus cambios.
Haz un commit (git commit -am 'Descripción de lo que hiciste').
Empuja tus cambios (git push origin nombre-de-la-rama).
Abre un pull request explicando los cambios realizados.

## Este proyecto fue creado como actividad de curso Universidad Python con la IA de ChatGPT - De Cero a Experto!

