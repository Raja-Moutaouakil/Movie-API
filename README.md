# Movie Review API

A small Django + Django REST Framework backend for storing movies and user reviews.

## Overview
- Purpose: provide a REST API to create, list, update, and delete movies and reviews.
- Tech: Python, Django, Django REST Framework, django-filter, drf-spectacular (OpenAPI), SimpleJWT for auth.

## Key Features
- **Movies:** full CRUD (title, description, release_date).
- **Reviews:** CRUD linked to a `Movie` and (optionally) a `User`.
- **Auth:** JWT access/refresh tokens for protected write operations.
- **Docs:** OpenAPI schema + Swagger UI and Redoc at `/api/docs/` and `/api/redoc/`.
- **Filters & Pagination:** DRF pagination and django-filter enabled.

## Quickstart (local development)
1. Create & activate the virtualenv (Windows PowerShell):
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```
2. Install dependencies:
```powershell
pip install -r requirements.txt
```
3. Apply migrations and start the server:
```powershell
python manage.py migrate
python manage.py runserver 8000
```
4. Open the docs in your browser:

- Swagger UI: `http://127.0.0.1:8000/api/docs/`
- Redoc: `http://127.0.0.1:8000/api/redoc/`

## Important Endpoints
- API root (router): `GET /api/`
- Movies collection: `GET/POST /api/movies/`
- Movie detail: `GET/PUT/PATCH/DELETE /api/movies/{id}/`
- Reviews collection: `GET/POST /api/reviews/`
- Review detail: `GET/PUT/PATCH/DELETE /api/reviews/{id}/`
- OpenAPI JSON: `GET /api/schema/`
- JWT token obtain: `POST /api/token/` (username + password)
- JWT token refresh: `POST /api/token/refresh/`

## Quick Demo (PowerShell)
- Create a test user (optional):
```powershell
python manage.py createsuperuser
```
- Obtain tokens:
```powershell
$body = @{ username='user'; password='pass' } | ConvertTo-Json
$tokens = Invoke-RestMethod -Uri 'http://127.0.0.1:8000/api/token/' -Method Post -Body $body -ContentType 'application/json'
$tokens | Format-List
```
- Create a movie (anonymous allowed by default in this dev setup):
```powershell
$body = @{ title='Demo Movie'; description='Smoke test' } | ConvertTo-Json
Invoke-RestMethod -Uri 'http://127.0.0.1:8000/api/movies/' -Method Post -Body $body -ContentType 'application/json'
```
- Create a review (authenticated):
```powershell
$access = '<ACCESS_TOKEN>'
$headers = @{ Authorization = "Bearer $access" }
$review = @{ movie=1; rating=5; content='Great' } | ConvertTo-Json
Invoke-RestMethod -Uri 'http://127.0.0.1:8000/api/reviews/' -Method Post -Body $review -ContentType 'application/json' -Headers $headers
```

## Smoke-test script
There is a helper script at `scripts\crud_test.ps1` that performs a basic create/list/delete flow against the running server. Run it with PowerShell:
```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\crud_test.ps1
```

## Development notes & known issues
- The root path `/` returns 404 by design — the API lives under `/api/`.
- For production, set `SECRET_KEY`, `DJANGO_DEBUG=False`, and `ALLOWED_HOSTS` environment variables.
- Tests and CI are not included; adding unit tests is recommended before deployment.

## Contributing
- PRs and issues welcome. If you find bugs, include server logs and reproduction steps.

---
Built as a learning capstone: Django + DRF patterns, JWT, and OpenAPI documentation.
