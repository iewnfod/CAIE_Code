# CAIE Code
CAIE Pseudocode Interpreter

## 安装与使用
1. 安装 `Python3` 环境
(**强烈推荐 `PyPy` 而不是 `CPython` 以获得一个可观的速度**)
(使用 [sort_test](test/sort_test.cpc) 测试，`PyPy3.9`运行了**3秒不到**，而同平台下`CPython3.10`则花费了**将近30秒**，`CPython3.11`也需**大约20秒**)
2. 克隆此项目
    ```git clone https://github.com/iewnfod/CAIE_Code.git```
3. 进入项目
    ```cd CAIE_Code```
4. 安装依赖
    ```pip install -r requirements.txt```
5. 运行
    * 二进制文件存在于`bin`中
    * `MacOS`若无法正常运行其中的二进制文件，可尝试自己编译
    ```./build.sh```
    * `Windows`若无法正常运行，也可尝试自己编译
    ```build.pw1```
    * `Linux`用户请自行编译
    ```./build.sh```


### 常见问题
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
* 核心数量: 8
* 系统版本: MacOS 13.3.1 (22E261)
* Python 版本: PyPy 3.9.16

### 基础测试
* 赋值运算: 740w/s - 750w/s
* 显式转换+赋值: 580w/s - 590w/s
* 隐式转换+赋值: 740w/s - 750w/s
* 输出: 71w/s - 72w/s

## 标准
### 基本标准
* 推荐使用驼峰命名发命名
* 源文件后缀名推荐使用 **.cpc**（CAIE Pseudo Code 的首字母简写）
* 源文件推荐使用 **utf-8** 编码
* 所有保留字均为大写，并且程序有大小写区分
* 使用 `//` 进行注释

### 一些特性
~~（说实话就是我不想改了）~~
* 四则运算只会在可运算的相同类型间运算，乘法除法的返回结果必定是`REAL`
* 单独书写某个变量会对其进行输出，打印其值以及类型
* 使用保留字以实现子空间 ~~（虽然官方文档要求有缩进，但是在此不做强制要求）~~
* 由于没有进行缩进的识别，`CASE`中的每一项末尾都需要添加`;`表达这一项结束了
* `INTEGER`与`REAL`在计算时并不会进行过多区分，只有在赋值给某个变量时才会最终确定其类型，因此在计算或函数返回与预期类型不同时，请勿慌张

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
* `BOOLEAN` 布尔值 (`TRUE`)
    ```
    TRUE
    FALSE
    ```
* `DATE` 任何合法的日期 (此类型暂时不会实现)

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
        CASE <identifier>
            <value> : <statements>;
            <value> : <statements>;
            ...
        ENDCASE

        CASE <identifier>
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
* 更多非官方内置函数，请查阅 [scripts](./scripts/README.md)

## 目标
- [x] 基础功能实现
- [x] 函数实现
- [ ] 实现 `TYPE`，`STRUCT`（准备实现）
- [x] 实现文件读写（还剩 `GETRECORD` 和 `PUTRECORD`，这需要等自定义类型实现后才能实现）
- [ ] 提供更多[非官方函数](./scripts/README.md)
