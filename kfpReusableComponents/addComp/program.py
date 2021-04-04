#!/usr/bin/env python3
import argparse
from pathlib import Path

# This code has been modified form the following code
# https://www.kubeflow.org/docs/components/pipelines/sdk/component-development/
# This is also a replica of the add function that we shall be creating a
# little later.
# This will take 
#   a = float,
#   b = float,
# Return 
#   c = a + b


# Defining and parsing the command-line arguments
parser = argparse.ArgumentParser(description='Add two numbers (output = a+b). Call this through `python3 program.py -a 5 -b 2`')
parser.add_argument('--value1', type=float, default=5, help='first parameter to be added')
parser.add_argument('--value2', type=float, default=5, help='second parameter to be added')
parser.add_argument('--output-path', type=str, help='Path of the local file where the Output 1 data should be written.') # Paths should be passed in, not hardcoded
args = parser.parse_args()

# Creating the directory where the output file will be created (the directory may or may not exist).
Path(args.output_path).parent.mkdir(parents=True, exist_ok=True)

result = args.value1 + args.value2
with open( args.output_path, 'w' ) as fOut:
    fOut.write( f'{result}' )

