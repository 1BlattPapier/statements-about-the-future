import json
import pandas as pd
#import re

class StaticFilter:
    
    '''instantiate with the dataset, which needs to be with columns [rowid, timestamp, text]\n

        filter() returns a dict of style:\n

        text : list of texts
        future : list of integers from {0,1})\n
        0 --> not future related\n
        1 --> future related '''

    ##
    ## load the filter keywords from json file
    ## filter is working as following:
    ## if one of [timerefs] or one of [refs] or [verbs] in so stage1 == 1
    ## for these pass through [stage2]
    # stemming has to be considered due to conjugation

    def __init__(self, dataset):
        with open("keywords.json", "r", encoding="utf8") as f:
            d = json.load(f)
        f.close()
        
        self.stage1 = []
        
        self.stage1.extend( d["stage1"]["timerefs"] )
        self.stage1.extend( d["stage1"]["verbs"] )
        self.stage1.extend( d["stage1"]["refs"] )
        
        self.stage2 = d["stage2"]["stemmed_verbs"]
        
        self.dataset = dataset

    def filter(self):
        # takes the dataset as input and outputs a dictionary {text:future}, where: 
        # 1 for future related
        # 0 for for not future related

        
        df = pd.read_csv(self.dataset)
        texts = df["text"]
        futures = []

        for i in range(len(texts)):
            stage1 = False
            stage2 = False

            for keyword in self.stage1:
                if keyword in texts[i]:
                    stage1 = True
            
            if stage1 == False:
                futures.append[0]
                break

            for keyword in self.stage2:
                if keyword in texts[i]:
                    stage2 = True
            
            if stage1 == True and stage2 == True:
                futures.append[1]

        if len(texts) == len(futures):
            df["tense"] = futures

            dict = {"text" : texts, "tense" : futures}

            return dict
        
        else:
            return {}








