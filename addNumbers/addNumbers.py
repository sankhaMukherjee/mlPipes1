import sys 
import json 

def add( contextStr:str ):

    context = json.loads(contextStr)

    numbers = [1, 2, 3, 4, 5, 6]
    result = sum(numbers)
    print(result)
    print(context)

    return json.dumps(context)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        add( sys.argv[1] )
    else:
        add( '{}' )

