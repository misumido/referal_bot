from database import get_db
from database.models import User, AdminInfo, Withdrawals, Checker
from datetime import datetime

def add_user(tg_id, user_name, invited="Никто", invited_id=None):
    with next(get_db()) as db:
        new_user = User(tg_id=tg_id, user_name=user_name, invited=invited, invited_id=invited_id,
                        reg_date=datetime.now())
        db.add(new_user)
        db.commit()

def add_ref(tg_id, inv_id):
    with next(get_db()) as db:
        new_ref = Checker(tg_id=tg_id, inv_id=inv_id)
        db.add(new_ref)
        db.commit()




def check_user(tg_id):
    with next(get_db()) as db:
        checker = db.query(User).filter_by(tg_id=tg_id).first()
        if checker:
            return True
        return False

def check_ban(tg_id):
    with next(get_db()) as db:
        checker = db.query(User).filter_by(tg_id=tg_id).first()
        if checker:
            if checker.banned == True:
                return True
        return False
def get_user_info_db(tg_id):
    with next(get_db()) as db:
        user = db.query(User).filter_by(tg_id=tg_id).first()
        if user:
            return [user.user_name, user.tg_id, user.balance, user.refs, user.invited, user.paid]

def plus_ref(tg_id):
    with next(get_db()) as db:
        user = db.query(User).filter_by(tg_id=tg_id).first()
        if user:
            user.refs += 1
            db.commit()
def plus_money(tg_id):
    with next(get_db()) as db:
        user = db.query(User).filter_by(tg_id=tg_id).first()
        money = db.query(AdminInfo).first().price
        if user:
            user.balance += money
            db.commit()
def reg_withdrawals(tg_id, amount, card, bank):
    with next(get_db()) as db:
        new_wa = Withdrawals(tg_id=tg_id, amount=amount, card=card, bank=bank)
        db.add(new_wa)
        db.commit()
        wda = db.query(Withdrawals).filter_by(status="ожидание", tg_id=tg_id).first()
    return [wda.id, wda.tg_id, wda.amount, wda.card, wda.bank]

def check_for_wa(tg_id):
    with next(get_db()) as db:
        check = db.query(Withdrawals).filter_by(tg_id=tg_id, status="ожидание").first()
        if check:
            return True
        return False
def get_admin_user():
    with next(get_db()) as db:
        check = db.query(AdminInfo).first()
        if check:
            return check.admin_channel
        return ""

def check_and_add(tg_id):
    with next(get_db()) as db:
        check = db.query(Checker).filter_by(tg_id=tg_id).first()
        if check:
            if not check.add:
                check.add = True
                plus_ref(check.inv_id)
                plus_money(check.inv_id)
                db.commit()

