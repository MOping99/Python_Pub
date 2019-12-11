import sqlite3

def main():
    con = sqlite3.connect("test.db")
    cur = con.cursor()

    con.execute("""CREATE TABLE samples (id integer, value text)""")

main()
