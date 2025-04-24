# 🚴️ StravaScraper

**StravaScraper** es una herramienta desarrollada en Python que permite obtener información pública de perfiles de atletas de Strava mediante *web scraping*. Está diseñada para ejecutarse como **API REST (FastAPI)** o desde la **línea de comandos (CLI)**. Además, está completamente contenedorizada con **Docker**.

---

## ✨ Funcionalidades

- 🔎 Buscar usuarios por nombre  
- 🧝 Obtener perfil individual por ID  
- 📦 Obtener múltiples perfiles por lista de IDs  
- 📄 Exportar los resultados en formato JSON  
- 🌐 Exposición vía API REST o CLI  
- 🐳 Contenedorizado con Docker y compatible con Make  

---

## ⚙️ Requisitos

- Python 3.11+ (probado con 3.13.3)  
- Docker + Docker Compose  
- GNU Make (opcional para desarrollo más ágil)  
- Archivo `.env` con cookies de sesión válidas  

---

## 🔐 Configuración `.env`

```env
STRAVA_SESSION=tu_cookie_strava_session
STRAVA_REMEMBER_ID=tu_strava_remember_id
STRAVA_REMEMBER_TOKEN=tu_strava_remember_token

UVICORN_HOST=0.0.0.0
UVICORN_PORT=8000
```

---

## 🐳 Uso con Docker

### 🔨 Levantar la API

```bash
docker-compose up -d
```


### 💻 Entrar al contenedor (para usar CLI manualmente)

```bash
docker exec -it strava_api bash
```

---

## ⚙️ Uso con Make (opcional)

```bash
make up                       # Inicia el contenedor con FastAPI
make down                    # Detiene el contenedor
make logs                    # Muestra los logs
make shell                   # Accede al contenedor con bash
make cli NAME=juan           # Ejecuta el CLI buscando por nombre
make cli IDS="123 456"       # Ejecuta el CLI buscando por IDs
make cli NAME=juan EXPORT=true  # Exporta a JSON
```

---

## 📬 Ejemplos de uso vía API (curl)

### 🔍 Buscar usuarios por nombre

```bash
curl --location 'http://127.0.0.1:8000/api/search/?name=juan'
```

### 👤 Obtener perfil por ID

```bash
curl --location 'http://127.0.0.1:8000/api/profile/45678'
```

### 📦 Obtener perfiles por lista de IDs

```bash
curl --location 'http://127.0.0.1:8000/api/profiles' \
     --header 'Content-Type: application/json' \
     --data '{
       "user_ids": [30995, 36442011, 5952380]
     }'
```

### 📄 Exportar perfiles a JSON (por IDs)

```bash
curl --location 'http://127.0.0.1:8000/api/export/by-ids' \
--header 'Content-Type: application/json' \
--data '{
  "user_ids": [3098895, 36442011, 5952380]
}'
```

---

## 💻 Uso por línea de comandos (CLI)

```bash
# Obtener por nombre
python -m cli --name juan

# Obtener por IDs
python -m cli --ids 3098895 36442011

# Exportar a JSON
python -m cli --name juan --export
```

---

## 🧪 Instalación local (sin Docker)

Desarrollar localmente sin usar contenedores Docker:

```bash
# Crea un entorno virtual
python -m venv .venv

# Activa el entorno
source .venv/bin/activate   # En Windows: .venv\Scripts\activate

# Instala las dependencias
pip install -r requirements.txt

# Ejecuta desde CLI
python -m cli --name juan
```

---

## 🧠 Decisiones técnicas

- 🔐 Autenticación por cookies capturadas desde una sesión legítima en Strava.
- 🧼 Uso de `BeautifulSoup` para parsear HTML.
- ⟲ Scraper centralizado en `StravaScraper`, reutilizable vía API o CLI.
- 🧱 Estructura modular con `file_system` para rutas y exportación.
- 📂 Sistema de archivos gestionado por `FileSystemManager` con soporte singleton.
- 📄 Exportación por defecto en `core/config/_data/users.json` o donde el desarrollador indique.

---

## 🔧 Arquitectura del cliente HTTP

- ✨ Cliente desacoplado mediante inyección: `RequestsClient`.
- 🌐 Cabeceras realistas generadas con `browserforge`.
- 🔧 Métodos: `request_get`, `request_post`, `load_cookies`.
- 🔌 Diseño extensible a Playwright, Selenium, etc.

```python
from core.http_client.requests_client import RequestsClient
scraper = StravaScraper(RequestsClient())
```

---

## 📂 Estructura del proyecto

```
.
├── api/                 # FastAPI
├── cli/                 # CLI ejecutable
├── core/
│   ├── engine/          # Lógica de scraping
│   ├── http_client/     # Cliente HTTP
│   ├── file_system/     # Rutas, exportaciones
│   └── config/          # _data/users.json
├── models.py            # DTO principal
├── api_models.py        # Pydantic para FastAPI
├── settings.py          # Configuración y logger
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── Makefile
```

---

## 👤 Autor

**Juan Daniel**  
Desarrollador backend | scraping & automatización  
GitHub: [@JuanDiaz91](https://github.com/JuanDiaz91)

