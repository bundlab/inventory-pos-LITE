# Inventory POS Lite

Lightweight **Inventory + Point of Sale** system built with modern stack.

**Backend**: FastAPI + SQLModel + PostgreSQL  
**Frontend**: React 18 + TypeScript + Vite + TanStack Query  
**Deployment-ready**: Docker + docker-compose

![dashboard-screenshot](https://via.placeholder.com/1280x720?text=Dashboard+Screenshot)  
*(replace with real screenshot later)*

## Features

- CRUD for products/items
- Simple POS cart + quick sale
- Basic stock movement tracking
- JWT authentication (admin + cashier roles planned)
- Responsive design (mobile friendly POS)

## Tech Stack

- Backend
  - Python 3.11+
  - FastAPI 0.115+
  - SQLModel 0.0.20+
  - PostgreSQL 16
  - python-jose[cryptography] + passlib
- Frontend
  - React 18
  - TypeScript
  - Vite
  - @tanstack/react-query
  - Tailwind CSS 3 + shadcn/ui (recommended)
  - lucide-react icons
- DevOps
  - Docker & docker-compose
  - GitHub Actions (lint + test)

## Quick Start (Development)

```bash
# 1. Clone repo
git clone https://github.com/yourusername/inventory-pos-lite.git
cd inventory-pos-lite

# 2. Copy env files
cp .env.example .env
cp backend/.env.example backend/.env
cp frontend/.env.example frontend/.env

# 3. Start everything with Docker
docker compose up -d --build

# Backend  →  http://localhost:8000/docs
# Frontend →  http://localhost:5173
