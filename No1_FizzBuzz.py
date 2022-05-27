from socket import AF_AAL5


for num in range(1, 101):
    string = ''

    # ここから記述
    if num % 3 == 0:
        string += 'Fizz'
    if num % 5 == 0:
        string += 'Buzz'
        
    if string == '': # 3, 5の倍数でない
        string = str(num)
    # ここまで記述
