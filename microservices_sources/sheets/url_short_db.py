import sqlite3


class Database:
    def __init__(self,database_file):
        self.connection = database_file
        self.cursor = database_file.cursor()

    def add_link(self, link, redirect_link):
        self.cursor.execute("INSERT INTO `links` (`true_url`, `redirect_url`) VALUES(?,?)",(link, redirect_link))
        self.connection.commit()

    def get_link(self, redirect_link):
        return self.cursor.execute('SELECT `true_url` FROM `links` WHERE `redirect_url` = ?',(redirect_link,)).fetchone()



