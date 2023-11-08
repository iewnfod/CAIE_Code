# CAIE Code (cpc)

<br/>
<p align="center">
<a href="./assets/">
<img src="./assets/cpc-icon-high.png" width="80" height="80" alt="logo">
</a>
<h3 align="center">the CAIE Pseudocode Interpreter</h3>
</p>
<p align="center">
<a href="./README_cn.md">中文</a> | <a href="./README.md">English</a>
</p>

## 安装与使用

### 安装前提
1. `Python3` 环境 *推荐使用 PyPy3 以获得更好的性能*
2. `git` 指令
> macOS用户请安装`Command Line Tools for Xcode`
3. `cargo`命令

### 正式安装
1. 克隆此项目
    ```git clone https://github.com/iewnfod/CAIE_Code.git```
2. MacOS 用户可直接运行Releases内的 [`CAIE_Code_Installer.pkg`](https://github.com/iewnfod/CAIE_Code/releases/tag/v0.1.4-pkg)，其他系统用户请继续根据`3, 4`步进行安装
3. 进入项目
    ```cd CAIE_Code```
4. 运行
    * 二进制文件存在于`bin`中，请将自己系统对应的二进制文件加入到`PATH`中
    * `MacOS`若无法正常运行其中的二进制文件，可尝试自己编译 [`build.sh`](./build.sh)
    * `Windows`若无法正常运行，也可尝试自己编译 [`build.ps1`](./build.ps1)
    >若运行已有二进制文件后无反应，同上。若依旧无法解决，请提交issue
    * 如果需要使用`man`指令，请自行将[cpc.1](./man/cpc.1)硬链接到你的`MANPATH`内，以便更新后不必再次链接。
        * `Linux`用户可以使用以下指令：
            ```
            sudo ln -f ./man/cpc.1 /your/man/path
            ```
        * `Windows`用户请自行搜索

### 更新
* 如果您是完全使用以上步骤进行安装的，您可以使用`cpc -u`快速更新
* 如果您并没有使用`git`进行安装，您需要手动下载新的版本，并使用和您之前相同的方法安装

## 用法
```
cpc [file_paths] [options]
```

### 选项
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

### 可选配置

- `remote`
  - `github`：使用GitHub作为更新源并始终保持最新。
  - `gitee`： 如果您在 GitHub 上遇到 Internet连接问题，请将其用作中国大陆用户的镜像源。
- `dev`
  - `true`： 启用开发者模式。
  - `false`： 关闭开发者模式。

### 常见问题

#### 出现 `Import Error`
尝试手动安装依赖：
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

#### cpc在启动时报OSError
进入`cpc`安装目录，可使用
删除`.cpc_history`文件
更新`cpc`
```shell
cd $(which cpc)/../..
rm -rf .cpc_history
cpc -u
```

*若依旧无法解决问题，请提交issue*


## 效率测试
### 测试环境：
* 机型： 2020 Macbook Pro
* 处理器： Apple M1
* 内存： 8GB
* 核心： 8个 (4能效，4性能)
* 系统版本： MacOS 13.3.1 (22E261)
* Python 版本： PyPy 3.9.16

### 基础测试
* 赋值： 1000w/s
```
DECLARE a : INTEGER
FOR i <- 1 TO 10000000
    a <- i
NEXT i
```
* 显式转换+赋值： 740w/s
```
DECLARE a : STRING
FOR i <- 1 TO 7400000
    a <- STRING(i)
NEXT i
```
* 隐式转换+赋值： 920w/s
```
DECLARE a : STRING
FOR i <- 1 TO 9200000
    a <- i
NEXT i
```
* 输出： 72w/s
```
FOR i <- 1 TO 720000
    OUTPUT i
NEXT i
```

### 常见运算测试
* [随机生成10w数据+希尔排序](test/sort_test.cpc)： 2.5s 左右


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
        * 在 `BYVAL` 中，如果确定了数组的类型，隐式转换将会发生，但在 `BYREF` 中，并不会考虑数组类型
        * `BYREF` ： 引用变量，在函数内修改后，函数外变量的本体的值也会修改
        * `BYVAL` ： 复制变量的值，在函数内做出的任何修改都不会影响到传入的变量本体
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
        WRITEFILE <file path>, <data>
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
    * 自定义 (注意： **若将一个类的实例`a`赋值给另一个实例`b`，此时不会检查类型，且`b`会成为`a`的引用**)
        ```
        TYPE <identifier>
            <statements>
        ENDTYPE
        ```
10. 由此解释器提供的特殊语法
    * DELETE 删除变量或常量
        ```
        DELETE <identifier>
        ```
    * PASS 跳过 (即不执行任何操作)
        ```
        PASS
        ```
    * IMPORT 导入文件
        ```
        IMPORT <expression>
        ```
        * 此处的`expression`通常为一个被双引号包裹的字符串
        * 导入操作并不会做任何隔离，也就是说，被导入的文件的所有内容都会完全暴露给当前文件，因此请注意变量名重复使用的问题
        * 因此推荐使用[`Import`](./scripts/import.cpc)函数进行导入操作
        ```
        CONSTANT test = Import("test/import_test.cpc")
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
* `PYTHON(code: STRING)` Python3代码运行接口，并会返回code的运行结果，由于两个语言的类型系统并不互通，其返回的所有结果的类型皆为None，可赋值给任何本语言类型但不保证是否能够获得预期的结果
    * ***若需要获得此接口的返回值，请将返回值赋值给名为`_result`的变量，否则将会返回值为None的None类型***
    * ***若需要向此接口内传入变量，请在Python3代码中使用与外部相同的变量名，并将那个变量作为参数传入此函数***
        ```
        > DECLARE a : INTEGER
        > PYTHON("_result=a+1", a)
        1
        ```

* 更多非官方内置函数，请查阅 [scripts](./scripts)

## 目标
- [x] 基础功能实现
- [x] 函数实现
- [x] 实现 `TYPE`
- [ ] 实现 `CLASS`
- [x] 实现文件读写（还剩 `GETRECORD` 和 `PUTRECORD`，这需要等自定义类型实现后才能实现）
- [ ] 提供更多[非官方函数](./scripts/README.md)
- [ ] 提高效率（正在进行）


## 作者与贡献者
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
