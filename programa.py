
def validar_codigo(codigo):
    return codigo.strip() != "" and len(codigo.strip()) >= 6



def registrar_solicitud():
    codigo = input("Código de estudiante: ")

    if not validar_codigo(codigo):
        print("Error: el código debe tener al menos 6 caracteres.")
        return

    nombre = input("Nombre del estudiante: ")
    tipo = input("Tipo de consulta: ")
    descripcion = input("Descripción breve: ")

    print("\nSolicitud registrada:")
    print("Código:", codigo)
    print("Nombre:", nombre)
    print("Tipo de consulta:", tipo)
    print("Descripción:", descripcion)


registrar_solicitud()