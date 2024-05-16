import sqlite3

# Connect to the SQLite database
connect = sqlite3.connect("prospect_tenants.db", check_same_thread=False)
cursor = connect.cursor()

def fetch_properties():
    cursor.execute("SELECT id, name, address, rent, area, agent_name FROM properties")
    return cursor.fetchall()

def get_property_name(property_id):
    cursor.execute("SELECT name FROM properties WHERE id = ?", (property_id,))
    property_name = cursor.fetchone()[0]
    return property_name

def insert_tenant(property_id, name, email, phone):
    cursor.execute("INSERT INTO tenants (property_id,property_name, name, email, phone) VALUES (?, ?, ?, ?,?)",
                   (property_id,get_property_name(property_id), name, email, phone))
    connect.commit()
