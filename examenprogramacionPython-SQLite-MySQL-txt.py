import sqlite3


#menu
def menu():
    print("Escoge una opcion: ")
    print("1.-Insertar un registro")
    print("2.-Mostrar registros")
    print("3.-Modificar un registro")
    print("4.-Eliminar un registro")
    print("5.-Buscar un registro")
    print("6.-Salir")
    opcion = input("Escoge una opcion: ")

    #if elif
    if opcion == "1":
        print("Insertamos un registro")
        nombre = input("Introduce el nombre del cliente: ")
        apellido = input("Introduce el apellido del cliente: ")
        telefono = input("Introduce el telefono del cliente: ")
        email = input("Introduce el email del cliente: ")
        direccion = input("Introduce la direccion del cliente: ")
        conexion = sqlite3.connect("clientes.db")
        cursor = conexion.cursor()
        peticion = "INSERT INTO clientes VALUES (NULL,'"+nombre+"','"+apellido+"','"+telefono+"','"+email+"','"+direccion+"')"    
        cursor.execute(peticion)
        conexion.commit()
        conexion.close()
        print("Tu resgistro de guardo correctamente")
    elif opcion == "2":
        print("Mostramos los registros")
        conexion = sqlite3.connect("discos.db")
        cursor = conexion.cursor()
        peticion = "SELECT * FROM discos"
        cursor.execute(peticion)
        while True:
            fila = cursor.fetchone()
            if fila is None:
                break
            print(fila)
        conexion.commit()
        conexion.close()
    elif opcion == "3":
        print("Modificamos los registros")
    elif opcion == "4":
        print("Eliminamos los registros")
    elif opcion == "5":
        print("Buscamos los registros")
    elif opcion == "6":
        print("Salimos del programa")
    #menurecursivo
    menu()
menu()
