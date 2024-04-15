import os
import requests
from urllib.parse import urlparse
from dotenv import load_dotenv


def shorten_link(token, original_url):
    bitly_api_url = "https://api-ssl.bitly.com/v4/bitlinks"
    headers = {
         "Authorization": f"Bearer {token}",
    }
    payload = {"long_url": original_url}
    response = requests.post(bitly_api_url, json=payload, headers=headers)
    response.raise_for_status()
    shortened_info = response.json()["id"]
    return shortened_info


def count_clicks(token, bitlink):
    clicks_summary_url = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary'
    headers = {'Authorization': f"Bearer {token}"}
    click_params = {"units": -1, "unit": "month"}
    response = requests.get(clicks_summary_url,
    params=click_params,
    headers=headers)
    response.raise_for_status()
    total_clicks_info = response.json()
    total_clicks = total_clicks_info.get('total_clicks', 0)
    return total_clicks


def parse_url(original_url):
    parsed_url = urlparse(original_url)
    return f"{parsed_url.netloc}{parsed_url.path}"


def is_bitlink(bitlink, access_token):
    url = f"https://api-ssl.bitly.com/v4/bitlinks/{bitlink}"
    headers = {
        "Authorization": f"Bearer {access_token}",
    }
    response = requests.get(url=url, headers=headers)
    return response.ok


def main():
    access_token = os.getenv('BITLY_TOKEN')
    original_url = input("Введите ссылку для сокращения:")
    parsing_result = parse_url(original_url)
    try:
        if is_bitlink(parsing_result, access_token):
            total_clicks = count_clicks(access_token, parsing_result)
            print(f"Количество кликов: {total_clicks}")
        else:
            shortened_url = shorten_link(access_token, original_url)
            print(f"ссылка: {shortened_url}")
    except Exception as e:
        print(f"Oшибка: {str(e)}")


if __name__ == "__main__":
    load_dotenv()
    main()
