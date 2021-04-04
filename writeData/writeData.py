import sys 
import json

def writeData():

    data = [1, 2, 3, 4, 5, 6]
    print(f'Writing data to disk: {data}')
    with open('/data/someData.json', 'w') as f:
        json.dump(data, f)

    return 

if __name__ == "__main__":
    writeData()
    
