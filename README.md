# Mi proyecto Django
Este es un proyecto Django que incluye una aplicación llamada **myapp**.

## Estructura del Proyecto
El proyecto tiene la siguiente estructura:
```
myapp/
  __init__.py
  admin.py
  apps.py
  forms.py
  migrations/
  models.py
  static/
  templates/
  tests.py
  urls.py
  views.py
mysite/
  __init__.py
  asgi.py
  settings.py
  urls.py
  wsgi.py
manage.py
README.md
```

## Funcionalidades
- La aplicación [myapp](./myapp/) tiene vistas para `index`, `about`, `hello`, `projects`, `project_detail`, `tasks`, `create_task` y `create_project`. Estas vistas están definidas en [myapp/views.py](./myapp/views.py) y las rutas correspondientes están en [myapp/urls.py](./myapp/urls.py).
- Hay formularios para crear nuevas tareas y proyectos en [myapp/forms.py](./myapp/forms.py).
- Los modelos de datos están definidos en [myapp/models.py](./myapp/models.py).
- Las plantillas HTML se encuentran en el directorio [myapp/templates/](./myapp/templates/).

## Cómo ejecutar el proyecto
1. Asegúrate de tener instalado Python y Django.
2. Clona este repositorio.
2. Navega hasta el directorio del proyecto.
3. Ejecuta python manage.py runserver para iniciar el servidor de desarrollo de Django.
4. Abre un navegador web y visita http://localhost:8000 para ver la aplicación en acción.

## Aclaraciones
Este proyecto es solo un ejemplo y no tiene funcionalidades reales. Se creó con fines educativos.