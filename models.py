from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String())
    fname = Column(String())
    lname = Column(String())
    location = Column(String())
    image = Column(String())

    def __repr__(self):
        return f'<User {self.id}>'

class Friendship(Base):
    __tablename__ = 'friendships'

    id = Column(Integer, primary_key=True)
    friend1_id = Column(Integer, ForeignKey('users.id'))
    friend1 = relationship('User', foreign_keys=[friend1_id], backref=backref('friend1'))
    friend2_id = Column(Integer, ForeignKey('users.id'))
    friend2 = relationship('User', foreign_keys=[friend2_id], backref=backref('friend2'))
    status = Column(String())

    def __repr__(self):
        return f'<Friendship {self.id}>'

class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    text = Column(String())
    author_id = Column(Integer, ForeignKey('users.id'))
    author = relationship('User', foreign_keys=[author_id], backref=backref('author'))
    recipient_id = Column(Integer, ForeignKey('users.id'))
    recipient = relationship('User', foreign_keys=[recipient_id], backref=backref('recipient'))

    def __repr__(self):
        return f'<Post {self.id}>'

if __name__ == '__main__':
    engine = create_engine('sqlite:///data.db')
    Base.metadata.create_all(engine)