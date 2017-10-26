#HelloFsl
Bajar Vagrant y Virtualbox de sus páginas o instalarlos desde tu administrador de paquetes
https://www.virtualbox.org/wiki/Downloads
https://www.vagrantup.com/downloads.html

Puedes buscar VMs de vagrant que se ajusten a tus necesidades
https://app.vagrantup.com/boxes/search
En nuestro caso usamos ubuntu/trusty64

***vagrant init ubuntu/trusty64***

Puedes sicronizar una carpeta con tu local, configuralo en VagrantFile(syncfile)
No olvides crear carpeta hello para sincronizar

Crea el archivo **hellov1.py** y guardalo con esta linea
***print "Hello"***

Si usas python 3, esa linea fallará
***python hello.py***

Confirma revisando la versión
***python --version***

Usaremos Tweepy
http://www.tweepy.org/

Usaremos el primer ejemplo solo para probar, del getting ready
***python hellov2.py***

Te faltó instalar el módulo de tweepy, pero necesitas instalar pip primero
https://pip.pypa.io/
***sudo pip install tweepy***

***sudo apt-get update***
***sudo apt-get install python-pip***
***sudo pip install tweepy***

Entra twitter para crear tu nueva app
https://apps.twitter.com/
Cambia los permisos y crea tus access tokens

Calemos viendo los últimos tuits de FSLMx
***api.user_timeline("fslmx")***

Ojo, la documentación de Twitter cambió de lugar así que los enlaces en la doc de Tweepy están rotos.
https://developer.twitter.com/en/docs/api-reference-index
