# Gestor de Tareas CLI

## Descripción

Este proyecto es un gestor de tareas de línea de comandos (CLI) que permite a los usuarios crear, listar, editar y eliminar tareas. Es ideal para quienes prefieren trabajar dentro del terminal y buscan una herramienta simple pero potente para gestionar sus tareas diarias.

## Características

- Crear tareas con nombre, descripción, fecha de vencimiento y prioridad.
- Listar todas las tareas existentes con opción a filtrar por estado.
- Editar cualquier aspecto de una tarea existente.
- Eliminar tareas no deseadas.

## Instalación

Para instalar este CLI, necesitarás tener Python instalado en tu sistema. Este proyecto ha sido probado con Python 3.8 y versiones superiores.

1. Clona el repositorio a tu máquina local:
    ```bash
    git clone https://github.com/davidgg090/gestor-de-tareas-cli.git
    cd gestor-de-tareas-cli
    ```

2. (Opcional) Crea un entorno virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    ```

3. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```
4. Crear un archivo `.env` en la raíz del proyecto con las siguientes variables de entorno:
    ```bash
    DATABASE_URL=sqlite:///db.sqlite3
    ```

## Uso

Una vez instalado, puedes ejecutar el CLI utilizando el script `main.py`. Aquí algunos ejemplos de cómo usarlo:

- Añadir una nueva tarea:
    ```bash
    python main.py add "Nombre de la Tarea" "Descripción de la Tarea" --due_date "2024-03-05" --priority 1
    ```

- Listar tareas:
    ```bash
    python main.py list
    ```

- Editar una tarea existente:
    ```bash
    python main.py edit 1 --name "Nombre Actualizado" --description "Descripción Actualizada"
    ```

- Eliminar una tarea:
    ```bash
    python main.py delete 1
    ```

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.
