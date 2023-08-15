#main file to run all the functions 

import argparse
from open_txt_file import open_txt_file
from print_sip_info import print_sip_info
from check_header import check_header

def main():
    parser = argparse.ArgumentParser(description='CLI program to parse and print SIP request information.')
    parser.add_argument('file_path', help='Path to the .txt file containing the SIP request')
    parser.add_argument('-p', '--print', action='store_true', help='Parse and print SIP information')
    parser.add_argument('-e', '--exists', metavar='header', help='Check if header exists and print its content')

    args = parser.parse_args()

    txt_file = open_txt_file(args.file_path)
    if args.print:
        print_sip_info(txt_file)
    
    if args.exists:
        exists, content = check_header(txt_file, args.exists)
        if exists:
            print(f"The header '{args.exists}' exists with content: {content}")
        else:
            print(f"The header '{args.exists}' does not exist.")

if __name__ == '__main__':
    main()
