## Project name
PITCH IT

### Author
Mungai Keren

### Email
wambukeren@gmail.com

## Project Description
An application designed to utilize 60 seconds of one's life to impress someone! A user submits a one minute pitch and other users votes on their pitch, leave comments and give feedback on the pitch. Pitches are arranged in categories; Business, Creative, Innovative, Interview pitch, Art

Logged in users have their profile page where they can view the pitches they pitched and see the voteage on them, upvotes and downvotes.

The application uses postgres sql database to store the various pitches and information in the website. WTF flask forms are heavily in use.

Project is then deployed to heroku

## Set-up instructions and installations
* Navigate to the projects folder then run ```python3 -m venv virtual```
* Go virtual ```source virtual/bin/activate``` You need to have the following installed
* Flask pip install flask
* Flask-script pip install flask-script
* Flask-bootstrap pip install flask-bootstrap you could still use the bootstrap cdn
* Flask-login pip install flask-login for user authentication
* Flask migrations are necessary for us to update our database

* Run ```python3.6 manage.py db init``` to initialize your migrations.
* Run ```python3.6 manage.py db migrate -m "message"``` for every migration required.
* Run  ```python3.6 manage.py db upgrade``` to upgrade your database migrations.
* Ensure to have the correct folder structure to minimize errors

## Development
It would be so great to have your contributions! Just follow the instructions below.

* Fork the repo
* Clone the repo in your machine but ensure you have all the necessary modules.(You can find them in the set up instructions above) ``git clone https://github.com/MungaiKeren/News-Highlight.git``
* Create a new branch ```git branch contributions```
* Edit your changes in your branch
* Run the application  ```python3.6 manage.py server```
* Push your changes so we can have a view!

### Known bugs
Currently the application is having trouble trying to send emails to the user.
The applications update 

## Behaviour Driven Development

| Input        | Output           | Behavior  |
| ------------- |:-------------:| -----:|
| Visit Bloggy site| Various blogs are displayed  | User can only see other people's pitches |
| Sign in    | Application sends a welcoming message | User has an account |
| Click on new blog| Application displays a form for you to post a blog  | Submit to save blog is saved |
| Subscribe... | Each time there's a new blog user recieves email | app send email |
| Sign out | Home page is displayed | leaves current logged in user |
| Visit profile| Profile details displayed | user can edit blogs they posted or upload profile photo|
## Technologies used
* Python (Flask micro-frame work)
* HTML for basic user interface
* Bootstrap CSS framework
* CSS

## License information
MIT license

## Visual representation
<img src="https://github.com/MungaiKeren/My-Shoe-images/blob/master/Blogsite1.png?raw=true" height='400px' width = '100%'>
