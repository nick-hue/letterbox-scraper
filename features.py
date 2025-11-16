from scrape import get_users_watchlist, get_movies_by_rating
from utils import save_movies_to_csv, filter_movies

def get_by_rating_and_user(username: str, min_rating: float, output_directory:str ="outputs/") -> list[tuple[str, str]]:
    # This function will filter movies by user and minimum rating
    print(f"Preparing to scrape [{username}] movies with rating >= {min_rating}.")
    ratings = [x / 10.0 for x in range(int(min_rating * 10), 55, 5)]
    print(ratings)
    movies: list[str] = []

    for rating in ratings:
        movies.extend(get_movies_by_rating(username=username, rating=rating))

    filtered_movies = filter_movies(movies)
    output_path = f"{output_directory}letterboxd_watchlist_{username}_{min_rating}.csv"
    save_movies_to_csv(filtered_movies, output_path)
    print(f"Movies of user: [{username}] with rating >= {min_rating} saved on {output_path}")

def get_all_watchlists(users: list[str] = [], output_directory:str ="outputs/") -> None:
    # This function is a placeholder for any setup needed before scraping watchlists
    print("Preparing to scrape provided users' watchlists.")
    
    all_movies = []

    for user in users:  
        all_movies.extend(get_users_watchlist(user=user))

    filtered_movies = filter_movies(all_movies)
    output_path = f"{output_directory}letterboxd_watchlist.csv"
    save_movies_to_csv(filtered_movies, output_path)
    print("All watchlists of users: {} saved on .".format(", ".join(users)), output_path)