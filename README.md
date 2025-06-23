Django User Authentication API
This project is a Django-based REST API for user authentication, including registration, login, profile management, password change, and password reset functionality. It uses Django REST Framework (DRF) and Simple JWT for token-based authentication.


Prerequisites :

Python 3.8+
Django 4.x
Django REST Framework
Simple JWT
Email backend configured (e.g., SMTP or console for testing)

Installation :

Clone the repository:git clone <repository-url>
cd <project-directory>


Create a virtual environment and activate it:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install dependencies:

pip install -r requirements.txt


Set up environment variables (e.g., .env file):

SECRET_KEY=your-secret-key
DEBUG=True
EMAIL_HOST=smtp.example.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@example.com
EMAIL_HOST_PASSWORD=your-email-password
EMAIL_USE_TLS=True


Run migrations:

python manage.py migrate


Start the development server:

python manage.py runserver



API Endpoints :

POST /register/: Register a new user.
POST /login/: Log in and receive JWT tokens.
GET /dashboard/: View user profile (authenticated).
POST /password-changed/: Change password (authenticated).
POST /password-reset/: Request password reset link.
POST /reset-password-confirm///: Confirm password reset.

Usage :

Register a user with email, name, terms & conditions (tc), password, and password confirmation.
Log in with email and password to receive access and refresh tokens.
Use the access token in the Authorization header (Bearer <access_token>) for authenticated endpoints.
Request a password reset link via email and use the provided link to reset the password.

Notes :

Email configuration is required for password reset functionality.
The password reset link is currently set to http://localhost:3000/reset-password/{uid}/{token}.

Update this in serializers.py to match your frontend URL.
Ensure JWT settings are configured in settings.py for Simple JWT.


ScreenShots:

Registration :

![1-registration](https://github.com/user-attachments/assets/6feb8490-7b84-400c-a2af-eae419361a35)

Login:

![2-succesfull login!](https://github.com/user-attachments/assets/405f0ddf-9c70-4efd-b729-29be966ebd55)

Registration With Token:

![3-registration with token](https://github.com/user-attachments/assets/616f04c3-5fcc-432e-8c25-3c74329f6f69)

Login With Token :

![4-Login with token](https://github.com/user-attachments/assets/71f839c4-05dc-40ea-8ae6-d831258c99df) 

Authorized user can see :

![5-Authorised user can see](https://github.com/user-attachments/assets/a0b78b13-f08d-43fc-ba6b-cc0b9c1871e9)

Password Changed:

![6-password Changed](https://github.com/user-attachments/assets/f0358ae3-e4b4-4108-84de-71f386af68d4)

Reset Link : 

![7 1-reset link](https://github.com/user-attachments/assets/fd13146f-f0b3-4bfa-ab35-b9abd6009a6e)

Password Reset:

![7-password Reset](https://github.com/user-attachments/assets/0a42cc95-2079-416a-9b92-1531801c250c)

Password Reset By click Link:

![8-password reset by click link](https://github.com/user-attachments/assets/0451d7f6-ecb0-43b1-a7dd-cc30486a116b)


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
