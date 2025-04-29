from cliente import Cliente
from cliente_dao import ClienteDAO

def listar_clientes():
    clientes = ClienteDAO.seleccionar()
    print(f'\n*** Listado de Clientes ***\n')
    for cliente in clientes:
        print(cliente)
        print()

def consultar_cliente_por_id():
    try:
        id_cliente_var = int(input('\nDigita el id del cliente a consultar: '))
    except ValueError:
        print('Error: El ID debe ser un número.\n')
        return
    # Verificamos sí el cliente existe
    cliente_existente = ClienteDAO.seleccionar_por_id(id_cliente_var)
    if cliente_existente:
        print(cliente_existente, '\n')
    else: 
        print(f'El cliente con ID {id_cliente_var} no existe.\n')

def crear_cliente():
    nombre_var = input('\nDigite el nombre: ')
    apellido_var = input('Digite el apellido: ')
    membresia_var = int(input('Digite la membresia:\n'))
    nuevo_cliente = Cliente(nombre=nombre_var, apellido=apellido_var, membresia=membresia_var)
    clientes_insertados = ClienteDAO.insertar(nuevo_cliente)
    print(f'Cliente creado correctamente: {clientes_insertados}')

def actualizar_cliente():
    try:
        id_cliente_var = int(input('\nDigita el id del cliente a actualizar: '))
    except ValueError:
        print('Error: El ID debe ser un número.\n')
        return
    # Verificamos sí el cliente existe
    cliente_existente = ClienteDAO.seleccionar_por_id(id_cliente_var)
    if cliente_existente:
        nombre_var = input('\nDigite el nombre: ')
        apellido_var = input('Digite el apellido: ')
        membresia_var = int(input('Digite la membresia: '))
        cliente = Cliente(id_cliente_var,nombre_var,apellido_var,membresia_var)
        clientes_actualizados = ClienteDAO.actualizar(cliente)
        print(f'Cliente actualizado correctamente: {clientes_actualizados}\n')
    else: 
        print(f'El cliente con ID {id_cliente_var} no existe.\n')

def eliminar_cliente():
    try:
        id_cliente_var = int(input('\nDigita el id del cliente a eliminar: '))
    except ValueError:
        print('Error: El ID debe ser un número.\n')
        return
    # Verificamos si existe
    cliente_existente = ClienteDAO.seleccionar_por_id(id_cliente_var)
    cliente = Cliente(id=id_cliente_var)
    if cliente_existente:
        clientes_eliminados = ClienteDAO.eliminar(cliente)
        print(f'Cliente eliminado correctamente: {clientes_eliminados}\n')
    else: 
        print(f'El cliente con ID {id_cliente_var} no existe.\n')


print('Bienvenido al Sistema de Gestión de Clientes Zona Fit.\n')
opcion = None
    
while opcion != 6:
    print(f'''Menú:\n
    1. Listar clientes
    2. Consultar cliente por ID
    3. Crear cliente
    4. Actualizar cliente
    5. Eliminar cliente
    6. Salir\n''')

    try:
        opcion = int(input('Digita una opción (1-6): '))
    except ValueError:
        print('Error: Ingresa un número válido.\n')
        opcion = None
        continue

    if opcion == 1:
        listar_clientes()
        
    elif opcion == 2:
        consultar_cliente_por_id()

    elif opcion == 3:
        crear_cliente()
        
    elif opcion == 4:
        actualizar_cliente()
        
    elif opcion == 5:
        eliminar_cliente()

    elif opcion == 6:
        print('Hasta pronto!')
        break 
    else:
        print(f'Opción inválida:{opcion}\n')
            



       



