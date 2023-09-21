from servicios import WebScraping
from servicios import DescargaDocumentos
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
        DescargaDocumentos.DescargarArchivo(enlace_provincia, nombre_provincia)


    else:
        print("No existe datos")    



if __name__ == '__main__':
    main()