# Import necessary libraries
from flask import Flask, render_template_string, request, redirect, url_for

# Create a Flask application
app = Flask(__name__)

# Sample user credentials
USER_CREDENTIALS = {
    "admin": "password123"
}

# HTML templates
login_page = """
<!DOCTYPE html>
<html>
<head><title>Login</title></head>
<body>
    <h2>Login Page</h2>
    <form method="POST">
        Username: <input type="text" name="username"/><br/>
        Password: <input type="password" name="password"/><br/>
        <input type="submit" value="Login"/>
    </form>
    {% if error %}<p style="color:red;">{{ error }}</p>{% endif %}
</body>
</html>
"""

dashboard_page = """
<!DOCTYPE html>
<html>
<head><title>Dashboard</title></head>
<body>
    <h2>Welcome to the Dashboard</h2>
    <form method="GET" action="{{ url_for('search') }}">
        Search: <input type="text" name="query"/>
        <input type="submit" value="Search"/>
    </form>
</body>
</html>
"""

search_results_page = """
<!DOCTYPE html>
<html>
<head><title>Search Results</title></head>
<body>
    <h2>Search Results for "{{ query }}"</h2>
    <p>Showing results for "{{ query }}"...</p>
    <a href="{{ url_for('dashboard') }}">Back to Dashboard</a>
</body>
</html>
"""

# Define routes
@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if USER_CREDENTIALS.get(username) == password:
            return redirect(url_for('dashboard'))
        else:
            error = "Invalid credentials"
    return render_template_string(login_page, error=error)

@app.route('/dashboard')
def dashboard():
    return render_template_string(dashboard_page)

@app.route('/search')
def search():
    query = request.args.get('query', '')
    return render_template_string(search_results_page, query=query)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)