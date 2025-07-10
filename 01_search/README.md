# 探索アルゴリズム
複数のデータの中から目的のデータを探し出すアルゴリズム
- [線形探索](#線形探索linear_searchpy)
- [二分探索](#二分探索binary_searchpy)

***
## 線形探索（linear_search.py）

### 概要
データ群の端から１つずつ目的のデータであるかチェックしていく探索方法

### 時間計算量
データ量`n`個に対して`n`回ループが回る
> ${O(n)}$

### 実装
配列`data`の中身を順番にループし、`key`の値が見つかったら`flg`を`True`にする

```python
data = [57, 48, 46, 52, 45, 59, 61, 60, 49, 71]

n = len(data)
key = 60
flg = False

for i in range(n):
    if data[i] == key:
        flg = True
        print(f'data[{i}]が{str(key)}です')
        break

if flg == False:
    print(f'{str(key)}は存在しません')
    
# data[7]が60です
```

### メリット
データが整理されていなくても利用できる

### デメリット
データ量が多くなると処理時間も長くなる

***
## 二分探索（binary_search.py）

### 概要
ソートされたデータ群を半分に分けて、そのどちらに目的のデータがあるかを判断し、探索範囲を絞りながらデータを探す方法

### 時間計算量
配列のサイズを’n’としたとき、下記の表のように範囲が絞られていく
| ステップ | 範囲サイズ |
| --- | --- |
| 1回目 | ${n}$ |
| 2回目 | ${n/2}$ |
| 3回目 | ${n/4}$ |
| 4回目 | ${n/8}$ |
| ... | ... |
| k回目 | ${n / 2^{k-1}}$ |

${n / 2^k}$が1以下になるまで繰り返すため
> ${n / 2^k = 1}$
${2^k = n}$
${k = log₂(n)}$


ビッグオー記法では底（基数）が省略されるため
> ${O(log n)}$

### 実装

#### ループ処理バージョン
1. 配列`data`の端の値をそれぞれ`left`、`right`とし、その間の範囲が検索範囲とする。
2. 検索範囲の真ん中の値`mid`が`key`と一致するか調べる。
3. 一致しなかった場合、
・`key`が`mid`の右側の範囲に存在するなら、`left`に`mid`の右隣の値を入れる。
・`key`が`mid`の左側の範囲に存在するなら、`right`に`mid`の左側の値を入れる。
4. 3で検索範囲が変わったので、2,3を繰り替す

```python
data = [1, 2, 9, 12, 20, 25, 32, 48, 50, 57, 72, 78, 80, 93, 100]
key = 72
left = 0 # 左端の値
right = len(data) - 1 # 右端の値
flg = False

# leftとrightが一致または逆転するまで繰り返す
while left <= right:
    mid = (left + right) // 2 # leftとrightの中央の値
    # midがkeyと一致すれば終了
    if data[mid] == key:
        print(f'data[{mid}]が{key}です')
        flg = True
        break

    # midがkeyより小さければ、leftをmidのひとつ右の値とする
    if data[mid] < key:
        left = mid + 1
    # midがkeyより大きければ、rightをmidのひとつ左の値とする
    else:
        right = mid - 1

if flg == False:
    print(f'{key}は存在しません')
```

#### 再帰バージョン
※ Pythonの再帰はデフォルトで1000回程度まで（`RecursionError`）。深い探索にはループ版が安定。
```python
data = [1, 2, 9, 12, 20, 25, 32, 48, 50, 57, 72, 78, 80, 93, 100]
key = 72
left = 0 # 左端の値
right = len(data) - 1 # 右端の値

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
```

> **中間値`mid`の取り方**
非常に大きな`left`と`right`の場合に整数オーバーフローのリスクがあるらしい（C++やJavaなどで注意）
その場合の対処：
> 
> 
> ```python
> mid = left + (right - left) // 2
> ```

### データの重複
データに重複する値がある場合、見つかった要素のインデックスが最初のものかどうかは保証されない
→最小または最大のインデックスを保証するには追加処理が必要

> **最小インデックスを探す**
重複する値の中で最初に現れる位置を返す
> 
> 
> ```python
> def lower_bound(data, key):
>     left, right = 0, len(data) - 1
>     result = -1
>     while left <= right:
>         mid = (left + right) // 2
>         if data[mid] == key:
>             result = mid
>             right = mid - 1  # 左側をさらに探す
>         elif data[mid] < key:
>             left = mid + 1
>         else:
>             right = mid - 1
>     return result
> ``` 

> **最後のインデックスを探す**
最大インデックスを探す場合は、候補を保存しながら探索範囲を右側に広げる
> 
> 
> `lower_bound`の`right = mid - 1` を`left = mid + 1` に変えて実装する
> 
> ```python
> if data[mid] == key:
>     result = mid
>     left = mid + 1 # 'right = mid - 1'から変更
> ```

### メリット
線形探索に比べて探索速度が速い
特にデータ量が多いときに威力を発揮する

### デメリット
探索を行うデータがソートされていないと使えない（事前にソートが必要）
