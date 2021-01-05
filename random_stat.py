import random
import collections

num_data = []

#ある回数乱数を出力した時のデータ
def random_list(n):
    for i in range(n):
        ran_num = random.randint(1,10)
        num_data.append(ran_num)

def num_counter(k):
    counter = collections.Counter(num_data)
    print(counter)
    for i in range(k):
        print('{}：{}個'.format(i + 1,counter[i + 1]))



random_list(100)
num_counter(10)
