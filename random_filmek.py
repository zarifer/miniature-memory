import random

movies = [
    "the incantation",
    "Dawn of the beast",
    "Ouja the final game",
    "The woman in black",
    "Shutter (az eredeti)",
    "Devil (2010)",
    "Smile",
    "The exorcist (original)",
    "It follows",
    "Drag me to Hell",
    "The Eye",
    "Hellhole",
    "The Whole truth",
    "The 8th night",
    "Gerald’s game",
    "The bridge curse",
    "Home for rent",
    "Terrifier",
    "Aftermath",
    "Invisible man",
    "Margaux"
]

selected_movies = random.sample(movies, 3)

for movie in selected_movies:
    print(movie)
