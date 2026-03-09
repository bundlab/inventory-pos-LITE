# Stage 1: Build React app
FROM node:20-alpine AS builder

WORKDIR /app

COPY package*.json ./
RUN npm ci

COPY . .
RUN npm run build

# Stage 2: Just copy dist (we serve from FastAPI)
FROM scratch AS export-stage
COPY --from=builder /app/dist /dist
