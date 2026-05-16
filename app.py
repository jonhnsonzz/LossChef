"""
Flask主应用 - 快餐店损耗记录+AI补货建议工具
"""
import os
import requests
from datetime import datetime
from flask import Flask, render_template, request, jsonify, redirect, url_for
from database import db, init_db, get_recent_records, get_all_dishes
from models import Dish, DailyRecord

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'quickfood-secret-key-2024')

# 初始化数据库
init_db(app)


# ==================== 页面路由 ====================

@app.route('/')
def index():
    """损耗记录首页"""
    dishes = get_all_dishes()
    return render_template('index.html', dishes=dishes)


@app.route('/history')
def history():
    """历史查询页面"""
    records = get_recent_records(days=7)
    return render_template('history.html', records=records)


@app.route('/advice')
def advice():
    """AI补货建议页面"""
    records = get_recent_records(days=7)
    return render_template('advice.html', records=records)


@app.route('/admin')
def admin():
    """菜品管理页面"""
    dishes = get_all_dishes()
    return render_template('admin.html', dishes=dishes)


# ==================== API接口 ====================

@app.route('/api/record', methods=['POST'])
def add_record():
    """添加损耗记录"""
    data = request.get_json()
    
    dish_id = data.get('dish_id')
    sales_qty = int(data.get('sales_qty', 0))
    remain_qty = int(data.get('remain_qty', 0))
    
    if not dish_id:
        return jsonify({'success': False, 'error': '请选择菜品'})
    
    # 获取成本价计算损耗
    dish = Dish.query.get(dish_id)
    if not dish:
        return jsonify({'success': False, 'error': '菜品不存在'})
    
    cost_price = dish.cost_price
    
    # 计算损耗
    loss_rate = round(remain_qty / sales_qty * 100, 1) if sales_qty > 0 else 0
    loss_amount = round(remain_qty * cost_price, 2)
    
    # 保存记录
    record = DailyRecord(
        date=datetime.utcnow().date(),
        dish_id=dish_id,
        sales_qty=sales_qty,
        remain_qty=remain_qty
    )
    db.session.add(record)
    db.session.commit()
    
    return jsonify({
        'success': True,
        'loss_rate': loss_rate,
        'loss_amount': loss_amount,
        'dish_name': dish.name
    })


@app.route('/api/history', methods=['GET'])
def api_history():
    """获取历史记录API"""
    days = int(request.args.get('days', 7))
    records = get_recent_records(days=days)
    return jsonify({'success': True, 'data': records})


@app.route('/api/advice', methods=['POST'])
def get_advice():
    """获取AI补货建议"""
    records = get_recent_records(days=7)
    
    if not records:
        return jsonify({'success': False, 'error': '暂无数据，请先记录损耗'})
    
    # 格式化数据
    data_text = ""
    for r in records:
        data_text += f"日期: {r['date']}, 总销量: {r['total_sales']}, 总剩余: {r['total_remain']}, 损耗金额: {r['total_loss']}元\n"
    
    today = datetime.utcnow()
    weekday_cn = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
    weekday = weekday_cn[today.weekday()]
    
    # DeepSeek API调用
    api_key = os.environ.get('DEEPSEEK_API_KEY')
    if not api_key:
        return jsonify({
            'success': False, 
            'error': '未配置DEEPSEEK_API_KEY环境变量'
        })
    
    prompt = f"""我是快餐店老板，过去7天损耗数据如下：
{data_text}
今天是{weekday}，根据历史数据分析：
1. 最近损耗率趋势如何？
2. 明天（周{weekday}）预计备货多少份？
3. 如何减少损耗？

请给出具体建议，用简洁的中文回复。"""
    
    try:
        response = requests.post(
            'https://api.deepseek.com/chat/completions',
            headers={
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {api_key}'
            },
            json={
                'model': 'deepseek-chat',
                'messages': [
                    {'role': 'user', 'content': prompt}
                ],
                'max_tokens': 500,
                'temperature': 0.7
            },
            timeout=30
        )
        result = response.json()
        
        if 'choices' in result and len(result['choices']) > 0:
            advice_text = result['choices'][0]['message']['content']
            return jsonify({'success': True, 'advice': advice_text})
        else:
            return jsonify({'success': False, 'error': result.get('error', 'API返回异常')})
            
    except Exception as e:
        return jsonify({'success': False, 'error': f'请求失败: {str(e)}'})


@app.route('/admin/add', methods=['POST'])
def add_dish():
    """添加新菜品"""
    name = request.form.get('name', '').strip()
    cost_price = float(request.form.get('cost_price', 10.0))
    
    if not name:
        return redirect(url_for('admin'))
    
    # 检查是否已存在
    existing = Dish.query.filter_by(name=name).first()
    if existing:
        return redirect(url_for('admin'))
    
    dish = Dish(name=name, cost_price=cost_price)
    db.session.add(dish)
    db.session.commit()
    
    return redirect(url_for('admin'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)