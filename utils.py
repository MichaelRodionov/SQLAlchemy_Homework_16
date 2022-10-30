import json
import paths
from models.models import User, Offer, Order


def get_json_files(path):
    with open(path, 'r', encoding='UTF-8') as f:
        data = json.load(f)
        return data


def load_user():
    users_list = []
    users = get_json_files(paths.USERS_PATH)
    for row in users:
        user = User(
            id=row.get('id'),
            first_name=row.get('first_name'),
            last_name=row.get('last_name'),
            age=row.get('age'),
            email=row.get('email'),
            role=row.get('role'),
            phone=row.get('phone'),
        )
        users_list.append(user)
    return users_list


def load_offer():
    offers_list = []
    offers = get_json_files(paths.OFFERS_PATH)
    for row in offers:
        offer = Offer(
            id=row.get('id'),
            order_id=row.get('order_id'),
            executor_id=row.get('executor_id'),
        )
        offers_list.append(offer)
    return offers_list


def load_order():
    orders_list = []
    orders = get_json_files(paths.ORDERS_PATH)
    for row in orders:
        order = Order(
            id=row.get('id'),
            name=row.get('name'),
            description=row.get('description'),
            start_date=row.get('start_date'),
            end_date=row.get('end_date'),
            address=row.get('address'),
            price=row.get('price'),
            customer_id=row.get('customer_id'),
            executor_id=row.get('executor_id'),
        )
        orders_list.append(order)
    return orders_list


def make_dict_users(query):
    return {
        'id': query.id,
        'first_name': query.first_name,
        'last_name': query.last_name,
        'age': query.age,
        'email': query.email,
        'role': query.role,
        'phone': query.phone,
    }


def make_dict_orders(query):
    return {
        'id': query.id,
        'name': query.name,
        'description': query.description,
        'start_date': query.start_date,
        'end_date': query.end_date,
        'address': query.address,
        'price': query.price,
        'customer_id': query.customer_id,
        'executor_id': query.executor_id,
    }


def make_dict_offers(query):
    return {
        'id': query.id,
        'order_id': query.order_id,
        'executor_id': query.executor_id,
    }
