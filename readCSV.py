#-*- coding:utf-8 -*-

import csv

def main():
    csv_reader = csv.reader(open('data.csv'))
    for row in csv_reader:
        print(row)

if __name__ == '__main__':
    main()