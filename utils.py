import csv

def save_movies_to_csv(movies: list[tuple[str, str]], filename: str):
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        for movie in movies:
            print(movie)
            title, year = movie[0][0], movie[0][1]
            rating = movie[1]
            write_list = [title]
            if year != "-":
                write_list.append(year)
            if rating != 0.0:
                write_list.append(rating)
            writer.writerow(write_list)

def extract_movie_title_year(movie_str: str) -> tuple[str, str]:
    # Assuming the movie string is in the format "Title (Year)" or just "Title"
    if "(" in movie_str:
        return movie_str.split(" (")[0].strip(), movie_str.split(" (")[1].strip(")")

    return movie_str.strip(), "-"

def filter_movies(movies: list[tuple[str, float]]) -> list[tuple[str, float]]:
    #remove duplicates and None values, "" from strings
    filtered_movies: list[tuple[str, str]] = []
    seen = set()
    for movie, rating in movies:
        if movie and movie != "None" and movie.strip() != "":
            if movie not in seen:
                filtered_movies.append((extract_movie_title_year(movie), rating))
                seen.add(movie)
    return filtered_movies
