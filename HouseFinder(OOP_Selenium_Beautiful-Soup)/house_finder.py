from bs4 import BeautifulSoup
import requests

ZILLOW_URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"

headers = {
            "User-Agent": "your headers info",
            "Accept-Language": "your headers info"
}


class HouseFinder:
    def __init__(self):
        response = requests.get(url=ZILLOW_URL, headers=headers)
        web_page = response.text
        self.soup = BeautifulSoup(web_page, "html.parser")
        self.final_links = []

    def get_links(self):
        links = self.soup.select(".list-card-top a")
        for link in links:
            href = link['href']
            if "http" not in href:
                self.final_links.append(f"https://www.zillow.com{href}")
            else:
                self.final_links.append(href)
        return self.final_links

    def get_adresses(self):
        addresses_list = self.soup.select(".list-card-addr")
        final_addresses = [adress.getText().split(" | ")[-1] for adress in addresses_list]
        return final_addresses

    def get_prices(self):
        final_prices = []
        prices_list = self.soup.select(".list-card-price")
        clear_prices_list = [price.getText() for price in prices_list]
        for price in clear_prices_list:
            clear_price = ""
            if "+" in price:
                clear_price = price.split("+")[0]
            elif "/" in price:
                clear_price = price.split("/")[0]
            final_prices.append(clear_price)
        return final_prices


