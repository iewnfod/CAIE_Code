# 非官方函数及常量

<p align="center">
<a href="./README_cn.md">中文</a> | <a href="./README.md">English</a>
</p>

> 所有官方函数名均全部大写（UPPERCASE）
> 所有由此解释器提供的函数名为大驼峰（UpperCamelCase）

## [Math](./math.cpc)
* `QPow` 手动实现的幂运算
    ```
    QPow(x : REAL, n : INTEGER) RETURNS REAL
    ```
* `Min` 最小值
    ```
    Min(x : REAL, y : REAL) RETURNS REAL
    ```
* `Max` 最大值
    ```
    Max(x : REAL, y : REAL) RETURNS REAL
    ```
* `Abs` 绝对值
    ```
    Abs(x : REAL) RETURNS REAL
    ```
* `Sum` 为一个数组求和
    ```
    Sum(BYREF arr : ARRAY, BYVAL start : INTEGER, end : INTEGER) RETURNS REAL
    ```
* `PI` π

## [Sort](./sort.cpc)
* `Sort` 排序（希尔排序）
    ```
    Sort(BYREF arr : ARRAY, BYVAL left : INTEGER, right : INTEGER)
    ```
* `QuickSort` 快速排序
    ```
    QuickSort(BYREF a : ARRAY, BYVAL low : INTEGER, high : INTEGER)
    ```

## [String](./string.cpc)
* `Split` 分割
    ```
    Split(s : STRING, sep : STRING) RETURNS ARRAY
    ```
* `Lcase` 小写
    ```
    Lcase(s : STRING) RETURNS STRING
    ```
* `Ucase` 大写
    ```
    Ucase(s : STRING) RETURNS STRING
    ```
* `Trim` 修剪空格
    ```
    Trim(s : STRING) RETURNS STRING
    ```
* `TrimStart` 修剪字符串开头空格
    ```
    TrimStart(s : STRING) RETURNS STRING
    ```
* `TrimEnd` 修剪字符串结尾空格
    ```
    TrimEnd(s : STRING) RETURNS STRING
    ```
* `ArrayFromString` 字符串转数组
    ```
    ArrayFromString(s : STRING) RETURNS ARRAY
    ```
* `Contains` 是否包含了字符串
    ```
    Contains(s : STRING, target : STRING) RETURNS BOOLEAN
    ```
* `Join` 将数组拼接成字符串
    ```
    Join(sep : STRING, BYREF list : ARRAY, start : INTEGER, end : INTEGER) RETURNS STRING
    ```
* `Reverse` 反转字符串
    ```
    Reverse(s : STRING) RETURNS STRING
    ```
* `Replace` 替换字符串
    ```
    Replace(s : STRING, from : STRING, to : STRING) RETURNS STRING
    ```
* `EndsWith` 字符串末端是否为另外一个字符串
    ```
    EndsWith(base : STRING, suffix : STRING) RETURNS BOOLEAN
    ```
* `StartsWith` 字符串开头是否为另外一个字符串
    ```
    StartsWith(base : STRING, prefix : STRING) RETURNS BOOLEAN
    ```
* `STR_TO_NUM`: 把字符串转换为数字
    ```
    STR_TO_NUM(s : STRING) RETURNS REAL
    ```
* `CHR`: 获取一个整数对应的ASCII值
    ```
    CHR(n : INTEGER) RETURNS CHAR
    ```
* `ORD`: 获取一个字符的ASCII码
    ```
    ORD(s : CHAR) RETURNS INTEGER
    ```
* `ASCII`: 获取一个字符的ASCII码 (和 `ORD` 一样)
    ```
    ASCII(s : CHAR) RETURNS INTEGER
    ```

## [Time](./time.cpc)
* `Time` 获取当前时间戳
    ```
    Time() RETURNS REAL
    ```

## [Import](./import.cpc)
* `Import` 导入另一个文件
    ```
    Import(target : STRING) RETURNS ImportObj
    ```

## [Array](./array.cpc)
* `ArrayOne` 设置一个自定义长宽的数组内容为1
    ```
    ArrayOne(BYVAL row : INTEGER, col : INTEGER) RETURNS ARRAY
    ```
* `ArrayArrange` 在闭包范围内生成均匀的间隔为n的数字
    ```
    ArrayArrange(BYVAL low : INTEGER, high: INTEGER, div : REAL) RETURNS ARRAY
    ```
* `ArrayLinSpace` 在闭包范围内生成间隔均匀的n个数字
    ```
    ArrayLinSpace(BYVAL low : INTEGER, high: INTEGER, num : INTEGER) RETURNS ARRAY
    ```
