# 階乗を計算する関数
def fact(n):
    # 0なら1を返す
    if n == 0:
        return 1
    # 再帰的に呼び出す
    return n * fact(n - 1)


n = 10
print(fact(n))