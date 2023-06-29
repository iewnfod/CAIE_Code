# CAIE Code
CAIE Pseudocode Interpreter

## 安装与使用
1. 安装 `Python3` 环境
2. 克隆此项目
    ```git clone https://github.com/iewnfod/CAIE_Code.git```
3. 进入项目
    ```cd CAIE_Code```
4. 安装依赖
    ```pip install -r requirements.txt```
5. 若是`MacOS`或`Linux`，使用指令`./cpc`运行，`MacOS`甚至可以直接双击目录内`cpc`文件启动终端模式运行
6. 若是`Windows`，请使用`python main.py`运行
7. 使用指令`./cpc -h`或`python main.py -h`获取更多帮助

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
* 所有变量在声明后默认值均为`None`，请即刻对其赋值，以避免不必要的错误
* 单独书写某个变量会对其进行输出，打印其值以及类型
* 使用保留字以实现子空间 ~~（虽然官方文档要求有缩进，但是在此不做强制要求）~~
* 由于没有进行缩进的识别，`CASE`中的每一项末尾都需要添加`;`表达这一项结束了
* `INTEGER`与`REAL`在计算时并不会进行过多区分，只有在赋值给某个变量时才会最终确定其类型，因此在计算或函数返回与预期类型不同时，请勿慌张

### 基础数据类型
* `INTEGER` 整型
    ```
    1
    2
    123
    -123
    ```
* `REAL` 浮点型
    ```
    1.1
    0.1
    -12.1233
    ```
* `CHAR` 单个字符
    ```
    '1'
    '!'
    'd'
    ```
* `STRING` 字符串
    ```
    "Hello"
    "World"
    "!"
    ```
* `BOOLEAN` 布尔值
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
* 更多非官方内置函数，请查阅 [scripts](./scripts/)

## 目标
- [x] 基础功能实现
- [x] 函数实现
- [ ] 实现 `TYPE`
- [ ] 实现 `STRUCT`
- [ ] 实现 `DATE`
- [ ] 实现文件读写
- [ ] 提供更多非官方函数
