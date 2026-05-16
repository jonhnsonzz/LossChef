"""
数据模型 - 快餐店损耗记录系统
"""
from datetime import datetime
from database import db


class Dish(db.Model):
    """菜品表"""
    __tablename__ = 'dishes'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    cost_price = db.Column(db.Float, default=10.0)  # 成本单价
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    records = db.relationship('DailyRecord', backref='dish', lazy=True)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'cost_price': self.cost_price
        }


class DailyRecord(db.Model):
    """每日损耗记录表"""
    __tablename__ = 'daily_record'
    
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    dish_id = db.Column(db.Integer, db.ForeignKey('dishes.id'), nullable=False)
    sales_qty = db.Column(db.Integer, default=0)  # 今日销量
    remain_qty = db.Column(db.Integer, default=0)  # 剩余量
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    @property
    def loss_rate(self):
        """损耗率 = 剩余量 / 销量 × 100%"""
        if self.sales_qty == 0:
            return 0
        return round(self.remain_qty / self.sales_qty * 100, 1)
    
    @property
    def loss_amount(self):
        """损耗金额 = 剩余量 × 成本单价"""
        if self.dish:
            return round(self.remain_qty * self.dish.cost_price, 2)
        return 0
    
    def to_dict(self):
        return {
            'id': self.id,
            'date': self.date.isoformat() if self.date else None,
            'dish_id': self.dish_id,
            'dish_name': self.dish.name if self.dish else None,
            'sales_qty': self.sales_qty,
            'remain_qty': self.remain_qty,
            'loss_rate': self.loss_rate,
            'loss_amount': self.loss_amount
        }