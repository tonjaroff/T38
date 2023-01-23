import spacy

def next_movie(description):
    #read in the movies file, and separate by new line
    with open('movies.txt', 'r') as file:
        my_movies = file.read().split("\n")

    #initiliase a comparison variable
    closest_match = ["Movie ?", 0]

    #loop through all the movies and check the descriptions semantic similarity, store the highest result as current highest
    for movie in my_movies:
        this_movie = movie.split(":")

        try:
            desc = this_movie[1]
        except IndexError:
            pass

        #NLP the description parameter for the function and the current description being checked in the loop
        description = nlp(description)
        desc = nlp(desc)
        
        similarity = description.similarity(desc)

        #if the similarity of the current pairing is greater than the current highest, update the highest
        if similarity > closest_match[1]:
            closest_match[0] = this_movie[0]
            closest_match[1] = similarity

    return closest_match[0]


nlp = spacy.load('en_core_web_md')
my_movies = []
hulk = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."

print(next_movie(hulk))

