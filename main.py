from features import get_by_rating_and_user, get_all_watchlists

def main():

    # get movies from user's watchlists
    users = [
        "loukoumadness",
        "lacost",
        "ioulios",
        "geezer_jeezer"
    ]
    # get_all_watchlists(users=users)

   # Get movies by rating and user
    username = "nikosfilmakias"
    min_rating = 3.5
    get_by_rating_and_user(username=username, min_rating=min_rating, output_directory="outputs/")

if __name__ == "__main__":
    main()
