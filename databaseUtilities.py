import sqlite3

def create_connection(db_file: str) -> sqlite3.Connection:
    """
    Create a database connection to the SQLite database specified by db_file.

    Parameters:
    db_file (str): The path to the SQLite database file.

    Returns:
    sqlite3.Connection: Connection object to the SQLite database.
    """
    conn = sqlite3.connect(db_file)
    return conn

def create_table(conn: sqlite3.Connection, sql_command: str):
    """
    Create a table in the SQLite database.

    Parameters:
    conn (sqlite3.Connection): Connection object to the SQLite database.
    sql_command (str): Raw sql command to create the table
    """

    with conn:
        conn.execute(sql_command)

def generic_select_query(conn: sqlite3.Connection, query: str) -> list[tuple[any]]:
    """
    Execute a SELECT query on the SQLite database and return the results.

    Parameters:
    db_file (str): The path to the SQLite database file.
    query (str): The SQL SELECT query to execute.
    params (tuple): Parameters to be used in the SQL query (default is an empty tuple).

    Returns:
    List[Tuple[Any]]: Results of the query as a list of tuples.
    """
    results = []
    try:
        cursor = conn.cursor()

        cursor.execute(query)

        results = cursor.fetchall()

    
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    
    return results

def add_team(conn: sqlite3.Connection, team_name: str):
    """
    Add a new team to the team table in the SQLite database.

    Parameters:
    conn (sqlite3.Connection): Connection object to the SQLite database.
    team_name (str): The name of the team to be inserted.

    Raises:
    sqlite3.Error: If an SQLite error occurs during the operation.
    """
    try:
        cursor = conn.cursor()
        
        command = f'''
        INSERT INTO team (team_name)
        VALUES ('{team_name}');
        '''
        cursor.execute(command)

        conn.commit()
        
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")


team_table_string = '''
 CREATE TABLE IF NOT EXISTS team (
        team_id INTEGER PRIMARY KEY AUTOINCREMENT,
        team_name TEXT NOT NULL
    );
'''

# Foreign key dependency on team
player_table_string = '''
 CREATE TABLE IF NOT EXISTS player (
    player_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    number INTEGER,
    position TEXT,
    team_id INTEGER,
    FOREIGN KEY (team_id) REFERENCES team(team_id)
);
'''

# Line needs to be packed and unpacked
# Foreign key dependency on player
attack_table_string = '''
CREATE TABLE IF NOT EXISTS Attack (
    Attack_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Line TEXT NOT NULL,                     
    Type TEXT NOT NULL,                     
    Result TEXT NOT NULL,                  
    player_id TEXT NOT NULL,              
    FOREIGN KEY (player_id) REFERENCES player(player_id) 
);
'''

# Foreign key dependency on player
defense_table_string = '''
CREATE TABLE IF NOT EXISTS Defense (
    Defense_ID INTEGER PRIMARY KEY NOT NULL,
    Quality INTEGER NOT NULL,
    Type TEXT NOT NULL,
    Location TEXT NOT NULL,
    player_id TEXT NOT NULL,
    FOREIGN KEY (player_id) REFERENCES player(player_id)
);
'''

tables = [team_table_string,
          player_table_string,
          attack_table_string,
          defense_table_string]



#DEBUG
def main():
    database = "testDatabase.db"  # SQLite database file

    conn = create_connection(database)

    for table in tables:
        create_table(conn, table)

    add_team(conn, 'Test_Team')
    print(generic_select_query(conn, 'SELECT * FROM team;'))
    add_team(conn, 'Test_Team')
    print(generic_select_query(conn, 'SELECT * FROM team;'))


    conn.close()

if __name__ == "__main__":
    main()
