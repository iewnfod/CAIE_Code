set -e

exit_install_failure() {
    echo "安装失败"
    exit 1
}

echo "安装 CAIE Code 中... (此过程中可能会需要sudo权限)"
# 获取当前执行目录
current_dir=$(cd $(dirname $0); pwd)
loggedInUser=$(/bin/ls -l /dev/console | /usr/bin/awk '{ print $3 }')

git config --global --add safe.directory ${current_dir} || exit_install_failure

# 链接到 bin 目录
sudo ln -sf ${current_dir}/bin/cpc /usr/local/bin/cpc || exit_install_failure

# 链接到 man 目录
sudo mkir -p /usr/local/share/man/man1
sudo ln -f ${current_dir}/man/cpc.1 /usr/local/share/man/man1/cpc.1 || exit_install_failure

echo "安装完成"
echo "若移动了当前目录，请重新运行此文件"
