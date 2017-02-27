from dateutil import parser
from flask import Blueprint, jsonify, request

from healthifyme.notifications.app import db
from healthifyme.notifications.models.notification_spec import NotificationSpec

notification_spec_blueprint = Blueprint('notification_spec_resource', __name__, url_prefix='/notifications')


@notification_spec_blueprint.route('/', methods=['GET', 'POST'])
def notification_specs():
    if request.method == 'GET':
        specs = NotificationSpec.query.all()
        return jsonify(items=map(lambda spec: spec.__dict__, specs))
    elif request.method == 'POST':
        request_json = request.get_json()
        request_json['schedule_time'] = parser.parse(request_json['schedule_time'])
        notification_spec = NotificationSpec(**request_json)
        db.session.add(notification_spec)
        db.session.commit()


@notification_spec_blueprint.route('/<spec_id>', methods=['GET'])
def get_spec(spec_id):
    specs = NotificationSpec.query.filter(NotificationSpec.id == spec_id).all()
    return jsonify(items=map(lambda spec: spec.__dict__, specs))
