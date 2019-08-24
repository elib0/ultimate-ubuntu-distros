### Como ejecutar:
 
~~~
> git clone git@github.com:elib0/ultimate-ubuntu-distros.git # ó git@gitlab.com:elib0/ultimate-ubuntu-distros.git
> cd ultimate-ubuntu-distros
> chmod +x first_step.sh #permiso de ejecución
> ./first_step.sh
~~~

### Como usar:
 - Se usa **Y** ó **N** para afirmar o negar instalaciones en el menú.
 - Usar las teclas de flechas **(Arriba/Abajo)** para desplazarte por la lista de aplicaciones.
 - Con la tecla **\<space\>** puedes marcar o desmarcar una aplicación.
 - Con la tecla **\<a>** marcas toda una categoría.
 - Con la tecla **\<i>** inviertes las aplicaciones marcas.
 
### Archivos de configuración:
- ##### default.txt(OPCIONAL):
    Archivo de texto simple que contiene los paquetes que son requeridos para el proceso de instalación, **Ej: make**.
    Están separados por un salto de linea *"\n"*. Estos paquetes se instalan automáticamente al iniciar el script.
- ##### menu.json:
    Archivo en formato json que contiene el diccionario de las aplicaciones del menu.
    estas aplicaciones pueden ser instaladas por `apt-get` o por `sh`.
    La estructura de un elemento del menu es la siguiente:
    
~~~
"<NombreCategoria>": {
    "message1": "Mensaje mostrado para confirmar instalación de programas de una categoría",
    "message2": "Mensaje mostrado cuando se esta en la lista de programas a instalar",
    "programs": {
        "Nombre a mostar": {"apt": "vim", ["checked": true]},
        "Ej: variety": {["apt": "variety"], "script": "install-variety.sh"}
    }
}
~~~
  
> Propiedad **apt** es opcional, se usa si se va a correr un paquete por `sudo apt-get` si no tomara la propiedad **script**.

> Propiedad **checked** es opcional, se usa instalación por defecto, `default: False`

> Propiedad **script** es opcional, se usa para correr un script **_".sh"_** mediante `sudo sh` se puede usar en conjunto con la propiedad **apt** y ambos comandos serán ejecutados.