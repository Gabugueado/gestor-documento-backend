
# Gestor de Documento - Backend

Este es el repositorio del backend para el proyecto de Gestor de Documento. El backend está desarrollado utilizando Django Rest Framework para proporcionar una API robusta para la gestión de documentos.

## Clonar el Repositorio

Para comenzar a trabajar con este proyecto, primero debes clonar este repositorio en tu máquina local. Puedes hacerlo ejecutando el siguiente comando en tu terminal:

```bash
git clone https://github.com/Gabugueado/gestor-documento-frontend.git
```

## Configurar el Entorno Virtual

Es una buena práctica crear un entorno virtual para aislar las dependencias de tu proyecto. Para hacerlo, navega al directorio clonado del repositorio frontend y ejecuta los siguientes comandos:

```bash
cd gestor-documento-frontend
python -m venv backend
```

Luego, activa el entorno virtual (esto puede variar según tu sistema operativo):

- En Windows:

```bash
backend\Scripts\activate.bat
```

- En macOS y Linux:

```bash
source backend/bin/activate
```

## Instalar Dependencias

Una vez que tengas el entorno virtual activado, instala las dependencias necesarias para el proyecto utilizando pip y el archivo `requirements.txt`. Ejecuta el siguiente comando:

```bash
pip install -r requirements.txt
```

## Ejecutar el Servidor

¡Estás listo para ejecutar el servidor de desarrollo de Django! Utiliza el siguiente comando para iniciar el servidor:

```bash
python manage.py runserver
```

El servidor se ejecutará en `http://127.0.0.1:8000/` por defecto. Puedes acceder a la API y comenzar a desarrollar tus funcionalidades.

¡Eso es todo! Ahora tienes el backend de tu proyecto Django Rest Framework configurado y listo para su desarrollo.