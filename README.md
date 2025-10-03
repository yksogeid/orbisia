# Instalación y Configuración - OrbisIA CRM

Este documento explica paso a paso cómo instalar y ejecutar el **CRM OrbisIA** desarrollado en Flask con MySQL, sin necesidad de archivo `.env`.

---

## 1️⃣ Requisitos

* **Python 3.10+**
* **MySQL** (o MariaDB) funcionando localmente o remoto
* **pip** (gestor de paquetes de Python)

---

## 2️⃣ Clonar el proyecto

```bash
git clone <tu-repositorio-url>
cd botia_crm
```

---

## 3️⃣ Crear un entorno virtual (opcional pero recomendado)

```bash
# En Windows
python -m venv venv
venv\Scripts\activate

# En Linux / macOS
python3 -m venv venv
source venv/bin/activate
```

---

## 4️⃣ Instalar dependencias

```bash
pip install flask flask_sqlalchemy pymysql
```

> Estas librerías son necesarias para correr la aplicación y conectar con MySQL.

---

## 5️⃣ Configuración de la base de datos

1. Asegúrate de tener **MySQL corriendo**.
2. Crea la base de datos si no existe:

```sql
CREATE DATABASE orbisia;
```

3. En `config.py` verifica que la conexión a la base de datos sea correcta:

```python
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://usuario:password@localhost:3306/orbisia"
```

> Cambia `usuario` y `password` por tu usuario y contraseña de MySQL si es diferente.

---

## 6️⃣ Inicializar la base de datos

La aplicación creará automáticamente las tablas al arrancar:

```bash
python run.py
```

Verifica en la consola que aparezca:

```
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
```

---

## 7️⃣ Ejecutar la aplicación

```bash
python run.py
```

* Accede desde tu navegador en: [http://127.0.0.1:5000](http://127.0.0.1:5000)
* Verás el dashboard con **Orbis Bot** listo para mostrar conversaciones.

---

## 8️⃣ Estructura del proyecto

```
CRM/
├─ app/
│  ├─ __init__.py
│  ├─ models.py
│  ├─ routes.py
│  ├─ controllers/
│  │  └─ mensaje_controller.py
│  ├─ templates/
│  │  └─ index.html
│  └─ static/
│      └─ img/
│          └─ logo.png
├─ config.py
└─ run.py
```

---

## 9️⃣ Notas importantes

* No uses `.env`, las variables de configuración están directamente en `config.py`.
* La app levantará automáticamente las tablas si no existen.
* Puedes modificar `run.py` para cambiar el puerto o activar/desactivar debug.

---

¡Listo! Tu CRM OrbisIA con **Orbis Bot** debería funcionar correct
