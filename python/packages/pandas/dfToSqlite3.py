import pandas as pd
import sqlite3

pf = pd.DataFrame({ 'AAA' : [4,5,6,7],
                    'BBB' : [10,20,30,40],
                    'CCC' : [100,50,-30,-50]})

print (pf)
name1 = 'example.db'
name2 = "NewSqlTable"

conn = sqlite3.connect(name1)

sqlDB = pf.to_sql(  name=name2,
                    con=conn,
                    #flavor='sqlite',
                    schema=None,
                    index_label = "Triple Letters")

print(sqlDB)

conn.clse()
