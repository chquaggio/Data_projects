import json
import psycopg2

# Connect to the football database
conn = psycopg2.connect(database="football", user="cquaggio", password="ch.r1st1an!", host="localhost", port="5432")

# Open the JSON file and load the data
with open("teams_league135_season2021.json", "r") as file:
    data = json.load(file)

# Create a cursor object to execute SQL queries
cur = conn.cursor()

# Check if the teams table already exists
cur.execute("SELECT EXISTS(SELECT * FROM information_schema.tables WHERE table_name='teams')")
table_exists = cur.fetchone()[0]

if not table_exists:
    # Create the table
    cur.execute('''
        CREATE TABLE teams (
            id INTEGER PRIMARY KEY,
            name VARCHAR(255),
            code VARCHAR(255),
            founded INTEGER,
            venue VARCHAR(255)
        )
    ''')

    # Loop over the response data and insert each team into the teams table
    for team_data in data["response"]:
        print("Processing team:", team_data["team"]["name"])

        # Extract the team and venue data
        team = team_data["team"]
        venue = team_data["venue"]

        # Insert the data into the teams table
        cur.execute("INSERT INTO teams (id, name, code, founded, venue) VALUES (%s, %s, %s, %s, %s)", (team["id"], team["name"], team["code"], team["founded"], venue["name"]))
        conn.commit()

# Close the database connection
conn.close()

