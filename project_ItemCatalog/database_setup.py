import os, sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine

Base = declarative_base()

#create table to hold users
class User(Base):
    __tablename__ = 'user'

    # column names
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)

    # return as JSON object
    @property
    def serialize(self):
		return {
			'id': self.id,
			'name': self.name,
			'email': self.email
		}

class GameCompany(Base):
    __tablename__ = 'gamecompany'

    # Column names for GameCompany
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User, backref=backref('companies', uselist=True, cascade='delete, all'))

    # return as JSON object
    @property
    def serialize(self):
        return {
            'name': self.name,
            'id': self.id,
        }


class GameConsole(Base):
    __tablename__ = 'gameconsole'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    price = Column(String(8))
    gamecompany_id = Column(Integer, ForeignKey('gamecompany.id'))
    gamecompany = relationship(GameCompany, backref=backref('consoles', uselist=True, cascade='delete, all'))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User, backref=backref('consoles', uselist=True, cascade='delete, all'))

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
        }

engine = create_engine('sqlite:///dbconsolecatalog.db')
Base.metadata.create_all(engine)