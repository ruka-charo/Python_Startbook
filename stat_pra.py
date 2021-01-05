import sqlite3
import itertools
import random
import collections

conn = sqlite3.connect('my_database.db')
conn.execute('create table data_table(id integer,random_val real)')

iter_cnt = itertools.count(1)
num = random.random()
conn.execute('insert into data_table values({},{})'.format(next(iter_cnt),num))

cur = conn.execute('select * from data_table')
for row in cur:
    print(row)

for i in range(500):
    num = random.random()
    conn.execute('insert into data_table values({},{})'.format(next(iter_cnt),num))

cur = conn.execute('select count(*) from data_table')
for row in cur:
    print(row)

cur = conn.execute('select * from data_table where id=501')
for row in cur:
    print(row)

cur = conn.execute('update data_table set id=-99 where id=501')
cur = conn.execute('select * from data_table where id=-99')
for row in cur:
    print(row)
cur = conn.execute('delete from data_table where id=-99')


data = []
cur = conn.execute('select random_val from data_table')
for row in cur:
    data.append((int(row[0] * 10)))

hist_data = collections.Counter(data)
for i in range(10):
    print('{:0.1f}〜{:0.1f}: {}個'.format(0.1 * i,0.1 * (i + 1),hist_data[i]))

conn.commit()
conn.close()
