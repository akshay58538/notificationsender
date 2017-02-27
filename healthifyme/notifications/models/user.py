from healthifyme.notifications.app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    push_id = db.Column(db.String(100))

    def __init__(self, push_id):
        self.push_id = push_id
