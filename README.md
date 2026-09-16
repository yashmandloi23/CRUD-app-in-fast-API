# Telusko Trac - Full-Stack Product Inventory App

A full-stack product management web application built with a **FastAPI** and **PostgreSQL** backend paired with a modern, responsive **React** frontend. It enables full CRUD (Create, Read, Update, Delete) operations, dynamic search filtering, and column-based sorting.

---

## Features

- **Full CRUD Operations**: Create, read, edit, and delete product entries stored in a PostgreSQL database.
- **Auto-Initialization**: Pre-populates sample catalog data on first startup if the database table is empty.
- **Client-Side Filtering & Sorting**: Real-time multi-field search (ID, name, description) and ascending/descending column sorting.
- **FastAPI Validation**: Pydantic models for request body validation and response serialization.
- **Modern Responsive UI**: Styled with clean CSS glassmorphism, responsive grid layouts, and status notifications.

---

## Tech Stack

### Backend
- **FastAPI**: Asynchronous web framework for REST API endpoints.
- **PostgreSQL**: Relational database for persistent storage.
- **SQLAlchemy**: ORM for database connection and query handling.
- **Pydantic**: Data parsing and schema validation.
- **Uvicorn**: Lightning-fast ASGI server.

### Frontend
- **React**: Interactive component-driven user interface.
- **Axios**: HTTP client for API communication.
- **Vanilla CSS**: Custom styling with glassmorphic cards, gradients, and flexbox/grid layout.

---

## Project Structure

```text
├── backend/
│   ├── database.py         # SQLAlchemy engine and session setup
│   ├── database_models.py  # SQLAlchemy ORM table definitions
│   ├── models.py           # Pydantic schemas
│   └── main.py             # FastAPI routes, middleware, and startup hooks
├── frontend/
│   ├── src/
│   │   ├── App.js          # Main React logic (CRUD, sort, search)
│   │   ├── App.css         # Main application styles
│   │   ├── TaglineSection.jsx
│   │   ├── TaglineSection.css
│   │   ├── index.js        # React DOM entrypoint
│   │   └── index.css       # Global base CSS
│   └── package.json
└── README.md