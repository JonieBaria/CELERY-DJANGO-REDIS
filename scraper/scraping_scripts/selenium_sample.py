from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BBCScraper:
    def __init__(self, headless=True):
        options = Options()
        if headless:
            options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Chrome(options=options)

    def scrape(self):
        """Scrape top stories from BBC News"""
        self.driver.get("https://www.bbc.com/news")

        # wait for headlines to load
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "h2"))
        )

        headlines = self.driver.find_elements(By.CSS_SELECTOR, "h2")
        results = [h.text for h in headlines[:10] if h.text.strip()]

        print("BBC Headlines:", results)
        return results

    def close(self):
        self.driver.quit()


def main():
    scraper = BBCScraper()
    try:
        return scraper.scrape()
    finally:
        scraper.close()


if __name__ == "__main__":
    main()
