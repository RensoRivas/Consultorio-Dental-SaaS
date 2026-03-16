# Consultorio Dental SaaS

Aplicación SaaS para clínicas dentales pequeñas.

## Stack
- **Frontend:** Next.js
- **Backend:** FastAPI
- **Base de datos:** PostgreSQL

## MVP inicial
- Login de usuarios
- Gestión de pacientes
- Gestión de citas

## Estructura del proyecto

```text
.
├── frontend/
│   ├── package.json
│   ├── next.config.js
│   ├── tsconfig.json
│   └── src/app/
│       ├── layout.tsx
│       ├── page.tsx
│       └── globals.css
├── backend/
│   ├── requirements.txt
│   ├── Dockerfile
│   └── app/
│       ├── main.py
│       ├── db.py
│       ├── models.py
│       └── schemas.py
├── docker-compose.yml
└── .env.example
```

## Requisitos
- Docker y Docker Compose (recomendado)
- O manualmente:
  - Node.js 20+
  - Python 3.11+
  - PostgreSQL 15+

## Levantar en local con Docker

```bash
docker compose up --build
```

Servicios:
- Frontend: http://localhost:3000
- Backend (API docs): http://localhost:8000/docs
- PostgreSQL: localhost:5432

## Variables de entorno

1. Copiar archivo de ejemplo:

```bash
cp .env.example .env
```

2. Ajustar valores según tu entorno.

## Próximos pasos sugeridos
- Implementar autenticación JWT.
- Crear endpoints CRUD de pacientes.
- Crear endpoints CRUD de citas.
- Conectar frontend con backend mediante cliente API.
