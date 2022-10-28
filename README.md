# prueba-tec-backend
Backend planificación mensual(Python 3.8.10)

1 - Crear entorno virtual
  python3 -m virtualenv venv

2 - Activar entorno virtual
  . ./venv/bin/activate (linux)
  activate (windows)

3 - Instalar paquetes.
  pip3 install -r requirements.txt

4 - Crear archivo .env en la raiz de la carpeta con las siguientes variables de entorno:
    MYSQL_USER = 
    MYSQL_PASSWORD =
    MYSQL_HOST = 
    MYSQL_PORT = 
    MYSQL_DATABASE =

5 - Ejecución de la app:
  python3 index.py