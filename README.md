Note Taking Application
This is a simple note-taking application built using Flask, HTML, and Python. The application allows users to add, edit, and delete notes, which are displayed with timestamps indicating when they were added.

Features
User Registration: Users can create an account with a unique username and password.
User Login: Registered users can log in to their account.
Add Notes: Users can enter a note in the input field and click "Add Note" to add it to the list with a timestamp.
Edit Notes: Users can edit existing notes.
Delete Notes: Users can delete notes they no longer need.

Installation
Create a new folder for your project:


mkdir note-taking-app
cd note-taking-app

Create a file named app.py for your Flask application:

touch app.py

Create a folder named templates for your HTML templates:

mkdir templates
Install Flask using pip:

pip install Flask

Running the Application
Run the application:

python app.py

Access the application in your web browser at http://localhost:5000.

Usage
Registration: If you don't have an account, click on the "Register" link to create one.
Login: If you already have an account, enter your username and password and click "Login".
Add Notes: Enter a note in the input field and click "Add Note". Your note will be displayed with a timestamp.
Edit Notes: Click on the "Edit" button next to a note to edit it.
Delete Notes: Click on the "Delete" button next to a note to delete it.
