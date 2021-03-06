from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint, jsonify, request
from flask_cors import CORS

main = Blueprint('main', __name__)
app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    rating = db.Column(db.Integer)


@app.route('/add_movie', methods=['POST'])
def add_movie():
    movie_data = request.get_json()
    new_movie = Movie(title=movie_data['title'], rating=movie_data['rating'])
    db.session.add(new_movie)
    db.session.commit( )
    return 'Done', 201


@app.route('/movie', methods=['GET'])
def movies():
    movies_list = Movie.query.all()
    movies = []
    for movie in movies_list:
        movies.append({'title': movie.title, 'rating': movie.rating})
    return jsonify({'movies': movies})


if __name__ == '__main__':
    app.run(debug=True, port=8080)
