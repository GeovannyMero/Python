import requests
import datetime

def DescargarArchivo(ruta: str, file: str) -> str:
    try:
        r = requests.get(ruta)
        file_name = f'{file}_{datetime.datetime.now().year}.csv'

        with open(file_name, 'wb') as f:
            f.write(r.content)
        
        return file_name
            
    except Exception as ex:
        print(ex)