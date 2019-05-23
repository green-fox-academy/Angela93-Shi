movie_dict = {}

movie_list = [
    {
        "id":1,
        "title":"Glass",
        "year": 1987,
        "description":"Security guard David Dunn uses his supernatural abilities to track Kevin Wendell Crumb, a disturbed man who has twenty-four personalities."
    },
    {
        "id":2,
        "title":"The Kid Who Would Be King",
        "year": 1990,
        "description":"A band of kids embark on an epic quest to thwart a medieval menace."
    },
    {
        "id":3,
        "title":"Miss Bala",
        "year": 2005,
        "description":"Gloria finds a power she never knew she had when she is drawn into a dangerous world of cross-border crime. Surviving will require all of her cunning, inventiveness, and strength. Based on the Spanish-language film."
    },
    {
        "id":4,
        "title":"The Lego Movie 2: The Second Part",
        "year": 2010,
        "description":"It's been five years since everything was awesome and the citizens are facing a huge new threat: Lego Duplo invaders from outer space, wrecking everything faster than they can rebuild."
    },
    {
        "id":5,
        "title":"What Men Want",
        "year": 2010,
        "description":"A woman is boxed out by the male sports agents in her profession, but gains an unexpected edge over them when she develops the ability to hear men's thoughts."
    },
]

for movie in movie_list:
    movie_dict['id'] = movie['id']
    movie_dict['title'] = movie['title']
    movie_dict['year'] = movie['year']
    movie_dict['description'] = movie['description']
    print(movie_dict)