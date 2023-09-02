import sqlite3
from dataclasses import dataclass

class Database:
    
    def __init__(self,conexao):
        self.name=conexao+'.db'
        self.conn=sqlite3.connect(conexao+'.db')
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS note ( id INTEGER PRIMARY KEY,title TEXT,content TEXT NOT NULL);")

    def add(self, note):
        insert_query = "INSERT INTO note (title, content) VALUES (?, ?)"
        values = (note.title, note.content)
        self.cur.execute(insert_query, values)
        self.conn.commit()

    def get_all(self):
        cursor = self.conn.execute("SELECT ID, TITLE, CONTENT FROM note")
        lista=[]

        for linha in cursor:
            id=linha[0]
            title = linha[1]
            content = linha[2]
            note=Note(id,title,content)
        
            lista.append(note)

        return lista
    
    def get(self,identa):
        cursor = self.conn.execute("SELECT ID, TITLE, CONTENT FROM note")

        for linha in cursor:
            id=linha[0]
            title = linha[1]
            content = linha[2]
            if id==identa:
                return Note(id=id,title=title,content=content)
        return None
        
            

    
    def update(self,entry):
            update_query = "UPDATE note SET title = ?, content = ? WHERE id = ?"
            values = (entry.title, entry.content, entry.id)
            self.conn.execute(update_query, values)
            self.conn.commit()
    def delete(self,note_id):
        delete_query="DELETE FROM note WHERE id=?"
        values=(note_id,)
        self.conn.execute(delete_query,values)
        self.conn.commit()

    

class Note:
    def __init__(self, id=None, title=None, content=''):
        self.id = id
        self.title = title
        self.content = content