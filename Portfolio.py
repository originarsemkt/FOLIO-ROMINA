class Proyecto:
    def __init__(self, nombre, tecnologia, descripcion):
        self.nombre = nombre
        self.tecnologia = tecnologia
        self.descripcion = descripcion

# Definir las secciones del portfolio
SECCIONES = ["Información Personal", "Proyectos", "Habilidades", "Contacto"]

# Información personal
NOMBRE = "Romina Raquel Galeano Blasco"
EDAD = 44
CORREO = "originarse.mkt@gmail.com"

# Proyectos realizados
PROYECTOS = [
    Proyecto("Blog Paradigma", "Python", "Se trata de un proyecto de blog para un espacio comunitario en el centro de Córdoba Capital, Argentina"),
    Proyecto("Trabajo final en Coderhouse", "JavaScript", "Se trata de una tienda virtual Ecommerce de una tienda de informatica reconocida en Códoba, Argentina"),
    Proyecto("Circuito de seguridad", "Ciberseguridad", "Se trata de un circuito con todo lo que tiene que ver en entradas externas a través de redes y el circuito conveniente para evitar malwares y todo tipo de archivo dañino"),
    Proyecto("Herramienta Pomodoro T-Aviso", "UX/UI", "Una simulación en Figma sobre una herramienta Pomodoro llamada T-AVISO, la cual ayuda a controlar tu tiempo"),
    Proyecto("Censo Violencia de Género", "Data Analytic", "Análisis de datos del censo nacional de 2022 apuntando a la violencia de género en Argentina")
]

# Habilidades
HABILIDADES = ["Python", "Data Analytic", "JavaScript", "Análisis de prevención de Fraude"]

# Contacto
CONTACTO = {"Telefono": 3516079540, "whatsapp": "+54 9 351 607 9540"}

def imprimir_informacion_personal():
    print("Nombre:", NOMBRE)
    print("Edad:", EDAD)
    print("Correo:", CORREO)

def imprimir_menu():
    print("\nMenú de Navegación:")
    for i, seccion in enumerate(SECCIONES, start=1):
        print(f"{i}. {seccion}")

def imprimir_proyectos():
    print("\nProyectos Realizados:")
    for proyecto in PROYECTOS:
        print("Nombre:", proyecto.nombre)
        print("Tecnología:", proyecto.tecnologia)
        print("Descripción:", proyecto.descripcion)

def imprimir_habilidades():
    print("\nHabilidades:")
    for habilidad in HABILIDADES:
        print("-", habilidad)

def imprimir_contacto():
    print("\nInformación de contacto:")
    for clave, valor in CONTACTO.items():
        print(clave + ":", valor)

# Imprimir información
print("Información Personal:")
imprimir_informacion_personal()

# Imprimir el menú de navegación
imprimir_menu()

# Imprimir proyectos
imprimir_proyectos()

# Imprimir habilidades
imprimir_habilidades()

# Imprimir contacto
imprimir_contacto()