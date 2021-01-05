#体型判定プログラム

def bmi(height,weight):

    bmi_num = weight / height ** 2

    if bmi_num < 18.5:
        print('身長：' + str(height * 100) + 'cm' + \
        '　体重：' + str(weight) + 'kg' + \
        '\nBMI：{:.1f}\n痩せ型です。'.format(bmi_num))
    elif 18.5 <= bmi_num < 25.0:
        print('身長：' + str(height * 100) + 'cm' + \
        '　体重：' + str(weight) + 'kg' + \
        '\nBMI：{:.1f}\n標準です。'.format(bmi_num))
    elif 25.0 <= bmi_num < 30.0:
        print('身長：' + str(height * 100) + 'cm' + \
        '　体重：' + str(weight) + 'kg' + \
        '\nBMI：{:.1f}\n肥満です。'.format(bmi_num))
    elif 30.0 <= bmi_num:
        print('身長：' + str(height * 100) + 'cm' + \
        '　体重：' + str(weight) + 'kg' + \
        '\nBMI：{:.1f}\n高度な肥満です。'.format(bmi_num))

#実行プログラム
con = input('体型判定を行いますか？\n行うなら「c」を、止めるなら「q」を入力してください。:')

while con == 'c':
    height = float(input('身長を入力してください。(単位：cm):')) / 100
    weight = float(input('体重を入力してください。(単位：kg):'))

    bmi(height,weight)
    con = input('もう一度行いますか？\n行うなら「c」を、止めるなら「q」を入力してください。:')
