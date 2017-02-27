from healthifyme.notifications.app import db


class NotificationSpec(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    text = db.Column(db.String(200))
    image_url = db.Column(db.String(200))
    schedule_time = db.Column(db.DateTime())
    sql_query = db.Column(db.Text())

    def __init__(self, title, text, image_url, schedule_time, sql_query):
        self.title = title
        self.text = text
        self.image_url = image_url
        self.schedule_time = schedule_time
        self.sql_query = sql_query
