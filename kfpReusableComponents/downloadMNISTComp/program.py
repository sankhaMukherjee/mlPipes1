import argparse
import gzip, wget
import struct, os
import numpy as np


def downloadFile(website):
    '''download the file present at the URL

    Given a URL, this function is goign to download the file
    present in the URL. This is then going to take the file
    and place it in the `data` folder in the same directory. If
    there is an error, the nature of the error will be printed,
    and a None is returned

    Parameters
    ----------
    website : str
        A string pointing to a URL that contains data that should
        be downloaded.

    Returns
    -------
    [type]
        [description]
    '''

    try:
        wget.download(website)
        if not os.path.exists('./data'):
            os.makedirs('data')

        folder, fileName = os.path.split(website)
        newFile = os.path.join('data', fileName)
        os.rename(fileName, newFile )

        return newFile

    except Exception as e:
        print(f'Unable to download file [{website}]: {e}')
        return None

    return

def unzipFile(inpFile):
    '''unzups a gzipped file

    This function takes a gzipped file and unzipps it. Unlike the cli
    version, this file does not remove the original file from the folder
    but rather keeps it

    Parameters
    ----------
    inpFile : str
        The path of the input file

    Returns
    -------
    str
        The path to the output file. If there was an error, a None is returned.
    '''

    try:

        if not inpFile.endswith('.gz'):
            print(f'The file {inpFile} must be a gzipped file with an `.gz` extension')
            return

        outFile = inpFile[:-3]

        with gzip.open(inpFile, 'rb') as fIn: 
            with open(outFile, 'wb') as fOut: 
                fOut.write( fIn.read()  ) 

        return outFile

    except Exception as e:
        print(f'Unable to unzip the file [{fileName}]: {e}')

    return 

def readImages(fileName):

    try:

        with open(fileName, 'rb') as f:
            temp = f.read(4*2)
            magicNumber, N, = struct.unpack('>ll', temp)
            print(f'+--------------------------------------------------------')
            print(f'| Data Specs')
            print(f'+--------------------------------------------------------')
            print(f'| magic number = {magicNumber}')
            print(f'| number of items = {N}')

            if magicNumber == 2051:
                print('| Type of data = image list')
                temp = f.read(4*2)
                rows, cols = struct.unpack('>ll', temp)
                print(f'| image size = {rows} x {cols}')
            else:
                print('| Type of data = label list')

            print(f'+--------------------------------------------------------')

            if magicNumber == 2051:
                nPixels = N*rows*cols
            else:
                nPixels = N

            formatString = f'>{nPixels}B'
            nBytes = f.read( nPixels )

            data = struct.unpack(formatString, nBytes)
            data = np.array( data )
            data = data.reshape((N, -1))

            print(f'| shape if read data = {data.shape}')

        outFile = fileName + '.npy'
        np.save( outFile, data )

        print(f'| Data saved to {outFile}')
        print(f'+--------------------------------------------------------')


        return(outFile)


    except Exception as e:
        print(f'Problem: {e}')

    return

def createParser():

    parser = argparse.ArgumentParser(description='Download MNIST data')
    
    # Figure out what action should be taken
    parser.add_argument('--download', dest='todo', action='store_const', const='download', help='download the requested file')
    parser.add_argument('--extract',  dest='todo', action='store_const', const='extract',  help='unzip the .gz files into the same folder')
    parser.add_argument('--toNumpy',  dest='todo', action='store_const', const='toNumpy',  help='convert unzipped files to numpy files')
    
    # specifications of what should be downloaded
    parser.add_argument('--url',  type=str, help='download data at the specifid url')
    parser.add_argument('--file', type=str, help='file used for unzipping or converting to numpy')
    
    parser.add_argument('--output-path', type=str, help='Path of the local file where the Output 1 data should be written.') # Paths should be passed in, not hardcoded
    
    args = parser.parse_args()

    if args.todo =='download' and args.url is None:
        print(f'when you use the [--download] argument you will also need to provide the [--url] argument.')
        pring(f'python3 --download --url "http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz"')

    if args.todo =='extract' and args.file is None:
        print(f'when you use the [--extract] argument you will also need to provide the [--file] argument.')
        pring(f'python3 --extract --file "data/train-images-idx3-ubyte.gz"')


    return args

def main():

    args = createParser()
    print(args)

    result = None

    if (args.todo == 'download') and (args.url is not None):
        result = downloadFile(args.url)
        
    if (args.todo == 'extract') and (args.file is not None):
        result = unzipFile(args.file)
    
    if (args.todo == 'toNumpy') and (args.file is not None):
        result = readImages(args.file)
    
    # -----------------------------
    # Post processing
    # -----------------------------
    print(f'\nresult = {result}\n')
    if args.output_path is not None:
        with open( args.output_path, 'w' ) as fOut:
            fOut.write( f'{result}' )


    # if True:
    #     readImages('data/train-images-idx3-ubyte')

        
    
    return

if __name__ == "__main__":
    main()
