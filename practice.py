#%%メゾット(何番目にあるか)
text = 'abcdefghijk'
text.index('g')

#%%datetimeモジュール
import datetime

today = datetime.date.today()
today.weekday()
birthday = datetime.date(1996,1,20)
bro_birth = datetime.date(1999,9,18)
birthday.weekday()
bro_birth.weekday()

life_day = today - birthday
life_day

#リスト操作

#%%要素削除の2つの仕方
list_1 = ['book','pen','computer','picture']
list_1.pop(2)
list_1
list_1.remove('pen')
list_1

#%%要素結合の2つの仕方
list_2 = [1,3,5,7]
list_3 = [2,4,6,8]

list_4 = list_2 + list_3
list_4
list_2.extend(list_3)
list_2

#%%リストの一部取り出し
list_5 = [1,2,3,4,5,6,7,8,9,10]
list_5[0:3]
list_5[3:7]
list_5[5:]
list_5[:4]

#%%リストのソート
list_6 = [3,2,7,6,45,1,9]
list_6.sort()
list_6
list_6.reverse()
list_6

list_7 = ['kitchen','book','japan','Mac','Windows']
list_7.sort()
list_7

#%%例外処理
try:
    a = 3
    b = 'z'
    print(a + b)
except:
    print('Error!')

#%%ファイルへの書き込み
text_file = open('/Users/rukaoide/Documents/Python/Python_Startbook/st.txt', 'w')
text_file.write('プログラムの勉強を継続中。')
text_file.close()

#%%ファイルの読み込み
text_file = open('/Users/rukaoide/Documents/Python/Python_Startbook/st.txt', 'r')
text = text_file.read()
text_file.close()
print(text)

#%%ファイルへの読み書きその２
with open('/Users/rukaoide/Documents/Python/Python_Startbook/st.txt','w') as f:
    f.write('プログラムの勉強を継続中。\n継続は力なり。これからも頑張ろう！')

with open('/Users/rukaoide/Documents/Python/Python_Startbook/st.txt','r') as f:
    print(f.read())

#%%その他ファイル処理
list_8 = ['1,2,3\n','4,5,6\n','7,8,9']
with open('/Users/rukaoide/Documents/Python/Python_Startbook/pra.txt','w') as f:
    f.writelines(list_8)

with open('/Users/rukaoide/Documents/Python/Python_Startbook/pra.txt','r') as f:
    print(f.read())

#%%ファイル操作とfor文
list_8 = ['1,2,3\n','4,5,6\n','7,8,9']
with open('/Users/rukaoide/Documents/Python/Python_Startbook/pra.txt','r') as f:
    for word in f:
        print(word.strip())

#%%区切り変換
list_8 = ['1,2,3\n','4,5,6\n','7,8,9']
with open('/Users/rukaoide/Documents/Python/Python_Startbook/pra.txt','r') as f:
    for word in f:
        a = word.strip().split(',')
        b = '\t'.join(a)
        print(b)

#%%空白削除
'  computer\n'.strip()

#%%モジュール読み込み
from random import*
randint(1,5)

import datetime as d
d.date.today()

#%%map関数
m = map(str,[1,2,3])
list(m)

#%%formatメゾッド
s = '{a} + {b} + {a}'
s.format(a = 1,b = 2)

data = {}
data['a'] = 1
data['b'] = 2
s.format(**data)

#%%itertoolsモジュール
import itertools
iter_cnt = itertools.count(1)
for i in range(10):
    print(next(iter_cnt))

#%%collectionsモジュール
import collections
counter = collections.Counter([1,1,2,2,2,2,3])
print(counter)
print(counter[2])
