import random

# 要素数がn個のランダムな数字の配列を生成
def rand_array(n):
    return [random.randint(1,99) for _ in range(n)]


# # ----データのマージ----
# data_a = [1, 3, 4, 7, 8, 9]
# data_b = [0, 2, 5, 6]
# na = len(data_a)
# nb = len(data_b)
# data_c = [0] * (na + nb)

# # i,j,pはそれぞれ、data_a,b,cのインデックス番号（ポインタ）
# i, j, p = 0, 0, 0

# print(data_a, 'data_a')
# print(data_b, 'data_b')

# # iがdata_aの最後まで行くか、jがdata_bの最後まで行くまで行う
# # →iがdata_aの要素数内かつ、jがdata_bの要素数内にある限りループ
# while i < na and j < nb:
#     # data_a[i]とdata_b[j]を小さい方をdata_c[p]に入れて、入れたほうとdata_cのポインタを進める
#     if data_a[i] <= data_b[j]:
#         data_c[p] = data_a[i]
#         i += 1
#         p += 1
#     else:
#         data_c[p] = data_b[j]
#         j += 1
#         p += 1

# # 上の処理で残った方のデータの中身をdata_cに入れる
# # data_aの中身が残った場合の処理
# while i < na:
#     data_c[p] = data_a[i]
#     i += 1
#     p += 1
# # data_bの中身が残った場合の処理
# while j < nb:
#     data_c[p] = data_b[j]
#     j += 1
#     p += 1

# print(data_c, 'マージ後のデータ')


# # ----マージソート----

# # マージを行う関数
# # left～mid-1間と、mid～right-1間でマージ
# def merge(left, mid, right):
#     # left→right間の値が入るサイズの配列
#     buff = [0] * (right - left)
#     i = left
#     j = mid
#     p = 0

#     while i < mid and j < right:
#         if data[i] <= data[j]:
#             buff[p] = data[i]
#             i += 1
#             p += 1
#         else:
#             buff[p] = data[j]
#             j += 1
#             p += 1

#     while i < mid:
#         buff[p] = data[i]
#         i += 1
#         p += 1

#     while j < right:
#         buff[p] = data[j]
#         j += 1
#         p += 1

#     # バッファの中身（並べ替えた値）をdataに戻す
#     data[left:right] = buff


# 要素数15個でランダムな数字の配列
# data = rand_array(15)
# print(data, '元データ')

# # マージを行うペアのサイズ（最初は1個と1個でマージするので2）
# s = 2

# # sがdataの範囲内でループ
# while s <= n:
#     # 配列全体をs個ずつのブロックに分割したときのブロック数（=マージの回数）
#     loop = n // s
#     # 配列の最後に余ってしまった部分（sで割り切れなかった部分の要素数）
#     fragment = n % s

#     # 各ブロックごとにマージ
#     for i in range(loop):
#         merge(
#             i * s, # 左側の開始インデックス
#             i * s + (s // 2), # 右側の開始インデックス（=中央）
#             i * s + s # マージ範囲の右端
#             )
#     # 端数がある場合（loopが1以下の場合、fragmentは前回のループ時の処理でソート済みなのでスキップする）
#     if fragment > 0 and loop > 1:
#         # 最後の1つ前のブロックと端数を一緒にマージ
#         merge(
#             (loop - 1) * s, # 最後のひとつ前のブロックの開始インデックス
#             loop * s, # 端数の開始インデックス
#             n # dataの最後
#         )
#     # sの範囲を2倍にする（2→4→8倍...となり、dataを2分するまで増える）
#     s *= 2

# print(data, 'ソート後のデータ')


# ----再帰関数版マージソート----

def merge_sort(data, left, right):
    # 範囲の要素の数が1以下ならこれ以上分割しない（再帰終了）
    if right - left <= 1:
        return
    
    mid = (left + right) // 2        
    merge_sort(data, left, mid)
    merge_sort(data, mid, right)

    # left→right間の値が入るサイズの配列
    buff = []

    i, j = left, mid
    
    while i < mid and j < right:
        if data[i] <= data[j]:
            buff.append(data[i])
            i += 1
        else:
            buff.append(data[j])
            j += 1

    while i < mid:
        buff.append(data[i])
        i += 1

    while j < right:
        buff.append(data[j])
        j += 1

    # バッファの中身（並べ替えた値）をdataに戻す
    data[left:right] = buff


# 要素数15個でランダムな数字の配列
data = rand_array(15)
print(data, '元データ')

merge_sort(data, 0, len(data))
print(data, 'ソート後のデータ')