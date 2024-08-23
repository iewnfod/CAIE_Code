# CAIE Code (cpc)

<p align="center">
<a href="./assets/cpc.svg">
<img src="./assets/cpc.svg" width="100" height="100" alt="logo">
</a>
<h3 align="center">CAIE 伪代码解释器</h3>
</p>
<p align="center">
<a href="./README_zh.md">中文</a> | <a href="./README.md">English</a>
</p>

## 安装与使用

> [在线版本](https://github.com/createchstudio/caie-code-environment)

### 安装前提
1. `Python3` 环境 *推荐使用 PyPy3 以获得更好的性能*
2. `git` 指令
> macOS用户请安装`Command Line Tools for Xcode`
3. `cargo`命令

### 正式安装
0. 对于 macOS 用户，可使用以下脚本一键安装：
```shell
curl -fsSL https://atcrea.tech/cpc.sh | sh
```

> 对于想要一并Visual Studio Code以及配套[拓展](https://marketplace.visualstudio.com/items?itemName=CreatechStudioShanghaiInc.cpc-interpreter-extension)的用户，请使用以下脚本：
> ```shell
> curl -fsSL https://atcrea.tech/cpc.sh | sh -s -- --with-vsc
> ```

 *对于其他用户...*

1. 克隆此项目
    ```git clone https://github.com/iewnfod/CAIE_Code.git```
2. 进入项目
    ```cd CAIE_Code```
3. 运行
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
* 在`dc0cd71`之后引入自动更新功能，每周自动检测一次更新，可由选项配置
* 如果您并没有使用`git`进行安装，您需要手动下载新的版本，并使用和您之前相同的方法安装

## 用法
```
cpc [file_paths] [options]
```

### 选项
| Mnemonic | Option | Description |
| -------- | ------ | ----------- |
| `-c` | `--config` | 对解释器进行设置 |
| `-d` | `--document` | 使用系统默认方式打开官方规范文件 |
| `-h` | `--help` | 显示帮助页面 |
| `-k` | `--keywords` | 显示所有的关键字 |
| `-m` | `--migrate` | 将一个目录中的所有 `.p` 文件切换为 `.cpc` |
| `-n` | `--notification` | 显示由开发者发布的未过期通知 |
| `-p` | `--parse` | 显示所有解析的信息 |
| `-t` | `--time` | 显示运行脚本花费的时间 |
| `-u` | `--update` | 更新此解释器的版本 |
| `-v` | `--version` | 显示解释器当前版本 |
| `-gt` | `--get-tree` | 显示脚本解析后生成的可运行的树 |
| `-lc` | `--list-configs` | 显示解释器的所有设置 |
| `-ne` | `--no-error` | 禁止所有错误的输出 |
| `-rc` | `--reset-configs` | 删除解释器的所有设置 |
| `-init` | `--init-requirements` | 安装所有的依赖 |

### 可选配置

- `remote`
  - `github`：使用 GitHub 作为更新源并始终保持最新。
  - `gitee`： 使用 Gitee 作为更新源。（此源可能比 Github 要慢）

- `branch`

  - `stable`：更新较慢，但最稳定。
  - `nightly`：此分支每天更新一次。早期用户可以试用此分支，请积极报告问题。
  - `dev`：最新版本的 CPC，可能包含许多未经测试的功能。

  > 此设置需要运行一次 `cpc -u` 才能生效。

  > 在开发者模式中，您的远程配置不会被更改，分支将被锁定在 `dev`。

- `auto-update`
  - `true`：启用自动更新。
  - `false`：关闭自动更新。

- `last-auto-update`
    接受所有非负实数，由系统自动更新。

- `interval-update`
    接受所有非负整数，单位秒，作为自动更新间隔。

- `recursion-limit(rl)`
    接受所有整数，作为解释器的递归深度限制。

- `dev`

  - `true`： 启用开发者模式。
  - `false`： 关闭开发者模式。

- `integrity-protection`

    - `true`: 启用完整性保护。
    - `false`: 禁用完整性保护。

    > 完整性保护将会阻止任何意外或恶意的解释器修改。

    > 此保护将在开发者模式下被自动禁用。

- 开发者选项

  - `dev.simulate-update`
    - `true`: 开启模拟更新
    - `false`: 关闭模拟更新

## 常见问题

### 出现 `Import Error`
尝试手动安装依赖：
```shell
pip install -r requirements.txt
```

### 成功执行了第四步的依赖安装但还是无法正常运行
`cpc`文件会优先选择 `PyPy3` 运行
因此，在安装依赖时，请确保安装在了正确版本的 `Python3` 上
可以使用 `<指定Python版本> -m pip install -r requirements.txt` 进行安装

### Playground 模式下，上下左右键无法正常使用
使用 `pip install readline` 安装依赖并尝试运行
若 `readline` 无法正常安装，请安装 `gnureadline`，即 `pip install gnureadline`，再尝试运行

### cpc在启动时报OSError
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
* 机型： 2020 Macbook Pro (A2338)
* 处理器： Apple M1
* 内存： 8GB
* 核心： 8个 (4能效，4性能)
* 系统版本： macOS 14.1.1 (23B81)
* Python 版本： PyPy 3.9.16

### 基础测试
* 赋值： 1200w/s
```
DECLARE a : INTEGER
FOR i <- 1 TO 12000000
    a <- i
NEXT i
```
* 显式转换+赋值： 760w/s
```
DECLARE a : STRING
FOR i <- 1 TO 7600000
    a <- STRING(i)
NEXT i
```
* 隐式转换+赋值： 1000w/s
```
DECLARE a : STRING
FOR i <- 1 TO 10000000
    a <- i
NEXT i
```
* 输出： 65w/s
```
FOR i <- 1 TO 650000
    OUTPUT i
NEXT i
```

### 常见运算测试
* [随机生成10w数据+希尔排序](test/sort_test.cpc)：3.5s 左右


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
        PROCEDURE <identifier> ()
            <statements>
        ENDPROCEDURE

        PROCEDURE <identifier> (<param> : <data type>, ...)
            <statements>
        ENDPROCEDURE
        ```
    * 无返回值函数调用
        ```
        CALL <identifier> ()

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
10. 面对对象
    * 定义对象
        ```
        CLASS <identifier>
            PUBLIC PROCEDURE NEW (<params>)
                <statements>
            ENDPROCEDURE
            <statements>
        ENDCLASS
        ```
    * 私有/公有变量
        ```
        PRIVATE <identifier> : <type>
        PUBLIC <identifier> : <type>
        ```
    * 私有/公有函数
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
    * 创建实例
        ```
        NEW <identifier> (<values>)
        ```

    > 若不标明变量或函数的访问权限，默认为公有

11. 由此解释器提供的特殊语法
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
        > 此处的`expression`通常为一个被双引号包裹的字符串
        > 导入操作并不会做任何隔离，也就是说，被导入的文件的所有内容都会完全暴露给当前文件，因此请注意变量名重复使用的问题
        > 因此推荐使用[`Import`](./scripts/import.cpc)函数进行导入操作
        ```
        CONSTANT <identifier> = Import("<path to import file>")
        ```

### 内置函数
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
> 从2023年开始弃用
    ```
    $ LCASE('W')
    'w'
    ```
* `UCASE(ThisChar : CHAR) RETURNS CHAR`
> 从2023年开始弃用
    ```
    $ UCASE('h')
    'H'
    ```
* `TO_UPPER(x : <datatype>) RETURNS <datatype>`
> <datatype> 可以是 `CAHR` 或者 `STRING`
  ```
    $ TO_UPPER("hello")
    "HELLO"

    $ TO_UPPER('a')
    'A'
  ```
* `TO_LOWER(x : <datatype>) RETURNS <datatype>`
> <datatype> 可以是 `CAHR` 或者 `STRING`
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
> 周日返回1，周一返回2，以此类推
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

* `VARTYPE(v)` 获取`v`的数据类型并以字符串的形式返回

* `ANY` 这是一个任意类型用于允许一些未知类型的输入

* 更多非官方内置函数，请查阅 [scripts](./scripts)

## 目标
### Version 0.1.x 目标
- [ ] 实现所有由[官方文档](./Pseudocode%20Guide%20for%20Teachers.pdf)规定的功能
- [ ] 提高运行的稳定性，使得整体达到一个相对可用的状态
### Version 0.2.x 目标
- [ ] 对核心进行大规模更新与优化
- [ ] 支持编译到高性能虚拟机 (也就是类似于Java的解决方法)
### Version 0.3.x 目标
- [ ] 支持直接编译为可执行文件
### 长期目标
- [ ] 提供更多包
- [ ] 提高运行速度与效率
- [ ] 实现自举

## 赞助商
<a herf="https://1password.com/">
    <img src="https://www.vectorlogo.zone/logos/1password/1password-ar21.svg" height="100" alt="1Password">

## 作者与贡献者
<a href="https://github.com/iewnfod/CAIE_Code/graphs/contributors">
    <img src="https://contrib.rocks/image?repo=iewnfod/CAIE_Code">
</a>
