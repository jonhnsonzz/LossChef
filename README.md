[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)

# LossChef 🍜 — Restaurant Food Waste Tracker

**Stop guessing how much food you're wasting. Start measuring it.**

> Restaurant owner Zhang closes up for the night. Today's Kung Pao Chicken sold 20 servings, but the kitchen reported 3 servings of waste. "Where did those 3 servings go? Did they really spoil, or did we just prep too much? How much should we prep tomorrow?" LossChef turns this into data — and the AI tells you exactly how much to prep next time.

[中文说明](README_CN.md)

---

## 😰 The Problem

Every restaurant owner knows this:

- **Waste is invisible** — Ingredients go into the kitchen, but how much was actually used vs. wasted? You rely on the chef's word
- **Prep is guesswork** — Too much prep = waste, too little = sold out. The chef goes by feel
- **Profit leaks** — Revenue looks fine, but food costs don't add up and you can't explain where the money went
- **AI tools are unaffordable** — Smart ordering systems cost tens of thousands of yuan. Small restaurants are left out

**LossChef makes waste measurable and optimizable — without the enterprise price tag.**

## ✨ Features

- **5-Second Logging** — Select dish → enter sales → enter leftovers → auto-calculates waste
- **7-Day Dashboard** — See which dishes waste the most, which days are abnormal
- **AI Prep Advice** — Based on your historical data, get next-day prep recommendations per dish
- **Cost Tracking** — See exactly how much money your waste represents

## 📱 Compatibility

Works in any phone or desktop browser. No app download, no account needed.

## 🔒 Data

- All data stored in **your own SQLite database** — nothing uploaded
- No account required
- No tracking, no data selling

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- DeepSeek API Key

### Installation

```bash
git clone https://github.com/jonhnsonzz/LossChef.git
cd LossChef
pip install -r requirements.txt
```

### Configuration

```bash
cp .env.example .env
# Edit .env and set: DEEPSEEK_API_KEY=your_key_here
```

### Run

```bash
python app.py
```

Open `http://localhost:5000` in your browser (works on phone and desktop).

---

## 📂 Project Structure

```
LossChef/
├── app.py           # Flask application
├── database.py     # Database operations
├── models.py       # Data models
├── templates/      # HTML pages
├── static/         # CSS/JS assets
├── instance/       # SQLite database (auto-generated)
└── requirements.txt
```

---

## 💡 Philosophy

Food waste isn't "normal overhead" — it's a profit leak.

Most small restaurants don't waste intentionally. They just lack the tools to **see** the problem.

LossChef turns daily "close enough" estimates into data-backed precision.

---

## 🤝 Contributing

Contributions welcome! Feel free to open issues or submit pull requests.

## 📄 License

MIT License — free to use, including commercially.
