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
BASE_PATH = Path("/app") 
FRONTEND_DIST = BASE_PATH / "frontend" / "dist"

if FRONTEND_DIST.exists():
    # Serve assets (JS/CSS)
    app.mount("/assets", StaticFiles(directory=str(FRONTEND_DIST / "assets")), name="assets")
    
    @app.get("/{path:path}", include_in_schema=False)
    async def serve_spa(path: str):
        # Always serve index.html for any non-API route (SPA behavior)
        index_path = FRONTEND_DIST / "index.html"
        if index_path.exists():
            return FileResponse(str(index_path))
        return {"error": "index.html not found in dist"}
else:
    print(f"Warning: {FRONTEND_DIST} not found – API only mode")

@app.get("/health")
async def health():
    return {"status": "ok"}


@app.on_event("startup")
def on_startup():
    create_db_and_tables()
