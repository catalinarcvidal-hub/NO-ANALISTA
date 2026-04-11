## Paso a paso: De VS Code a GitHub


###  Abrir la terminal
En VS Code presiona:

Ctrl + `



#  Ver qué archivos cambiaron

git status

Verás los archivos con **M** (modificado) o **U** (nuevo)

### Inicializa Git en tu carpeta

Ejecuta este comando UNA sola vez:

git init

🔹 Esto crea el repositorio (.git) en esa carpeta


###  Agregar los archivos

git add .

> El punto `.` significa "agregar **todos** los archivos cambiados"


### Hacer el commit (guardar con mensaje)

git commit -m "escribe aquí qué hiciste"

Ejemplos de buenos mensajes:

git commit -m "agrego ejercicio de clase 10"
git commit -m "corrijo tarea del 24 de marzo"


### Subir a GitHub

git push



## ✅ Resumen rápido

git status
git init
git add .
git commit -m "tu mensaje"
git push

Esos **5 comandos** son todo lo que necesitas cada vez que quieras subir algo a GitHub.

