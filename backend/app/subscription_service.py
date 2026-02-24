from datetime import datetime, timedelta
from .models import Subscription
from sqlalchemy.orm import Session

def has_active_subscription(db: Session, user):
    sub = db.query(Subscription).filter_by(user_id=user.id, is_active=True).first()
    if sub and sub.expires_at > datetime.utcnow():
        return True
    return False

def activate_subscription(db: Session, user):
    sub = Subscription(
        user_id=user.id,
        is_active=True,
        expires_at=datetime.utcnow() + timedelta(days=30)
    )
    db.add(sub)
    db.commit()