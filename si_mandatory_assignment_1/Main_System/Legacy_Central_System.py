import pandas as pd
import random as rand
import numpy as np
import json
import requests
import os.path 

def read_data(file, list):
    data = pd.read_csv(file, usecols=col_list)
    return data

def create_cpr(df, symbol):
    number = np.random.randint(1111, 9999, size=len(df)).astype(str)
    df['CprNumber'] = df.pop('DateOfBirth').str.replace('-', '') + symbol + number
    return df

def create_xml(df):
    shema = 'Person'
    xml = ["<{}>".format(shema)]
    for data in df.index:
        xml.append('  <field name="{0}">{1}</field>'.format(data, df[data]))
    xml.append("</{}>".format(shema))
    return '\n'.join(xml)

if __name__ == "__main__":
    col_list = ['FirstName', 'LastName', 'DateOfBirth', 'Email']
    symbol = ('-') 
    base_url = "http://127.0.0.1:8080"

    df = create_cpr(read_data('NemID-Project/si_mandatory_assignment_1/Main_System/people.csv', col_list), symbol)
    xml_person = '\n'.join(df.apply(create_xml, axis=1))

    headers = {'Content-Type': 'application/xml'}
    response = requests.post("{}/nemId".format(base_url), xml_person, headers=headers).text

    print(response)
