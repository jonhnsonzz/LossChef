# 🍜 QuickLoss — 快餐店损耗记录与智能补货助手

> 一款面向餐饮小店的轻量级损耗追踪工具，通过 AI 分析历史数据，提供科学的备货建议。

[English](#english) | [中文](#中文)

---

## English

### 🍜 QuickLoss — Smart Loss Tracker & Restock Assistant for Fast Food Restaurants

**QuickLoss** is a lightweight web application designed for small restaurants to track food waste and get AI-powered restocking recommendations.

### Features

- 📊 **Loss Recording** — Log daily sales and remaining food for each dish
- 💰 **Auto Calculation** — Automatically calculates loss rate and monetary loss
- 📅 **History Dashboard** — View 7-day aggregated loss data
- 🤖 **AI Restock Advice** — Powered by DeepSeek LLM, provides科学的备货建议
- 📱 **Mobile Friendly** — Responsive design works on phones and desktops

### Tech Stack

- **Backend**: Python Flask + SQLite
- **Frontend**: Vanilla HTML/CSS (no framework)
- **AI**: DeepSeek API (user provides their own API key)

### Quick Start

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/quickfood-mvp.git
cd quickfood-mvp

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate    # Windows

# Install dependencies
pip install -r requirements.txt

# Set your DeepSeek API key
export DEEPSEEK_API_KEY="your-api-key-here"

# Run the application
python app.py
```

Visit `http://localhost:5000` in your browser.

### Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `DEEPSEEK_API_KEY` | Yes | Your DeepSeek API key |

### Project Structure

```
quickfood-mvp/
├── app.py           # Main Flask application
├── database.py      # Database operations
├── models.py        # Data models (SQLAlchemy)
├── templates/       # HTML templates
├── static/          # CSS/JS assets
├── instance/        # SQLite database (auto-generated)
└── requirements.txt # Python dependencies
```

### License

MIT License

---

## 中文

### 🍜 QuickLoss — 快餐店损耗记录与智能补货助手

**QuickLoss** 是一款面向中小型餐饮门店的轻量级工具，帮助餐饮从业者追踪每日食材损耗，并通过 AI 分析给出科学的补货建议。

### 功能特点

- 📊 **损耗记录** — 选择菜品 → 输入销量 → 输入剩余量 → 自动计算损耗
- 💰 **金额换算** — 根据成本价自动算出损耗金额
- 📅 **历史看板** — 查看近7天汇总数据，掌握损耗趋势
- 🤖 **AI 补货建议** — 基于 DeepSeek 大模型，分析历史数据给出明天备货量建议
- 📱 **手机适配** — 响应式布局，手机/电脑都能用

### 技术栈

- **后端**：Python Flask + SQLite（零配置，自带数据库）
- **前端**：原生 HTML/CSS（无框架依赖，轻量运行）
- **AI**：DeepSeek API（用户需自行提供 API Key）

### 5分钟快速上手

```bash
# 克隆项目
git clone https://github.com/YOUR_USERNAME/quickfood-mvp.git
cd quickfood-mvp

# 创建虚拟环境
python3 -m venv venv
source venv/bin/activate  # Mac/Linux
# venv\Scripts\activate    # Windows

# 安装依赖
pip install -r requirements.txt

# 设置你的 DeepSeek API Key
export DEEPSEEK_API_KEY="sk-xxxxxxxxxxxxxxxx"

# 启动应用
python app.py
```

打开浏览器访问 `http://localhost:5000`

### 环境变量说明

| 变量名 | 必须 | 说明 |
|--------|------|------|
| `DEEPSEEK_API_KEY` | ✅ | 你的 DeepSeek API Key |

### 界面预览

- **损耗记录页**：选择菜品、输入今日销量、输入剩余量，提交后自动计算
- **历史查询页**：查看近7天每日汇总（总销量、总剩余、总损耗金额）
- **AI 建议页**：输入补货问题，AI 分析历史数据给出建议
- **菜品管理页**：添加/删除菜品，设置成本价

### 项目结构

```
quickfood-mvp/
├── app.py           # Flask 主应用
├── database.py      # 数据库操作
├── models.py        # 数据模型（SQLAlchemy）
├── templates/       # HTML 页面模板
├── static/          # 静态资源
├── instance/        # SQLite 数据库文件（自动生成）
└── requirements.txt # Python 依赖
```

### 致谢

- [Flask](https://flask.palletsprojects.com/) — 轻量级 Python Web 框架
- [SQLAlchemy](https://www.sqlalchemy.org/) — Python ORM
- [DeepSeek](https://deepseek.com/) — AI 大模型支持

### License

MIT License