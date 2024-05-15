from flask import Flask, render_template, request, redirect, url_for
import sqlite3


#Initializing the flask app (creates an instance of the flask class)
app = Flask(__name__)


#Connect Sqlite database
connect = sqlite3.connect("prospect_tenants.db",check_same_thread=False)
cursor = connect.cursor()

#Define the home page route and rendering index.html
@app.route("/", methods=["GET", "POST"])
def index():
    
    # Fetch properties from the database with column names
    cursor.execute("SELECT id, name, address,rent, area, agent_name FROM properties")
    properties = cursor.fetchall()
            
    return render_template("/index.html",properties=properties)


# Route to handle registration form submission
@app.route('/register_interest', methods=["POST"])
def register_interest():
    # Get form data from the request
    name = request.form["name"]
    email = request.form["email"]
    phone = request.form["phone"]
    property_id = request.form["property_id"]

    # Insert tenant information into the tenants table
    cursor.execute("INSERT INTO tenants (property_id, property_name, name, email, phone) VALUES (?, ?, ?, ?, ?)",
              (property_id, get_property_name(property_id), name, email, phone))
    connect.commit()

    # Redirect back to the home page or display a success message
    return redirect(url_for('index'))

# Helper function to get the property name from the property ID
def get_property_name(property_id):
    cursor.execute("SELECT name FROM properties WHERE id = ?", (property_id,))
    property_name = cursor.fetchone()[0]
    return property_name


if __name__ == "__main__":
    app.run(debug=True)