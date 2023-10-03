# SERVIDORES DUROS DE ROER

# Consideraciones finales: `Se va a realizar un servidor web con Linux`.
## 1. Consola de comandos
* Un comando es un programa de software qeu al ejecutarlo en la `CLIiza` realiza una accion en la computadora
## 1.2 Sintaxis comando LInux
```bash
    $ Orden <opciones> [argumentos]
    $ top
    $ free -m
    $ grep -o apples
```
```kali
┌──(kali㉿kali)-[~/Desktop]
└─$ 

```
* `Kali`: nombre del usuairo
* `Kali`: nombre de la maquina
* `~/Desktop`: nombre de la carpta.

* Nota: Las mayusculas y minusculas si son importante y diferenciadoras en `Linux`.
## 1.3 Comandos.
* `lscpu`: Comando para ver a detalle de la computadora
* `top`: Es el comando equivalente a la administrador de tareas de windows.util para verificar los processo + `q`.
* `lspci`: Codigo para ver el tarjeta madre
* `lsusb`: para ver los tipos de usb
* `whoami`: Verifica el  usuario
* `uname -a`: el usuario
* `history`: verifica los comanods que has ejecutado
* `history -c`: boora el history del los comandos.
* `cal`: calendario
* `cal -y`: calendario de todo el anio.
* `date`: nos da la fecha y hora del sistema
* `shutdown`: Apagar el sistema en el que estamos corriendo el SO
* `shutdown -h0`: Apaga el sistema inmediatamente.
* `shutdown -r`: Este comando reinica el sistema y lo enciende nuevamente
* `reboot`: Reinicia el sistema con tiempo cero (automaticamente)
* `$`: Un solo signo de dolar significa que yo soy un simple `usuario`.
* `useradd`:

* `Los admnistrador son los que estan por encima de los usuarios`: Son los priviligios de administrador
* `sudo useradd`: Esto es  realizar una tarea por encargo del aministradado pero sin serlo.
* `sudo su`: Le da privilegios de administrador a un usuario simple.
* `env`: variables de entorno
* `echo $VARIABLE`: imprime el valor de la variabl

* `Prompt personaliado`: 

```bash
\d> \@ export PS1="Fecha: \d> \@ Hora: \@ >>>>

```
* `''`: Las comillas dobles reconocen las variables que se les pasan.
* `man`: imprime el manual de los comandos
* `pinfo`: impreme el manual en colores
* `ls --help`: impreme la ayuda del comando o que hace
* `comando para ver todos los manuales`:
```bash
┌──(kali㉿kali)-[/usr/share/doc]
└─$ 
```

* `info top`: Muestra el manual del comando en formato grafico visible.
* `cat`: para ver el contenido del archivo que se selecciona.
* `clear`: borra o limpia la pantalla.
* `->`: con la tecla `shift` se puede completar.
* `ls -l`: Detalle de la lista a `detalle` con mas metadatos del file.
* ``
## 1.4 Comandos administracion de direcctorios y archivos

* `cd`: para nevegar atravez de los directorios
* `cd /home/share`: Ruta para ir al directorio `share`.
* `pwd`: me permite ver la ruta en el que me encuentro
* `mkdir`: me permite crear un nuevo directorio 
* `cd ..`: permite navegar hacia atras en la ruta del directorio.
* `rmdir`: me permite borrar el directorio que  se seleccione
* `rmdir -r`: forzar la eliminacion de directorios
* `mv ./demo ./documentos1`: mover todo el directorio `./demo` al `./documentos1`.
* `sudo install <nombre_del_programa>`: nos sirve para intalar algun programa
* `tree`: este comanod es util para
* `head`: muestra las primeras lineas del archivo
* `tail -n 1 <file>`: muestra las ultimas lineas del archivo.
* `tail -n +5 <file>`: muestra las ultimas lineas a aparti rde la linea 5
* `greap caracter <file>`: nos permite buscar un determinado caracter(inspeccionar) si existe en el archivo
* `vi`: nos permite ver y editar el contenido de un archivo seleccionado.
* `cmp <file1> <file2>`: permite compar dos archivos seleccionados si son iguales para poder verificar su autenticidad.
* `diff`: permite ver en que lineas o en que parte del file se diferencian pra cerrar el file se usa el comando `:wq! + enter`.
* `file <file>`: Este comando me permite verificar que tipo de file es este.
* `lsof`: Este comando me puede mostrar todos los files habiertos y corriendo en el sistema
* `mv`: Este comando tambien nos permite `editar` o cambiar el nombre del file no solo es para moverlo los files sino tambien para renombrarlo.
* `vi <file_name> `: Nos permite crear un archivo nuevo o agregar contenido en este.
* `sort`: este comando nos permite ordenar los elementos o el contenido de un file
* `sort -r`: sort reverse
* `sort frutas.txt > frutas_sorted.txt`: esto nos permite rederigir la salida  a una nueva archivo "frutas_sorted.txt"
* `md5sum <file>`: este comanod nos permite agregar una firma digital a nuestro file. Es decir que se agregue una clave `hash` que lo diferencia del resto. Esto nos permite si cambiamos el nombre el clave hash no se modifica.Pero si cambiamos el contenido del file su hash tambien cambia.