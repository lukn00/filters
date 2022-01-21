import pandas as pd
import glob
from tqdm import tqdm
import argparse

def get_zip(phone):
    
    phone = str(phone)[0 : 6]
    
    ziplist = pd.read_csv('area_to_zip.csv')
    
    # print('Zip Lookup...')
    found_zip = '#N/A'
    for i , row in ziplist.iterrows():
        area_code = row['Area Code']
        zip_code = row['Zip Code']
        
        if phone in str(area_code):
            found_zip = zip_code
            break
    return(found_zip)

