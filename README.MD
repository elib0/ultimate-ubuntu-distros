 #### Como usar:
~~~
> git clone git@gitlab.com:elib0/linux-mint-19.2-script.git
> cd inux-mint-19.2-script
> chmod +x first_step.sh #permiso de ejecucion
> ./first_step.sh
~~~
 
#### Archivos de configuración
- ##### default.txt(OPCIONAL):
    Archivo de texto simple que contiene los paquetes que son requeridos para el proceso de instalación, **Ej: make**.
    Están separados por un salto de linea *"\n"*. Estos paquetes se instalan automáticamente al iniciar el script.
- ##### menu.json:
    Archivo en formato json que contiene el diccionario de las aplicaciones del menu.
    estas aplicaciones pueden ser instaladas por `apt-get` o por `sh`.
    La estructura de un elemento del menu es la siguiente:
    ~~~
    "<NombreCategoria>": {
        "Nombre a mostar": {"apt": "vim", ["checked": true]},
        "Ej: variety": {["apt": "variety"], "script": "install-variety.sh"}
    }
    ~~~
  
  > Propiedad **apt** es opcional, se usa si se va a correr un paquete por `sudo apt-get` si no tomara la propiedad **script**.

  > Propiedad **checked** es opcional, se usa instalación por defecto, `default: False`

  > Propiedad **script** es opcional, se usa para correr un script **_".sh"_** mediante `sudo sh` se puede usar en conjunto con la propiedad **apt** y ambos comandos serán ejecutados.