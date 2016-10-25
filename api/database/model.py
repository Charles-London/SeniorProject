# A SQLAlchemy Model for the Database
# Generated from the existing DDL with `sqlacodegen` tool
# With some hand modifications
# The only need to touch this file is if any DDLs need to be written
# TODO: Check into using Alembic for database migrations here

from sqlalchemy import Boolean, Column, Date, ForeignKey, Integer, Text, text
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy

# useful link: http://stackoverflow.com/questions/9692962/flask-sqlalchemy-import-context-issue/9695045#9695045
db = SQLAlchemy()

class Allergen(db.Model):
    __tablename__ = 'allergens'

    product_id = Column(ForeignKey(u'product.product_id'), primary_key=True, nullable=False, server_default=text("nextval('allergens_product_id_seq'::regclass)"))
    allergy_type = Column(Text, primary_key=True, nullable=False)

    product = relationship(u'Product')


class Baker(db.Model):
    __tablename__ = 'baker'

    baker_id = Column(Integer, primary_key=True, server_default=text("nextval('baker_baker_id_seq'::regclass)"))
    baker_fname = Column(Text, nullable=False)
    baker_lname = Column(Text, nullable=False)
    baker_email = Column(Text, nullable=False)
    baker_phone = Column(Text, nullable=False)
    baker_password = Column(Text, nullable=False)
    bakerpaypal_id = Column(Text, nullable=False)
    baker_license = Column(Text, nullable=False)


class Bakery(db.Model):
    __tablename__ = 'bakery'

    bakery_id = Column(Integer, primary_key=True, server_default=text("nextval('bakery_bakery_id_seq'::regclass)"))
    baker_id = Column(ForeignKey(u'baker.baker_id'), nullable=False)
    bakery_name = Column(Text, nullable=False)
    bakery_address = Column(Text, nullable=False)
    bakery_offline = Column(Boolean, nullable=False)
    close_time = Column(Text, nullable=False)
    open_time = Column(Text, nullable=False)
    delivery = Column(Integer, nullable=False)
    phone_number = Column(Text, nullable=False)

    baker = relationship(u'Baker')


class Bakeryfeedback(db.Model):
    __tablename__ = 'bakeryfeedback'

    bakery_id = Column(ForeignKey(u'bakery.bakery_id'), primary_key=True, nullable=False, server_default=text("nextval('bakeryfeedback_bakery_id_seq'::regclass)"))
    user_id = Column(ForeignKey(u'users.user_id'), primary_key=True, nullable=False)
    entry = Column(Text, nullable=False)
    feedback_date = Column(Date, nullable=False)

    bakery = relationship(u'Bakery')
    user = relationship(u'User')


class HelloWorld(db.Model):
    __tablename__ = 'hello_world'

    some_stuff = Column(Text, primary_key=True)


class OrderContent(db.Model):
    __tablename__ = 'order_content'

    order_id = Column(ForeignKey(u'orders.order_id'), primary_key=True, nullable=False, server_default=text("nextval('order_content_order_id_seq'::regclass)"))
    product_id = Column(ForeignKey(u'product.product_id'), primary_key=True, nullable=False)
    quantity = Column(Integer, nullable=False)

    order = relationship(u'Order')
    product = relationship(u'Product')


class Order(db.Model):
    __tablename__ = 'orders'

    order_id = Column(Integer, primary_key=True, server_default=text("nextval('orders_order_id_seq'::regclass)"))
    user_id = Column(ForeignKey(u'users.user_id'), nullable=False)
    status = Column(Integer, nullable=False)
    order_date = Column(Date, nullable=False)
    order_address = Column(Text, nullable=False)

    user = relationship(u'User')


class Product(db.Model):
    __tablename__ = 'product'

    product_id = Column(Integer, primary_key=True, server_default=text("nextval('product_product_id_seq'::regclass)"))
    bakery_id = Column(ForeignKey(u'bakery.bakery_id'), nullable=False)
    pname = Column(Text, nullable=False)
    price = Column(Text, nullable=False)
    picture = Column(Text, nullable=False)
    description = Column(Text, nullable=False)
    product_type = Column(Text, nullable=False)

    bakery = relationship(u'Bakery')


class Rating(db.Model):
    __tablename__ = 'rating'

    product_id = Column(ForeignKey(u'product.product_id'), primary_key=True, nullable=False, server_default=text("nextval('rating_product_id_seq'::regclass)"))
    user_id = Column(ForeignKey(u'users.user_id'), primary_key=True, nullable=False)
    entry = Column(Text)
    rating_value = Column(Integer, nullable=False)
    rating_date = Column(Date, nullable=False)

    product = relationship(u'Product')
    user = relationship(u'User')


class User(db.Model):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, server_default=text("nextval('users_user_id_seq'::regclass)"))
    user_fname = Column(Text, nullable=False)
    user_lname = Column(Text, nullable=False)
    saved_address = Column(Text)
    user_email = Column(Text, nullable=False)
    user_phone = Column(Text, nullable=False)
    user_password = Column(Text, nullable=False)
    userpaypal_id = Column(Text, nullable=False)