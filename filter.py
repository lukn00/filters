import pandas as pd
import glob
from tqdm import tqdm
import argparse

def get_zip(phone):
    
    phone = str(phone)[0 : 6]
    
    ziplist = pd.read_csv('/home/antide/angi/bots/filters/area_to_zip.csv')
    
    # print('Zip Lookup...')
    found_zip = '#N/A'
    for row in ziplist.itertuples(index=False):
        area_code = row[0]
        zip_code = row[1]
        # print(area_code, zip_code)
        if phone in str(area_code):
            found_zip = zip_code
            break
    return(found_zip)

def get_pwc(title):
    
    pwc_filter = pd.read_csv('/home/antide/angi/bots/filters/pwc_filter.csv')
    
    found_pwc = '0'
    # print('Filtering Pwc ...')
    for row in pwc_filter.itertuples(index=False):
        term = row[0]
        pwc = row[1]
        if term in title:
            found_pwc = pwc
            break
    
    return(found_pwc)

def get_info(path_to_directory,output_path):
    
    dflist = []

    path = path_to_directory + '/*.csv'

    files = glob.glob(path)
    
    for file in files:
        df = pd.read_csv(file)
        dflist.append(df)

    cdf = pd.concat(dflist)
    cdf = cdf.drop_duplicates()
    cdf = cdf.drop_duplicates(subset=['phone'])
    
    print('getting infos :P')
    
    namelist = []
    phonelist = []
    linklist = []
    citylist = []
    ziplist = []
    pwclist = []
    
    count = 0
    
    for row in tqdm(cdf.itertuples(index=False)):
        # print(row)
        count+=1
        filtered = 0
        good = 0
        # print(count,'/',len(cdf))
                
        name = row[0]
        phone = row[1]
        # print(len(str(phone)))
        if len(str(phone)) == 10:
            pass
        else:
            filtered+=1
            continue
        try:
            city = row[2]
        except:
            city = ''
        try:
            link = row[3]
            except:
            link = ''
        zipcode = get_zip(phone)
        if zipcode == '#N/A':
            filtered +=1
            continue
        pwc = get_pwc(name)
        if pwc == '0':
            filtered+=1
            continue
        
        good+=1
        # print(name, zipcode, pwc)
        namelist.append(name)
        phonelist.append(phone)
        linklist.append(link)
        citylist.append(city)
        ziplist.append(zipcode)
        pwclist.append(pwc)
        cleaned_df = pd.DataFrame({'Company Name':namelist, 'Business Phone':phonelist, 'Source_Link':linklist,'City':citylist,'Zip Code':ziplist,'PWC':pwclist})
        cleaned_df.to_csv(output_path + 'FilteredList.csv', index=False)
    print('Cleaning successful!\n',good, 'good links', filtered, 'bad links filtered out')
    
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', dest='input_path', help='specify directory of csv files you wish to filter', action='store', required=True)
    parser.add_argument('-o', '--output', dest='output_path', help='specify where you want output to be saved. default is in current working directory', action='store')
    
    args = parser.parse_args()

    input_directory = args.input_path
    if args.output_path:
        output=args.output_path + '/'
    else:
        output=''
    get_info(input_directory,output)

if __name__ == '__main__':
    main()