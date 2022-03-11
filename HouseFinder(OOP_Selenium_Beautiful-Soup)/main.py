from house_finder import HouseFinder
from savedata import SaveData
from showexcel import ShowExcel

houses = HouseFinder()
links = houses.get_links()
addresses = houses.get_adresses()
prices = houses.get_prices()

for i in range(len(links)):
    save_data = SaveData(links[i], addresses[i], prices[i])
    save_data.import_data()

show = ShowExcel()
