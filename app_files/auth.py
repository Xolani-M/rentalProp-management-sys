from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3

app = Flask(__name__)
app.secret_key = "Champ!101"

# Connect to the SQLite database
connect = sqlite3.connect("prospect_tenants.db", check_same_thread=False)
cursor = connect.cursor()

# Authentication routes
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        # Check for agents
        cursor.execute("SELECT * FROM agents WHERE email = ?", (email,))
        agent = cursor.fetchone()
        if agent and agent[3] == password:  
            session["agent_id"] = agent[0]
            session["agent_name"] = agent[1]
            session["role"] = "agent"
            return redirect(url_for("agent_dashboard"))

        # Check for admins
        cursor.execute("SELECT * FROM admins WHERE email = ?", (email,))
        admin = cursor.fetchone()
        if admin and admin[3] == password:  # Compare plaintext passwords
            session["admin_id"] = admin[0]
            session["admin_name"] = admin[1]
            session["role"] = "admin"
            return redirect(url_for("admin_dashboard"))

        flash("Invalid email or password", "error")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))


# Agent dashboard
@app.route("/agent")
def agent_dashboard():
    if "agent_id" in session and session["role"] == "agent":
        agent_id = session["agent_id"]
        cursor.execute("""
            SELECT t.id, t.name, t.email, t.phone, p.name AS property_name, agent_id
            FROM tenants t
            JOIN properties p ON t.property_name = p.id
            WHERE p.agent_id = ?  -- Filter tenants by agent_id,
        """,((agent_id,)))
        tenant_data = cursor.fetchall()
        return render_template("agent_dashboard.html", tenant_data=tenant_data)
    else:
        flash("Access denied", "error")
        return redirect(url_for("login"))
    
    
# Admin dashboard
@app.route("/admin")
def admin_dashboard():
    if "admin_id" in session and session["role"] == "admin":
        cursor.execute("""
            SELECT t.id, t.name, t.email, t.phone, p.name AS property_name
            FROM tenants t
            JOIN properties p ON t.property_name = p.name
        """)
        tenant_data = cursor.fetchall()
        return render_template("admin_dashboard.html", tenant_data=tenant_data)
    else:
        flash("Access denied", "error")
        return redirect(url_for("login"))