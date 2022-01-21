def get_pwc(title):
    
    pwc_filter = pd.read_csv('pwc_filter.csv')
    
    found_pwc = '0'
    # print('Filtering Pwc ...')
    for i, row in pwc_filter.iterrows():
        term = row['Term']
        pwc = row['PWC']
        if term in title:
            found_pwc = pwc
            break
    
    return(found_pwc)
