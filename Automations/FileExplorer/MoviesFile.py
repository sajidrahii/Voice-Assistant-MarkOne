import os

movies_file_path = r"F:\Movies\Temp Movies and Web Series"
formats = [".mkv", ".mp4", "avi"]
movies = []

def getMovies():
    for movie in os.listdir(movies_file_path):
        if any(f in movie for f in formats):
            movies.append(movie.lower())
            
    return movies

def playMovie(query):
    getMovies()
    
    movie_name = query.replace("play movie name", "").replace("play movie", "").replace("play", "").strip()

    for movie_get_name in movies:
        if movie_name.lower() in movie_get_name.lower():
            
            movie_path = os.path.join(movies_file_path, movie_get_name)

            if os.path.isfile(movie_path):
                try:
                    print(f"Playing {movie_name}")
                    os.startfile(movie_path)
                    return True
                
                except Exception as e:
                    print(f"Failed to play the movie: {e}")
                    return False
            else:
                print("Movie file does not exist.")
                return False

    print("Movie not found in the list.")
    return False

if __name__ == "__main__":

    while True:
        a = input(": ")
        if "movie" in a.lower() or "play movie" in a.lower():
            playMovie(a)
        
        elif a == "x":
            exit()

    
    
            