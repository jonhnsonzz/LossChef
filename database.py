"""
数据库初始化和操作
"""
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_db(app: Flask):
    """初始化数据库"""
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quickfood.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    
    with app.app_context():
        db.create_all()
        # 预置5个常见快餐品名
        from models import Dish
        if Dish.query.count() == 0:
            default_dishes = [
                ('快餐套餐A', 10.0),
                ('快餐套餐B', 12.0),
                ('单品盖饭', 8.0),
                ('面条类', 7.0),
                ('小菜加量', 3.0),
            ]
            for name, price in default_dishes:
                dish = Dish(name=name, cost_price=price)
                db.session.add(dish)
            db.session.commit()
            print("✓ 预置菜品已添加")


def get_recent_records(days: int = 7):
    """获取最近N天的损耗记录汇总"""
    from models import DailyRecord, Dish
    from datetime import datetime, timedelta
    
    end_date = datetime.utcnow().date()
    start_date = end_date - timedelta(days=days-1)
    
    # 按日期和菜品查询
    records = DailyRecord.query.filter(
        DailyRecord.date >= start_date,
        DailyRecord.date <= end_date
    ).order_by(DailyRecord.date.desc(), DailyRecord.dish_id).all()
    
    # 汇总
    daily_summary = {}
    for r in records:
        date_str = r.date.isoformat()
        if date_str not in daily_summary:
            daily_summary[date_str] = {
                'date': date_str,
                'total_sales': 0,
                'total_remain': 0,
                'total_loss': 0,
                'dishes': []
            }
        daily_summary[date_str]['total_sales'] += r.sales_qty
        daily_summary[date_str]['total_remain'] += r.remain_qty
        loss = r.remain_qty * (r.dish.cost_price if r.dish else 10)
        daily_summary[date_str]['total_loss'] += loss
        daily_summary[date_str]['dishes'].append({
            'name': r.dish.name if r.dish else '未知',
            'sales': r.sales_qty,
            'remain': r.remain_qty,
            'cost': r.dish.cost_price if r.dish else 10
        })
    
    # 转换loss为实际金额
    for date_str in daily_summary:
        daily_summary[date_str]['total_loss'] = round(daily_summary[date_str]['total_loss'], 2)
    
    return list(daily_summary.values())


def get_all_dishes():
    """获取所有菜品"""
    from models import Dish
    return Dish.query.order_by(Dish.id).all()