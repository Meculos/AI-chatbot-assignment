# AI Chat Project

## Overview
AI Chat Project is a simple API-based chat application where users can send messages and receive AI-generated responses. The system implements authentication, user token management, and message tracking.

## Project Structure
- **Project Name**: `ai_chat_project`
- **App Name**: `ai_chat_app`

## Features
- User registration and authentication using **JWT**.
- Token-based system where users spend tokens for each chat.
- RESTful API with endpoints for user info, chat messages, and token retrieval.
- API documentation with **DRF Spectacular**.
- **REST Client API testing file (`api.http`)** included.

## Installation & Setup
### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- Django & Django REST Framework
- DRF Spectacular for API documentation

### Steps
1. **Clone the repository**:
   ```sh
   git clone https://github.com/Meculos/AI-chatbot-assignment.git
   cd ai_chat_project
   ```
2. **Create and activate a virtual environment**:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install dependencies**:
   ```sh
   pip install -r requirements.txt
   ```
4. **Run migrations**:
   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```
5. **Start the server**:
   ```sh
   python manage.py runserver
   ```
6. **Generate API schema (Optional, if not auto-generated)**:
   ```sh
   python manage.py spectacular --color --file schema.yml
   ```

## API Endpoints
### Authentication
- `POST /ai_chat_app/api/token/` - Obtain JWT token
- `POST /ai_chat_app/api/token/refresh/` - Refresh JWT token

### User Management
- `POST /ai_chat_app/register/` - Register a new user
- `GET /ai_chat_app/user_info/` - Retrieve user details (includes username & tokens)

### Chat Management
- `POST /ai_chat_app/chat/` - Send a chat message
- `GET /ai_chat-app/chat/` - View chat history (for authenticated users)

### API Documentation
- **Swagger UI**: [`/ai_chat_app/api/schema/swagger-ui/`](http://127.0.0.1:8000/api/schema/swagger-ui/)
- **ReDoc**: [`/ai_chat_app/api/schema/redoc/`](http://127.0.0.1:8000/api/schema/redoc/)

## Improvements Made
- **Switched to Django’s `AbstractUser` model** for better user management.
- **Implemented JWT authentication** instead of custom token handling.
- **Added DRF Spectacular** for auto-generated API documentation.
- **REST Client (`api.http`) file** included for easy API testing.

## Potential Future Improvements
- **Pagination for chat history** to handle large message logs efficiently.
- **Search functionality** for easier retrieval of past messages.
- **Rate limiting** to prevent excessive API usage.
- **Frontend UI** for better user experience.

## Testing
- Use **REST Client API (`api.http`)** to test API endpoints.
- Use **Swagger UI** or **ReDoc** to interact with the API.

## License
This project is for learning purposes and is not intended for production use.
