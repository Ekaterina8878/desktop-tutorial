import random
def get_code():
    num = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    numbers = list(range(3, 21))
    code = random.choice(numbers)
    return code
def get_passcode(n):
    entrance = {}
    entrance.update({3: 12, 4: 13, 5: 1423, 6: 121524, 7: 162534, 8: 13172635, 9: 1218273645, 10: 141923283746})
    entrance.update({11: 11029384756, 12: 12131511124210394857, 13: 112211310495867, 14: 1611325212343114105968})
    entrance.update({15: 1214114232133124115106978, 16: 1317115262143531341251161079, 17: 11621531441351261171089})
    entrance.update({18: 12151811724272163631545414513612711810, 19: 118217316415514613712811910})
    entrance.update({20: 13141911923282183731746416515614713812911})
    passcode = entrance.get(n)
    return passcode
n = get_code()
print('Шифр   :', n)
pairnum1 = list(range(1, n))
pairnum2 = list(range(1, n))
pairs = []
result = ''
for i in pairnum1:
    for j in pairnum2:
        pn1 = i
        pn2 = j
        if pn1 >= pn2:
            continue
        else:
            kratno = n % (pn1 + pn2)
            if kratno == 0:
                pairs.append([pn1, pn2])
                result = result + str(pn1) + str(pn2)
print('Пары чисел', *pairs)
print('Введите пароль', result, 'во вторую вставку')
if int(result) == get_passcode(n):
    print('Вы свободны!')

