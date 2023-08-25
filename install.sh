echo "安装 CAIE Code 中..."
# 获取当前执行目录
current_dir=$(cd $(dirname $0); pwd)
# 合成写入内容
content="export PATH=${current_dir}/bin:\$PATH"
# 写入 bash_profile 文件
echo "" >> ~/.bash_profile  # 换行
echo "# CAIE Code Binary Environment" >> ~/.bash_profile
echo $content >> ~/.bash_profile
# 写入 zshrc 文件
echo "" >> ~/.zshrc  # 换行
echo "# CAIE Code Binary Environment" >> ~/.zshrc
echo $content >> ~/.zshrc

echo "安装完成"
echo "请重启终端使配置生效"
echo "若移动了当前目录，请重新运行此文件"
