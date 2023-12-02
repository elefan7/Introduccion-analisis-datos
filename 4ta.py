import requests


url = 'https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv'

def descargar_datos(url):

    timeout = 10

    response = requests.get(url, timeout=timeout)


    if response.status_code == 200:
        ruta_destino = 'Introduccion-analisis-datos.csv'

        with open(ruta_destino, 'wb') as archivo:
            archivo.write(response.content)
        print(f'Archivo descargado correctamente en: {ruta_destino}')

    else:
        print(f'Error en la solicitud. Codigo de estado: {response.status_code}' )

descargar_datos(url)