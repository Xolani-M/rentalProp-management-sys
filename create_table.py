"""
This module sets up the database schema for the Bitprop property rental system.
The database schema consists of four tables:
1. agents: Stores information about agents, such as name, email, and password.
2. properties: Stores information about properties, such as name, address, and agent_id.
3. flats: Stores information about rental flats, including property_id, rent, and area.
4. tenants: Stores information about tenants who have registered their interest in flats.

The schema is designed to allow one agent to manage multiple properties, and each property can have multiple rental flats.
Tenants can register their interest in a specific flat, and the agent responsible for the corresponding property will be notified.
"""

import sqlite3
from faker import Faker
from werkzeug.security import generate_password_hash

# Initialize a Faker instance
fake = Faker()

# Connect to SQLite database (create a new one if not exists)
connect = sqlite3.connect("prospect_tenants.db")
print("Connected to the database successfully")

# Create a cursor object to execute SQL commands
cursor = connect.cursor()

# Create table for agents
cursor.execute("""CREATE TABLE IF NOT EXISTS agents (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL
                )""")
print("Created agents table successfully")
connect.commit()

# Create table for tenants
cursor.execute("""CREATE TABLE IF NOT EXISTS tenants (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    property_name TEXT,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    phone TEXT NOT NULL,
                    property_id INTEGER NOT NULL,
                    FOREIGN KEY(property_id) REFERENCES properties(id)
                )""")
print("Created tenants table successfully")
connect.commit()

# Create table for properties
cursor.execute("""CREATE TABLE IF NOT EXISTS properties (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    address TEXT NOT NULL,
                    rent INTEGER NOT NULL,
                    area INTEGER NOT NULL,
                    agent_id INTEGER NOT NULL,
                    agent_name TEXT NOT NULL,
                    FOREIGN KEY (agent_id) REFERENCES agents(id)
                )""")
print("Created properties table successfully")
connect.commit()

# Add dummy data for agents
cursor.execute("INSERT INTO agents (name, email, password) VALUES (?, ?, ?)",
               ("Phil Dunphy", "xomvana022@Student.wethinkcode.co.za", "password1"))
cursor.execute("INSERT INTO agents (name, email, password) VALUES (?, ?, ?)",
               ("Carolyn Burnham", "agent2@example.com", "password2"))
print("Added dummy data for agents successfully")
connect.commit()

# Add dummy data for properties
properties_data = [
    ("Sapphire Towers", fake.address(), fake.random_int(5000, 10000), fake.random_int(800, 1500), 1, "Phil Dunphy"),
    ("Golden Crest Apartments", fake.address(), fake.random_int(5000, 10000), fake.random_int(800, 1500), 1, "Phil Dunphy"),
    ("City View Suites", fake.address(), fake.random_int(5000, 10000), fake.random_int(800, 1500), 2, "Carolyn Burnham"),
    ("Oceanfront Oasis", fake.address(), fake.random_int(5000, 10000), fake.random_int(800, 1500), 2, "Carolyn Burnham"),
    ("Coastal View Residences", fake.address(), fake.random_int(5000, 10000), fake.random_int(800, 1500), 1, "Phil Dunphy"),
    ("Riverside Apartments", fake.address(), fake.random_int(5000, 10000), fake.random_int(800, 1500), 1, "Phil Dunphy"),
    ("Parkside Residences", fake.address(), fake.random_int(5000, 10000), fake.random_int(800, 1500), 2, "Carolyn Burnham"),
    ("Lakeview Apartments", fake.address(), fake.random_int(5000, 10000), fake.random_int(800, 1500), 2, "Carolyn Burnham")
]



# Insert dummy data into properties table
cursor.executemany(
    "INSERT INTO properties (name, address,rent, area, agent_id,agent_name) VALUES (?, ?, ?, ?, ?,?)", properties_data)
print("Added dummy data for properties successfully")

# Commit the changes for dummy data insertion and close the connection
connect.commit()


# Create the admins table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS admins (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
''')
print("Successfully created admins table")

# Insert dummy data into the admins table
cursor.execute("""
    INSERT INTO admins (name, email, password)
    VALUES (?, ?, ?)
""", ("nathaniel mvana", "nathanielmvana@gmail.com", "sageninja101"))

print("Successfully populated admins table")
# Commit the changes and close the connection
connect.commit()
connect.close()
