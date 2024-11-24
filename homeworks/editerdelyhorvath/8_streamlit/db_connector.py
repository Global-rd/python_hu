'''
adatbázis kapcsolódás és adatbázis műveletek gyüjteménye
'''

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

    def write_single_record(self, table, record):
        """
        Insert a single record into a table.
        :param table: str, name of the table
        :param record: dict, column-value pairs
        """
        columns = ", ".join(record.keys())
        placeholders = ", ".join(['?' for _ in record])
        query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})" 
        with self.conn:
            self.conn.execute(query, tuple(record.values()))
        
    def write_multiple_records(self, table, records):
        """
        Insert multiple records into a table.
        :param table: str, name of the table
        :param records: list of dicts, each dict is a column-value pair
        """
        columns = ', '.join(records[0].keys())
        placeholders = ', '.join(['?' for _ in records[0]])
        query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
        with self.conn:
            self.conn.executemany(query, [tuple(r.values()) for r in records])
    
    def select_records(self, query):
        """
        Execute a SELECT query and return the results as a DataFrame.
        :param query: str, SQL SELECT query
        :return: pandas.DataFrame
        """
        df = pd.read_sql_query(query, self.conn)
        return df
    
    def delete_records(self, table, where_clause):
        """
        Delete records from a table based on a WHERE clause.
        :param table: str, name of the table
        :param where_clause: str, conditions for deletion
        """
        query = f"DELETE FROM {table} WHERE {where_clause}" 
        with self.conn:
            self.conn.execute(query)
    
    def update_record(self, table, updates, identifier):
        """
        Update records in a table based on an identifier.
        :param table: str, name of the table
        :param updates: dict, columns to update with their new values
        :param identifier: dict, columns to identify which records to update
        """
        update_clause = ', '.join([f"{k} = ?" for k in updates.keys()])
        identifier_clause = ' AND '.join([f"{k} = ?" for k in identifier.keys()])
        query = f"UPDATE {table} SET {update_clause} WHERE {identifier_clause}"
        with self.conn:
            self.conn.execute(query, tuple(updates.values()) + tuple(identifier.values()))
    
    def upsert_records(self, table, records, conflict_columns):
        """
        Insert records or update them if they already exist based on conflict columns.
        :param table: str, name of the table
        :param records: list of dicts, records to upsert
        :param conflict_columns: list of str, columns to check for conflicts
        """
        columns = ', '.join(records[0].keys())
        placeholders = ', '.join(['?' for _ in records[0]])
        conflict_clause = ', '.join(conflict_columns)
        update_clause = ', '.join([f"{k} = excluded.{k}" for k in records[0].keys()])
        query = f"""
            INSERT INTO {table} ({columns}) VALUES ({placeholders})
            ON CONFLICT({conflict_clause}) DO UPDATE SET {update_clause}
        """
        with self.conn:
            self.conn.executemany(query, [tuple(record.values()) for record in records])
