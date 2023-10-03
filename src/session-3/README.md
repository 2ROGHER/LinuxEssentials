# 1. El poder del la linea de comandos de Linux.
# 1.2 Archivo / fichero
* Documento de determinado extesion y que se puede modificar o trabajar.
# 1. 3 Archivar
* La tecnica por la cual se comprime o se guarda el archivo  o se archican  y se guardan en algun lugar del sistema.
*  Se pueden guardar por un tema de backup
* Linux provee de diferenetes herramientas para `comprimir` archivos y empaquetar archivos con la finalidad de optimizar el espacio en el disco de almacenamiento.
* `archivar files tar`: se hace con herramientas de compresion `gzip, .bzip, xz`.
* `tar -cf <file>`: Comando mas anitiguo de linux para comprimir archivos
```bash
    #Crear un archiv comprimido
    tar -cf ejemplo.tar archivo1.txt archivo2.txt
    # extraer-descomprimir en el archivo actual un file tipo tar
    tar -xf ejemplo.tar 
    # mostrar el contenido comprimido del archivo
    tar -tvf ejemplo.tar
    # tipos de formatear

```
* `GNU Zip or gunzip(.gzip)`: Este es una herramienta util de Linux con el cual podemos comprimir `zippear` o descomprimir archivos en el `bash` tranquilamente y comodamente

* `-J(xz)`: es el formato que es mas recomendado y el mejor para `zippear` archivos, estos son tipos o `formatos de zippeo`.
* 
* `ls -lh`: Permite listar el directorio pero en `kilobytes` de almacenamiento.
* `du -hsc <directory_or_file_name>*`: (* todos) permite mostrar el tamanio o el peso del directorio

* `tar -cf <file_zip_name> <directory_name_to_zip>`: Forma como hacer un `zippero` en linux

* Cuando se usa el factor de compresion `xz` existe un `delay` mucho mayor debido a que el factor de  compresion es mayor

```bash
    # empaquetar el directorio
    tar -cf Documentos1.tar Documentos

    # Esto nos sirve para ver (view) el proceso 
    #que sige la herramienta para empaquetar el directorio
    tar -cvf Documentos2.tar Documentos

    # como `zippear ` un directorio por un determinado factor de compresion en  este caso el  formato .bzip2
    tar -cjvf Documentos2.tar.bzip2 Documentos
    # comprimiendo con formato `xz`
    tar -cJvf Documentos2.tar.xz Documentos
    # comprimiendo archivos con formato gzip
    tar 

    # Ahora para extrear o `descomprimir` el archivo samos
    tar -xvf Documentos1.tar # Esto descomprime el archivo `Decumentos.tar` (x) de extract. Lo extrae en el mismo directorio y con el mismo nombre.

    # Comprimir cada archivo del directorio selecionado y agregandole `gz`, es decir cada archivo se reduce de tamanio.
    gzip -r Documentos # compresion

    # Descompresion de directorio que se comprimio.
    gunzip -r Documentos # descompresion

    # Manatiene el archivo original y hace una copia de los mismos archivos del directorio pero comprimido, es decir una copia y otra compia comprimida
    gzip -kr Documentos

    # Comprimir el archivo con formato `bzip2`. Ojo el archivo
    bzip2 carta1.txt
    
    # Descomprimir el archivo con el formato `bzip2`
    bunzip2 carta1.txt.bz2

    # comprimiendo con el formato `xz`
    xz carta2.txt

    # descomprimir el archivo con el formato `xz`
    unzx carta2.txt.xz

```
# 1.4 Busquedas en Linux
* Comandos utiles de Linux para reaalizar busquedas de archivos.
`find`: comando para buscar archivos
```bash
    # buscar un archivo en el directorio raiz con las iniciales del nombre o que contenga a dichos esos caracteres
    find / -name pass*

    # afinando al busqueda en carpetas con privilegios de administrador en la carpeta `etc`.
    sudo find /etc -name pass* 

    # busqueda del archivo index.html en la carpeta `/etc/``
    find /etc -name index.html

    # grep: imprime las lineas en los que existe coincidencia con la palabra `root` en la carpera `/etc/passw`.
    grep root /etc/passw

    # Listado de todos los archivo que no tiene login
    grep nologin /etc/passw
    
    # buscar un nombre en esepcifico en un archivo
    grep nara frutas.txt

    
```