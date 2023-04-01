from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from models import User, Friendship, Post, Base

app = Flask(__name__)
app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app, model_class=Base)

CORS(app)

@app.route("/")
def hello():
    return "Welcome to Flask Application!"

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{'id': user.id, 'email': user.email, 'fname': user.fname, 'lname': user.lname, 'location': user.location, 'image': user.image} for user in users])

@app.route('/friendships', methods=['GET'])
def get_friendships():
    friendships = Friendship.query.all()
    return jsonify([{'id': friendship.id, 'friend1_id': friendship.friend1_id, 'friend2_id': friendship.friend2_id, 'status': friendship.status} for friendship in friendships])

@app.route('/posts', methods=['GET'])
def get_posts():
    posts = Post.query.all()
    return jsonify([{'id': post.id, 'text': post.text, 'author_id': post.author_id, 'recipient_id': post.recipient_id} for post in posts])

@app.route('/users', methods=['POST'])
def add_user():
    email = request.json['email']
    fname = request.json['fname']
    lname = request.json['lname']
    location = request.json['location']
    image = request.json['image']
    user = User(email=email, fname=fname, lname=lname, location=location, image=image)
    db.session.add(user)
    db.session.commit()
    return jsonify({'email': user.email, 'fname': user.fname, 'lname': user.lname, 'location': user.location, 'image': user.image})

@app.route('/friendships', methods=['POST'])
def add_friendship():
    friend1_id = request.json['friend1_id']
    friend2_id = request.json['friend2_id']
    status = request.json['status']
    friendship = Friendship(friend1_id=friend1_id, friend2_id=friend2_id, status=status)
    db.session.add(friendship)
    db.session.commit()
    return jsonify({'friend1_id': friendship.friend1_id, 'friend2_id': friendship.friend2_id, 'status': friendship.status})

@app.route('/posts', methods=['POST'])
def add_post():
    text = request.json['text']
    author_id = request.json['author_id']
    recipient_id = request.json['recipient_id']
    status = request.json['status']
    post = Post(text=text, author_id=author_id, recipient_id=recipient)
    db.session.add(post)
    db.session.commit()
    return jsonify({'text': post.text, 'author_id': post.author_id, 'recipient_id': post.recipient_id})

@app.route('/friendships/<int:friendship_id>', methods=['PUT'])
def update_friendship(friendship_id):
    friendship = Friendship.query.get(friendship_id)
    friendship.friend1_id = request.json['friend1_id']
    friendship.friend2_id = request.json['friend2_id']
    friendship.status = request.json['status']
    db.session.commit()
    return jsonify({'id': friendship.id, 'friend1_id': friendship.friend1_id, 'friend2_id': friendship.friend2_id, 'status': friendship.status})

@app.route('/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    post = Post.query.get(post_id)
    post.text = request.json['text']
    post.author_id = request.json['author_id']
    post.recipient_id = request.json['recipient_id']
    db.session.commit()
    return jsonify({'id': post.id, 'text': post.text, 'author_id': post.author_id, 'recipient_id': post.recipient_id})

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    db.session.delete(user)
    db.session.commit()
    return '', 204

@app.route('/friendships/<int:friendship_id>', methods=['DELETE'])
def delete_friendship(friendship_id):
    friendship = Friendship.query.get(friendship_id)
    db.session.delete(friendship)
    db.session.commit()
    return '', 204

@app.route('/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    post = Post.query.get(post_id)
    db.session.delete(post)
    db.session.commit()
    return '', 204


if __name__ == "__main__":
    app.run(host='0.0.0.0')