# LIST OF NON-OFFICIAL CONSTANTS AND FUNCTIONS

<p align="center">
<a href="./README_zh.md">中文</a> | <a href="./README.md">English</a>
</p>

> All CAIE standard functions are in UPPER CASE.
> All non-official functions are UpperCamelCase.

## [Math](./math.cpc)
* `QPow`: quick power
    ```
    QPow(x : REAL, n : INTEGER) RETURNS REAL
    ```
* `Min`: smaller value between two
    ```
    Min(x : REAL, y : REAL) RETURNS REAL
    ```
* `Max`: larger value between two
    ```
    Max(x : REAL, y : REAL) RETURNS REAL
    ```
* `Abs`: absolute value
    ```
    Abs(x : REAL) RETURNS REAL
    ```
* `Sum`: get the sum of an array
    ```
    Sum(BYREF arr : ARRAY, BYVAL start : INTEGER, end : INTEGER) RETURNS REAL
    ```
* `PI` π

## [Sort](./sort.cpc)
* `Sort`: shell sort
    ```
    Sort(BYREF arr : ARRAY, BYVAL left : INTEGER, right : INTEGER)
    ```
* `QuickSort` quick sort
    ```
    QuickSort(BYREF a : ARRAY, BYVAL low : INTEGER, high : INTEGER)
    ```

## [String](./string.cpc)
* `Split`: truncate a string
    ```
    Split(s : STRING, sep : STRING) RETURNS ARRAY
    ```
* `Lcase`: to lower case
    ```
    Lcase(s : STRING) RETURNS STRING
    ```
* `Ucase`: to upper case
    ```
    Ucase(s : STRING) RETURNS STRING
    ```
* `Trim`: remove blanks at the beginning and the end of a string
    ```
    Trim(s : STRING) RETURNS STRING
    ```
* `TrimStart`: remove blanks at the beginning of a string
    ```
    TrimStart(s : STRING) RETURNS STRING
    ```
* `TrimEnd`: remove blanks at the end of a string
    ```
    TrimEnd(s : STRING) RETURNS STRING
    ```
* `ArrayFromString`: returns an array of characters of a string
    ```
    ArrayFromString(s : STRING) RETURNS ARRAY
    ```
* `Contains`: if the `target` string is contained in a string `s`
    ```
    Contains(s : STRING, target : STRING) RETURNS BOOLEAN
    ```
* `Join`: join a array of string together with seperation
    ```
    Join(sep : STRING, BYREF list : ARRAY, start : INTEGER, end : INTEGER) RETURNS STRING
    ```
* `Reverse`: return a new string in reverse order
    ```
    Reverse(s : STRING) RETURNS STRING
    ```
* `Replace`: replace string `from` in string `s` to a string named `to`
    ```
    Replace(s : STRING, from : STRING, to : STRING) RETURNS STRING
    ```
* `EndsWith`: if a string `s` ends with a string `suffix`
    ```
    EndsWith(base : STRING, suffix : STRING) RETURNS BOOLEAN
    ```
* `StartsWith`: if a string `s` starts with a string `prefix`
    ```
    StartsWith(base : STRING, prefix : STRING) RETURNS BOOLEAN
    ```
* `STR_TO_NUM`: transform a string `s` to a number
    ```
    STR_TO_NUM(s : STRING) RETURNS REAL
    ```
* `NUM_TO_STR`: transform a number `s` to a string
    ```
    NUM_TO_STR(s : REAL) RETURNS STRING
    ```
* `CHR`: get the ASCII value of an integer `n`
    ```
    CHR(n : INTEGER) RETURNS CHAR
    ```
* `ORD`: get the ASCII index of a char
    ```
    ORD(s : CHAR) RETURNS INTEGER
    ```
* `ASCII`: get the ASCII index of a char (Same as `ORD`)
    ```
    ASCII(s : CHAR) RETURNS INTEGER
    ```

## [Time](./time.cpc)
* `Time`: get current timestamp
    ```
    Time() RETURNS REAL
    ```

## [Import](./import.cpc)
* `Import`: import another *cpc* file
    ```
    Import(target : STRING) RETURNS ImportObj
    ```
## [Array](./array.cpc)
* `ArrayOne` sets the contents of an array of custom length and width to 1
    ```
    ArrayOne(BYVAL row : INTEGER, col : INTEGER) RETURNS ARRAY
    ```
* `ArrayArrange` generates evenly spaced n numbers within the closure range
    ```
    ArrayArrange(BYVAL low : INTEGER, high: INTEGER, div : REAL) RETURNS ARRAY
    ```
* `ArrayLinSpace` generates n evenly spaced numbers in the closure range
    ```
    ArrayLinSpace(BYVAL low : INTEGER, high: INTEGER, num : INTEGER) RETURNS ARRAY
    ```
