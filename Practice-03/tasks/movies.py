movies = [
    {
        "name": "Usual Suspects",
        "imdb": 7.0,
        "category": "Thriller"
    },
    {
        "name": "Hitman",
        "imdb": 6.3,
        "category": "Action"
    },
    {
        "name": "Dark Knight",
        "imdb": 9.0,
        "category": "Adventure"
    },
    {
        "name": "The Help",
        "imdb": 8.0,
        "category": "Drama"
    },
    {
        "name": "The Choice",
        "imdb": 6.2,
        "category": "Romance"
    },
    {
        "name": "Colonia",
        "imdb": 7.4,
        "category": "Romance"
    },
    {
        "name": "Love",
        "imdb": 6.0,
        "category": "Romance"
    },
    {
        "name": "Bride Wars",
        "imdb": 5.4,
        "category": "Romance"
    },
    {
        "name": "AlphaJet",
        "imdb": 3.2,
        "category": "War"
    },
    {
        "name": "Ringing Crime",
        "imdb": 4.0,
        "category": "Crime"
    },
    {
        "name": "Joking muck",
        "imdb": 7.2,
        "category": "Comedy"
    },
    {
        "name": "What is the name",
        "imdb": 9.2,
        "category": "Suspense"
    },
    {
        "name": "Detective",
        "imdb": 7.0,
        "category": "Suspense"
    },
    {
        "name": "Exam",
        "imdb": 4.2,
        "category": "Thriller"
    },
    {
        "name": "We Two",
        "imdb": 7.2,
        "category": "Romance"
    }
]


def is_good_movie(movie):
    return movie["imdb"] > 5.5


print(is_good_movie(movies[0]))
print(is_good_movie(movies[8]))

def get_good_movies(movies):
    return [movie for movie in movies if movie["imdb"] > 5.5]


good_movies = get_good_movies(movies)

for movie in good_movies:
    print(movie["name"], movie["imdb"])

def get_movies_by_category(movies, category):
    return [movie for movie in movies if movie["category"] == category]


romance_movies = get_movies_by_category(movies, "Romance")

for movie in romance_movies:
    print(movie["name"], movie["imdb"])

def average_imdb(movies):
    total = sum(movie["imdb"] for movie in movies)
    return total / len(movies)


print("Average IMDb:", average_imdb(movies))

def average_imdb_by_category(movies, category):
    category_movies = [movie for movie in movies if movie["category"] == category]

    if not category_movies:
        return 0

    total = sum(movie["imdb"] for movie in category_movies)

    return total / len(category_movies)


print("Average Romance IMDb:", average_imdb_by_category(movies, "Romance"))