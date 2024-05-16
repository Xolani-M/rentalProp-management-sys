from flask import Flask, render_template, request
from app_files.database import fetch_properties, insert_tenant
from app_files.auth import login, logout, agent_dashboard, admin_dashboard
from app_files.email_utils import send_notification_email
import sqlite3


app = Flask(__name__)
app.secret_key = "Champ!101"

@app.route("/", methods=["GET", "POST"])
def index():
    properties = fetch_properties()
    return render_template("/index.html", properties=properties)

@app.route('/register_interest', methods=["POST"])
def register_interest():
    properties = fetch_properties()
    name = request.form["name"]
    email = request.form["email"]
    phone = request.form["phone"]
    property_id = request.form["property_id"]

    insert_tenant(property_id, name, email, phone)
    
    print(property_id,name, email,phone)
    
    # Connect to the SQLite database
    connect = sqlite3.connect("prospect_tenants.db", check_same_thread=False)
    cursor = connect.cursor()
        
    # Retrieve agent email based on property_id
    cursor.execute("""
        SELECT a.email
        FROM properties p
        JOIN agents a ON p.agent_name = a.name
        WHERE p.id = ?
    """, (property_id,))
    agent_email = cursor.fetchone()[0]
    
    # Send notification email to agent
    send_notification_email(agent_email, name, property_id)
    
    
    return render_template("index.html", properties=properties, success_modal=True)

# Authentication routes
app.add_url_rule("/login", view_func=login, methods=["GET", "POST"])
app.add_url_rule("/logout", view_func=logout)
app.add_url_rule("/agent", view_func=agent_dashboard)
app.add_url_rule("/admin", view_func=admin_dashboard)


if __name__ == "__main__":
    app.run(debug=True)
