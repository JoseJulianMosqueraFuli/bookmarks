# Bookmarks

This repository contains the code for a bookmarking application. That used Django Social Auth to add social authentication to your site using Facebook, Google, and Twitter.That run in development server with HTTPS on your local machine using Django Extensions. Customized the social authentication pipeline to create a user profile for new users automatically.

## Getting Started

To run this project on your local machine require docker, follow these steps:

1. Clone the repository:

```bash
git clone git@github.com:JoseJulianMosqueraFuli/bookmarks.git
```

2. Navigate into the repository:

```bash
cd bookmarks
```

3. Create the `.env` file for authentication, similar to the `.env.example` file:

```bash
FACEBOOK_APP_ID = <App Identifier>
FACEBOOK_APP_SECRET = <App Secret Key>
TWITTER_API_KEY = <App Identifier>
TWITTER_API_SECRET = <App Secret Key>
GOOGLE_CLIENT_ID = <App Identifier>
GOOGLE_CLIENT_SECRET = <App Secret Key>
```

4. Run docker command:

```bash
docker-compose up --build
```

Or Manual configuration use:

1. Clone the repository:

```bash
git clone git@github.com:JoseJulianMosqueraFuli/bookmarks.git
```

2. Create a virtual environment:

```bash
python3 -m venv venv
```

3. Activate the virtual environment:

```bash
source venv/bin/activate
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. Navigate into the cloned directory:

```bash
cd bookmarks
```

6. Create the `.env` file for authentication, similar to the `.env.example` file:

```bash
FACEBOOK_APP_ID = <App Identifier>
FACEBOOK_APP_SECRET = <App Secret Key>
TWITTER_API_KEY = <App Identifier>
TWITTER_API_SECRET = <App Secret Key>
GOOGLE_CLIENT_ID = <App Identifier>
GOOGLE_CLIENT_SECRET = <App Secret Key>
```

7. Start docker and run:

```bash
docker pull redis
docker run -it --rm --name redis -p 6379:6379 redis
```

8. Apply the database migrations:

```bash
python manage.py migrate
```

9. Start the development server:

```bash
python manage.py runserver
```

10. _Optional_: If you want to run the development server with HTTPS, use:

    **_NOTE_**: Remember that you have to configure your [hosts](https://www.hostinger.com/tutorials/how-to-edit-hosts-file) for https configuration.

```bash
python manage.py runserver_plus --cert-file cert.pem
```

Now, you can access the application in your browser at [http://127.0.0.1:8000/](http://127.0.0.1:8000/). Enjoy using the bookmarking application!

## Key Features Implemented

- User registration: Users can create an account by providing their username, email, and password.
- User login: Registered users can log in to their accounts using their credentials.
- User logout: Users can securely log out of their accounts.
- Password management: Users can change their passwords and reset them if they forget.
- Custom user profiles: A model is implemented to store additional information about each user, such as their date of birth and profile photo.
- Custom authentication backend: An authentication backend is added to allow users to log in using their email address instead of their username.
- Creating many-to-many relationships
- Customizing behavior for forms
- Using JavaScript with Django
- Building a JavaScript bookmarklet
- Generating image thumbnails using easy-thumbnails
- Implementing asynchronous HTTP requests with JavaScript and Django
- Building infinite scroll pagination
- Building a follow system
- Creating an activity stream application
- Adding generic relations to models
- Optimizing QuerySets for related objects
- Using signals for denormalizing counts
- Using Django Debug Toolbar to obtain relevant debug information
- Counting image views with Redis
- Creating a ranking of the most viewed images with Redis

## Next Steps

This improvements could be cover the following points:

- Create Test
- Always could improve

## License

This project is licensed under the [MIT License](LICENSE).

## Author

Build it by [Jose Julian Mosquera Fuli](https://github.com/JoseJulianMosqueraFuli).
