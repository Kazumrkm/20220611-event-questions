def main():
    # 昇順にソートされた配列
    sorted_array = [1, 2, 3, 5, 12, 7890, 12345]
    # 探索対象の番号
    target_number = 7890

    # 探索実行
    target_index = serch_index(sorted_array, target_number)
    # 結果出力
    print(target_index)

def serch_index(sorted_array, target_number):

    # ここから記述
    n = len(sorted_array)
    res = 0

    for i in range(n):
        if len(sorted_array) == 0:
            break

        mid = int(len(sorted_array)/2)
        if sorted_array[mid] == target_number:
            res += mid
            return res

        elif sorted_array[mid] < target_number:
            del sorted_array[0:mid+1]
            res += mid+1

        else:
            del sorted_array[mid:len(sorted_array)]
    # ここまで記述

    # 探索対象が存在しない場合、-1を返却
    return -1

if __name__ == '__main__':
    main()
