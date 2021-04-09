import os
from datetime import datetime as dt

def main():

    try:

        now = dt.now().strftime('%Y-%m-%d--%H-%M-%S')

        print('+---------------------------------')
        print(f'| Writing data to [data/test.txt] at {now}')
        print('+---------------------------------')
        
        with open('data/test.txt', 'w') as fOut:
            fOut.write(f'Current time = {now}')
            fOut.write('This is the first line\n')
            fOut.write('This is the second line\n')
            fOut.write('This is the last line\n')
        
    except Exception as e:
        print(f'Unable to write data into the file data/test.txt: {e}')


    return

if __name__ == '__main__':
    main()
