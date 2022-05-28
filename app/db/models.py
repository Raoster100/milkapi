from sqlalchemy import Column, String, DateTime, Boolean, ForeignKey, Integer
from sqlalchemy.dialects.mssql.base import MSMoney

from sqlalchemy.orm import relationship

from misc import Base


class UsersModel(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(40))
    telegram_id = Column(Integer)
    telegram_login = Column(String)


class CatalogsModel(Base):
    __tablename__ = "catalogs"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(40))


class ProductsModel(Base):
    __tablename__ = "Products"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    description = Column(String)
    price = Column(MSMoney)
    available = Column(Integer)
    catalog_id = relationship('CatalogsModel', ForeignKey='catalogs.id')


class SalesModel(Base):
    __tablename__ = "Sales"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    buyer_id = relationship('UsersModel', ForeignKey='Users.id')
    product_id = relationship('ProductsModel', ForeignKey='Products.id')


class DeliveryModel(Base):
    __tablename__ = "Delivery"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    street = Column(String)
    house_number = Column(String)
    date = Column(DateTime)
    sale_id = relationship('SalesModel', ForeignKey='Sales.id')
