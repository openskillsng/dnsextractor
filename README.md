# dnsextractor
Extracción de información en servidores DNS con Python

Query Type | Comments
------------ | -------------
A | IPv4
AAAA | IPv6
MX | MailServers
NS | NameServers

# Instalación de dnspython - Opción 1
Para instalar la librería, solamente es necesario descargarla, descomprimirla y ejecutar el script setup.py con el argumento install.

1. Descargar dnspython

``` wget http://www.dnspython.org/kits/1.15.0/dnspython-1.15.0.tar.gz ```

2. Descomprimir

tar -xzvf dnspython-1.15.0.tar.gz

3. Ingresar a la carpeta resultado de la descompresión dnspython-1.15.0

python setup.py install

# Instalación de dnspython - Opción 2
Para instalar la librería mediante el gestor de paquetes pip solamente es necesario ejecutar el siguiente comando.

1. Descargar e instalar dnspython

pip install dnspython

2. Comprobar instalación

pip list

# Ejecución de prueba

**Usage:** python dnsextractor.py [domain] [querytype]

**Example:** python dnsextractor.py github.com NS
