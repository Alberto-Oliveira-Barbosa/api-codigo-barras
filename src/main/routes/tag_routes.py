from flask import Blueprint, request, jsonify

tags_route_bp = Blueprint('tags_routes', __name__)

@tags_route_bp.route('/create_tag', methods=['POST'])
def create_tags():
    print(request.json)
    return jsonify({
        "response": "OK"
    }), 200
