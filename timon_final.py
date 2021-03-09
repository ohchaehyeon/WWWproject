import csv
import glob
import os

input_path = './' #검색할 디렉토리, 폴더명 지정(현재위치)
output_file = 'timon_final.csv' #결과물 파일명

is_first_file = True
for input_file in glob.glob(os.path.join(input_path, 'timon_*_final.csv')): #검색할 파일명
    print(os.path.basename(input_file))
    with open(input_file, 'r', newline='', encoding='utf-8') as csv_in_file:
        with open(output_file, 'a', newline='', encoding='utf-8') as csv_out_file:
            freader = csv.reader(csv_in_file)
            fwriter = csv.writer(csv_out_file)
            if is_first_file:
                for row in freader:
                    fwriter.writerow(row)
                    print(row)
                is_first_file = False
            else:
                header = next(freader)
                for row in freader:
                    fwriter.writerow(row)
                    print(row)

