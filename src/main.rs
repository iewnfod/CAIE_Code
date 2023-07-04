#![allow(non_snake_case)]

use std::{env, process::Command};

pub const PYTHON : &[&str] = &[
    "pypy3",
    "pypy",
    "python3",
    "python"
];

fn main() {
    let mut args : Vec<String> = env::args().collect();
    // 删除第一个
    args.reverse();
    args.pop();
    args.reverse();

    // 获取文件所在目录
    let exe_path = env::current_exe().unwrap();
    let sdk_catalog = exe_path.parent().unwrap().parent().unwrap();
    let script_path = sdk_catalog.join("main.py");

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
        spawn.wait().unwrap();
        break;
    }
}
