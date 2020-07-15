import sqlite3


class TeleDB:
    def __init__(self, dbname="todo.sqlite"):
        self.dbname = dbname
        self.conn = sqlite3.connect(dbname, check_same_thread=False)

    def setup(self):
        tblstmt = "CREATE TABLE IF NOT EXISTS details(Chat_id integer PRIMARY KEY, Name text, College text, Source text, Experience_level text, Linux text, Programming_language text, Programming_experience text, Framework text, Storage text, Interest text, Leadership text, Github text, Points text)"
        self.conn.execute(tblstmt)
        self.conn.commit()

    def add_item(self, Chat_id, Name, College, Source, Experience_level, Linux, Programming_language, Programming_experience, Framework, Storage, Interest, Leadership, Github, Points):

        stmt = "INSERT INTO details(Chat_id) SELECT (?) WHERE NOT EXISTS(SELECT 1 FROM details WHERE Chat_id = (?))"
        args = (Chat_id, Chat_id)
        self.conn.execute(stmt, args)

        stmt = f"UPDATE details SET (Name, College, Source, Experience_level, Linux, Programming_language, Programming_experience, Framework, Storage, Interest, Leadership, Github, Points) = (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) WHERE Chat_id = (?)"
        args = (Name, College, Source, Experience_level, Linux, Programming_language, Programming_experience, Framework, Storage, Interest, Leadership, Github, Points, Chat_id)
        self.conn.execute(stmt, args)
        self.conn.commit()




    # def get_items(self, owner):
    #     try:
    #         stmt = "SELECT * FROM details WHERE Chat_id = (?)"
    #         args = (owner,)
    #         return [x[1:] for x in self.conn.execute(stmt, args)][0]
    #     except:
    #         return 'error'

