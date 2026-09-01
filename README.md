<div align="center">

  <h1>Inventory POS Lite</h1>

  <p>
    <strong>Lightweight Inventory + Point-of-Sale system</strong><br />
    Modern full-stack application built for small businesses & retail shops
  </p>

  <p>
    <a href="https://github.com/bundlab/inventory-pos-lite/actions/workflows/ci.yml">
      <img src="https://img.shields.io/github/actions/workflow/status/yourusername/inventory-pos-lite/ci.yml?branch=main&label=CI&logo=github" alt="CI Status">
    </a>
    <a href="https://github.com/bundlab/inventory-pos-lite/blob/main/LICENSE">
      <img src="https://img.shields.io/github/license/yourusername/inventory-pos-lite?color=blue" alt="License">
    </a>
    <a href="https://github.com/bundlab/inventory-pos-lite/stargazers">
      <img src="https://img.shields.io/github/stars/yourusername/inventory-pos-lite?style=social" alt="Stars">
    </a>
    <img src="https://img.shields.io/badge/Python-3.11%2B-blue?logo=python&logoColor=white" alt="Python">
    <img src="https://img.shields.io/badge/React-18-blue?logo=react&logoColor=white" alt="React">
    <img src="https://img.shields.io/badge/FastAPI-0.115+-brightgreen?logo=fastapi&logoColor=white" alt="FastAPI">
    <img src="https://img.shields.io/badge/Docker-ready-blue?logo=docker" alt="Docker">
  </p>

  <br />

  <!-- Replace with your real screenshot later -->
  <img src="https://via.placeholder.com/1280x720/1e3a8a/ffffff?text=Inventory+POS+Lite+Dashboard" alt="Dashboard Screenshot" width="800" />

</div>

<br />

## ✨ Features

- CRUD operations for inventory items (name, price, stock, barcode)
- Simple POS-like sale interface (planned)
- Real-time stock updates
- JWT authentication foundation (extendable)
- Responsive design (mobile-friendly POS view)
- PostgreSQL database
- Docker & docker-compose ready (single-command local production)
- Static frontend served directly from FastAPI (single port)

## 🛠️ Tech Stack

| Layer       | Technology                          | Purpose                              |
|-------------|-------------------------------------|--------------------------------------|
| Backend     | FastAPI 0.115+ • SQLModel • Pydantic | REST API, data validation, ORM       |
| Database    | PostgreSQL 16                       | Persistent storage                   |
| Frontend    | React 18 • TypeScript • Vite        | SPA, fast development & build        |
| State/Query | TanStack Query (React Query)        | Data fetching, caching, mutations    |
| Styling     | Tailwind CSS (recommended)          | Modern, utility-first styling        |
| Container   | Docker • docker-compose             | Local & production-like environment  |

## 📂 Project Structure
inventory-pos-lite/
├── backend/                    # FastAPI application
│   ├── app/                    # Core application code
│   │   ├── api/                # Routers (items, auth, etc.)
│   │   ├── core/               # Settings, security, JWT
│   │   ├── crud/               # Database operations
│   │   ├── models/             # SQLModel tables
│   │   ├── schemas/            # Pydantic models
│   │   ├── database.py
│   │   └── main.py             # App entry + static mount
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/                   # React + Vite + TypeScript
│   ├── src/
│   │   ├── components/         # Reusable UI
│   │   ├── pages/              # Page components
│   │   ├── hooks/              # Custom hooks (useItems, etc.)
│   │   ├── lib/                # API client (axios instance)
│   │   ├── types/              # TypeScript interfaces
│   │   ├── App.tsx
│   │   └── main.tsx
│   ├── public/
│   ├── vite.config.ts
│   ├── Dockerfile (multi-stage)
│   └── package.json
├── docker-compose.yml          # PostgreSQL + backend (frontend static)
├── .env.example
├── .gitignore
└── README.md

## 🚀 Quick Start (Local Production Mode)

```bash
# 1. Clone the repository
git clone https://github.com/bundlab/inventory-pos-lite.git
cd inventory-pos-lite

# 2. Copy environment files
cp .env.example .env
cp backend/.env.example backend/.env

# 3. Build frontend (important!)
cd frontend
npm install
npm run build
cd ..

# 4. Start everything with Docker
docker compose up -d --build

# 5. Open in browser
# → http://localhost:8000