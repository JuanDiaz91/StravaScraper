from bs4 import BeautifulSoup
from models import UserProfile


def extract_user_profile(resp_text: str, user_id: int) -> UserProfile:
    soup = BeautifulSoup(resp_text, "html.parser")

    name_tag = soup.select_one("h1.athlete-name")
    location_tag = soup.select_one("div.location")
    desc_tag = soup.select_one("#athlete-description .description-content p")
    image_tag = soup.select_one("img.avatar-img")

    return UserProfile(
        id=user_id,
        name=name_tag.get_text(strip=True) if name_tag else None,
        location=location_tag.get_text(strip=True) if location_tag else None,
        image_url=image_tag["src"] if image_tag else None,
        description=desc_tag.get_text(strip=True) if desc_tag else None
    )


def extract_users_list(resp_text: str) -> list[UserProfile]:
    soup = BeautifulSoup(resp_text, "html.parser")
    users = []

    rows = soup.select("ul.athlete-search > li.row")

    for row in rows:
        name_tag = row.select_one("a.athlete-name-link")
        location_tag = row.select_one("div.location")
        image_tag = row.select_one("img.avatar-img")

        if not name_tag:
            continue

        user_id = int(name_tag["href"].split("/")[-1])
        full_name = name_tag.get_text(strip=True)
        location = location_tag.get_text(strip=True) if location_tag else None
        image_url = image_tag["src"] if image_tag else None

        users.append(UserProfile(
            id=user_id,
            name=full_name,
            location=location,
            image_url=image_url,
        ))

    return users


def extract_pagination_user_list(resp_text: str) -> int:
    soup = BeautifulSoup(resp_text, "html.parser")
    pages = [int(link.get_text()) for link in soup.select("ul.pagination li a") if link.get_text().isdigit()]

    return max(pages) if pages else 1
