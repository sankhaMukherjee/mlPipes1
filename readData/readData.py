import sys 
import json

def writeData():

    print(f'Reading data from disk:')
    with open('/data/someData.json') as f:
        data = json.load(f)
    
    print(f'Read data = {data}')

    return 

if __name__ == "__main__":
    writeData()
    
