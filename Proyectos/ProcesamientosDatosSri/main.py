from servicios import WebScraping
from servicios import DescargaDocumentos
from servicios import ProcesarDatos
import os
# principal function
def main():
    print(f"Hola, desde el procesamiento del SRI")
    lista_provincia_enlace = WebScraping.ObtenerDataWeb()
    
    if len(lista_provincia_enlace) > 0:
        print('Listado de las provincias a procesar:')
        index = 1

        for item in lista_provincia_enlace:
            print(f'{index}. {item["provincia"]} -> {item["enlace"]}')
            index += 1
        
        opcion = int(input('Ingrese la opción de la provincia a procesar. \n'))
        print(f'La opción seleccionada es: {opcion}')
        nombre_provincia = lista_provincia_enlace[opcion-1]['provincia']
        enlace_provincia = lista_provincia_enlace[opcion-1]['enlace']
        print(f'Se procede con la descarga del archivo de la provincia: {nombre_provincia}')
        nombre_archivo = DescargaDocumentos.DescargarArchivo(enlace_provincia, str(nombre_provincia).strip())
        print(f'El archivo descargado es: {nombre_archivo}')
        extension_file = os.path.splitext(nombre_archivo)[1]

        if(extension_file == '.zip'):
           nombre_archivo = DescargaDocumentos.Descomprimir(nombre_archivo, nombre_provincia)
           print(f'DES: {nombre_archivo}')

        if nombre_archivo != "":
            ProcesarDatos.leer_archivo(nombre_archivo)


    else:
        print("No existe datos")    



if __name__ == '__main__':
    main()
    # print('http://descargas.sri.gob.ec/download/datosAbiertos/SRI_RUC_Guayas.zip'.split('/')[5])
    # nombre_archivo = DescargaDocumentos.DescargarArchivo('http://descargas.sri.gob.ec/download/datosAbiertos/SRI_RUC_Guayas.zip', 'Guayas')
    # nombre_archivo = 'C:\\Users\\USUARIO\\Downloads\\SRI_RUC_Guayas.zip'
    # extension_file = os.path.splitext(nombre_archivo)[1]
    # print(extension_file)

    # if(extension_file == '.zip'):
    #     print('ingreso:')
    #     nombre_archivo = DescargaDocumentos.Descomprimir(nombre_archivo, 'Guayas')