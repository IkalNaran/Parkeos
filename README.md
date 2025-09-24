Para clonar el repositorio es: 
git clone https://github.com/IkalNaran/Parkeos.git

Configuracion de Git (Se hace una  vez):
git config --global user.name "nombre del usuario git"
git config --global user.email johndoe@github.com

Para crear la carpeta del entorno virtual: 
python -m venv env

Para activar el entorno virtual del proyecto: 
env\Scripts\activate o source env/bin/activate  - (env) C:\ruta\del\proyecto>

deactivate  -> desactiva el entorno virtual cuando ya no lo ocupas 

Instalacion del los paquetes que se ocupan en el proyecto: 
pip install -r requirements.txt

Para visualizar en tiempo real tu pagina: 
python app.py

git push origin nombre-de-la-rama
