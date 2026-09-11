# Contributing to Inventory POS Lite

Thank you for your interest in contributing!  
This project is a lightweight Inventory + Point of Sale system built with **FastAPI**, **React (Vite)**, **PostgreSQL**, and **Docker**.

We welcome contributions of all kinds — bug fixes, new features, documentation improvements, and performance enhancements.

---

## Getting Started

### 1. Fork & Clone

```bash
git clone https://github.com/YOUR_USERNAME/inventory-pos-lite.git
cd inventory-pos-lite
```

### 2. Set up the development environment

```bash
# Copy environment files
cp .env.example .env
cp backend/.env.example backend/.env

# Build and start with Docker
docker compose up -d --build
```

- Frontend + Backend: http://localhost:8001  
- API Docs: http://localhost:8001/docs

### 3. Frontend development (optional)

```bash
cd frontend
npm install
npm run dev
```

---

## How to Contribute

### Reporting Bugs

- Check if the issue already exists.
- Open a new issue and include:
  - Clear title
  - Steps to reproduce
  - Expected vs actual behavior
  - Screenshots or logs (if relevant)
  - Your environment (OS, Docker version, browser)

### Suggesting Features

- Open an issue with the `enhancement` label.
- Describe the problem the feature solves and a possible solution.

### Pull Requests

1. Create a new branch from `main`:
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/your-bug-fix
   ```

2. Make your changes.

3. Commit using clear messages (see Commit Guidelines below).

4. Push your branch and open a Pull Request against `main`.

5. Fill in the Pull Request template and link any related issues.

---

## Commit Guidelines

We follow a simple conventional style:

- `feat:` → new feature
- `fix:` → bug fix
- `docs:` → documentation only
- `style:` → formatting, missing semi-colons, etc (no code change)
- `refactor:` → code change that neither fixes a bug nor adds a feature
- `chore:` → maintenance tasks (dependencies, config, etc.)

**Examples:**
```bash
feat(frontend): add edit and delete buttons to inventory table
fix(backend): correct static file serving for Vite build
docs: improve setup instructions in README
chore(docker): remove unused volume mount
```

---

## Code Style

### Backend (Python / FastAPI)
- Follow PEP 8
- Use type hints
- Keep endpoints thin — business logic in `crud` or services
- Write clear docstrings for non-obvious functions

### Frontend (React + TypeScript)
- Use functional components and hooks
- Prefer TypeScript interfaces/types
- Keep components small and focused
- Use Tailwind CSS utility classes

---

## Project Structure (quick reference)

```
backend/
  app/
    api/          # routers
    core/         # config, security
    crud/         # database operations
    models/       # SQLModel
    schemas/      # Pydantic models
    main.py
frontend/
  src/
    components/
    pages/
    hooks/
    lib/
    types/
```

---

## Need Help?

- Open an issue with the `question` or `help wanted` label
- Be respectful and patient — this is a learning-friendly project

Thank you for contributing!


