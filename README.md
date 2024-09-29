# sprint_6
TRABAJO RELACIONADO AL SPRINT 6 DE TRIPLETEN
# Pasos realziados en el proyecto
1. Cree mi repositorio vistual en git hub llamado sprint 6
2. Abri visual estuduio y enlace mi repo sprint 6 
3. Como no habia configurado git hub en visual me toco hacerlo e intalar git ene l pc pq lo habia desistalado:
git config --global user.name "Tu Nombre"
git config --global user.email "tuemail@example.com"
4. Ya con el repo enlazado procedo a crear el entorno virtual
python -m venv vehicles_env
5. En gitignore me aseguro de dejar:
vehicles_env/
6 Ejecuto el siguietne comando para plazmar trodas las librerias instaladas
pip freeze > requirements.txt
7. A modo de prueba creo un archivo test.py a fin de validar en enlace y la libreria stramlit para entornos visuales.
8. Activo el ambiente virtual
.\vehicles_env\Scripts\activate
9. Corro la prueba la cual me ejecuta un enlace web con la visual del mensaje 
streamlit run test.py
10. En este punto mi repo ya esta enlazado con el git ignore y el requirments identificado
# PASOS POSTERIORES\

11. Se crea el foolder notebook donde ejcuto graficos a partir del archivo vehicles_us.csv 
12. Tener presente que ha de estar activado el entonrno vitrual
13. Instalo pipinstall jupyter y asi mismo actualizo el requirementes con emi mismo comando anterior de  pip freeswe > requiremente.txt.
14. Ejecuto el archivo  EDA el cual me mostrara unos graficos.
15. Subo lo anterior al repositorio.
16. Para hacer que Streamlit sea compatible con Render, añadi un archivo de configuración de Streamlit al repositorio de tu proyecto en streamlit/config.toml con el siguiente contenido:
[server]
headless = true
port = 10000

[browser]
serverAddress = "0.0.0.0"
serverPort = 10000


# LINK DE EJECUCION EN RENDER

https://sprint-6-8g20.onrender.com/

