import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pathlib import Path
from fastapi.middleware.cors import CORSMiddleware

from app.api.router import items   # your existing routers
from app.core.config import settings
from app.database import create_db_and_tables

app = FastAPI(title="Inventory POS Lite", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount API routers
app.include_router(items.router, prefix="/api/items", tags=["items"])
# ... other routers

# Serve React build in production mode
# Inside the Docker container, everything is relative to /app
# Serve React build
BASE_PATH = Path("/app")
FRONTEND_DIST = BASE_PATH / "frontend" / "dist"

if FRONTEND_DIST.exists():
    # 1. Serve JS / CSS / images from /assets
    app.mount(
        "/assets",
        StaticFiles(directory=FRONTEND_DIST / "assets"),
        name="assets",
    )

    # 2. Serve index.html for the root
    @app.get("/")
    async def serve_root():
        return FileResponse(FRONTEND_DIST / "index.html")

    # 3. SPA fallback for client-side routes (exclude assets and api)
    @app.get("/{full_path:path}")
    async def serve_spa(full_path: str):
        if full_path.startswith(("api/", "assets/", "docs", "openapi.json", "health")):
            return {"detail": "Not Found"}
        return FileResponse(FRONTEND_DIST / "index.html")
else:
    print(f"Warning: Frontend dist not found at {FRONTEND_DIST}")

@app.get("/health")
async def health():
    return {"status": "ok"}


@app.on_event("startup")
def on_startup():
    create_db_and_tables()
