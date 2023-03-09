import requests

# Get de la web
web = requests.get('https://www.filmaffinity.com/es/film899895.html')

# Convierto la respuesta en cadena
html = web.text

# variable diccionario
diccionario_pelicula = {} 

# Función para capturar los bloques completos
def capturar_bloques(inicio):
    return inicio[:(inicio.find('</dd>'))]

def capturar_clave(bloque):
    return bloque[4:bloque.find('</dt>')].strip()

# Listas
keys = []
values = []

# ------- Capturo el título original
bloque_tituloOriginal = capturar_bloques(html[html.find('<dt>Título original</dt>'):])
clave_titulo = capturar_clave(bloque_tituloOriginal)
principio_titulo = bloque_tituloOriginal[bloque_tituloOriginal.find('<dd>')+4:].strip()
valor_titulo = principio_titulo[:principio_titulo.find('<')]
# Añado a las listas lo que capturo
keys.append(clave_titulo)
values.append(valor_titulo)

# ------- Capturo el año
bloque_anyo = capturar_bloques(html[html.find('<dt>Año</dt>'):])
clave_anyo = capturar_clave(bloque_anyo)
principio_anyo = bloque_anyo[bloque_anyo.find('<dd')+4:].strip()
valor_anyo = principio_anyo[principio_anyo.find('>')+1:].strip()
# Añado a las listas lo que capturo
keys.append(clave_anyo)
values.append(valor_anyo)

# ------- Capturo la duración
bloque_duracion = capturar_bloques(html[html.find('<dt>Duración</dt>'):])
clave_duracion = capturar_clave(bloque_duracion)
principio_duracion = bloque_duracion[bloque_duracion.find('<dd')+4:].strip()
valor_duracion = principio_duracion[principio_duracion.find('>')+1:].strip()
# Añado a las listas lo que capturo
keys.append(clave_duracion)
values.append(valor_duracion)

# ------- Capturo el país
bloque_pais = capturar_bloques(html[html.find('<dt>País</dt>'):])
clave_pais = capturar_clave(bloque_pais)
valor_pais = bloque_pais[bloque_pais.find(';')+1:].strip()
# Añado a las listas lo que capturo
keys.append(clave_pais)
values.append(valor_pais)

# ------- Capturo la dirección
bloque_direccion = capturar_bloques(html[html.find('<dt>Dirección</dt>'):])
clave_direccion = capturar_clave(bloque_direccion)
principio_direccion = bloque_direccion[bloque_direccion.find('<span itemprop="name">'):].strip()
valor_direccion = principio_direccion[principio_direccion.find('>')+1:principio_direccion.find('/')-1].strip()
# Añado a las listas lo que capturo
keys.append(clave_direccion)
values.append(valor_direccion)

# ------- Capturo el guion
bloque_guion = capturar_bloques(html[html.find('<dt>Guion</dt>'):])
clave_guion = capturar_clave(bloque_guion)
tramo = bloque_guion[bloque_guion.find('<span>'):bloque_guion.find('<i>')].split('<span class="nb">')
valor_guion = []
# Recorro cada elemento, para limpiarlo, y  añadirlo al array final de géneros
for person in tramo:
    limpio = person[person.find('>')+1:person.find('</')].strip()
    valor_guion.append(limpio)
# Añado a las listas lo que capturo
keys.append(clave_guion)
values.append(valor_guion)

# ------- Capturo la musica
bloque_musica = capturar_bloques(html[html.find('<dt>Música</dt>'):])
clave_musica = capturar_clave(bloque_musica)
valor_musica = bloque_musica[bloque_musica.find('<span>')+6:bloque_musica.find('</span>')].strip()
# Añado a las listas lo que capturo
keys.append(clave_musica)
values.append(valor_musica)

# ------- Capturo la fotografía
bloque_fotografia = capturar_bloques(html[html.find('<dt>Fotografía</dt>'):])
clave_fotografia = capturar_clave(bloque_fotografia)
principio_fotografia = bloque_fotografia[bloque_fotografia.find('<span>'):bloque_fotografia.find('</span>')].strip()
valor_fotografia = principio_fotografia[principio_fotografia.find('>')+1:]
# Añado a las listas lo que capturo
keys.append(clave_fotografia)
values.append(valor_fotografia)

