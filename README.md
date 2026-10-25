API de Usuarios y Tareas
API REST desarrollada con FastAPI, SQLAlchemy 2, Pydantic 2 y PostgreSQL, con la base de datos ejecutándose mediante Docker Compose.
Este proyecto permite administrar usuarios y sus tareas, aplicar validaciones de datos y proteger la integridad de las relaciones entre ambas entidades.
Funcionalidades
- Crear, consultar, actualizar y eliminar usuarios.
- Crear, listar, consultar, actualizar y eliminar tareas.
- Asociar cada tarea a un usuario mediante usuario_id (clave foránea).
- Devolver errores 404 Not Found para recursos inexistentes.
- Evitar la creación de tareas para usuarios inexistentes.
- Impedir la eliminación de usuarios con tareas asociadas mediante 409 Conflict.
- Detectar correos duplicados en las operaciones de usuarios y responder 409 Conflict.
- Explorar y probar la API desde la documentación interactiva de Swagger.
Tecnologías
- Python
- FastAPI
- SQLAlchemy 2 (ORM)
- Pydantic 2
- PostgreSQL 17
- Docker Compose
- Uvicorn
Estructura del proyecto
Proyecto_2_Tareas/
├── App/
│   ├── __init__.py
│   ├── main.py
│   ├── database/
│   │   ├── __init__.py
│   │   └── database.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── usuario.py
│   │   └── tarea.py
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── usuario.py
│   │   └── tarea.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── usuario.py
│   │   └── tarea.py
│   └── services/
│       └── __init__.py
├── compose.yaml
├── requirements.txt
├── .env                 # Local: no subir a GitHub
├── .gitignore
└── README.md
El entorno virtual venv/ tampoco debe incluirse en el repositorio.

Modelo de datos
Usuario
- id: identificador único.
- nombre: nombre del usuario.
- correo: correo electrónico único.
- tareas: relación ORM con las tareas del usuario.
Tarea
- id: identificador único.
- titulo: título de la tarea.
- descripcion: descripción de la tarea.
- completada: estado de finalización (true o false).
- usuario_id: clave foránea que referencia usuarios.id.
La relación es uno a muchos: un usuario puede tener varias tareas; cada tarea pertenece a un usuario.
Endpoints
Usuarios
Método	Ruta	Descripción
POST	/usuarios/	Crear un usuario
GET	/usuarios/	Listar usuarios
GET	/usuarios/{usuario_id}	Consultar un usuario
PUT	/usuarios/{usuario_id}	Actualizar un usuario
DELETE	/usuarios/{usuario_id}	Eliminar un usuario sin tareas asociadas


Tareas
Método	Ruta	Descripción
POST	/tareas/	Crear una tarea para un usuario existente
GET	/tareas/	Listar tareas
GET	/tareas/{tarea_id}	Consultar una tarea
PUT	/tareas/{tarea_id}	Actualizar una tarea
DELETE	/tareas/{tarea_id}	Eliminar una tarea


Requisitos previos
- Python instalado.
- Docker Desktop con Docker Compose disponible.
- Git (si se va a publicar en GitHub).
Instalación y ejecución
Los siguientes ejemplos utilizan PowerShell en Windows.
1. Clonar el repositorio (sustituir la URL por la del repositorio publicado):
   git clone <URL_DEL_REPOSITORIO>
   cd Proyecto_2_Tareas
2. Crear y activar un entorno virtual:
   python -m venv venv
   .\venv\Scripts\Activate.ps1
3. Instalar las dependencias:
   pip install -r requirements.txt
4. Crear el archivo .env en la raíz del proyecto. Debe contener la variable DATABASE_URL con los datos de conexión correspondientes a compose.yaml. Por ejemplo, si PostgreSQL está publicado en el puerto 5434:
   DATABASE_URL=postgresql+psycopg2://postgres:TU_CONTRASENA@localhost:5434/proyecto_2_tareas
   Importante: el ejemplo es ilustrativo. Ajusta el usuario, la contraseña, el controlador y la base de datos a tu configuración real. No publiques credenciales en GitHub.
5. Iniciar PostgreSQL:
   docker compose up -d
6. Iniciar la API desde la raíz del proyecto:
   uvicorn App.main:app --reload
7. Abrir la documentación interactiva:
   - Swagger UI: http://127.0.0.1:8000/docs
   - OpenAPI JSON: http://127.0.0.1:8000/openapi.json
Nota: antes de publicar, verifica que la cadena de conexión del ejemplo coincida con el controlador de PostgreSQL instalado en requirements.txt y con la configuración real de compose.yaml.

Ejemplos de uso
Crear un usuario
POST /usuarios/
{
  "nombre": "Ricardo",
  "correo": "ricardo@ejemplo.com"
}
Crear una tarea
POST /tareas/
{
  "titulo": "Estudiar FastAPI",
  "descripcion": "Practicar relaciones con SQLAlchemy",
  "completada": false,
  "usuario_id": 1
}
El usuario_id debe corresponder a un usuario existente.
Actualizar una tarea
PUT /tareas/1
{
  "titulo": "Estudiar FastAPI",
  "descripcion": "Práctica finalizada",
  "completada": true,
  "usuario_id": 1
}
Validaciones y códigos HTTP
Código	Significado	Ejemplo
200	Operación exitosa	Consultar, actualizar o eliminar
201	Recurso creado	Crear una tarea
404	Recurso inexistente	Buscar una tarea o usuario no registrado
409	Conflicto con el estado actual	Correo duplicado o intento de eliminar un usuario con tareas


Seguridad y buenas prácticas
- Mantener .env, venv/ y archivos locales de configuración fuera de Git.
- No publicar contraseñas ni credenciales.
- Validar los datos de entrada con Pydantic.
- Utilizar dependencias para gestionar y cerrar las sesiones de base de datos.
- Comprobar la existencia de los recursos antes de modificarlos.
Estado del proyecto
CRUD de usuarios y tareas implementado y probado manualmente en Swagger.
Posibles mejoras futuras: pruebas automatizadas, migraciones con Alembic, separación de lógica en servicios, manejo adicional de errores de integridad, autenticación y despliegue.