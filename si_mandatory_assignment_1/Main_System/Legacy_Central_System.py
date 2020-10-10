import pandas as pd
import random as rand
import numpy as np
import json
import requests
from os.path import dirname, abspath
from pip._vendor import msgpack

def read_data(file, list):
    data = pd.read_csv(file, usecols=col_list)
    return data

def create_cpr(df, symbol):
    number = np.random.randint(1111, 9999, size=len(df)).astype(str)
    df['CprNumber'] = df.pop('DateOfBirth').str.replace('-', '') + symbol + number
    return df

def create_xml(df):
    shema = 'Person'
    version = "1.1"
    xml = ['<?xml version="{}" encoding="UTF-8"?>'.format(version)]
    xml.append("<{}>".format(shema))
    for data in df.index:
        xml.append('  <field name="{0}">{1}</field>'.format(data, df[data]))
    xml.append("</{}>".format(shema))
    return '\n'.join(xml)

if __name__ == "__main__":
    col_list = ['FirstName', 'LastName', 'DateOfBirth', 'Email']
    symbol = ('-') 
    cwd = dirname(dirname(abspath(__file__)))
    base_url = 'http://127.0.0.1:8080'

    df = create_cpr(read_data('{}/people.csv'.format(cwd), col_list), symbol)
    person = '\n'.join(df.apply(create_xml, axis=1))
    print(person)

    headers = {'Content-Type': 'application/xml'}
    response = requests.post("{}/nemId".format(base_url), data=person, headers=headers).text

    person.nemID = json.loads(response.content)["nemID"]

    with open('{}/msgpack_files/{}.msgpack'.formart(cwd, person.cpr), "wb") as outfile:
        packed = msgpack.packb(person.__dict__)
        outfile.write(packed)

    print(response)
