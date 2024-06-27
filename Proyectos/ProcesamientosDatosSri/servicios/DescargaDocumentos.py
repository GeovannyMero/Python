import requests
import datetime
import os
import zipfile

def DescargarArchivo(ruta: str, file: str) -> str:
    try:
        file_extension = str(ruta[-3:])
        r = requests.get(ruta)
        
        # file_name = f'{file}_{datetime.datetime.now().year}.{file_extension}'
        file_name = ruta.split('/')[5]
        print(f'El archivo a descargar es: {file_name}')
        with open(file_name, 'wb') as f:
            f.write(r.content)
        
        # print(os.path.splitext(file_name)[1])
        return file_name
            
    except Exception as ex:
        print(ex)


def Descomprimir(filePath: str, file: str) -> str:
    # nombre_archivo_descomprimido = f'D:\\GEOVANNY MERO\\Training\\PYTHON2023\\Python\\Proyectos\\ProcesamientosDatosSri\\desc'
    print(f'nombre del archivo a descomprimir: {filePath}')
    try:
        if(filePath != ''):
            isFile = os.path.exists(filePath)

            if(isFile):
                print('Archivo zip existe...')
                is_zip = zipfile.is_zipfile(filePath);

                if is_zip :
                    print(filePath);
                    with zipfile.ZipFile(filePath, 'r') as myzip:
                        myzip.extractall()
                else:
                    print('No es ZIP...')
            else:
                print('Archivo no existe')

        return filePath.replace('zip', 'csv')
    except Exception as ex:
        print(ex)
        raise Exception('Error al descomprimir....')
    
        