def registrar_solicitud():
    codigo = input("Código de estudiante: ")
    nombre = input("Nombre del estudiante: ")
    tipo = input("Tipo de consulta: ")
    descripcion = input("Descripción breve: ")

    print("\nSolicitud registrada:")
    print("Código:", codigo)
    print("Nombre:", nombre)
    print("Tipo de consulta:", tipo)
    print("Descripción:", descripcion)


registrar_solicitud()