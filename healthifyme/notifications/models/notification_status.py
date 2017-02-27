from healthifyme.notifications.app import db


class NotificationStatus(db.Model):
    spec_id = db.Column(db.String(12), db.ForeignKey('notificationspec.id'), primary_key=True)
    user_id = db.Column(db.String(12), db.ForeignKey('user.id'), primary_key=True)
    status = db.Column(db.String(12))

    def __init__(self, spec_id, user_id, status):
        self.spec_id = spec_id
        self.user_id = user_id
        self.status = status
