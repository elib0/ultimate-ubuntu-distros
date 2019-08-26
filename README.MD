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
        "Ej: variety": {["apt": "variety"], "script": "addrepo-variety.sh"},
        "Google Chrome": {"checked": true, "script": "install-google-chrome.sh"},
        "iPython": {["pip": "ipython"], ["checked": true]},
        "Git": {["apt": "git"], "post": "setup-git.sh"}
    }
}
~~~
> Propiedad **script** es opcional, se usa para correr un script **_".sh"_** mediante `sudo sh`.

> Propiedad **apt** es opcional, se usa si se va a instalar un paquete por `sudo apt-get`.

> Propiedad **pip** es opcional, se usa si se va a instalar un paquete por `pip install`.

> Propiedad **post** es opcional, se usa para correr un script después de instalar un programa, Por ej: Para configurar un programa ya instalado.

> Propiedad **checked** es opcional, se usa para marcar por defecto la aplicación a instalar, `default: False`

> **NOTA:** Todas las propiedades se pueden usar en conjunto para instalar dependencias o ejecutar script pre y post instalación.
>
> el orden de ejecución de las propiedades es el siguiente:
> 1. script.
> 2. apt.
> 3. pip.
> 4. post.