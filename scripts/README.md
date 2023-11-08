# LIST OF NON-OFFICIAL CONSTANTS AND FUNCTIONS

<p align="center">
<a href="./README_zh.md">中文</a> | <a href="./README.md">English</a>
</p>

> All CAIE standard functions are in UPPER CASE.
> All non-official functions are Capitalized.

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
* `PI` π

## [Sort](./sort.cpc)
* `Sort`: shell sort
    ```
    Sort(BYREF arr : ARRAY, BYVAL left : INTEGER, right : INTEGER)
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
* `Trim`: remove blanks at the beginning and the ending of a string
    ```
    Trim(s : STRING) RETURNS STRING
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

## [Time](./time.cpc)
* `Time`: get current time seal
    ```
    Time RETURNS REAL
    ```

## [Import](./import.cpc)
* `Import`: import another *cpc* file
    ```
    Import(target : STRING) RETURNS ImportObj
    ```
