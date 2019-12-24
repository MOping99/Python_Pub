import sqlite3

def main():
    con = sqlite3.connect("test.db")
    cur = con.cursor()

    #con.execute("""CREATE TABLE samples (id integer, value text)""")
    con.execute("INSERT INTO samples VALUES (1, 'abc')")
    con.commit()

main()
