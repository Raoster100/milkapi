from sqlalchemy import Column, String, DateTime, Integer, ForeignKey, Numeric

from sqlalchemy.orm import relationship

from misc import Base


class UsersModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(40))
    telegram_id = Column(Integer)
    telegram_login = Column(String)
    password = Column(String)


class CatalogsModel(Base):
    __tablename__ = "catalogs"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(40))


class ProductsModel(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    description = Column(String)
    price = Column(Numeric)
    available = Column(Integer)
    catalog_id = Column(Integer, ForeignKey('catalogs.id'))
    catalog = relationship("CatalogsModel", lazy='joined')


class SalesModel(Base):
    __tablename__ = "sales"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    buyer_id = Column(Integer, ForeignKey('users.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    buyer = relationship("UsersModel", lazy='joined')
    product = relationship("ProductsModel", lazy='joined')


class DeliveryModel(Base):
    __tablename__ = "delivery"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    street = Column(String)
    house_number = Column(String)
    date = Column(DateTime)
    sale_id = Column(Integer, ForeignKey('sales.id'))
    sale = relationship("SalesModel", lazy='joined')
