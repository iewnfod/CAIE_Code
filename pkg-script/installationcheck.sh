#!/bin/sh

if ! xcode-select -p &> /dev/null; then
	xcode-select --install
    exit 0
else
    # 获取 macOS 版本号
    os_version=$(sw_vers -productVersion)
    # 分割版本号并提取主要版本号
    IFS='.' read -r -a version_parts <<< "$os_version"
    major_version="${version_parts[0]}"
    # 检查主要版本号是否大于等于 12
    if [[ "$major_version" -ge 12 ]]; then
        exit 0
    else
        exit 33
    fi
fi