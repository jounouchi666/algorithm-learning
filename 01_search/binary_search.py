data = [1, 2, 9, 12, 20, 25, 32, 48, 50, 57, 72, 78, 80, 93, 100]
key = 72
left = 0 # 左端の値
right = len(data) - 1 # 右端の値
# flg = False

# # leftとrightが一致または逆転するまで繰り返す
# while left <= right:
#     mid = (left + right) // 2 # leftとrightの中央の値
#     # midがkeyと一致すれば終了
#     if data[mid] == key:
#         print(f'data[{mid}]が{key}です')
#         flg = True
#         break

#     # midがkeyより小さければ、leftをmidのひとつ右の値とする
#     if data[mid] < key:
#         left = mid + 1
#     # midがkeyより大きければ、rightをmidのひとつ左の値とする
#     else:
#         right = mid - 1

# if flg == False:
#     print(f'{key}は存在しません')


# -----再帰バージョン-----
def binary_search(data, key, left, right):
    # leftとrightが逆転してしまったら終了
    if left > right:
        return -1
    
    mid = (left + right) // 2 # leftとrightの中央の値
    # midがkeyと一致すれば終了
    if data[mid] == key:
        return mid
    # midがkeyより小さければ、leftをmidのひとつ右の値として自身を呼び出す
    elif data[mid] < key:
        return binary_search(data, key, mid + 1, right)
    # midがkeyより大きければ、rightをmidのひとつ左の値として自身を呼び出す
    else:
        return binary_search(data, key, left, mid - 1)

index = binary_search(data, key, left, right)
if index != -1:
    print(f'data[{index}]が{key}です')
else:
    print(f'{key}は存在しません')