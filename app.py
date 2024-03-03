from flask import Flask, render_template, request, redirect, url_for, session
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Dictionary to store user information
users = {}

# Notes dictionary to store user-specific notes
notes = {}

@app.route('/')
def index():
    if 'username' in session:
        # Get notes for the logged-in user
        user_notes = notes.get(session['username'], [])
        return render_template('index.html', notes=user_notes)
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username not in users:
            users[username] = password
            notes[username] = []
            return redirect(url_for('login'))  # Redirect to the login page
        return "Username already exists. Please choose another username."
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('index'))
        return "Invalid username or password."
    return render_template('login.html')

@app.route('/logout')
def logout():
    # Remove the username from the session if it exists
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/add_note', methods=['POST'])
def add_note():
    if 'username' in session:
        note_content = request.form.get('note')
        if note_content:
            # Get the current date and time
            now = datetime.now()
            current_date = now.strftime("%Y-%m-%d %H:%M:%S")
            # Create a new note dictionary
            new_note = {'content': note_content, 'timestamp': current_date}
            # Add the new note to the user's notes
            notes.setdefault(session['username'], []).append(new_note)
    return redirect(url_for('index'))

@app.route('/edit_note/<int:index>', methods=['POST'])
def edit_note(index):
    if 'username' in session:
        # Set the editing flag to True for the note at the specified index
        notes[session['username']][index]['editing'] = True
        return redirect(url_for('index'))
    return redirect(url_for('login'))

@app.route('/save_edit/<int:index>', methods=['POST'])
def save_edit(index):
    if 'username' in session:
        note_content = request.form.get('note')
        if note_content:
            # Update the note content
            notes[session['username']][index]['content'] = note_content
            # Remove the editing flag
            del notes[session['username']][index]['editing']
    return redirect(url_for('index'))

@app.route('/delete_note/<int:index>', methods=['POST'])
def delete_note(index):
    if 'username' in session:
        # Delete the note at the specified index
        del notes[session['username']][index]
        return redirect(url_for('index'))
    return redirect(url_for('login'))

if __name__ == '__main__':
       app.run(debug=True,host='0.0.0.0',port=5000)
