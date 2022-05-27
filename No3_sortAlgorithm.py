from socket import AF_AAL5


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
    left = [] # 前半の配列
    right = [] # 後半の配列
    l_num = 0 # 探索位置（先頭から末端へ）
    r_num = len(array)-1 # 探索位置（末端から先頭へ）

    for i in range(len(array)):

        # 入れ替え操作不要な場合、探索位置を一つ中央側へ
        if pivot > array[l_num]:
            l_num += 1
        elif pivot < array[r_num]:
            r_num -= 1

        # 入れ替え操作　→ 　それぞれ探索位置を一つ中央側へ
        else:
            l = array[l_num]
            array[l_num] = array[r_num]
            array[r_num] = l
            l_num += 1
            r_num -= 1

        # 探索位置（先頭側と末端側）が入れ替わったら終了
        if r_num < l_num:
            break

    left = array[0:l_num]
    right = array[l_num:len(array)]

    # 配列が空でなければ、分かれたそれぞれでsort（空の場合はエラー）
    if left != []:
        left = sort(left)
    if right != []:
        right = sort(right)

    return left + right
    # ここまで記述

if __name__ == '__main__':
    main()