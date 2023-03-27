from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

CORS(app)


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Item {self.name}>'

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    author = db.Column(db.String(50))
    genre = db.Column(db.String(50))
    year = db.Column(db.String(50))
    image = db.Column(db.String(50))
    review = db.Column(db.String(50))
    owner = db.Column(db.String(50))

    def __repr__(self):
        return f'<Book {self.title}>'

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50))
    fname = db.Column(db.String(50))
    lname = db.Column(db.String(50))
    location = db.Column(db.String(50))
    image = db.Column(db.String(50))

    def __repr__(self):
        return f'<User {self.email}>'

class Friendship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    friend1 = db.Column(db.String(50))
    friend2 = db.Column(db.String(50))
    status = db.Column(db.String(50))

    def __repr__(self):
        return f'<Friendship {self.id}>'

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(50))
    author = db.Column(db.String(50))
    recipient = db.Column(db.String(50))

    def __repr__(self):
        return f'<Post {self.id}>'

@app.route("/")
def hello():
    return "Welcome to Flask Application!"
if __name__ == "__main__":
    app.run(host='0.0.0.0')

@app.route('/items', methods=['GET'])
def get_items():
    items = Item.query.all()
    return jsonify([{'id': item.id, 'name': item.name} for item in items])

@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([{'id': book.id, 'title': book.title, 'author': book.author, 'genre': book.genre, 'year': book.year, 'image': book.image, 'review': book.review, 'owner': book.owner} for book in books])

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{'id': user.id, 'fname': user.fname, 'lname': user.lname, 'location': user.location, 'image': user.image} for user in users])

@app.route('/friendships', methods=['GET'])
def get_friendships():
    friendships = Friendship.query.all()
    return jsonify([{'id': friendship.id, 'friend1': friendship.friend1, 'friend2': friendship.friend2, 'status': friendship.status} for friendship in friendships])

@app.route('/posts', methods=['GET'])
def get_posts():
    posts = Post.query.all()
    return jsonify([{'id': post.id, 'text': post.text, 'author': post.author, 'recipient': post.recipient} for post in posts])

@app.route('/items', methods=['POST'])
def add_item():
    name = request.json['name']
    item = Item(name=name)
    db.session.add(item)
    db.session.commit()
    return jsonify({'id': item.id, 'name': item.name})

@app.route('/friendships', methods=['POST'])
def add_friendship():
    friend1 = request.json['friend1']
    friend2 = request.json['friend2']
    status = request.json['status']
    friendship = Friendship(friend1=friend1, friend2=friend2, status=status)
    db.session.add(friendship)
    db.session.commit()
    return jsonify({'id': friendship.id, 'friend1': friendship.friend1, 'friend2': friendship.friend2, 'status': friendship.status})

@app.route('/posts', methods=['POST'])
def add_post():
    friend1 = request.json['friend1']
    friend2 = request.json['friend2']
    status = request.json['status']
    friendship = Friendship(friend1=friend1, friend2=friend2, status=status)
    db.session.add(friendship)
    db.session.commit()
    return jsonify({'id': friendship.id, 'friend1': friendship.friend1, 'friend2': friendship.friend2, 'status': friendship.status})

@app.route('/books', methods=['POST'])
def add_book():
    title = request.json['title']
    author = request.json['author']
    genre = request.json['genre']
    year = request.json['year']
    image = request.json['image']
    review = request.json['review']
    owner = request.json['owner']
    book = Book(title=title, author=author, genre=genre, year=year, image=image, review=review, owner=owner)
    db.session.add(book)
    db.session.commit()
    return jsonify({'id': book.id, 'title': book.title, 'author': book.author, 'genre': book.genre, 'year': book.year, 'image': book.image, 'review': book.review, 'owner': book.owner})

@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = Item.query.get(item_id)
    item.name = request.json['name']
    db.session.commit()
    return jsonify({'id': item.id, 'name': item.name})

@app.route('/friendships/<int:friendship_id>', methods=['PUT'])
def update_friendship(friendship_id):
    friendship = Friendship.query.get(friendship_id)
    friendship.friend1 = request.json['friend1']
    friendship.friend2 = request.json['friend2']
    friendship.friend2 = request.json['friend2']
    db.session.commit()
    return jsonify({'id': friendship.id, 'friend1': friendship.friend1, 'friend2': friendship.friend2, 'status': friendship.status})

@app.route('/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    post = Post.query.get(post_id)
    post.text = request.json['text']
    post.author = request.json['author']
    post.recipient = request.json['recipient']
    db.session.commit()
    return jsonify({'id': post.id, 'text': post.text, 'author': post.author, 'recipient': post.recipient})

@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = Item.query.get(item_id)
    db.session.delete(item)
    db.session.commit()
    return '', 204

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