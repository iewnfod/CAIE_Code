#!/bin/sh

# 检查是否存在CAIE_Code文件夹
if [ -d "/usr/local/sbin/CAIE_Code" ]; then
    echo "Found existing CAIE_Code folder. Removing it..."
    
    # 删除CAIE_Code文件夹及其内容
    rm -rf "/usr/local/sbin/CAIE_Code"

    # 检查删除是否成功
    if [ $? -eq 0 ]; then
        echo "CAIE_Code folder removed successfully."
        exit 0
    else
        echo "Failed to remove CAIE_Code folder."
        exit 1
    fi
fi

# 如果CAIE_Code文件夹不存在，则继续安装
exit 0
