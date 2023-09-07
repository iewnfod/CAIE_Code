# 非官方函数及常量

## [Math](./math.cpc)
* QPow 手动实现的幂运算
    ```
    QPow(x : REAL, n : INTEGER) RETURNS REAL
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
* PI π

## [Sort](./sort.cpc)
* Sort 排序（希尔排序）
    ```
    Sort(BYREF arr : ARRAY, BYVAL left : INTEGER, right : INTEGER)
    ```

## [String](./string.cpc)
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
* Contains 是否包含了字符串
    ```
    Contains(s : STRING, target : STRING) RETURNS BOOLEAN
    ```
* Join 将数组拼接成字符串
    ```
    Join(sep : STRING, BYREF list : ARRAY, start : INTEGER, end : INTEGER) RETURNS STRING
    ```
