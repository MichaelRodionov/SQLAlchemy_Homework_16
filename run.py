from flask import Flask
from models.models import db
import utils as u
from app.users.views import users_blueprint
from app.offers.views import offers_blueprint
from app.orders.views import orders_blueprint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
db.init_app(app)


# creating IMDB and filling up
with app.app_context():
    db.create_all()
    with db.session.begin():
        db.session.add_all(u.load_user())
        db.session.add_all(u.load_offer())
        db.session.add_all(u.load_order())
        db.session.commit()


# Register blueprints
app.register_blueprint(users_blueprint)
app.register_blueprint(offers_blueprint)
app.register_blueprint(orders_blueprint)


# 400 error handler
@app.errorhandler(404)
def get_404_error(error):
    return '404 Error'


# 500 error handler
@app.errorhandler(500)
def get_404_error(error):
    return '404 Error'


if __name__ == '__main__':
    app.run(debug=True)
