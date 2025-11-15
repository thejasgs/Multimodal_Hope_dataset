import pandas as pd

SD = pd.read_csv('SD_Img.csv')
DE = pd.read_csv('De_Img.csv')
HP = pd.read_csv('HP_Img.csv')

sample1 = SD.sample(n=200, random_state=42)
sample2 = DE.sample(n=200, random_state=42)
sample3 = HP.sample(n=200, random_state=42)

conc = pd.concat([sample1,sample2, sample3],ignore_index=True)

conc = conc[["image"]]

conc['An1'] = ""
conc['An2'] = ""

conc.to_csv("Combined_Images_IRR.csv", index=False)