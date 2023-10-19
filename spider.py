
import requests
import yaml
import re
import json
import logging

logger = logging.getLogger("global")

class WebDataFlow:
    def __init__(self,url,conference,year):
        self.url = url
        self.text = None
        self.conference = conference
        self.year = year
        # self.titles = None
        
    def __call__(self):
        self.get_web()
        return self.extrat_titles()

    def get_web(self):
        r = requests.get(self.url)
        self.text = r.text

    
    def extrat_titles(self):
        if self.conference ==  "ACL":
            if self.year in [2023,2021]:
                titles = re.findall("<strong>(.{21,})</strong>",self.text)
            elif self.year == 2020:
                titles = re.findall("<p><b>(.{21,})</b><br />",self.text)
            elif self.year == 2019:
                text = json.loads(self.text)
                titles = [t["info"]["title"] for t in text["result"]["hits"]["hit"]]
        elif self.conference ==  "EMNLP":
            if self.year in [2022]:
                titles = re.findall("<strong><a class=align-middle href=/2022.emnlp-main.\d*/>(.{21,})</a></strong>",self.text)
            elif self.year in [2021]:
                titles = re.findall("<strong>(.{21,})</strong>",self.text)
            elif self.year in [2020]:
                titles = re.findall("<span class=\"paper-title\">(.*?)</span>",self.text)
            elif self.year in [2019]:
                titles = re.findall("<span style=\"color:cornflowerblue\">(.*?)</span>",self.text)
        
        logger.info(f"Get {len(titles)} papers.")
        # logger.info(titles)
        return titles
        
if __name__ == "__main__":
    with open("conference_list.yaml") as f:
        config = yaml.safe_load(f)
    # r = requests.get(config["ACL_2023_main"])
    # text = re.findall("<strong>(.{21,})</strong>",r.text)
    # print(text[0],text[-1])
    workflow = WebDataFlow(config["ACL_2023_main"],ACL.extract_2023)
    titles = workflow()
    