import random

# クイックソートを行う関数
def quick_sort(data, left, right):
    i = left
    j = right
    pivot = data[(left + right) // 2] # leftとrightの真ん中の値を軸の値とする

    # i <= jの逆のi > j（iとjが入れ替わる）になったらループが終わる
    while i <= j:
        # dataの左から順に、軸の値以上になる値まで進む
        while data[i] < pivot:
            i += 1
        # dataの右から順に、軸の値以下になる値まで進む
        while data[j] > pivot:
            j -= 1

        # 上のwhileでiとjが入れ替わったら処理しないようにしておく
        if i <= j:
            # data[i]の値とdata[j]の値を入れ替えて、iとjを次に進める
            data[i], data[j] = data[j], data[i]
            i += 1
            j -= 1

    # pivotより左側の範囲でquick_sort()を行う
    if left < j:
        quick_sort(data, left, j)
    # pivotより右側の範囲でquick_sort()を行う
    if right > i:
        quick_sort(data, i, right)


# 要素数n個でランダムな数字の配列
n = 15
data = [random.randint(1, 99) for _ in range(n)]
print(data, '元データ')

quick_sort(data, 0 , n - 1)
print(data, 'ソート後のデータ')