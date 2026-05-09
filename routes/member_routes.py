from flask import Blueprint, request, jsonify
from extensions import db
from models.member import Member

member_bp = Blueprint('member_bp', __name__)

# Add Member API
@member_bp.route('/members', methods=['POST'])
def add_member():

    data = request.json

    member = Member(
        name=data['name'],
        email=data['email'],
        department=data['department'],
        phone=data['phone']
    )

    db.session.add(member)
    db.session.commit()

    return jsonify({
        "message": "Member added successfully"
    })


# Get All Members API
@member_bp.route('/members', methods=['GET'])
def get_members():

    members = Member.query.all()

    result = []

    for member in members:

        result.append({
            "id": member.id,
            "name": member.name,
            "email": member.email,
            "department": member.department,
            "phone": member.phone
        })

    return jsonify(result)


# Update Member API
@member_bp.route('/members/<int:id>', methods=['PUT'])
def update_member(id):

    member = Member.query.get(id)

    if not member:
        return jsonify({
            "message": "Member not found"
        }), 404

    data = request.json

    member.name = data['name']
    member.email = data['email']
    member.department = data['department']
    member.phone = data['phone']

    db.session.commit()

    return jsonify({
        "message": "Member updated successfully"
    })


# Delete Member API
@member_bp.route('/members/<int:id>', methods=['DELETE'])
def delete_member(id):

    member = Member.query.get(id)

    if not member:
        return jsonify({
            "message": "Member not found"
        }), 404

    db.session.delete(member)
    db.session.commit()

    return jsonify({
        "message": "Member deleted successfully"
    })