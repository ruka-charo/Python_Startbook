import random

class Dice:
    def __init__(self,num):
        self.num = num

    def shoot(self):
        return random.randint(1, self.num)


def judge(player,computer):
    print('Player：' + str(player) + '\nComputer：' + str(computer))

    if player > computer:
        print('プレイヤーの勝ちです。')

    elif player == computer:
        print('同点です。')

    else:
        print('Computerの勝ちです。')
