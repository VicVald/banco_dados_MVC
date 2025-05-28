import sqlite3

def clear_database():
    conexao = sqlite3.connect("Trello.db")
    cursor = conexao.cursor()
    
    # Get list of all tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    
    # Disable foreign keys temporarily
    cursor.execute("PRAGMA foreign_keys = OFF;")
    
    # Drop each table
    for table in tables:
        table_name = table[0]
        if table_name != 'sqlite_sequence':  # Skip sqlite_sequence table
            print(f"Dropping table: {table_name}")
            cursor.execute(f"DROP TABLE IF EXISTS {table_name};")
    
    # Re-enable foreign keys
    cursor.execute("PRAGMA foreign_keys = ON;")
    
    # Reset autoincrement counters
    cursor.execute("DELETE FROM sqlite_sequence;")
    
    conexao.commit()
    conexao.close()
    print("\nDatabase cleared successfully!")

if __name__ == "__main__":
    confirm = input("This will delete ALL data in the database. Are you sure? (y/N): ")
    if confirm.lower() == 'y':
        clear_database()
    else:
        print("Operation cancelled.") 