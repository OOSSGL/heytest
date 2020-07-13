# Author
Oscar David Garcia Medina

# Purpose
To resolve at least 1 of 4 different algorithm challenges and pass the "Prueba de Aptitud en Línea" and get the job position "Desarrollador Backend Python y Django" for the HEY business

# Description of the test
A continuación encontrará 4 problemas de diferente nivel de dificultad, debe seleccionar
libremente 1 problema y desarrollarlo cumpliendo los siguientes requerimientos.
● Utilizar python 3.5 o superior
● Crear un proyecto en Django 2.0 ó superior
● Instalar ​https://www.django-rest-framework.org/​ y crear un web service que al
momento de ser llamado por petición GET deberá ejecutar la lógica para el problema
seleccionado y responder por medio de Json el resultado del problema resuelto.
● Crear un repositorio en GitHub o Bitbucket y subir el código fuente de la solución
(compartir el acceso al encargado de la prueba)

# Algorithms and status
- ¿Cuántos Domingos?:  
Not yet implemented

- Derivar Contraseña (Ethical Hacking):  
Solved and Iplemented

- Números de Fibonacci Pan-digitales  
Solved and Iplemented

- Triángulo de Pascal  
Not yet implemented

# URLs
Those are the urls to use the REST GET services of each algorithm

- ¿Cuántos Domingos?<br/>
http://127.0.0.1:8000/prueba/domingos

- Derivar Contraseña (Ethical Hacking)<br/>
http://127.0.0.1:8000/prueba/password

- Números de Fibonacci Pan-digitales:  
I made two versions, one that is the fastest one:
http://127.0.0.1:8000/prueba/fibopan_faster
And a second one that is slower but shows in console the full fibonacci number:
http://127.0.0.1:8000/prueba/fibopan_full

- Triángulo de Pascal  
http://127.0.0.1:8000/prueba/pascals

# How to run
1. Clone the project
2. Open the project and run the server with 
    $ python manage.py runserver
3. With postman or another program or webbrowser go to the desired algorithm URL and do a GET call, you will get in JSON format the name, description and answer of each problem
4. Enjoy!