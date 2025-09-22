# simple-notes-app-24019-24033

Notes App - Backend (Flask, Ocean Professional)

This repository contains a simple notes backend that supports CRUD operations and exposes RESTful endpoints with OpenAPI/Swagger documentation.

How to run (development):

1. Change directory:
   cd notes_app_backend

2. Create and activate a virtual environment (recommended):
   python3 -m venv .venv
   source .venv/bin/activate   # Windows: .venv\\Scripts\\activate

3. Install dependencies:
   pip install -r requirements.txt

4. Start the server:
   python run.py

5. Open API docs:
   The Swagger UI is served at /docs (e.g., http://localhost:5000/docs)
   OpenAPI JSON at /openapi.json

Available endpoints:

- Health:
  GET /            -> {"message": "Healthy"}

- Notes:
  GET    /api/notes/         -> list all notes
  POST   /api/notes/         -> create a note (JSON: { "title": "...", "content": "..." })
  GET    /api/notes/<id>     -> get a note by id
  PATCH  /api/notes/<id>     -> update a note (JSON: { "title"?: "...", "content"?: "..." })
  DELETE /api/notes/<id>     -> delete a note

Notes:
- Storage is in-memory for simplicity; data resets on process restart.
- No environment variables are required for this minimal setup.
- The code follows a clean and modular architecture (models, schemas, repositories, services, routes).