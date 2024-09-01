# CAIE Code (cpc)

<p align="center">
<a href="./assets/cpc.svg">
<img src="./assets/cpc.svg" width="100" height="100" alt="logo">
</a>
<h3 align="center">the CAIE Pseudocode Interpreter</h3>
</p>
<p align="center">
<a href="./README_zh.md">中文</a> | <a href="./README.md">English</a>
</p>

## Installation and Update

> [Online Version](https://github.com/createchstudio/caie-code-environment)

### Installation Preliminaries

1. Have `python3` installed on your computer.

> It is suggested to use `pypy3` to achieve the best efficiency.

1. Have `git` installed on your computer. If you do not know what `git` is, see https://git-scm.com/downloads.

> For **macOS** users ensure you installed `Command Line Tools for Xcode`.

3. `cargo` if you want to compile manually

### Installation

0. For **macOS** users, you can install directly using following scripts:
```shell
curl -fsSL https://atcrea.tech/cpc.sh | sh
```

> For those who want to install with Visual Studio Code as well as its [extension](https://marketplace.visualstudio.com/items?itemName=CreatechStudioShanghaiInc.cpc-interpreter-extension), you can use the following script:
> ```shell
> curl -fsSL https://atcrea.tech/cpc.sh | sh -s -- --with-vsc
> ```

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
* If you followed the instructions and used `git` or PKG to install `cpc`, you can update easily using `cpc -u`.

* An auto-update feature is introduced after `dc0cd71` to automatically detect updates once a week.

* Otherwise, you should manually re-install the whole project.

## Usage

`cpc [filepath] [options]`

It runs the entire file if `filepath` is provided, otherwise, it enters playground mode.
### Options

| Mnemonic | Option | Description |
| -------- | ------ | ----------- |
| `-c` | `--config` | To set configs of this interpreter |
| `-d` | `--document` | To show the official document |
| `-h` | `--help` | To show the help page |
| `-k` | `--keywords` | To show all the keywords |
| `-m` | `--migrate` | To migrate `.p` files to `.cpc` in a specified directory |
| `-n` | `--notification` | To show notification published by developer (only if this is not expired) |
| `-p` | `--parse` | To show parse information during running |
| `-t` | `--time` | To show the time for the script to run |
| `-u` | `--update` | To update the version |
| `-v` | `--version` | To show the version of this interpreter |
| `-gt` | `--get-tree` | To show the tree of the program after being parsed |
| `-lc` | `--list-configs` | To list all the configs of the interpreter |
| `-ne` | `--no-error` | To remove all error messages |
| `-rc` | `--reset-configs` | To reset all the configs of the interpreter |
| `-init` | `--init-requirements` | To install all dependences |

### Config

- `remote`
  - `github`: Use GitHub as the update source. This source is always the latest.
  - `gitee`: Use Gitee as the update source, which might be slower than Github.

- `branch`

  - `stable`: Updates are slow, but the most stable.
  - `nightly`: This branch will update once a day. Early adopters can try this branch, please actively report the issue.
  - `dev`: The latest version of CPC may contain many untested functions.

  > This setting needs to be run `cpc -u` once for it to take effect.

  > In a developer mod, your remote will not be changed by config and the branch will be locked in `dev`.

- `auto-update`
  - `true`：Enable auto update.
  - `false`：Disable auto update.

- `last-auto-update`
    All non-negative real numbers are accepted and automatically updated by the system.

- `interval-update`
    All non-negative integers, in seconds, are accepted as the automatic update interval.

- `recursion-limit(rl)`
    all integer number as the recursion depth limit of the interpreter.

- `integrity-protection`

    - `true`: Enable integrity protection.
    - `false`: Disable integrity protection.

    > Integrity Protection prevent any accidental or malicious modification of the interpreter.

    > This protection will be automatically disabled in developer mode.

- `dev`

    - `true`: Enable developer mode.
    - `false`: Disable developer mode.

- Developer Options

    - `dev.simulate-update`
      - `true`: Enable simulation updates
      - `false`: Disable simulation updates

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
- OS: macOS 14.1.1 (23B81)
- Python version: PyPy 3.9.16

### Basic Tests
- assignment: 1200w/s
```
DECLARE a : INTEGER
FOR i <- 1 TO 12000000
    a <- i
NEXT i
```

- explicit conversion and assignment: 760w/s
```
DECLARE a : STRING
FOR i <- 1 TO 7600000
    a <- STRING(i)
NEXT i
```

- implicit conversion and assignment: 1000w/s
```
DECLARE a : STRING
FOR i <- 1 TO 10000000
    a <- i
NEXT i
```

- print to terminal: 65w/s
```
FOR i <- 1 TO 650000
    OUTPUT i
NEXT i
```

### Computation Tests
- [generating 100k randoms and shell sorting](test/sort_test.cpc): about 3.5s


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
        > IMPORTANT: official standards do not have semicolons `;` here
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
        PROCEDURE <identifier> ()
            <statements>
        ENDPROCEDURE

        PROCEDURE <identifier> (<param> : <data type>, ...)
            <statements>
        ENDPROCEDURE
        ```
    * call a procedure
        ```
        CALL <identifier> ()

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
        ```
        TYPE <identifier>
            <statements>
        ENDTYPE
        ```
10. Object Oriented Programme
    * define an object
        ```
        CLASS <identifier>
            PUBLIC PROCEDURE NEW (<params>)
                <statements>
            ENDPROCEDURE
            <statements>
        ENDCLASS
        ```
    * private or public variable
        ```
        PRIVATE <identifier> : <type>
        PUBLIC <identifier> : <type>
        ```
    * private or public procedure and function
        ```
        PRIVATE PROCEDURE <identifier> (<params>)
            <statements>
        ENDPROCEDURE

        PUBLIC PROCEDURE <identifier> (<params>)
            <statements>
        ENDPROCEDURE

        PRIVATE FUNCTION <identifier> (<params>) RETURNS <type>
            <statements>
        ENDFUNCTION

        PUBLIC FUNCTION <identifier> (<params>) RETURNS <type>
            <statements>
        ENDFUNCTION
        ```
    * create an object
        ```
        NEW <identifier> (<values>)
        ```

    > If you do not sign a variable or procedure or function explicitly, it will be public by default.

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
    > `expression` here should be a string within double quotes.
    > There is no isolation between the imported file and the main file. Identifiers may collide.
    > It is suggested to use the [`Import`](scripts/import.cpc) function to import a package instead.
    ```
    CONSTANT <identifier> = Import("<path to import file>")
    ```

### Built-in Functions from CAIE Standard
* `LEFT(ThisString : STRING, x : INTEGER) RETURNS STRING`
    ```
    $ LEFT("ABCDEFGH", 3)
    "ABC"
    ```
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
> Decrapricated since 2023
    ```
    $ LCASE('W')
    'w'
    ```
* `UCASE(ThisChar : CHAR) RETURNS CHAR`
> Decrapricated since 2023
    ```
    $ UCASE('h')
    'H'
    ```
* `TO_UPPER(x : <datatype>) RETURNS <datatype>`
> <datatype> may be `CHAR` or `STRING`
  ```
    $ TO_UPPER("hello")
    "HELLO"

    $ TO_UPPER('a')
    'A'
  ```
* `TO_LOWER(x : <datatype>) RETURNS <datatype>`
> <datatype> may be `CHAR` or `STRING`
  ```
    $ TO_LOWER("HELLO")
    "hello"

    $ TO_LOWER('A')
    'a'
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
* `DAY(ThisDate : DATE) RETURNS INTEGER`
  ```
    $ DAY(25/07/2023)
    25
  ```
* `MONTH(ThisDate : DATE) RETURNS INTEGER`
  ```
    $ MONTH(25/07/2023)
    7
  ```
* `YEAR(ThisDate : DATE) RETURNS INTEGER`
  ```
    $ YEAR(12/12/2005)
    2005
  ```
* `DAYINDEX(ThisDate : DATE) RETURNS INTEGER`
> Where Sunday = 1, Monday = 2 etc
  ```
    $ DAYINDEX(25/03/2024)
    2
  ```
* `SETDATE(day : INTEGER, month : INTEGER, year : INTEGER) RETURNS DATE`
  ```
    $ SETDATE(25, 03, 2024)
    25/03/2024
  ```
* `TODAY() RETURNS DATE`
  ```
    $ TODAY()
    25/03/2024
  ```

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

* `VARTYPE(v)` is an interface to get the type of `v` and return it as a string.

* `ANY` is a type that used to allow some unknown type data.

* For more non-official scripts, please see [scripts](./scripts).

## Targets
### Version 0.1.x Target
- [ ] Implement all features provided by [official document](./Pseudocode%20Guide%20for%20Teachers.pdf).
- [ ] Increase the stability for running to achieve a relatively useable situation.
### Version 0.2.x Target
- [ ] Give the kernel a great update and optimization.
- [ ] Implement a high performance virtual machine to run. (Similar as the solution of Java)
### Version 0.3.x Target
- [ ] Allow building into executable binary file.
### Long-term Targets
- [ ] Provide more packages for use.
- [ ] Increase running speed and stability.
- [ ] Implement bootstrap.

## Sponsors
<a herf="https://1password.com/">
    <img src="https://www.vectorlogo.zone/logos/1password/1password-ar21.svg" height="100" alt="1Password">

## Author and Contributors
<a href="https://github.com/iewnfod/CAIE_Code/graphs/contributors">
    <img src="https://contrib.rocks/image?repo=iewnfod/CAIE_Code">
</a>
