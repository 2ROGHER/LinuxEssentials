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
* `GNU Zip or gnuzip(.gzip)`: Este es una herramienta util de Linux con el cual podemos comprimir `zippear` o descomprimir archivos en el `bash` tranquilamente y comodamente

* `-J(xz)`: es el formato que es mas recomendado y el mejor para `zippear` archivos, estos son tipos o `formatos de zippeo`.
* 
* `ls -lh`: Permite listar el directorio pero con `kilobytes` de almacenamiento.
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
```



# 1.4 Busquedas en Linux
