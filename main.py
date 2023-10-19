import datetime
import logging
import yaml
import argparse


from process import TextProcessor
from spider import *


def init_logger(logger_name="global"):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)

    # Formatter
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # StreamHandler for console
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    # FileHandler for output to a file
    current_time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    fh = logging.FileHandler(f'./logs/{current_time}.log')
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    
    return logger

def run_single(args,config):
    if args.track != "null":
        index = f"{args.conference}_{args.year}_{args.track}"
    else:
        index = f"{args.conference}_{args.year}"
        
    logger.info(f"Task: {index}")
    if index not in config:
        logger.error("No conference matched. Please check your input.")
        return
        # raise IndexError("Check your input of 'conference', 'year' and 'track'")

    workflow = WebDataFlow(config[index],args.conference,args.year)
    titles = workflow()
    
    processor = TextProcessor()
    wordcloud_img = processor.process_titles(titles)
    
    wordcloud_img.to_file(f"figs/{index}.png")

if __name__ == "__main__":
    
    init_logger()
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--conference","-c",type=str)
    parser.add_argument("-y","--year", type=int)
    parser.add_argument("--track", choices=["finding","main","null"],default="null")
    parser.add_argument("--all", action='store_true')
    args = parser.parse_args()
    
    with open("conference_list.yaml") as f:
        config = yaml.safe_load(f)
        
    r = requests.get(config["ACL_2020"])
    # # titles = re.findall("<strong><a class=align-middle href=/2022.emnlp-main.\d*?/>(.{21,})</a></strong>",r.text)
    # # text = re.findall("<strong>(.{21,})</strong>",r.text)
    # # print(titles[0],titles[-1])
    # with open("text.txt","w") as f:
    #     f.write(r.text)
    # # print(len(titles),titles[0])
    if args.all:
        for conference in ["ACL","EMNLP"]:
            for year in [2023,2022,2021,2020,2019]:
                args.conference = conference
                args.year = year
                if conference == "ACL" and year == 2023:
                    for track in ["finding","main"]:
                        args.track = track
                        run_single(args,config)
                else:
                    args.track = "null"
                    run_single(args,config)
    else:
        run_single(args,config)
 