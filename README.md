# CAIE Code
CAIE Pseudocode Interpreter

## 安装与使用

### 安装前提
1. `Python3` 环境
2. `git` 指令

### 正式安装
1. 克隆此项目
    ```git clone https://github.com/iewnfod/CAIE_Code.git```
2. MacOS 用户可直接运行项目目录内的 [`install.sh`](./install.sh)，其他系统用户请继续根据`3, 4`步进行安装
3. 进入项目
    ```cd CAIE_Code```
4. 运行
    * 二进制文件存在于`bin`中，请将自己系统对应的二进制文件加入到`PATH`中
    * `MacOS`若无法正常运行其中的二进制文件，可尝试自己编译 [`build.sh`](./build.sh)
    * `Windows`若无法正常运行，也可尝试自己编译 [`build.ps1`](./build.ps1)
    * `Linux`用户请在[bin](./bin/linux/)中寻找自己对应系统平台的编译文件，若没有找到，请自行修改[`build-linux.sh`](./build-linux.sh)并编译
    * 非常欢迎`Linux`用户编译后提交pr

### Usage
```
cpc [file_path] [options]
```

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

### 常见问题
#### 出现 `Import Error`
尝试手动安装依赖:
```shell
pip install -r requirements.txt
```

#### 成功执行了第四步的依赖安装但还是无法正常运行
`cpc`文件会优先选择 `PyPy3` 运行
因此，在安装依赖时，请确保安装在了正确版本的 `Python3` 上
可以使用 `<指定Python版本> -m pip install -r requirements.txt` 进行安装

#### Playground 模式下，上下左右键无法正常使用
使用 `pip install readline` 安装依赖并尝试运行
若 `readline` 无法正常安装，请安装 `gnureadline`，即 `pip install gnureadline`，再尝试运行

*若依旧无法解决问题，请提交issue*


## 效率测试
### 测试环境:
* 机型: 2020 Macbook Pro
* 处理器: Apple M1
* 内存: 8GB
* 核心: 8个 (4能效，4性能)
* 系统版本: MacOS 13.3.1 (22E261)
* Python 版本: PyPy 3.9.16

### 基础测试
* 赋值: 1000w/s
```
DECLARE a : INTEGER
FOR i <- 1 TO 10000000
    a <- i
NEXT i
```
* 显式转换+赋值: 740w/s
```
DECLARE a : STRING
FOR i <- 1 TO 7400000
    a <- STRING(i)
NEXT i
```
* 隐式转换+赋值: 920w/s
```
DECLARE a : STRING
FOR i <- 1 TO 9200000
    a <- i
NEXT i
```
* 输出: 72w/s
```
FOR i <- 1 TO 720000
    OUTPUT i
NEXT i
```

### 常见运算测试
* [随机生成10w数据+希尔排序](test/sort_test.cpc): 2.5s 左右


## 标准
### 基本标准
* 推荐使用驼峰命名法
* 源文件后缀名推荐使用 **.cpc**（CAIE Pseudo Code 的首字母简写）
* 源文件推荐使用 **utf-8** 编码
* 所有保留字均为大写，并且程序有大小写区分
* 使用 `//` 进行注释

### 一些特性
~~（说实话就是我不想改了，也有可能是没想到什么好方法来改）~~
* 使用保留字以实现子空间 ~~（虽然官方文档要求有缩进，但是在此不做强制要求）~~
* 由于没有进行缩进的识别，`CASE`中的每一项末尾都需要添加`;`表达这一项结束了

### 基础数据类型
* `INTEGER` 整型 (`0`)
    ```
    1
    2
    123
    -123
    ```
* `REAL` 浮点型 (`0.0`)
    ```
    1.1
    0.1
    -12.1233
    ```
* `CHAR` 单个字符 (`''`)
    ```
    '1'
    '!'
    'd'
    ```
* `STRING` 字符串 (`""`)
    ```
    "Hello"
    "World"
    "!"
    ```
* `BOOLEAN` 布尔值 (`FALSE`)
    ```
    TRUE
    FALSE
    ```
* `DATE` 日期 (当前日期)
    ```
    25/07/2023
    10/12/2012
    ```
* `None` 此类型表示未知的类型，无法通过常规方法声明，也不应该滥用，仅会作为某些特殊函数的返回值存在

### 语法定义

1. 变量与常量
    * 变量声明
        ```
        DECLARE <identifier> : <data type>
        DECLARE <identifier> : ARRAY [<lower>:<upper>, ...] OF <data type>
        ```
    * 常量声明
        ```
        CONSTANT <identifier> = <value>
        ```
    * 赋值
        ```
        <identifier> <- <value>
        <identifier>[<index>, ...] <- <value>
        ```
