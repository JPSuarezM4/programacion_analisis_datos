# Workflow de ETL para Datos del Dólar con GitHub Actions

Este proyecto implementa un flujo completo de ETL (Extracción, Transformación y Carga) para datos del dólar usando GitHub Actions como orquestador de CI/CD.

## Estructura del Flujo de Trabajo con Docker en GitHub Actions

El proceso está centralizado en un único workflow Docker (`docker.yml`) que automatiza la construcción y ejecución de contenedores para manejar el flujo de datos.

### 1. Build & Setup Docker Image
- Se ejecuta al hacer push al branch principal (`main`).
- Realiza checkout del repositorio.
- Hace login en Docker Hub con las credenciales almacenadas en los secrets de GitHub.
- Construye la imagen Docker nombrada `contenedor` usando el Dockerfile del proyecto.

### 2. Data Extraction (Contenedor Docker)
- Ejecuta el script de extracción (`main_extractor.py`) dentro del contenedor Docker.
- Monta los volúmenes locales `static/csv` y `static/db` para persistencia de archivos CSV y base de datos.
- Extrae datos desde la fuente (Yahoo Finance) y guarda el CSV dentro del volumen compartido.

### 3. Data Ingestion (Contenedor Docker)
- Ejecuta el script de ingesta (`main_ingesta.py`) dentro del contenedor Docker.
- Usa los mismos volúmenes para leer el CSV generado y cargar los datos en la base de datos SQLite.
- Elimina el archivo CSV temporal después de la ingesta.

---

### Resumen

| Etapa                  | Acción                             | Frecuencia/Ejecución              |
|------------------------|----------------------------------|---------------------------------|
| Build Docker Image      | Construcción de imagen `contenedor` | Al hacer push a `main`           |
| Data Extraction        | Ejecutar `main_extractor.py` en Docker | Automático dentro del workflow  |
| Data Ingestion         | Ejecutar `main_ingesta.py` en Docker | Automático justo después de extracción |

---

Este flujo aprovecha la portabilidad y consistencia que ofrece Docker, asegurando que la extracción y la ingesta de datos se ejecuten en un entorno controlado y reproducible.


## Requisitos para la Configuración

Para que este workflow funcione correctamente, necesitas configurar los siguientes secretos en GitHub:

1. Para el envío de alertas por correo electrónico:
   - `EMAIL_SENDER`: Dirección de correo del remitente
   - `EMAIL_RECEIVER`: Dirección de correo del destinatario
   - `EMAIL_PASSWORD`: Contraseña o token de la cuenta del remitente
   - `SMTP_SERVER`: Servidor SMTP (valor predeterminado: smtp.gmail.com)
   - `SMTP_PORT`: Puerto SMTP (valor predeterminado: 587)

## Estructura del Proyecto

```
└── programacion_analisis_datos/
    ├── .github
    │   └── workflows
    ├── README.md
    ├── dockerfile
    ├── docs
    │   └── arquitectura.drawio
    ├── edu_pad.egg-info
    │   ├── PKG-INFO
    │   ├── SOURCES.txt
    │   ├── dependency_links.txt
    │   ├── requires.txt
    │   └── top_level.txt
    ├── main.yml
    ├── setup.py
    ├── src
    │   └── edu_pad
    └── tabla.html
```

## Instalación

1. Clona este repositorio
2. Configura los secretos en GitHub
3. Los workflows se ejecutarán automáticamente según lo programado o puedes iniciarlos manualmente

## Características Principales

- **Unificado**: Todo el flujo ETL se ejecuta dentro de un contenedor Docker para garantizar consistencia y portabilidad.
- **Automatizado**: Construcción de imagen Docker y ejecución de los procesos de extracción e ingesta en un solo workflow.
- **Montaje de volúmenes**: Uso de volúmenes para persistencia de archivos CSV y base de datos SQLite entre ejecuciones.
- **Aislamiento del entorno**: Los procesos corren dentro del contenedor, evitando conflictos de dependencias y configuración local.
- **Reutilización de imágenes**: La imagen Docker se construye y puede usarse para diferentes etapas sin reconstruir.
- **Facilidad de despliegue**: Integración directa con Docker Hub mediante login automático para subir o usar imágenes privadas.
- **Integración continua**: El workflow se dispara automáticamente al hacer push a la rama principal (`main`), manteniendo el pipeline actualizado.


## Personalización

Para adaptar este workflow a tus necesidades:

1. Modifica `dataweb.py` para extraer datos de otras fuentes
2. Ajusta la frecuencia de ejecución modificando las expresiones cron en los archivos YAML
3. Añade más análisis o transformaciones en la clase `DatabaseMonitor`
4. Actualiza `setup.py` si necesitas instalar paquetes adicionales

---

Creado para la formacion de analitica de datos utilizando GitHub Actions y Python
