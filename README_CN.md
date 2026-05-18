[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)

# 损耗宝 🍜 — 餐饮损耗追踪与智能备货助手

**每天倒掉的菜，都是真金白银。损耗宝帮你管住这个漏洞。**

> 快餐店老板老张关店盘点：今天的宫保鸡丁卖了20份，后厨报损了3份。"这3份哪去了？是真的坏掉了，还是备多了？明天到底该备多少货？" 损耗宝把这些问题变成数据，AI 帮你分析明天该备多少。

[English Version](README.md)

---

## 😰 你是不是遇到过这些情况

- **损耗看不见** — 食材进了后厨，到底用了多少、浪费了多少，全靠厨师口头报数
- **备货靠经验** — 每天备多少菜，厨师凭感觉，备多了是损耗，备少了不够卖
- **月底对不上账** — 营收看起来还行，但食材成本一算，发现钱不知道去哪了
- **AI 工具太贵用不起** — 市面上的智能订货系统要几万元，小快餐店根本用不起

**损耗宝解决这个问题：把损耗从糊涂账变成可量化、可优化的数据。**

## ✨ 功能

- **5秒记录损耗** — 选菜品 → 输入销量 → 输入剩余量 → 自动算损耗份数和金额
- **7天损耗看板** — 哪个菜损耗最高、哪天异常、整体成本占比
- **AI 备货建议** — 基于你的历史数据，分析明天每道菜该备多少份
- **成本金额追踪** — 损耗对应多少钱，清清楚楚

## 📱 适用设备

手机和电脑浏览器均可使用。不需要下载 App，不需要注册账号。

## 🔒 数据安全

- 数据存在**你自己的 SQLite 数据库**里，不上传到任何服务器
- 不需要注册账号
- 不追踪、不贩卖数据

---

## 🚀 快速开始

### 环境要求

- Python 3.8+
- DeepSeek API Key（免费注册获取）

### 安装

```bash
git clone https://github.com/jonhnsonzz/LossChef.git
cd LossChef
pip install -r requirements.txt
```

### 配置

```bash
cp .env.example .env
# 编辑 .env，填入你的 DeepSeek API Key
# DEEPSEEK_API_KEY=你的密钥
```

### 运行

```bash
python app.py
```

浏览器打开 `http://localhost:5000`，手机和电脑都能用。

---

## 📂 项目结构

```
LossChef/
├── app.py           # Flask 主应用
├── database.py      # 数据库操作
├── models.py        # 数据模型
├── templates/       # HTML 页面
├── static/          # CSS/JS 资源
├── instance/        # SQLite 数据库（自动生成）
└── requirements.txt
```

---

## 💡 产品理念

餐饮损耗不是"正常损耗"——它是利润的黑洞。

大多数小快餐店不是故意浪费，而是没有工具来看见问题。

损耗宝帮你：把每天的"差不多"变成有数据支撑的"精准"。

---

## 🤝 参与贡献

欢迎提交 Issue 或 Pull Request！

## 📄 许可证

MIT License — 可自由使用，包括商用。
