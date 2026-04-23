from Automations.FileExplorer.MoviesFile import (playMovie, getMovies)

def fileEx(query):
    if "play movie" in query.lower():
        print("Playing movie...")
        playMovie(query)
        
    elif "show" in query.lower() or "show all movies" in query.lower() or "movie list" in query.lower():
        print("Available movies...")
        movies = getMovies()
        for m in movies:
            print(m)

if __name__ == "__main__":
    fileEx("show all")
