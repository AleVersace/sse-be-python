from flask import Blueprint

sse_bp = Blueprint('sse_blueprint', __name__)


@sse_bp.route('/events', methods=['GET'])
def events():
    event = "events"
    print(event)
    return event
