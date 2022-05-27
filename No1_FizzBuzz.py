for num in range(1, 101):
    string = ''
    # ここから記述
    if num % 3 == 0:
        string += 'Fizz'
    if num % 5 == 0:
        string += 'Buzz'
    if string == '':
        string = str(num)
    # ここまで記述

    print(string)