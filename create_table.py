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

# Create a Faker instance
fake = Faker()

# Connect to SQLite database (create a new one if not exists)
connect = sqlite3.connect("prospect_tenants.db")
print("Connected to the database successfully")

# Create a cursor object to execute SQL commands
cursor = connect.cursor()

# Create table for agents
cursor.execute("""CREATE TABLE IF NOT EXISTS agents (
                   id INTEGER PRIMARY KEY,
                   name TEXT NOT NULL,
                   email TEXT NOT NULL UNIQUE,
                   password TEXT NOT NULL
               )""")
print("Created agents table successfully")

# Create table for Properties
cursor.execute("""CREATE TABLE IF NOT EXISTS properties (
                   id INTEGER PRIMARY KEY,
                   name TEXT NOT NULL,
                   address TEXT NOT NULL,
                   agent_id INTEGER NOT NULL,
                   FOREIGN KEY (agent_id) REFERENCES agents(id)
               )""")
print("Created properties table successfully")

# Create table for flats
cursor.execute("""CREATE TABLE IF NOT EXISTS flats (
                   id INTEGER PRIMARY KEY,
                   property_id INTEGER NOT NULL,
                   rent INTEGER,
                   area INTEGER,
                   FOREIGN KEY (property_id) REFERENCES properties(id)
               )""")
print("Created flats table successfully")

# Create table for tenants
cursor.execute("""CREATE TABLE IF NOT EXISTS tenants (
                   id INTEGER PRIMARY KEY,
                   flat_id INTEGER NOT NULL,
                   name TEXT NOT NULL,
                   email TEXT NOT NULL UNIQUE,
                   phone TEXT NOT NULL,
                   FOREIGN KEY (flat_id) REFERENCES flats(id)
               )""")
print("Created tenants table successfully")

# Commit the changes and close the connection
connect.commit()
connect.close()

# Populate the agents table with two agents
connect = sqlite3.connect("prospect_tenants.db")
cursor = connect.cursor()

agent1 = ('John ', 'john@example.com', 'password1')
agent2 = ('Jane Smith', 'jane@example.com', 'password2')

cursor.execute("INSERT INTO agents (name, email, password) VALUES (?, ?, ?)", agent1)
cursor.execute("INSERT INTO agents (name, email, password) VALUES (?, ?, ?)", agent2)

connect.commit()
connect.close()
print("Populated agents table with two agents")