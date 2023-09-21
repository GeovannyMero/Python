import requests
import datetime

def DescargarArchivo(ruta: str, file: str):
    try:
        r = requests.get(ruta)
        file_name = f'{file}_{datetime.datetime.now().year}.csv'

        with open(file_name, 'wb') as f:
            f.write(r.content)
            
    except Exception as ex:
        print(ex)