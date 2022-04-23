import json

def cargar_datos(ruta):
    with open(ruta) as contenido:
        cursos = json.load(contenido)
        for curso in cursos:
            print(curso.get('duracion', 'nombre', 'slug'))

if __name__ == '__main__':
    ruta = 'data/cursos.json'
    cargar_datos(ruta)