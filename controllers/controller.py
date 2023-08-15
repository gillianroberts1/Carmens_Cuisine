from flask import render_template, Blueprint
from models.orders import orders


orders_blueprint = Blueprint("orders", __name__)

@orders_blueprint.route("/")
def index():
    return render_template("index.html", title="Carmens Cuisine", orders=orders)

@orders_blueprint.route("/orders")
def orders():
    return render_template("orders.html", title="Carmens Cuisine", orders=orders)

@orders_blueprint.route("/orders/<index>")  #code for viewing single order url/items/<index position of order>
def show(index):
    chosen_order = orders[int(index)]  # as it extracted as a str it needs converting to Int

    return render_template("orders.html", order=chosen_order)  #whatever item is aateched to chosen_order will be returned