import requests
from bs4 import BeautifulSoup

def scrape_headlines(url, output_file="headlines.txt"):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            print(f"Failed to fetch page, status code: {response.status_code}")
            return

        soup = BeautifulSoup(response.text, "html.parser")

        # Extract <h2> tags (commonly used for news headlines)
        headlines = soup.find_all("h2")

        with open(output_file, "w", encoding="utf-8") as f:
            for idx, headline in enumerate(headlines, 1):
                text = headline.get_text(strip=True)
                if text:
                    f.write(f"{idx}. {text}\n")

        print(f"✅ Headlines saved successfully in {output_file}")

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    news_url = "https://www.bbc.com/news"   # Example news site
    scrape_headlines(news_url)
