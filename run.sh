#!/bin/bash
# 启动快餐店损耗记录系统

cd "$(dirname "$0")"

# 安装依赖
pip install -r requirements.txt -q

# 启动服务
echo "启动服务: http://0.0.0.0:5000"
python app.py