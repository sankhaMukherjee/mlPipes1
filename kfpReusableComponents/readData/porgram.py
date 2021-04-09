import os

def main():

    pwd = os.path.dirname(os.path.realpath(__file__))
    print(f'The current folder = {pwd}\n')

    print('+---------------------------------')
    print('| Folder Contents')
    print('+---------------------------------')
    files = os.listdir('.')
    for f in files:
        if os.path.isdir(f):
            print(f'    [folder] {f}')
        else:
            print(f'[file] {f}')

    if os.path.exists( 'data/test.txt' ):
        print('+---------------------------------')
        print('| Contents of the file data/test.txt')
        print('+---------------------------------')
        
        with open('data/test.txt') as f:
            for l in f:
                print(l, end='')
        

    return

if __name__ == '__main__':
    main()
