#![allow(non_snake_case)]

use std::{env, process::Command};

pub const PYTHON : &[&str] = &[
    "pypy3",
    "pypy",
    "python",
    "python3"
];

fn main() {
    let mut args : Vec<String> = env::args().collect();
    // 删除第一个
    args.reverse();
    args.pop();
    args.reverse();

    // 获取文件所在目录
    let exe_path = env::current_exe().unwrap();
    let mut sdk_catalog = exe_path.parent().unwrap();
    // 循环向上查找，直到找到包含main.py的目录
    loop {
        if sdk_catalog.join("main.py").exists() {
            break;
        }
        sdk_catalog = sdk_catalog.parent().unwrap();
    }
    let script_path = sdk_catalog.join("main.py");

    // 标记是否找到并成功运行
    let mut flag = false;
    for py in PYTHON {
        let mut cmd = Command::new(py);
        cmd.arg(&script_path);
        cmd.args(&args);
        let mut spawn = match cmd.spawn() {
            Ok(c) => c,
            Err(_) => {
                continue;
            }
        };

        match spawn.wait() {
            Ok(_) => {
                flag = true;
                break;
            },
            Err(_) => {
                continue;
            }
        }
    }

    // 如果没有找到 python，发出错误
    if !flag {
        println!("Cannot find Python3. ");
        println!("Please make sure Python3 is installed and is in your PATH. ");
    }
}
