from datetime import datetime
import enum
from sqlalchemy import (
    Column, Integer, Enum, Numeric, Text, 
    String, TIMESTAMP, Boolean, DateTime, 
    ForeignKey, ForeignKeyConstraint, UniqueConstraint, CheckConstraint
)
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.orm import relationship
from db.base_class import Base


class GenderType(enum.Enum):
    male = 1
    female = 2

class City(Base):
    __tablename__='city'
    id = Column(Integer, nullable=False, primary_key=True, autoincrement='auto')
    name_city = Column(String(40), nullable=False, unique=True)
    
'''
class Preference(Base):
    __tablename__='preferences'
    id = Column(Integer, nullable=False, primary_key=True, autoincrement='auto')
    title = Column(String(20), nullable=False, unique=True)
'''


class User(Base):
    __tablename__='users'
    id = Column(Integer, nullable=False, primary_key=True, autoincrement='auto')
    login = Column(String(30), nullable=False, unique=True)
    about = Column(Text, nullable=True)
    gender = Column(Enum(GenderType))
    password = Column(String(200), nullable=False)
    id_city = Column(Integer, ForeignKey('city.id'), nullable=True)
    avatar = Column(String, nullable=True)
    email = Column(String, nullable=False, unique=True)



class Hobbies(Base):
    __tablename__ = 'hobbies'
    id = Column(Integer, nullable=False, primary_key=True, autoincrement='auto')

class UserPreferences(Base):
    __tablename__ = 'user_preferences'
    __table_args__ = (CheckConstraint('weight >= 0 AND weight <= 1', name='check_weight'),)
    id = Column(Integer, nullable=False, primary_key=True, autoincrement='auto')
    id_user = Column(Integer, ForeignKey('users.id'))
    id_hobby = Column(Integer, ForeignKey('hobbies.id'))
    weight = Column(Numeric)

class Match(Base):
    __tablename__ = 'matches'
    __table_args__ = (CheckConstraint('id_user1 <> id_user2', name='check_users'),)
    id = Column(Integer, nullable=False, primary_key=True, autoincrement='auto')
    id_user1 = Column(Integer, ForeignKey('users.id'))
    id_user2 = Column(Integer, ForeignKey('users.id'))

#Чаты
#Сделать для многих?
class Chat(Base):
    __tablename__ = 'chats'
    __table_args__= (UniqueConstraint('id_user1', 'id_user2', name='chat_users_unique'),)
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    id_user1 = Column(Integer, ForeignKey('users.id', ondelete='cascade'))
    id_user2 = Column(Integer, ForeignKey('users.id', ondelete='cascade'))
    created_at = Column(TIMESTAMP, default=current_timestamp())

class Message(Base):
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    id_chat = Column(Integer, ForeignKey('chats.id', ondelete='cascade'))
    id_sender = Column(Integer, ForeignKey('users.id', ondelete='cascade'))
    message = Column(Text, nullable=False)
    sent_at = Column(TIMESTAMP, default=current_timestamp())