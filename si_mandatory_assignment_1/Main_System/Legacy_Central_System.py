import pandas as pd
import random as rand
import numpy as np
import json
import requests

col_list = ['FirstName', 'LastName', 'DateOfBirth', 'Email',]

symbol = ('-') 

number = str(rand.randint(1111, 9999))

def read_data(file, list):
    data = pd.read_csv(file, usecols=col_list)
    return data


def create_cpr(df):
    df['CprNumber'] = df['DateOfBirth'].str.replace('-', '') + symbol + number
    df = df.drop(['DateOfBirth'], axis=1)
    return df
    

def create_xml(df):
    xml = ['<Person>']
    for field in df.index:
        xml.append('  <field name="{0}">{1}</field>'.format(field, df[field]))
    xml.append('</Person>')
    return '\n'.join(xml)
    

if __name__ == "__main__":
    df = create_cpr(read_data('si_mandatory_assignment_1/Main_System/people.csv', col_list))
    print('\n'.join(df.apply(create_xml, axis=1)))
    
    df1 = df[['CprNumber', 'Email']]
    person = df1.to_json(r'people.json', orient="records")
    requests.post('http://localhost:8088/generate-nemID', json=person)