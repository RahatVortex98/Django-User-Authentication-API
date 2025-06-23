Django User Authentication API
This project is a Django-based REST API for user authentication, including registration, login, profile management, password change, and password reset functionality. It uses Django REST Framework (DRF) and Simple JWT for token-based authentication.
Prerequisites

Python 3.8+
Django 4.x
Django REST Framework
Simple JWT
Email backend configured (e.g., SMTP or console for testing)

Installation

Clone the repository:git clone <repository-url>
cd <project-directory>


Create a virtual environment and activate it:python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install dependencies:pip install -r requirements.txt


Set up environment variables (e.g., .env file):SECRET_KEY=your-secret-key
DEBUG=True
EMAIL_HOST=smtp.example.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@example.com
EMAIL_HOST_PASSWORD=your-email-password
EMAIL_USE_TLS=True


Run migrations:python manage.py migrate


Start the development server:python manage.py runserver



API Endpoints

POST /register/: Register a new user.
POST /login/: Log in and receive JWT tokens.
GET /dashboard/: View user profile (authenticated).
POST /password-changed/: Change password (authenticated).
POST /password-reset/: Request password reset link.
POST /reset-password-confirm///: Confirm password reset.

Usage

Register a user with email, name, terms & conditions (tc), password, and password confirmation.
Log in with email and password to receive access and refresh tokens.
Use the access token in the Authorization header (Bearer <access_token>) for authenticated endpoints.
Request a password reset link via email and use the provided link to reset the password.

Notes

Email configuration is required for password reset functionality.
The password reset link is currently set to http://localhost:3000/reset-password/{uid}/{token}. Update this in serializers.py to match your frontend URL.
Ensure JWT settings are configured in settings.py for Simple JWT.

Testing
Run tests with:
python manage.py test

Contributing

Fork the repository.
Create a feature branch (git checkout -b feature-name).
Commit changes (git commit -m "Add feature").
Push to the branch (git push origin feature-name).
Create a pull request.

License
MIT License
