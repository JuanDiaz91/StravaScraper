import argparse
from core.engine.strava_scraper import StravaScraper
from core.http_client.requests_client import RequestsClient


def main():
    scraper = StravaScraper(RequestsClient())

    parser = argparse.ArgumentParser(description="Strava Scraper CLI")
    parser.add_argument("--ids", nargs='+', type=int, help="Lista de IDs a consultar")
    parser.add_argument("--name", type=str, help="Nombre para buscar usuarios")
    parser.add_argument("--export", action='store_true', help="Exportar resultados a JSON")

    args = parser.parse_args()

    if args.ids:
        users = scraper.get_profiles_by_ids(args.ids)
        for user in users:
            print(user.to_json())
        if args.export:
            scraper.export_users(users=users)

    elif args.name:
        users = scraper.get_users_by_name(args.name)
        for user in users:
            print(user.to_json())
        if args.export:
            scraper.export_users(users=users)

    else:
        print("Debes pasar --ids o --name")


if __name__ == "__main__":
    main()
