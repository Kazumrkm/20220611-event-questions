def main():
    #ランダムに並べられた重複のない整数の配列
    array = [5, 4, 6, 2, 1, 9, 8, 3, 7, 10]
    # ソート実行
    sortedArray = sort(array)
    # 結果出力
    [print(i) for i in sortedArray]

def sort(array):
    # 要素が一つの場合はソートの必要がないので、そのまま返却
    if len(array) == 1:
        return array

    # 配列の先頭を基準値とする
    pivot = array[0]

    # ここから記述
    left = []
    right = []
    l_num = 0 # 先頭
    r_num = len(array)-1 # 末端

    for i in range(len(array)):
        if pivot > array[l_num]:
            l_num += 1
        elif pivot < array[r_num]:
            r_num -= 1
        else:
            p = array[l_num]
            array[l_num] = array[r_num]
            array[r_num] = p
            l_num += 1
            r_num -= 1

        if r_num < l_num:
            break
    left = array[0:l_num]
    right = array[l_num:len(array)]

    if left != []:
        left = sort(left)
    if right != []:
        right = sort(right)

    return left + right
    # ここまで記述

if __name__ == '__main__':
    main()