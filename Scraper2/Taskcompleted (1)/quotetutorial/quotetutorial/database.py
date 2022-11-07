import sqlite3
conn = sqlite3.connect('myquotes.db')
cur = conn.cursor()
cur.execute("""
        create table quote_tb(
            title text,
            author text,
            tag  text
        )
        """) 
cur.execute("""
        insert into quote_tb values(
            'python is aweswom','gido van','Django'
        )
        """) 
conn.commit()
conn.close()