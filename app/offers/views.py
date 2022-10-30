from flask import Blueprint, request, jsonify
from models.models import db, Offer
import utils as u

offers_blueprint = Blueprint('offers_blueprint', __name__)


@offers_blueprint.route('/offers/', methods=['GET', 'POST'])
@offers_blueprint.route('/offers/<int:offer_id>', methods=['GET', 'PUT', 'DELETE'])
def get_offers(offer_id=None):
    offers = []
    if not offer_id:

        if request.method == 'GET':
            data = Offer.query.all()
            for offer in data:
                offers.append(u.make_dict_offers(offer))
            return jsonify(offers)

        elif request.method == 'POST':
            data = request.json
            offer = Offer(
                order_id=data.get('order_id'),
                executor_id=data.get('executor_id')
            )
            db.session.add(offer)
            db.session.commit()
            return f"Offer with ID: {offer.id} added!", 201
    else:
        try:

            if request.method == 'GET':
                offer = Offer.query.get(offer_id)
                data = u.make_dict_offers(offer)
                return jsonify(data)

            elif request.method == 'PUT':
                data = request.json
                offer = Offer.query.get(offer_id)
                offer.order_id = data.get('order_id')
                offer.executor_id = data.get('executor_id')
                db.session.add(offer)
                db.session.commit()
                return f"Offer with ID: {offer_id} overwritten!"

            elif request.method == 'DELETE':
                offer = Offer.query.get(offer_id)
                db.session.delete(offer)
                db.session.commit()
                return f"Offer with ID: {offer_id} deleted!", 204

        except AttributeError:
            return f'ID "{offer_id}" for offers not found'