# ------- Capturo el reparto
bloque_reparto = capturar_bloques(html[html.find('<dt>Reparto</dt>'):])
clave_reparto = capturar_clave(bloque_reparto)
tramo = bloque_reparto[bloque_reparto.find('<span itemprop="name">'):].split(',')
valor_reparto = []
# Recorro cada elemento, para limpiarlo, y  añadirlo al array final de géneros
for person in tramo:
    len_principio = len('<span itemprop="name">')
    parte_principio = person.find('<span itemprop="name">')
    parte_final = person.find('</span></a>')
    limpio = person[parte_principio+len_principio:parte_final]
    valor_reparto.append(limpio)
# Añado a las listas lo que capturo
keys.append(clave_reparto)
values.append(valor_reparto)

# ------- Capturo las compañías
bloque_companyias = capturar_bloques(html[html.find('<dt>Compañías</dt>'):])
clave_companyias = capturar_clave(bloque_companyias)
tramo = bloque_companyias[bloque_companyias.find('<span>'):bloque_companyias.find('.')].split(',')
valor_companyias = []
# Recorro cada elemento, para limpiarlo, y  añadirlo al array final de géneros
for companyia in tramo:
    len_principio = len('<span>')
    parte_principio = companyia[companyia.find('<span>')+len_principio:]
    limpio = parte_principio[:parte_principio.find('</span>')]
    valor_companyias.append(limpio)
# Añado a las listas lo que capturo
keys.append(clave_companyias)
values.append(valor_companyias)

# ------- Capturo el género
bloque_genero = capturar_bloques(html[html.find('<dt>Género</dt>'):])
clave_genero = capturar_clave(bloque_genero)
# Capturo todos los géneros y los divido, añadiéndolos a un array
tramo = bloque_genero[bloque_genero.find('=rat_'):].split('count&nodoc">')
valor_genero = []
# Recorro cada elemento, para limpiarlo, y  añadirlo al array final de géneros
for gen in tramo:
    valor_genero.append(gen[:gen.find('</a>')])
# Añado a las listas lo que capturo
keys.append(clave_genero)
values.append(valor_genero[1:])

# ------- Capturo la sinopsis
bloque_sinopsis = capturar_bloques(html[html.find('<dt>Sinopsis</dt>'):])
clave_sinopsis = capturar_clave(bloque_sinopsis)
principio_sinopsis = bloque_sinopsis[bloque_sinopsis.find('itemprop="description">'):].strip()
valor_sinopsis = principio_sinopsis[principio_sinopsis.find('>')+1:]
# Añado a las listas lo que capturo
keys.append(clave_sinopsis)
values.append(valor_sinopsis)


# --------------- Construcción del diccionario
for i in range(len(keys)):
    diccionario_pelicula[keys[i]] = values[i]

print(diccionario_pelicula)

""" 
{'Título original': 'Avatar: The Way of Water', 
'Año': '2022', 
'Duración': '192 min.', 
'País': 'Estados Unidos', 
'Dirección': 'James Cameron', 
'Guion': ['James Cameron', 'Rick Jaffa', 'Amanda Silver'], 
'Música': 'Simon Franglen', 
'Fotografía': 'Russell Carpenter', 
'Reparto': ['Sam Worthington', 'Zoe Saldana', 'Sigourney Weaver', 'Kate Winslet', 'Stephen Lang', 'Cliff Curtis', 'Joel David Moore', 'Giovanni Ribisi', 'Edie Falco', 'CCH Pounder', 'Jemaine Clement', 'Brendan Cowell', 'Jamie Flatters', 'Britain Dalton', 'Trinity Jo-Li Bliss', 'Jack Champion', 'Bailey Bass', 'Filip Geljo', 'Duane Wichman-Evans', 'Dileep Rao', 'Matt Gerald', 'Keston John', 'Alicia Vela-Bailey', 'Sean Anthony Moran', 'Andrew Arrabito', 'Johnny Alexander'], 
'Compañías': ['20th Century Studios', 'Lightstorm Entertainment', 'TSG Entertainment'], 
'Género': ['Ciencia ficción', 'Aventuras', 'Fantástico', 'Acción', 'Familia', 'Extraterrestres', 'Secuela', '3-D'], 
'Sinopsis': "Más de una década después de los acontecimientos de 'Avatar', los Na'vi Jake Sully, Neytiri 
y sus hijos viven en paz en los bosques de Pandora hasta que regresan los hombres del cielo. Entonces comienzan los problemas que persiguen sin descanso a la familia Sully, que decide hacer un gran sacrificio para mantener a 
su pueblo a salvo y seguir ellos con vida. (FILMAFFINITY)"}
"""