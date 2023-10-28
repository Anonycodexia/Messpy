#!/usr/bin/env python
# coding: utf-8
# By Anonycodexia

import marshal
import random
import argparse
import os

REQUIRED_PACKAGES = ['colorama==0.4.4', 'pyfiglet==0.8.post1', 'tqdm==4.62.2', 'requests==2.26.0']

def install_dependencies():
    for package in REQUIRED_PACKAGES:
        os.system(f'pip install {package} >/dev/null 2>&1')

def check_dependencies():
    try:
        import colorama, pyfiglet, tqdm, requests
    except ImportError:
        return False
    return True

def marsh_enc(source):
    encoded_source = marshal.dumps(compile(source, 'Anonycodexia', 'exec'))
    return f'import marshal\nexec(marshal.loads({encoded_source}))'

def main():
    if not check_dependencies():
        print("Installing required packages...")
        install_dependencies()

    input_file = input("Enter the input file name: ")
    output_file = input("Enter the output file name: ")
    complexity = int(input("Enter the complexity level: "))

    encoded_pro = ''
    for _ in range(complexity):
        if not encoded_pro:
            with open(input_file, 'r') as file:
                source_code = file.read()
            encoded_pro = marsh_enc(source_code)
        else:
            encoded_pro = marsh_enc(encoded_pro)

    with open(output_file, 'w') as file:
        file.write(f'# Encoded By Anonycodexia\n{encoded_pro}')

    print(f'Encoding successful!\nSaved as {output_file}')

if __name__ == '__main__':
    main()
