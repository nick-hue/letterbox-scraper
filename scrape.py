from bs4 import BeautifulSoup
import requests

def get_users_watchlist(user: str = "") -> list[tuple[str, float]]:
    if not user:
        raise ValueError("Username must be provided")
    
    base_url = f"https://letterboxd.com/{user}/watchlist/"

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0 Safari/537.36"
        )
    }

    # If you need to be logged in, add your cookie here (example):
    # cookies = {"letterboxd_session": "YOUR-SESSION-HERE"}
    # and then pass cookies=cookies to requests.get(...)
    cookies = None

    movies: list[str] = []
    page = 1
    max_pages = 100  # safety guard

    while page <= max_pages:
        if page == 1:
            page_url = base_url
        else:
            # watchlist pagination looks like /watchlist/page/2/
            if base_url.endswith("/"):
                page_url = f"{base_url}page/{page}/"
            else:
                page_url = f"{base_url}/page/{page}/"

        resp = requests.get(page_url, headers=headers, cookies=cookies)
        if resp.status_code == 404:
            print("Got 404, stopping.")
            break

        soup = BeautifulSoup(resp.text, "html.parser")
        grid_items = soup.select("li.griditem")

        if not grid_items:
            # No more films on this page → done
            break

        for li in grid_items:
            comp = li.select_one("div.react-component")
            if not comp:
                continue

            title = comp.get("data-item-name") or comp.get("data-item-full-display-name")
            if title:
                movies.append((title.strip(), 0.0))  # Watchlist movies have no rating

        page += 1

    return movies


def get_movies_by_rating(username: str = "", rating: float = 0.0) -> list[tuple[str, float]]:
    base_url = f"https://letterboxd.com/{username}/films/rated/{rating}/"

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0 Safari/537.36"
        )
    }

    # If you need to be logged in, add your cookie here (example):
    # cookies = {"letterboxd_session": "YOUR-SESSION-HERE"}
    # and then pass cookies=cookies to requests.get(...)
    cookies = None

    movies: list[str] = []
    page = 1
    max_pages = 100  # safety guard

    while page <= max_pages:
        if page == 1:
            page_url = base_url
        else:
            # watchlist pagination looks like /watchlist/page/2/
            if base_url.endswith("/"):
                page_url = f"{base_url}page/{page}/"
            else:
                page_url = f"{base_url}/page/{page}/"

        resp = requests.get(page_url, headers=headers, cookies=cookies)
        if resp.status_code == 404:
            print("Got 404, stopping.")
            break

        soup = BeautifulSoup(resp.text, "html.parser")
        grid_items = soup.select("li.griditem")

        if not grid_items:
            # No more films on this page → done
            break

        for li in grid_items:
            comp = li.select_one("div.react-component")
            if not comp:
                continue

            title = comp.get("data-item-name") or comp.get("data-item-full-display-name")
            if title:
                movies.append((title.strip(), rating))

        page += 1

    return movies