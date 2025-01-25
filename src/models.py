import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(10), nullable=False)
    email = Column(String(20), nullable=False) 
    pasword = Column(String(10), nullable=False )

class Seguidores(Base):
    __tablename__ = 'seguidores'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    me_sigue = Column(Integer, ForeignKey(Usuario.id)) 
    lo_sigo = Column(Integer, ForeignKey(Usuario.id))
    person_id = Column(Integer, ForeignKey('Usuario_id'))
    user = relationship('Usuario')

class Post(Base):
    __tablename__ = 'post'
    id = Column (Integer, primary_key=True)
    titulo = Column(String(50), nullable=False)
    contenido = Column(String(100), nullable=False)
    autor_id = Column(Integer, ForeignKey(Usuario.id), nullable=False)

class Comentarios(Base):
    __tablename__ = 'comentarios'
    id = Column (Integer, primary_key=True)
    contenido = Column (String(250), nullable=False)
    usuario_id = Column(Integer, ForeignKey(Usuario.id), nullable=False)
    post_id = Column(Integer, ForeignKey(Post.id), nullable=False)

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    url = Column(String(250), nullable=False)
    tipo= Column(String(50), nullable=False)
    post_id= Column(Integer, ForeignKey(Post.id))


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
