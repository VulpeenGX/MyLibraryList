# **Guion: Trabajo con Flask y SQLite**

## **1. Navegar al proyecto**
Desde la terminal, accede al directorio donde se encuentra tu proyecto de Flask:
```bash
cd C:\Users\DAM\Desktop\2ºDAM\flask\MyLibraryList
```

## **2. Acceder al shell interactivo de Flask**
Para trabajar con el shell interactivo de Flask, inicia el shell indicando el módulo principal:
```bash
flask --app app shell
```
**Nota:** Asegúrate de que tu archivo `__init__.py` contiene la función `create_app()` y que la variable `app` está correctamente definida.

---

## **3. Comandos dentro del shell**

### **a. Importar modelos y base de datos**
```python
from app.models import User, Libro
from app import db
```

### **b. Crear un usuario**
Crea una instancia de un usuario:
```python
user = User('alex', '123456')
```

### **c. Consultar usuarios existentes**
Comprueba si hay usuarios en la base de datos:
```python
users = User.query.all()
users  # Devuelve una lista con los usuarios
```

### **d. Añadir un usuario a la base de datos**
Añade el usuario y confirma los cambios:
```python
db.session.add(user)
db.session.commit()
```

Consulta nuevamente para verificar:
```python
users = User.query.all()
users  # Debería incluir el nuevo usuario <User: alex>
```

---

## **4. Trabajar con libros**

### **a. Importar `date`**
Antes de crear un libro con una fecha, importa la función `date` del módulo `datetime`:
```python
from datetime import date
```

### **b. Crear un libro**
Crea una instancia de `Libro`:
```python
Libro1 = Libro(1, 'El Quijote', 'Miguel de Cervantes', 'Novela', date(1605, 1, 16))
```

### **c. Añadir el libro a la base de datos**
Guarda el libro en la base de datos:
```python
db.session.add(Libro1)
db.session.commit()
```

---

## **Errores comunes y solución**

### **Error al importar el módulo principal**
Si ves un error como:
```bash
Error: Could not import 'MyLibraryList'.
```
Asegúrate de que:
- El nombre del módulo principal (`app`) coincide con el argumento de `--app`.
- Tu archivo `__init__.py` contiene correctamente la función `create_app()`.

### **Error al usar `date`**
Si obtienes:
```python
NameError: name 'date' is not defined
```
Importa `date` explícitamente desde `datetime`:
```python
from datetime import date
```

---

## **5. Resumen de comandos**

### Comandos de terminal:
```bash
cd C:\Users\DAM\Desktop\2ºDAM\flask\MyLibraryList
flask --app app shell
```

### Comandos de shell de Flask:
```python
# Importar modelos y base de datos
from app.models import User, Libro
from app import db

# Crear un usuario
user = User('alex', '123456')

# Consultar usuarios
users = User.query.all()

# Añadir usuario a la base de datos
db.session.add(user)
db.session.commit()

# Importar date y crear un libro
from datetime import date
Libro1 = Libro(1, 'El Quijote', 'Miguel de Cervantes', 'Novela', date(1605, 1, 16))

# Añadir libro a la base de datos
db.session.add(Libro1)
db.session.commit()
