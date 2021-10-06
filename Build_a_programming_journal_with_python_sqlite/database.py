import sqlite3



connection = sqlite3.connect("data.db")

def create_table(): 
    with connection:
        connection.execute(
            "CREATE TABLE IF NOT EXISTS entries (content TEXT, date Text);"
            )
    

def add_entry(entry_content, entry_date): 
    """Add the data"""
    with connection:
        connection.execute(
            "INSERT INTO entries VALUES (?,?);", (entry_content, entry_date)
            )
    
def get_entries():
    """Getting the data"""
    cursor = connection.execute("SELECT * FROM entries;")
    return cursor
    
