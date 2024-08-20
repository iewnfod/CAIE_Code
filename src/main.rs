#![allow(non_snake_case)]

use std::{env, process::Command, fs, path::PathBuf, str::FromStr};

pub const PYTHON : &[&str] = &[
    "pypy3",
    "pypy",
    "python",
    "python3",
];

pub const MAC_PYTHON_HOME : &str = "/Library/Frameworks/Python.framework/Versions";

fn solve_system_python(_python_home: &str) -> Vec<PathBuf> {
    let mut system_python = vec![];
    if !PathBuf::from_str(_python_home).unwrap().exists() {
        return vec![];
    }
    let paths = fs::read_dir(_python_home).unwrap();
    for path in paths {
        let p = path.unwrap();
        let expect_py = p.path().join("bin").join("python3");
        if expect_py.exists() {
            // 如果是 pypy，就把他提前到前面，让他优先运行
            let p_name = p.file_name();
            let str_name = p_name.to_str().unwrap();
            if str_name.contains("pypy") {
                system_python.insert(0, expect_py);
            } else {
                system_python.push(expect_py);
            }
        }
    }
    system_python
}

fn main() {
    let mut args : Vec<String> = env::args().collect();
    // 删除第一个
    args.reverse();
    args.pop();
    args.reverse();

    // 获取文件所在目录
    let mut exe_path = env::current_exe().unwrap();
    while exe_path.is_symlink() {
        exe_path = exe_path.read_link().unwrap();
    }
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

    // 通过系统查找 Python
    let mut system_python = vec![];
    for py in PYTHON {
        system_python.push(PathBuf::from_str(py).unwrap());
    }

    if cfg!(target_os = "macos") {
        system_python = [system_python, solve_system_python(MAC_PYTHON_HOME)].concat();
    }

    // println!("{:?}", system_python);

    for py in system_python {
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
        println!("Cannot find Python3 in your computer. ");
        println!("Please make sure Python3 is installed and is in your PATH. ");
    }
}
