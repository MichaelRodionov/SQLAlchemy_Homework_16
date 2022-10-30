from flask import Blueprint, request, jsonify
import utils as u
from models.models import db, Order


orders_blueprint = Blueprint('orders_blueprint', __name__)


@orders_blueprint.route('/orders/', methods=['GET', 'POST'])
@orders_blueprint.route('/orders/<int:order_id>', methods=['GET', 'PUT', 'DELETE'])
def get_orders(order_id=None):
    orders = []
    if not order_id:

        if request.method == 'GET':
            data = Order.query.all()
            for order in data:
                orders.append(u.make_dict_orders(order))
            return jsonify(orders)

        elif request.method == 'POST':
            data = request.json
            order = Order(
                name=data.get('name'),
                description=data.get('description'),
                start_date=data.get('start_date'),
                end_date=data.get('end_date'),
                address=data.get('address'),
                price=data.get('price'),
                customer_id=data.get('customer_id'),
                executor_id=data.get('executor_id')
            )
            db.session.add(order)
            db.session.commit()
            return f"Order {data.get('name')} added!", 201
    else:
        try:

            if request.method == 'GET':
                order = Order.query.get(order_id)
                data = u.make_dict_orders(order)
                return jsonify(data)

            elif request.method == 'PUT':
                data = request.json
                order = Order.query.get(order_id)
                order.name = data.get('name')
                order.description = data.get('description')
                order.start_date = data.get('start_date')
                order.end_date = data.get('end_date')
                order.address = data.get('address')
                order.price = data.get('price')
                order.customer_id = data.get('customer_id')
                order.executor_id = data.get('executor_id')
                db.session.add(order)
                db.session.commit()
                return f"Order with ID: {order_id} overwritten"

            elif request.method == 'DELETE':
                order = Order.query.get(order_id)
                db.session.delete(order)
                db.session.commit()
                return f"Order with ID: {order_id} deleted", 204

        except AttributeError:
            return f'ID "{order_id}" for orders not found'
