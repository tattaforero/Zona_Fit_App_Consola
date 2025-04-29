from cliente import Cliente
from cliente_dao import ClienteDAO

print('Bienvenido al Sistema de Gestión de Clientes Zona Fit.')
opcion = None
    
while opcion != 6:
    print(f''' Menú:
    1. Listar clientes
    2. Consultar cliente por ID
    3. Crear cliente
    4. Actualizar cliente
    5. Eliminar cliente
    6. Salir''')

    try:
        opcion = int(input('Digita una opción (1-6): '))
    except ValueError:
        print('❌ Error: Ingresa un número válido.')
        opcion = None
        continue


    if opcion == 1:
        clientes = ClienteDAO.seleccionar()
        print(f'\n*** Listado de Clientes ***')
        for cliente in clientes:
            print(cliente)
    elif opcion == 2:
        try:
            id_cliente_var = int(input('Digita el id del cliente a consultar: '))
        except ValueError:
            print('❌ Error: El ID debe ser un número.')
            continue
        # Verificamos sí el cliente existe
        cliente_existente = ClienteDAO.seleccionar_por_id(id_cliente_var)
        if cliente_existente:
            print(cliente_existente)
        else: 
            print(f'El cliente con ID {id_cliente_var} no existe.')
    elif opcion == 3:
        nombre_var = input('Digite el nombre: ')
        apellido_var = input('Digite el apellido: ')
        membresia_var = int(input('Digite la membresia: '))
        nuevo_cliente = Cliente(nombre=nombre_var, apellido=apellido_var, membresia=membresia_var)
        clientes_insertados = ClienteDAO.insertar(nuevo_cliente)
        print(f'Cliente creado correctamente: {clientes_insertados}')
    elif opcion == 4:
        try:
            id_cliente_var = int(input('Digita el id del cliente a actualizar: '))
        except ValueError:
            print('❌ Error: El ID debe ser un número.')
            continue
        # Verificamos sí el cliente existe
        cliente_existente = ClienteDAO.seleccionar_por_id(id_cliente_var)
        if cliente_existente:
            nombre_var = input('Digite el nombre: ')
            apellido_var = input('Digite el apellido: ')
            membresia_var = int(input('Digite la membresia: '))
            cliente = Cliente(id_cliente_var,nombre_var,apellido_var,membresia_var)
            clientes_actualizados = ClienteDAO.actualizar(cliente)
            print(f'Cliente actualizado correctamente: {clientes_actualizados}')
        else: 
            print(f'El cliente con ID {id_cliente_var} no existe.')
    elif opcion == 5:
        try:
            id_cliente_var = int(input('Digita el id del cliente a consultar: '))
        except ValueError:
            print('❌ Error: El ID debe ser un número.')
            continue
        # Verificamos si existe
        cliente_existente = ClienteDAO.seleccionar_por_id(id_cliente_var)
        cliente = Cliente(id=id_cliente_var)
        if cliente_existente:
            clientes_eliminados = ClienteDAO.eliminar(cliente)
            print(f'Cliente eliminado correctamente: {clientes_eliminados}')
        else: 
            print(f'El cliente con ID {id_cliente_var} no existe.')
    elif opcion == 6:
        print('Hasta pronto!')
        break 
    else:
        print(f'Opción inválida:{opcion}')
            



       



