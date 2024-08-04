# TweetNow

TweetNow is a social media platform built with Python and Django that allows users to share their thoughts and images through tweets. It features robust user management and secure data storage, making it easy for users to register, log in, and manage their tweets. [image](https://github.com/Nitin-Pilkhwal/tweetnow.git)

## Features

- **Platform**: Built with Python and Django.
- **User Management**: New user registration and existing user login.
- **Database**: All data is stored in PostgreSQL on Supabase.
- **Tweeting**: Users can tweet with text and an image.
- **Tweet Management**: Users can view all tweets, but can only edit and delete their own tweets.

## Installation

To get a local copy up and running, follow these steps:

### Prerequisites

- Python 3.x
- PostgreSQL
- Django
- [Supabase account](https://supabase.com/)

### Setup

1. **Clone the repository:**
    ```sh
    git clone https://github.com/Nitin-Pilkhwal/tweetnow.git
    cd tweetnow
    ```

2. **Create and activate a virtual environment:**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Configure the database:**

    Update the `DATABASES` setting in `settings.py` with your Supabase PostgreSQL credentials:
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'your_database_name',
            'USER': 'your_database_user',
            'PASSWORD': 'your_database_password',
            'HOST': 'your_supabase_host',
            'PORT': '5432',
        }
    }
    ```

5. **Apply migrations:**
    ```sh
    python manage.py migrate
    ```

6. **Run the server:**
    ```sh
    python manage.py runserver
    ```

7. **Create a superuser (admin):**
    ```sh
    python manage.py createsuperuser
    ```

8. **Access the application:**

    Open your browser and go to `http://127.0.0.1:8000/tweet`.

## Usage

1. **Register a new user**: Go to the registration page and create a new account.
2. **Login**: Use your credentials to log in.
3. **Tweet**: Create a new tweet with text and an image.
4. **Manage Tweets**: View all tweets, edit your own tweets, and delete your own tweets.

## Contributing

Contributions are welcome! Please follow these steps:

1. **Fork the repository**
2. **Create a new branch**: `git checkout -b feature/YourFeature`
3. **Commit your changes**: `git commit -m 'Add some feature'`
4. **Push to the branch**: `git push origin feature/YourFeature`
5. **Open a pull request**

## Contact

Your Name - [Your Email](mailto:youremail@example.com)

---

Happy tweeting!
