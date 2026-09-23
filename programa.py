
def validar_codigo(codigo):
    return codigo.strip() != "" and len(codigo.strip()) >= 6



def validar_tipo_consulta(tipo):
    tipos = ["matrícula", "pagos", "constancia", "plataforma", "otro"]
    return tipo.strip().lower() in tipos



def mostrar_menu():
    print("\n===== SOPORTE ACADÉMICO =====")
    print("1. Registrar solicitud")
    print("2. Salir")



def asignar_prioridad(tipo):
    prioridades = {
        "matrícula": "Alta",
        "plataforma": "Alta",
        "pagos": "Media",
        "constancia": "Baja",
        "otro": "Baja"
    }

    return prioridades.get(tipo.strip().lower(), "No definida")


def registrar_solicitud():
    codigo = input("Código de estudiante: ")

    if not validar_codigo(codigo):
        print("Error: el código debe tener al menos 6 caracteres.")
        return

    nombre = input("Nombre del estudiante: ")

    tipo = input(
        "Tipo de consulta "
        "(matrícula, pagos, constancia, plataforma u otro): "
    )

    if not validar_tipo_consulta(tipo):
        print("Error: tipo de consulta no válido.")
        return

    descripcion = input("Descripción breve: ")

    prioridad = asignar_prioridad(tipo)

    print("\nSolicitud registrada:")
    print("Código:", codigo)
    print("Nombre:", nombre)
    print("Tipo de consulta:", tipo)
    print("Descripción:", descripcion)
    print("Prioridad:", prioridad)


mostrar_menu()