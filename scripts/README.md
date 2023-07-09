# 非官方函数

## Math
* MOD 取模
    ```
    MOD(n1 : INTEGER, n2 : INTEGER) RETURNS INTEGER
    ```
* POW 幂运算
    ```
    POW(x : REAL, n : INTEGER) RETURNS REAL
    ```
* Min 最小值
    ```
    Min(x : REAL, y : REAL) RETURNS REAL
    ```
* Max 最大值
    ```
    Max(x : REAL, y : REAL) RETURNS REAL
    ```
* Abs 绝对值
    ```
    Abs(x : REAL) RETURNS REAL
    ```
## Sort
* Sort 排序（希尔排序）
    ```
    Sort(BYREF arr : ARRAY, BYVAL left : INTEGER, right : INTEGER)
    ```

## String
* Split 分割
    ```
    Split(s : STRING, sep : STRING) RETURNS ARRAY
    ```
* Lcase 小写
    ```
    Lcase(s : STRING) RETURNS STRING
    ```
* Ucase 大写
    ```
    Ucase(s : STRING) RETURNS STRING
    ```
* Trim 修剪空格
    ```
    Trim(s : STRING) RETURNS STRING
    ```
* ArrayFromString 字符串转数组
    ```
    ArrayFromString(s : STRING) RETURNS ARRAY
    ```
