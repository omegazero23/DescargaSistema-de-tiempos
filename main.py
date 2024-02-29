import shutil
from LeerJson import ReadJson
from DescargasRSM import AutomatizadorWeb

def main():
    # Leer información del archivo JSON
    info = ReadJson('secret.json')

    # Obtener datos del archivo JSON
    ruta_descargas = info.secretdata['PATH']
    url_login = info.secretdata['url']
    usuario = info.secretdata['user']
    contrasena = info.secretdata['password']

    # Configurar y ejecutar el automatizador web
    try:
        shutil.rmtree(ruta_descargas)
        shutil.os.makedirs(ruta_descargas)
    except:
        shutil.os.makedirs(ruta_descargas)

    automatizador = AutomatizadorWeb(url_login, usuario, contrasena, ruta_descargas)
    automatizador.configurar_descargas()
    automatizador.iniciar_sesion()
    automatizador.procesar_pagina()
    automatizador.cerrar_navegador()

if __name__ == "__main__":
    main()
