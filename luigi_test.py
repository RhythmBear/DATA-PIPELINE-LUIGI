import luigi
import requests
import json


class StockTwitScrape(luigi.Task):

    def output(self):
        return luigi.LocalTarget("raw_data.json")
    
    def run(self):
        url = "https://api.stocktwits.com/api/2/streams/symbol/wy.json"
        response = requests.get(url=url).text
        
        with self.output().open("w") as f:
            json.dump(json.JSONDecoder().decode(response), f)