# 🚀 Crypto Tracker Backend API

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![JWT](https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens)](https://jwt.io/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)

RESTful API сервис для отслеживания курсов криптовалют, управления пользовательскими портфелями и аутентификации. Написан на **FastAPI** с асинхронной архитектурой, использованием ORM **SQLAlchemy** и авторизацией по **JWT**.

---

## 🛠 Технологический стек

- **Фреймворк**: [FastAPI](https://fastapi.tiangolo.com/) (Python 3.10+)
- **База данных**: SQLite (с возможностью легкого перехода на PostgreSQL)
- **ORM & Миграции**: SQLAlchemy & Pydantic v2
- **Безопасность**: OAuth2 с JWT-токенами (Passlib, bcrypt)
- **Контейнеризация**: Docker & Docker Compose

---

## ✨ Основной функционал

- 🔑 **Аутентификация и Авторизация**: Регистрация пользователей, генерация безопасных JWT-токенов access/refresh.
- 📈 **Мониторинг криптовалют**: Получение актуальных данных о ценах и динамике рынка.
- 💼 **Портфель пользователя**: Управление активами, подсчет общего баланса и истории транзакций.
- 🛡 **Защита эндпоинтов**: Безопасный доступ к приватным маршрутам с валидацией токена.

---

## 🚀 Быстрый запуск

### Вариант 1: Локальный запуск (Python)

1. **Клонируйте репозиторий:**
   ```bash
   git clone [https://github.com/clawfast14-hash/crypto-tracker-backend.git](https://github.com/clawfast14-hash/crypto-tracker-backend.git)
   cd crypto-tracker-backend