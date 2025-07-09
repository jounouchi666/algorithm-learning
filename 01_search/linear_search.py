data = [57, 48, 46, 52, 45, 59, 61, 60, 49, 71]

n = len(data)
key = 60
flg = False

# 配列'data'の中身を順番にループし、keyの値が見つかったらflgをTrueにする
for i in range(n):
    if data[i] == key:
        flg = True
        print(f'data[{i}]が{str(key)}です')
        break

if flg == False:
    print(f'{str(key)}は存在しません')