#!/bin/sh

# 获取当前执行目录
current_dir="/usr/local/sbin/CAIE_Code"
loggedInUser=$(/bin/ls -l /dev/console | /usr/bin/awk '{ print $3 }')
git config --global --add safe.directory /usr/local/sbin/CAIE_Code
chown -R $loggedInUser $current_dir

# 链接到 bin 目录
if [ $(arch) = "arm64" ]; then
   ln -sf ${current_dir}/bin/cpc_arm /usr/local/bin/cpc
elif [ $(arch) = "x86_64" ]; then
   ln -sf ${current_dir}/bin/cpc_x86 /usr/local/bin/cpc
fi

# 链接到 man 目录
ln -f ${current_dir}/man/cpc.1 /usr/local/share/man/man1/cpc.1

# 检查上述命令是否成功执行，根据情况设置退出代码
if [ $? -eq 0 ]; then
    echo "Installation completed successfully."
    exit 0
else
    echo "Installation failed."
    exit 1
fi