import webbrowser, json
# Movie Object
class Movie:
    def __init__(self, id_movie, name_movie, date, score_ranking, link_movie):
        self.id_movie = id_movie
        self.name_movie = name_movie
        self.date = date
        self.score_ranking = score_ranking
        self.link_movie = link_movie
    #get properties 
    def getId(self):
        return self.id_movie
    def getName(self):
        return self.name_movie
    def getDate(self):
        return self.date
    def getScore(self):
        return self.score_ranking
    def getLink(self):
        return self.link_movie
    
    def show(self):
        print(self.id_movie, "-", self.name_movie, "-", self.date, "-", self.score_ranking, "-", self.link_movie)
    # def update(self, id, name, date, score_ranking, link_movie):
    #     ...
    def open_movie(self):
        webbrowser.open(self.link_movie)


class ListMovie:
    def __init__(self):
        self.list = []
        self.loadAllMovies()
    def getAllMovies(self):
        return self.list
    def add_movie(self, Movie):
        self.list.append(Movie)
        self.saveAllMovies()
    def show_all_movie(self):
        for i in self.list:
            i.show()
    def loadAllMovies(self):
        with open("data/movies.json", "r") as f:
            jsonfile = json.load(f)
            for data in jsonfile:
                self.list.append(Movie(data["id_movie"], data["name_movie"], data["date"], data["score_ranking"], data["link_movie"]))
    def saveAllMovies(self):
        jsonfile = []
        for movie in self.list:
            jsonfile.append(movie.__dict__)
        with open("data/movies.json", 'w') as file:
            json.dump(jsonfile, file, indent=5) 

l  = ListMovie()
l.add_movie(Movie("1","1","1","1","1"))