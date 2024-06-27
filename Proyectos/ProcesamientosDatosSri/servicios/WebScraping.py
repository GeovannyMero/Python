import requests
from bs4 import BeautifulSoup

URL_BASE = 'https://www.sri.gob.ec/datasets'

def ObtenerDataWeb() -> []:    
    try:
        data_obtenida = requests.get(URL_BASE)
        html_obtenido = data_obtenida.text

        # 2. Parsear ese HTML obtenido
        soup = BeautifulSoup(html_obtenido, "html.parser")

        # Seleccionamos los elementos
        result = soup.css.select('span.contenido-final')
        index = 0
        num = 1
        provincia_enlace = [] # variable para almacenar los datos

        for item in result:
            provincia = result[index].findChildren('strong')
            enlace = result[index].findChildren('a')
            
            if len(provincia) > 0:
                provincia_enlace.append({'provincia': provincia[0].text, 'enlace': enlace[0].attrs["href"]}) # se almacena los datos en la variable indicada
                # print(f'{num} - {provincia[0].text} -> {enlace[0].attrs["href"]}') # se presenta las opciones para el procesamiento
                num += 1
            index += 1

        return provincia_enlace
    except Exception as ex:
        print(ex)
        raise Exception('OCURRIO UN PROBLEMA AL OBTENER DATASET....')
        

