# CAIE Code (cpc)

<br/>
<p align="center">
<a href="./assets/">
<img src="./assets/CPC4096.png" width="80" height="80" alt="logo">
</a>
<h3 align="center">the CAIE Pseudocode Interpreter</h3>
</p>
<p align="center">
<a href="./README_zh.md">中文</a> | <a href="./README.md">English</a>
</p>

## Installation and Update

### Installation Preliminaries

1. Have `python3` installed on your computer.
> It is suggested to use `pypy3` to achieve best efficiency.

2. Have `git` installed on your computer. If you do not know what `git` is, see https://git-scm.com/downloads.

> For **macOS** users ensure you installed `Command Line Tools for Xcode`.

3. `cargo` if you want to compile manually

### Installation

0. For **macOS** users, you can install directly using **CAIE_Code_Installer.pkg**from the [releases](https://github.com/iewnfod/CAIE_Code/releases/tag/v0.1.4-pkg) page.

  *For other users...*

1. Clone the project to your computer using
    `git clone https://github.com/iewnfod/CAIE_Code.git`.
2. Enter the project folder: `cd CAIE_Code`.

3. The executable programs are in `bin/` folder. You may directly run or consider adding `bin/` to your `PATH`.
    
4. If you want to compile manually:
  - **macOS**: run `build.sh`
  - **Windows**: run `build.ps1`

5. If you want to see the manual page from `man` command, you should consider link the manual file `man/cpc.1` to your `MANPATH`.

    > For example(**Linux**): `sudo ln -f ./man/cpc.1 /your/man/path`.

6. If you cannot execute the complied files, please submit the problems on our [issue page](https://github.com/iewnfod/CAIE_Code/issues).

### Update
If you followed the instructions and used `git` or PKG to install `cpc`, you can update easily using `cpc -u`.

Otherwise, you should manually re-install the whole project.

## Usage

`cpc [filepath] [options]`

It runs the entire file if `filepath` is provided, otherwise it enters playground mode.
### Options

| Mnemonic | Option | Description |
| -------- | ------ | ----------- |
| `-gt` | `--get-tree` | To show the tree of the program after being parsed |
| `-h` | `--help` | To show this help page |
| `-k` | `--keywords` | To show all the keywords |
| `-p` | `--parse` | To show parse information during running |
| `-t` | `--time` | To show the time for the script to run |
| `-v` | `--version` | To show the version of this interpreter |
| `-ne` | `--no-error` | To remove all error messages |
| `-u` | `--update` | To update the version (only useful when using a version equal or greater than `0.1.2` and installed by git) |
| `-r` | `--recursive-limit` | To set the recursive limit of the interpreter |
| `-c` | `--config` | To set configs of this interpreter |
| `-m` | `--migrate` | To migrate .p files to .cpc in a specified directory |

### Config

- `remote`
  - `github`: Use GitHub as the update source. This source is always the latest.
  - `gitee`: If you have an Internet connection issue to GitHub, please use this as a mirror source in China Mainland.
- `dev`
  - `true`: Enable the developer mode.
  - `false`: Disable the developer mode.

## FAQs

### Import Error
Please try to install all Python packages manually using
`pip install -r requirements.txt`

### Import Error after I manually installed packages
The program will automatically detect `pypy3` when available and use it to interpret pseudocode because it has better efficiency.

If you have `pypy3` installed you should install manually using `pypy3 -m pip install -r requirements.txt`

### Incorrect \<up\>, \<down\>, \<left\>, \<right\> key actions when in playground mode
You should retry `pip install readline` or `pip install gnureadline`.

### OSError when launching
Enter the directory of this project, and run
```shell
rm -rf .cpc_history
cpc -u
```

### Other problems?
If it still fails after re-installation, please report it to us on the [issue page](https://github.com/iewnfod/CAIE_Code/issues).


## Efficiency test

### Test Environment
- machine: 2020 MacBook Pro
- processor: Apple M1
- RAM: 8GB
- Cores: 8 (4 efficient, 4 performance)
- OS: macOS 13.3.1 (22E261)
- Python version: PyPy 3.9.16

### Basic Tests
- assignment: 10m/s
```
DECLARE a : INTEGER
FOR i <- 1 TO 10000000
    a <- i
NEXT i
```

- explicit conversion and assignment: 7.4m/s
```
DECLARE a : STRING
FOR i <- 1 TO 7400000
    a <- STRING(i)
NEXT i
```

- implicit conversion and assignment: 9.2m/s
```
DECLARE a : STRING
FOR i <- 1 TO 9200000
    a <- i
NEXT i
```

- print to terminal: 720k/s
```
DECLARE a : STRING
FOR i <- 1 TO 9200000
    a <- i
NEXT i
```

### Computation Tests
- [generating 100k randoms and shell sorting](https://github.com/iewnfod/CAIE_Code/blob/master/test/sort_test.cpc): about 2.5s


## Standards

### Basic Standards

- use camelCase naming
- use `.cpc` as the file suffix
- use `utf-8` encoding
- all reserved words are in upper case
- the program is case-sensitive
- use `//` to comment code

### Features
Most syntax follows the [pseudocode standard of CAIE](https://www.cambridgeinternational.org/Images/697401-2026-syllabus-legacy-notice.pdf).

However, indentation is *suggested but not compulsory*.

Each statement following `CASE` statement must end with a `;`, semicolon.

### Basic Data Types
The following items give the `DATATYPE`, its description, and the default value set when defined in brackets.

* `INTEGER` integer, whole number (`0`)
    ```
    1
    2
    123
    -123
    ```
* `REAL` float-point number (`0.0`)
    ```
    1.1
    0.1
    -12.1233
    ```
* `CHAR` one single character (`''`)
    ```
    '1'
    '!'
    'd'
    ```
* `STRING` string (`""`)
    ```
    "Hello"
    "World"
    "!"
    ```
* `BOOLEAN` boolean (`FALSE`)
    ```
    TRUE
    FALSE
    ```
* `DATE` date (current date)
    ```
    25/07/2023
    10/12/2012
    ```
    *

`None` is a null datatype returned by some special functions. it should not be used in normal coding and cannot be declared.

### Syntax Definitions

1. Variables and constants
    * Declare variables
        ```
        DECLARE <identifier> : <data type>
        DECLARE <identifier> : ARRAY [<lower>:<upper>, ...] OF <data type>
        ```
    * Declare constants
        ```
        CONSTANT <identifier> = <value>
        ```
    * Assignment
        ```
        <identifier> <- <value>
        <identifier>[<index>, ...] <- <value>
        ```
      > Pseudocode uses `<-` instead of `=`.
2. I/O
    * Input
        ```
        INPUT <identifier>
        ```
    * Output
        ```
        OUTPUT <value>, ...
        ```
3. Operations
    * `+` addition
    * `-` subtraction
    * `*` multiplication
    * `/` division
    * `>` greater than
    * `>=` greater than or equal to
    * `<` smaller than
    * `<=` smaller than  or equal to
    * `=` equal (NOT AN ASSIGNMENT STATEMENT)
    * `<>` not equal
    * `&` conglomerate strings
    * `MOD` modulus, find the remainder
    * `DIV` integer division
4. Logic operations
    * `AND`
    * `OR`
    * `NOT`
5. Conditional statements
    * IF statements
        ```
        IF <condition> THEN
            <statements>
        ENDIF
        
        IF <condition> THEN
            <statements>
        ELSE
            <statements>
        ENDIF
        ```
    * CASE statements
        > IMPORTANT: official standards do not have semicolons;` here
        ```
        CASE OF <identifier>
            <value> : <statements>;
            <value> : <statements>;
            ...
            OTHERWISE : <statements>;
        ENDCASE
        ```
6. Loop statements
    * FOR loop
        ```
        FOR <identifier> <- <value> TO <value>
            <statements>
        NEXT <identifier>
        ```
    * REPEAT loop
        ```
        REPEAT
            <statements>
        UNTIL <condition>
        ```
    * WHILE loop
        ```
        WHILE <condition>
            <statements>
        ENDWHILE
7. functions
    * functions without a return value (procedure)
        ```
        PROCEDURE <identifier>
            <statements>
        ENDPROCEDURE
        
        PROCEDURE <identifier> (<param> : <data type>, ...)
            <statements>
        ENDPROCEDURE
        ```
    * call a procedure
        ```
        CALL <identifier>
        
        CALL <identifier> (<value>, ...)
        ```
    * functions with return values
        ```
        FUNCTION <identifier> RETURNS <data type>
            <statements>
            RETURN <value>
        ENDFUNCTION
        
        FUNCTION <identifier> (<param> : <data type>, ...) RETURNS <data type>
            <statements>
            RETURN <value>
        ENDFUNCTION
    * call a function with return values
        ```
        <identifier> ()
        
        <identifier> (<value>, ...)
        ```
    * Before the parameters of those sub-routines, you *can* use `BYREF` or `BYVAL` to force the program to pass those parameters by reference or by-value respectively. If no `BYREF` nor `BYVAL` is given, the program will follow the prior parameter. If the program cannot find a clear indication it will, by default pass parameters by value.
        * If you explicitly define the data types of the array passed `BYVAL` the program will implicitly convert to the designated data type; the program will not convert data types when passed `BYREF`.
        * `BYREF` : pass the reference of a variable
        * `BYVAL` : pass a copy of the variable
8. File I/O
    * open a file
        ```
        OPENFILE <file path> FOR <file mode>
        ```
    * read a file
        ```
        READFILE <file path>, <variable>
        ```
    * write to a file
        ```
        WRITEFILE <file path>, <data>
        ```
    * close a file
        ```
        CLOSEFILE <file path>
        ```
    * locate in the file
        ```
        SEEK <file path>, <address>
        ```
    * File Mode
        1. `READ`
        2. `WRITE`
        3. `APPEND`
        4. `RANDOM`
9. Self-defined data types
    * enumerate type
        ```
        TYPE <identifier> = (<identifier>, ...)
        ```
    * pointer type
        ```
        TYPE <identifier> = ^<data type>
        ```
    * records(classes)
    > In this case, the program will not check the data types when assigning a variable of this type to another. The program will assign the other variable as the *reference* for this one.
    > ```
    > TYPE <identifier>
           <statements>
        ENDTYPE
         ```
### Special Syntax of **CPC** Interpreter
* delete a variable or constant on RAM
        ```
        DELETE <identifier>
        ```
    * do nothing
        ```
        PASS
        ```
    * import **CPC** files
        ```
        IMPORT <expression>
        ```
        * `expression` here should be a string within double quotes.
        * There is no isolation between the imported file and the
        main file. Identifiers may collide.
        * It is suggested to use the [`Import`](scripts/import.cpc) function
        to import a package instead.
        ```
        CONSTANT test = Import("test/import_test.cpc")
        ```
### Built-in Functions from CAIE Standard
* `RIGHT(ThisString : STRING, x : INTEGER) RETURNS STRING`
    ```
    $ RIGHT("ABCDEFGH", 3)
    "FGH"
    ```
* `LENGTH(ThisString : STRING) RETURNS INTEGER`
    ```
    $ LENGTH("Happy Days")
    10
    ```
* `MID(ThisString : STRING, x : INTEGER, y : INTEGER) RETURNS STRING`
    ```
    $ MID("ABCDEFGH", 2, 3)
    "BCD"
    ```
* `LCASE(ThisChar : CHAR) RETURNS CHAR`
    ```
    $ LCASE('W')
    'w'
    ```
* `UCASE(ThisChar : CHAR) RETURNS CHAR`
    ```
    $ UCASE('h')
    'H'
    ```
* `INT(x : REAL) RETURNS INTEGER`
    ```
    $ INT(27.5415)
    27
    ```
* `RAND(x : INTEGER) RETURNS REAL`
    ```
    $ RAND(87)
    35.43
    ```
* `EOF(file_path : STRING) RETURNS BOOLEAN`
* `POW(x: REAL, y: REAL) RETURNS REAL`

### Built-in Functions of this Interpreter
> These functions are fairly useful, but they are not included in the [CAIE standard](https://www.cambridgeinternational.org/Images/697401-2026-syllabus-legacy-notice.pdf).

* `EXIT(code : INTEGER)`: exit the program with the exit code
    `code`. Defalt exit code is 0.

* `ROUND(x : REAL, decimalPlace : INTEGER)`: round the
    float-point number `x` to some decimal place. The default decimal place is 0(to the nearest whole number).

* `PYTHON(code : STRING, *args)` is a Python interface. You can pass any Python statements into `code` and the program will run it in standard Python. the return value of this function is the value of variable `_result` in the Python code.

    Example:
    ```
    > DECLARE a : INTEGER
    > a <- 0
    > OUTPUT PYTHON("_result=a+1", a)
    1
    ```
    > if the Python code does not assign a value to `_result`, the function will return `None`.
    > you *must* pass all variables used in the Python code in `*args`, otherwise, it will not run correctly.

* For more non-official scripts, please see [scripts](./scripts).

## Targets
The following are the development targets of this project. Issues
and PRs are welcome.

- [x] basic operations
- [x] functions and procedures
- [x] materialize `TYPE`
- [ ] materialize `CLASS`
- [x] full file I/O support (`GETRECORD` and `PUTRECORD` not yet implemented)
- [ ] more [non-official functions](./scripts/README.md)
- [ ] improve efficiency (now improving)

## Author and Contributors
<a href="https://github.com/iewnfod/CAIE_Code/graphs/contributors">
    <img src="https://contrib.rocks/image?repo=iewnfod/CAIE_Code">
</a>

## License
MIT License

Copyright (c) 2023 Iewnfod

Permission is hereby granted, free of charge, to any person obtaining a copy of this software
and associated documentation files (the "Software"), to deal in the Software without
restriction, including without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or
substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING
BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
