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


num_list = [4,6,8,12,20]
n = int(input('サイコロを選んでください。\n(面の数：[4,6,8,12,20]):'))

if n in num_list:
    dice = Dice(n)
    player_dice = dice.shoot()
    computer_dice = dice.shoot()

    judge(player_dice,computer_dice)

elif n not in num_list:
    print('5つの面の数の中から選んでください。')
