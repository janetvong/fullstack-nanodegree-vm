import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

#class User(Base):
#    __tablename__ = 'user'
#
#    id = Column(Integer, primary_key=True)
#    name = Column(String(250), nullable=False)
#    email = Column(String(250), nullable=False)
#    picture = Column(String(250))


# sport table
class Sport(Base):
    __tablename__ = 'sport'

    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
#    user_id = Column(Integer, ForeignKey('user.id'))
#    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
         }

# sport item table
# inside CatalogItem class
class CatalogItem(Base):
    __tablename__ = 'catalog_item'

    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    description = Column(String(2000))
    sport_id = Column(Integer, ForeignKey('sport.id'))
    sport = relationship(Sport)
#    user_id = Column(Integer, ForeignKey('user.id'))
#    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
            'description': self.description,
            'sport_id': self.sport_id,
            'sport': self.sport.serialize,
        }

engine = create_engine('sqlite:///sportcatalog.db') ## create an instance of our create_engine class and point to the database we will use.

Base.metadata.create_all(engine) ## goes into the database and adds the classes we will soon create as new tables in our database.
