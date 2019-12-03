from flask import Blueprint, request, jsonify

from funbox import utils
from funbox import db

bp = Blueprint('api', __name__)


@bp.route('/visited_links', methods=['POST'])
def process_visited_links():
    data = request.json
    links = data.get('links') if type(data) is dict else None
    if not links or type(links) is not list:
        return process_error('sent data is not valid', 422)
    try:
        domains = set([utils.parse_link(link) for link in links])
    except ValueError:
        return process_error('sent urls is not valid', 422)
    db.store_domains(domains)
    return jsonify({'status': 'ok'})


@bp.route('/visited_domains')
def return_visited_domains():
    from_ts = request.args.get('from')
    to_ts = request.args.get('to')
    if not (from_ts and to_ts):
        return process_error('pass required arguments to complete a request', 422)
    if not (from_ts.isdigit() and to_ts.isdigit()):
        return process_error('pass correct arguments to complete a request', 400)
    domains = db.get_domains(from_ts, to_ts)
    if not domains:
        return process_error('not found', 404)
    return jsonify({'domains': domains, 'status': 'ok'})


def process_error(status='unknown error', status_code=400):
    return jsonify({'status': status}), status_code
