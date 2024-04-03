import os
import csv
from Models import DatosSri
from db import connect
import json
# from bson import json_util

def leer_archivo(path_file: str):
    datos = []

    try:
        if path_file != '':
            check_file = os.path.isfile(path_file)

            if check_file:
                with open(path_file, 'r') as csv_file:
                    csv_reader = csv.reader(csv_file, delimiter='|')
                    line_count = 0
                    for row in csv_reader:
                        if line_count == 0:
                            print(f'Column names are {", ".join(row)}')
                            line_count += 1
                        else:
                            # contribuyente = DatosSri.Datos(row[0], row[1], row[2], row[3], row[4], row[5], row[6],row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19])
                            # print(contribuyente.razon_social)
                            datos.append(DatosSri.Datos(row[0], row[1], row[2], row[3], row[4], row[5], row[6],row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19]).__dict__)
                            # print(f'{datos[0]["ruc"]}')
                            line_count += 1 
                    # print(datos[0])
                    print(f'Processed {line_count} lines')
                    print(f'Cantidad de registro{len(datos)}')
                    # for item in datos:
                    #     print(f'{item.ruc} - {item.razon_social}')

                    # Insertar en DB
                    conexion = connect.ConectarMongoDB()
                    tabla = conexion.contribuyente
                    

                    # # res = tabla.find()
                    result_insert = tabla.insert_many(datos)         
                    print(result_insert)
            else:
                print('El archivo no existe.')
    except Exception as ex:
        print(ex)
        