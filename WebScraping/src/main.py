import requests
from bs4 import BeautifulSoup
import datetime

URL_BASE = 'https://www.sri.gob.ec/datasets'
data_obtenida = requests.get(URL_BASE)
html_obtenido = data_obtenida.text

# 2. Parsear ese HTML obtenido
soup = BeautifulSoup(html_obtenido, "html.parser")

# Seleccionamos los elementos
result = soup.css.select('span.contenido-final')
index = 0
num = 1
provincia_enlace = [] # variable para almacenar los datos

print('Listado de Provincias a procesar los datos de SRI.')

# iteramos los elementos que encontramos
for item in result:
    provincia = result[index].findChildren('strong')
    enlace = result[index].findChildren('a')
    
    if len(provincia) > 0:
        provincia_enlace.append({'provincia': provincia[0].text, 'enlace': enlace[0].attrs["href"]})
        print(f'{num} - {provincia[0].text} -> {enlace[0].attrs["href"]}')
        num += 1
    index += 1

option = int(input('Ingrese la opción de la provincia a procesar \n')) # Preguntamos la opción que se desea procesar

if option > 24:
    print(f'ERROR: La opción ingresada debe ser menor a {option}')
else:
    print(f'La provincia seleccionada es: \n {provincia_enlace[option-1]}') 
    print('Procesando ...')
    enlace = provincia_enlace[option-1]["enlace"]
    provincia_name = provincia_enlace[option-1]['provincia']
    print(enlace)
    r = requests.get(enlace) # se envia petición para realizar la descarga
    file_name = f'{provincia_name}_{datetime.datetime.now().year}.csv'
    
    with open(file_name, 'wb') as f: # se guarda el archivo.
        f.write(r.content)
    
    print('Proceso finalizado.')
                
