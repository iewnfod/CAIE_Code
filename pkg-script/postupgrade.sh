#!/bin/sh

# 设置在出现非零退出代码时停止脚本执行
set -e

# 获取当前执行目录
current_dir="/usr/local/sbin/CAIE_Code"
loggedInUser=$(/bin/ls -l /dev/console | /usr/bin/awk '{ print $3 }')

# 如果git config失败，则返回退出代码1
git config --global --add safe.directory /usr/local/sbin/CAIE_Code || exit 1

# 如果chown失败，则返回退出代码1
chown -R $loggedInUser $current_dir || exit 1

# 链接到 bin 目录
if [ $(arch) = "arm64" ]; then
   ln -sf ${current_dir}/bin/cpc_arm /usr/local/bin/cpc || exit 1
elif [ $(arch) = "x86_64" ]; then
   ln -sf ${current_dir}/bin/cpc_x86 /usr/local/bin/cpc || exit 1
elif [ $(arch) = "i386" ]; then
   ln -sf ${current_dir}/bin/cpc_x86 /usr/local/bin/cpc || exit 1
else
   echo "Unknown architecture"
   exit 1
fi

# 链接到 man 目录，如果失败则返回退出代码1
ln -f ${current_dir}/man/cpc.1 /usr/local/share/man/man1/cpc.1 || exit 1
