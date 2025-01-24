# 📚 MyLibraryList

**MyLibraryList** es una aplicación web desarrollada con **Flask** en Python, diseñada para gestionar tus libros favoritos de manera eficiente y organizada. Con una interfaz intuitiva y funcionalidades avanzadas, te permite administrar, crear, editar y eliminar libros fácilmente, todo mientras asegura la privacidad y la protección de tus datos con un sistema de autenticación seguro.

---

## 🚀 Características principales

### 🛡️ Seguridad y autenticación
- **Inicio de sesión**: Los usuarios pueden registrarse e iniciar sesión para acceder a sus bibliotecas personales.
- **Mantener sesión**: Permite mantener la sesión activa hasta que el usuario decida cerrarla.
- **Protección de rutas**: Las rutas están protegidas mediante autenticación de sesión; no se puede acceder a ellas ni siquiera desde la URL sin iniciar sesión.
- **Cierre de sesión seguro**: Permite a los usuarios cerrar sesión y garantiza la protección de sus datos.

### 📖 Gestión de libros
- **Lista de libros**: Visualiza todos los libros agregados por el usuario.
- **Crear libros**: Añade nuevos libros a tu colección personal con un formulario intuitivo.
- **Editar libros**: Modifica los detalles de un libro existente.
- **Borrar libros**: Elimina libros de tu colección con facilidad.

### 🛠️ Desarrollo robusto
- **Framework Flask**: Backend rápido y ligero con funcionalidad extendida.
- **SQLAlchemy + SQLite**: Gestión y persistencia de datos mediante un ORM confiable.
- **Jinja2 y HTML**: Plantillas dinámicas para una experiencia de usuario mejorada.
- **Bootstrap**: Diseño responsivo y visualmente atractivo.
- **Manejo de formularios**: Validación de datos y manejo sencillo de entradas de usuarios.

---

## 🖥️ Instalación y configuración

Sigue estos pasos para ejecutar la aplicación en tu máquina local:

### 1️⃣ Clonar el repositorio
```bash
git clone https://github.com/tuusuario/mylibrarylist.git
cd mylibrarylist
```
### 📂 Estructura del proyecto

 La aplicación está organizada de la siguiente manera:

    MyLibraryList/
    │
    ├── app/
    │   ├── static/               # Archivos estáticos (CSS, JS, imágenes)
    │   ├── templates/            # Plantillas HTML (base.html, index.html, etc.)
    │   ├── __init__.py           # Configuración de la aplicación Flask
    │   ├── models.py             # Modelos de datos con SQLAlchemy
    │   ├── routes.py             # Rutas y lógica de la aplicación
    │   └── forms.py              # Manejo de formularios con Flask-WTF
    │
    ├── instance/
    │   └── app.db                # Base de datos SQLite
    │
    ├── requirements.txt          # Dependencias del proyecto
    ├── README.md                 # Documentación del proyecto
    └── run.py                    # Archivo principal para ejecutar la app

 ### 💡 Funcionalidades futuras
Algunas ideas para mejorar la aplicación en versiones futuras:

-**Sistema** de recomendaciones de libros basado en intereses del usuario.
-**Organización** de libros por categorías como género, autor o año de publicación.
-**Funcionalidad** para exportar e importar la lista de libros en formatos CSV o PDF.
-**Diseño** más interactivo con animaciones y gráficos dinámicos.
-**Notificaciones** por correo para recordar libros pendientes de leer.


### 👩‍💻 Tecnologías utilizadas
Esta aplicación utiliza las siguientes herramientas y tecnologías:

-**Python**: Framework Flask, ORM SQLAlchemy, validación con Flask-WTF.
-**HTML5**: Estructuración de contenido con Jinja2.
-**CSS3**: Diseño visual con Bootstrap para una interfaz moderna y responsiva.
-**SQLite**: Base de datos ligera para almacenamiento local.
-**JavaScript**: Añade interactividad y mejora la experiencia del usuario.


###📝 Contacto
Desarrollado por Alejandro Gutiérrez Pereira.
Estudiante de Desarrollo de Aplicaciones Multiplataforma (DAM).