2. 输入与输出
    * 输入
        ```
        INPUT <identifier>
        ```
    * 输出
        ```
        OUTPUT <value>, ...
        ```
3. 操作符
    * `+` 加法
    * `-` 减法
    * `*` 乘法
    * `/` 除法
    * `>` 大于
    * `>=` 大于等于
    * `<` 小于
    * `<=` 小于等于
    * `=` 等于
    * `<>` 不等于
    * `&` 字符串拼接
    * `MOD` 取模
    * `DIV` 整除
4. 逻辑运算
    * `AND` 与
    * `OR` 或
    * `NOT` 否
5. 条件语句
    * IF 语句
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
    * CASE 语句
        此处官方语法中并没有分号`;`
        ```
        CASE OF <identifier>
            <value> : <statements>;
            <value> : <statements>;
            ...
            OTHERWISE : <statements>;
        ENDCASE
        ```
6. 循环语句
    * FOR 循环
        ```
        FOR <identifier> <- <value> TO <value>
            <statements>
        NEXT <identifier>
        ```
    * REPEAT 循环
        ```
        REPEAT
            <statements>
        UNTIL <condition>
        ```
    * WHILE 循环
        ```
        WHILE <condition>
            <statements>
        ENDWHILE
7. 函数
    * 无返回值函数定义
        ```
        PROCEDURE <identifier>
            <statements>
        ENDPROCEDURE

        PROCEDURE <identifier> (<param> : <data type>, ...)
            <statements>
        ENDPROCEDURE
        ```
    * 无返回值函数调用
        ```
        CALL <identifier>

        CALL <identifier> (<value>, ...)
        ```
    * 有返回值函数定义
        ```
        FUNCTION <identifier> RETURNS <data type>
            <statements>
            RETURN <value>
        ENDFUNCTION

        FUNCTION <identifier> (<param> : <data type>, ...) RETURNS <data type>
            <statements>
            RETURN <value>
        ENDFUNCTION
    * 有返回值函数调用
        ```
        <identifier> ()

        <identifier> (<value>, ...)
        ```
    * 在定义函数的每个参数前，都可以使用 `BYREF` 或是 `BYVAL` 声明是需要引用还是复制。若一个参数前没有声明传入方式，会向上一个参数靠齐。在没有全部都没有声明，或者没有前一个参数可供参考时，默认的传入方式为 `BYVAL`。
        * `BYREF` : 引用变量，在函数内修改后，函数外变量的本体的值也会修改
        * `BYVAL` : 复制变量的值，在函数内做出的任何修改都不会影响到传入的变量本体
8. 文件读写
    * 打开文件
        ```
        OPENFILE <file path> FOR <file mode>
        ```
    * 读取文件
        ```
        READFILE <file path>, <variable>
        ```
    * 写入文件
        ```
        READFILE <file path>, <data>
        ```
    * 关闭文件
        ```
        CLOSEFILE <file path>
        ```
    * 定位读取
        ```
        SEEK <file path>, <address>
        ```
    * File Mode
        1. `READ`
        2. `WRITE`
        3. `APPEND`
        4. `RANDOM`
9. 自定义类型
    * 枚举类型
        ```
        TYPE <identifier> = (<identifier>, ...)
        ```
    * 类型指针
        ```
        TYPE <identifier> = ^<data type>
        ```
    * 自定义 (注意: **若将一个类的实例`a`赋值给另一个实例`b`，此时不会检查类型，且`b`会成为`a`的引用**)
        ```
        TYPE <identifier>
            <statements>
        ENDTYPE
        ```

### 内置函数
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

**(以下方法均不属于CAIE提供的标准方法)**
* `EXIT(code : INTEGER)` 以code为退出码，退出程序 (若不填写code，则默认为0)
* `ROUND(x : REAL, decimalPlace : INTEGER)` decimalPlace不填写默认为0
* `PYTHON(code: STRING)` Python3代码运行接口，并会返回code的运行结果，由于两个语言的类型系统并不互通，其返回的所有结果的类型皆为None，可赋值给任何本语言类型但不保证是否能够获得预期的结果 ***若需要获得此接口的返回值，请将返回值赋值给名为`result`的变量，否则将不会返回任何值***
* 更多非官方内置函数，请查阅 [scripts](./scripts)

## 目标
- [x] 基础功能实现
- [x] 函数实现
- [x] 实现 `TYPE`
- [ ] 实现 `CLASS`
- [x] 实现文件读写（还剩 `GETRECORD` 和 `PUTRECORD`，这需要等自定义类型实现后才能实现）
- [ ] 提供更多[非官方函数](./scripts/README.md)
- [ ] 提高效率（正在进行）
