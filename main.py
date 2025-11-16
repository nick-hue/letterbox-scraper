from features import get_by_rating_and_user, get_all_watchlists

def main():

    # get movies from user's watchlists
    users = [
        "loukoumadness",
        "lacost",
        "iouliosp",
        "geezer_jeezer"
    ]
    # get_all_watchlists(users=users)

   # Get movies by rating and user
    username = "nikosfilmakias"
    username = "iouliosp"
    min_rating = 4
    get_by_rating_and_user(username=username, min_rating=min_rating, output_directory="outputs/")

if __name__ == "__main__":
    main()
