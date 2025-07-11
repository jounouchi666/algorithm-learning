data = [9, 4, 7, 2, 3, 8, 6, 1, 5, 0]
n = len(data)

# # 先頭からの確定数を「i」とする
# for i in range(0, n - 1):
#     # 「j」は配列dataの末尾からi+1番目まで逆順に進む
#     for j in range(n - 1 , i, -1):
#         # 「j」と「j-1」を比較し、「j-1」のほうが大きければ値を入れ替える
#         if data[j - 1] > data[j]:
#             data[j], data[j - 1] = data[j - 1], data[j]

# print(data)


# # -----左から比較していくパターン-----

# for i in range(0, n - 1):
#     # 「j」は配列dataの1先頭からn-1-i-1番目まで進む
#     for j in range(0, n - 1 - i):
#         # 「j」と「j-1」を比較し、「j-1」のほうが大きければ値を入れ替える（ここの処理は同じ）
#         if data[j] > data[j + 1]:
#             data[j], data[j + 1] = data[j + 1], data[j]

# print(data)


# -----降順にソートする-----

for i in range(0, n - 1):
    for j in range(n - 1 , i, -1):
        # 「j」と「j-1」を比較し、「j-1」のほうが小さければ値を入れ替える
        if data[j - 1] < data[j]:
            data[j], data[j - 1] = data[j - 1], data[j]

print(data)