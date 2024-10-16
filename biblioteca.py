import json 
import datetime 

#Funciones para gestionar libros
def registrar_libro(id_libro, titulo, autor, editorial, año_publicacion, genero, cantidad_disponible):
    with open('libros.json', 'r') as f:
        data = json.load(f)
        data.append({'id_libro': id_libro, 'titulo': titulo, 'autor': autor, 'editorial': editorial, 'año_publicacion': año_publicacion, 'genero': genero, 'cantidad_disponible': cantidad_disponible})
    with open('libros.json', 'w') as f:
        json.dump(data, f, indent=4)

def editar_libro(id_libro, nuevo_titulo=None, nuevo_autor=None, nueva_editorial=None, nuevo_año_publicacion=None, nuevo_genero=None, nueva_cantidad_disponible=None):
    with open('libros.json', 'r') as f:
        data = json.load(f)
    for libro in data:
        if libro['id_libro'] == id_libro:
            if nuevo_titulo:
                libro['titulo'] = nuevo_titulo
            if nuevo_autor:
                libro['autor'] = nuevo_autor
            if nueva_editorial:
                libro['editorial'] = nueva_editorial
            if nuevo_año_publicacion:
                libro['anio_publicacion'] = nuevo_año_publicacion
            if nuevo_genero:
                libro['genero'] = nuevo_genero
            if nueva_cantidad_disponible:
                libro['cantidad_disponible'] = nueva_cantidad_disponible
            break
    with open('libros.json', 'w') as f:
        json.dump(data, f, indent=4)

def eliminar_libro(id_libro):
    with open('libros.json', 'r') as f:
        data = json.load(f)
    data = [libro for libro in data if libro['id_libro'] != id_libro]
    with open('libros.json', 'w') as f:
        json.dump(data, f, indent=4)

def buscar_libro(criterio, valor): 
    #Busca libros en 'libros.json' por título, género, autor o editorial
    with open('libros.json', 'r') as f: 
        data = json.load(f) 
        resultados = [libro for libro in data if libro[criterio] == valor] 
        return resultados 
    
#Funciones para gestionar socios
def registrar_socio(id_socio, nombre, apellido, fecha_nacimiento, direccion, correo_electronico, telefono): 
    # Registra un nuevo socio en el archivo 'socios.json'
    with open('socios.json', 'r+') as f: 
        data = json.load(f) 
        data.append({ 
            "id_socio": id_socio, 
            "nombre": nombre, 
            "apellido": apellido, 
            "fecha_nacimiento": fecha_nacimiento, 
            "direccion": direccion, 
            "correo_electronico": correo_electronico, 
            "telefono": telefono 
        }) 
        f.seek(0) 
        json.dump(data, f, indent=4)
        
def editar_socio(id_socio, nuevo_nombre=None, nuevo_apellido=None, nueva_fecha_nacimiento=None, nueva_direccion=None, nuevo_correo_electronico=None, nuevo_telefono=None): 
    # Edita la información de un socio existente en 'socios.json'
    with open('socios.json', 'r+') as f: 
        data = json.load(f) 
        for socio in data: 
            if socio["id_socio"] == id_socio: 
                if nuevo_nombre: 
                    socio["nombre"] = nuevo_nombre 
                if nuevo_apellido: 
                    socio["apellido"] = nuevo_apellido 
                if nueva_fecha_nacimiento: 
                    socio["fecha_nacimiento"] = nueva_fecha_nacimiento 
                if nueva_direccion: 
                    socio["direccion"] = nueva_direccion 
                if nuevo_correo_electronico: 
                    socio["correo_electronico"] = nuevo_correo_electronico 
                if nuevo_telefono: 
                    socio["telefono"] = nuevo_telefono 
                break 
        f.seek(0) 
        json.dump(data, f, indent=4) 

def eliminar_socio(id_socio): 
    # Elimina un socio del archivo 'socios.json'
    with open('socios.json', 'r+') as f: 
        data = json.load(f) 
        data = [socio for socio in data if socio["id_socio"] != id_socio] 
        f.seek(0) 
        json.dump(data, f, indent=4) 


# Funciones para gestionar préstamos
def registrar_prestamo(id_prestamo, id_socio, id_libro, fecha_prestamo): 
    # Registra un nuevo préstamo en el archivo 'prestamos.json'
    with open('prestamos.json', 'r+') as f: 
        data = json.load(f) 
        data.append({ 
            "id_prestamo": id_prestamo, 
            "id_socio": id_socio, 
            "id_libro": id_libro, 
            "fecha_prestamo": fecha_prestamo, 
            "fecha_devolucion": None, 
            "estado_prestamo": "En Curso" 
        }) 
        f.seek(0) 
        json.dump(data, f, indent=4) 

    # Actualizar cantidad disponible del libro 
    editar_libro(id_libro, nueva_cantidad_disponible=obtener_cantidad_disponible(id_libro) - 1) 
 
def devolver_libro(id_prestamo): 
    # Registra la devolución de un libro en 'prestamos.json'
    with open('prestamos.json', 'r+') as f: 
        data = json.load(f) 
        for prestamo in data: 
            if prestamo["id_prestamo"] == id_prestamo: 
                prestamo["fecha_devolucion"] = datetime.date.today().strftime("%Y-%m-%d") 
                prestamo["estado_prestamo"] = "Devuelto" 
                break 
        f.seek(0) 
        json.dump(data, f, indent=4) 

    # Actualizar cantidad disponible del libro 
    id_libro = obtener_id_libro_por_prestamo(id_prestamo) 
    editar_libro(id_libro, nueva_cantidad_disponible=obtener_cantidad_disponible(id_libro) + 1) 

# Funciones auxiliares
def obtener_cantidad_disponible(id_libro): 
    # Obtiene la cantidad de ejemplares disponibles de un libro
    with open('libros.json', 'r') as f: 
        data = json.load(f) 
        for libro in data: 
            if libro["id_libro"] == id_libro: 
                return libro["cantidad_disponible"] 
        return None 
    
def obtener_id_libro_por_prestamo(id_prestamo): 
    # Obtiene el ID del libro asociado a un préstamo
    with open('prestamos.json', 'r') as f: 
        data = json.load(f) 
        for prestamo in data: 
            if prestamo["id_prestamo"] == id_prestamo: 
                return prestamo["id_libro"] 
        return None 
    
# Funciones para generar reportes
def reportes_prestamos_por_socio(id_socio): 
    # Genera un reporte de préstamos realizados por un socio específico
    with open('prestamos.json', 'r') as f: 
        data = json.load(f) 
        prestamos_socio = [prestamo for prestamo in data if prestamo["id_socio"] == id_socio] 
        return prestamos_socio 
def reportes_prestamos_por_libro(id_libro): 
    # Genera un reporte de préstamos realizados de un libro específico
    with open('prestamos.json', 'r') as f: 
        data = json.load(f) 
        prestamos_libro = [prestamo for prestamo in data if prestamo["id_libro"] == id_libro] 
        return prestamos_libro 
def reportes_prestamos_por_rango_fechas(fecha_inicio, fecha_fin): 
    # Genera un reporte de préstamos realizados en un rango de fechas determinado
    with open('prestamos.json', 'r') as f: 
        data = json.load(f) 
        prestamos_rango_fechas = [prestamo for prestamo in data if fecha_inicio <= prestamo["fecha_prestamo"] <= fecha_fin] 
        return prestamos_rango_fechas 
