import os
import csv
import time

class Person():
    def __init__(self, ruc):
        self.ruc = ruc

def read_file(url: str) -> []:
    start = time.time()
    datos = []
    if url != "":
        print(f"Archivo a procesar es: {url}")
        check_file = os.path.isfile(url)
        
        if check_file:    
            with open(url, "r") as csv_file:
             csv_reader = csv.reader(csv_file, delimiter="|")
             line_count =0
             for row in csv_reader:
                 if line_count == 0:
                     print(f"Column names are {', '.join(row)}") 
                     line_count += 1
                 else:
                     datos.append(Person(row[0]))
                    #  print(f'\tRUC: {row[0]} RAZÓN SOCIAL{row[1]}')
                     line_count += 1
            print(f'Processed {line_count} lines')
            print(f'Cantidad de registro{len(datos)}')
            end = time.time()
            print(end - start)
            return datos
        else:
            print("Archivo no existe")
    else:
        print("No ha ingresado archivo")


result = read_file("D:\Downloads\SRI_RUC_Azuay.csv")
print(len(result))

if len(result) > 0:
    for item in result:
        print(item.ruc)