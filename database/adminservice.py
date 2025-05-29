from database import get_db
from database.models import *



def change_user_info(tg_id, column, new_info):
    with next(get_db()) as db:
        all_info = db.query(User).filter_by(user_id=tg_id).first()
        if column == "balance":
            all_info.balance = new_info
        elif column == "refs":
            all_info.refs = new_info
        elif column == "banned":
            all_info.banned = new_info
        db.commit()

def get_user_info(tg_id):
    with next(get_db()) as db:
        user = db.query(User).filter_by(tg_id=tg_id).first()
        if user:
            return [user.tg_id, user.banned, user.invited, user.balance, user.refs, user.paid]

def admin_menu_info():
    with next(get_db()) as db:
        users = db.query(User).count()
        wda = db.query(Withdrawals).filter_by(status="ожидание").count()
        return [users, wda]
def get_all_wait_payment():
    with next(get_db()) as db:
        wda = db.query(Withdrawals).filter_by(status="ожидание").all()
        all_wda = []
        try:
            for i in wda:
                all_wda.append([i.id, i.tg_id, i.amount, i.card, i.bank])
        except:
            pass
        return all_wda
def status_accepted(id):
    with next(get_db()) as db:
        wda = db.query(Withdrawals).filter_by(id=id).first()
        user_info = db.query(User).filter_by(tg_id=wda.tg_id).first()
        user_info.balance -= wda.amount
        user_info.paid += wda.amount
        wda.status = "принята"
        db.commit()
        return [wda.tg_id, wda.amount]
def status_declined(id):
    with next(get_db()) as db:
        wda = db.query(Withdrawals).filter_by(id=id).first()
        wda.status = "отклонена"
        db.commit()
        return [wda.tg_id, wda.amount]



def change_price(new_price):
    with next(get_db()) as db:
        info = db.query(AdminInfo).filter_by(id=1).first()
        if info:
            info.price = new_price
            db.commit()
def change_min_amount(new_amount):
    with next(get_db()) as db:
        info = db.query(AdminInfo).filter_by(id=1).first()
        if info:
            info.min_amount = new_amount
            db.commit()
def get_channels_for_admin():
    with next(get_db()) as db:
        all_channels = db.query(Channels).all()
        return [[i.id, i.channel_url, i.channel_id] for i in all_channels]
def add_new_channel_db(url, id):
    with next(get_db()) as db:
        new_channel = Channels(channel_url=url, channel_id=id)
        db.add(new_channel)
        db.commit()
        return True
def delete_channel_db(id):
    with next(get_db()) as db:
        channel = db.query(Channels).filter_by(id=id).first()
        if channel:
            db.delete(channel)
            db.commit()
            return True
        return False
def get_all_users_tg_id():
    with next(get_db()) as db:
        users = db.query(User).all()
        return [i.tg_id for i in users]
def ban_unban_db(id, bool):
    with next(get_db()) as db:
        user = db.query(User).filter_by(tg_id=id).first()
        user.banned = bool
        db.commit()

def addbalance_db(id, amount):
    with next(get_db()) as db:
        user = db.query(User).filter_by(tg_id=id).first()
        user.balance += amount
        db.commit()
def changebalance_db(id, amount):
    with next(get_db()) as db:
        user = db.query(User).filter_by(tg_id=id).first()
        user.balance = amount
        db.commit()
def changerefs_db(id, amount):
    with next(get_db()) as db:
        user = db.query(User).filter_by(tg_id=id).first()
        user.refs = amount
        db.commit()

def get_all_refs_db(tg_id):
    with next(get_db()) as db:
        users = db.query(User).filter_by(invited_id=tg_id).all()
        if users:
            return [[user.user_name, user.tg_id, user.balance, user.refs, user.invited, user.paid] for user in users]
        return []