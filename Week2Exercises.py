import argparse
import csv, platform

def print_file_content(file):
        with open(file) as f_obj:
            content = f_obj.readlines()
        print(content)

def write_list_to_file(output_file2, lst):
    with open(output_file2, 'w', newline='') as output_file:
        output_writer = csv.writer(output_file)
    
        for ele in lst:
            output_writer.writerow(ele)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A program that reads from one file and writes to another')
    parser.add_argument('file', help='The file to read')
    parser.add_argument('-l', '--list', nargs='*' ,help='The list to write')

    args = parser.parse_args()

    print_file_content(args.file)

    if args.list != None:
        write_list_to_file('my_notebooks/test.csv', args.list)
    
    
