import sqlite3


class DataBase:
    def __init__(self):
        self.conn = sqlite3.connect('student.db')

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('create table IF NOT EXISTS user (id string(10) primary key, name varchar(20))')

        self.conn.commit()
        cursor.close()

    def select_stu(self, id):
        cursor = self.conn.cursor()
        sql = "select * from user where id=?"
        cursor.execute(sql, (id,))
        result1 = cursor.fetchone()
        self.conn.commit()
        cursor.close()
        return result1

    def add_stu(self, id, name):
        cursor = self.conn.cursor()
        data = (id, name)
        v = self.select_stu(id)
        if v:
            print(id + " already exists")
        else:
            sql = "INSERT INTO user(id, name) VALUES(?, ?)"
            cursor.execute(sql, data)
            self.conn.commit()
        cursor.close()

    def delete_stu(self, id):
        cursor = self.conn.cursor()
        v = self.select_stu(id)
        if v:
            sql = "DELETE FROM user WHERE id=?"
            cursor.execute(sql, (id,))
            self.conn.commit()
        else:
            print(id + " does not exists")
        cursor.close()


if __name__ == '__main__':
    db1 = DataBase()
    db1.create_table()
    # db1.add_stu("100", "aaa")
    # db1.delete_stu("107")
    # db1.add_stu("108", "bbb")
    value = db1.select_stu("108")
    if value:
        print(value[1])
