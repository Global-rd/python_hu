import sqlite3
import pandas as pd

class SqliteDB:

    def __init__(self, db_name):
        self.db_name = db_name

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        return self
       
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            print(exc_type)
            print(exc_value)
            print(traceback)
        self.conn.close()

    def write_single_record(self, table, record): # ('department', {'department_id': 7, 'department_name': 'test department'})
        #INSERT INTO department (department_id, department_name) VALUES (?, ?)
        columns = ", ".join(record.keys())
        placeholders = ", ".join(['?' for _ in record])
        query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})" 
        with self.conn:
            self.conn.execute(query, tuple(record.values()))
        
    def write_multiple_records(self, table, records):
        columns = ', '.join(records[0].keys())
        placeholders = ', '.join(['?' for _ in records[0]])
        query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
        with self.conn:
            self.conn.executemany(query, [tuple(r.values()) for r in records])

    def select_records(self, query):
        df = pd.read_sql_query(query, self.conn)
        return df
    
    def delete_records(self, table, where_clause):
        query = f"DELETE FROM {table} WHERE {where_clause}" #e.g.: DELETE FROM department WHERE department_id = 1
        with self.conn:
            self.conn.execute(query)

    def update_record(self, table, updates, identifier):
        update_clause = ', '.join([f"{k} = ?" for k in updates.keys()]) # e.g.: department_name = ? (amit updatelni akarunk)
        identifier_clause = ' AND '.join([f"{k} = ?" for k in identifier.keys()]) #e.g.: department_id = ? and xy = ? (feltétel az update-hez)
        query = f"UPDATE {table} SET {update_clause} WHERE {identifier_clause}" # UPDATE department SET department_name = ? WHERE department_id = ?
        with self.conn:
            self.conn.execute(query, tuple(updates.values()) + tuple(identifier.values()))

    def upsert_record(self, table, record, conflict_columns):
        
        """ formátum amit a query-hez összerakunk:
            INSERT INTO department (department_id, department_name) VALUES (?, ?)
            ON CONFLICT(department_id) DO UPDATE SET department_name = excluded.department_name
        """
        #abban az esetben hasznos, ha olyan adatokat töltünk be amiben lehet hogy szerepel olyan ami már jelen van a táblában.
        #ha nincs jelen a rekord -> insert, ha jelen van -> update
        columns = ', '.join(record.keys()) #(department_id, department_name)
        placeholders = ', '.join(['?' for _ in record]) #(?, ?)
        conflict_clause = ', '.join(conflict_columns) # (department_id) a CONFLICT után, ez lehet több oszlopnév is
        update_clause = ', '.join([f"{k} = excluded.{k}" for k in record.keys()]) #department_name = excluded.department_name
        query = f"""
            INSERT INTO {table} ({columns}) VALUES ({placeholders})
            ON CONFLICT({conflict_clause}) DO UPDATE SET {update_clause}
        """
        with self.conn:
            self.conn.execute(query, tuple(record.values()))


with SqliteDB("lessons/15/department-db") as db:
    #single record load:
    db.write_single_record('department', {'department_id': 7, 'department_name': 'SingleRecordDepartment'})

    #multiple record load:
    departments = [
        {'department_id': 8, 'department_name': 'ExecutueManyDepartment1'},
        {'department_id': 9, 'department_name': 'ExecuteManyDepartment2'}
    ]
    db.write_multiple_records('department', departments)
    
    #update records:
    db.update_record('department', {'department_name': 'UpdatedDepartmentName'}, {'department_id': 8})

    #upsert record
    db.upsert_record('department', {'department_id': 9, 'department_name': 'Updated9'}, ['department_id'])
    db.upsert_record('department', {'department_id': 10, 'department_name': 'Inserted10'}, ['department_id'])

    #select
    employee_df = db.select_records("SELECT * FROM department")
    print(employee_df)

    #delete to reset the data:
    db.delete_records('department', "department_id > 6")
    print("all queries finished successfully.")