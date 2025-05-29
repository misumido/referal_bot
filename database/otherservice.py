from database import get_db
from database.models import User, Channels, AdminInfo, Withdrawals
from datetime import datetime

def get_channels_for_check():
    with next(get_db()) as db:
        all_channels = db.query(Channels).all()
        if all_channels:
            return [[i.channel_id, i.channel_url] for i in all_channels]
        return []
def add_channel(channel_url, channel_id):
    with next(get_db()) as db:
        new_channel = Channels(channel_url=channel_url, channel_id=channel_id)
        db.add(new_channel)
        db.commit()

def get_actual_price():
    with next(get_db()) as db:
        money = db.query(AdminInfo).first().price
        return money
def get_actual_min_amount():
    with next(get_db()) as db:
        amount = db.query(AdminInfo).first().min_amount
        return amount
def get_user_name(tg_id):
    with next(get_db()) as db:
        user = db.query(User).filter_by(tg_id=tg_id).first()
        if user:
            return user.user_name


def add_admin_info(admin):
    with next(get_db()) as db:
        # TODO вписать сюда айди админа
        info = AdminInfo(id=1, admin_channel=admin)
        db.add(info)
        db.commit()
def count_info():
    with next(get_db()) as db:
        users = db.query(User).count()
        wa = db.query(Withdrawals).filter_by(status="принята").all()
        amount = 0
        try:
            for i in wa:
                amount += i.amount
        except:
            pass
        return [users, amount]