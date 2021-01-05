import dice_game_f

num_list = [4,6,8,12,20]
n = int(input('サイコロを選んでください。\n(面の数：[4,6,8,12,20]):'))

#クラスは前にモジュール名を入れる。
#（from dice_game_f import Dice　でクラスをインポートした場合はクラスの前にモジュール名はいらない。）
#クラス内で定義した関数は前にモジュール名はいらない。
if n in num_list:
    dice = dice_game_f.Dice(n)
    player_dice = dice.shoot()
    computer_dice = dice.shoot()

    #関数は前にモジュール名を入れる。
    dice_game_f.judge(player_dice,computer_dice)

elif n not in num_list:
    print('5つの面の数の中から選んでください。')
