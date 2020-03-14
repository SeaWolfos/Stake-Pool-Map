#!/usr/bin/env python
import sys

def log_output(line):
    split_line = line.split()
    return {'[0]': split_line[0],
            '[1]': split_line[1],
            '[2]': split_line[2],
            '[3]': split_line[3],
            }

def final_report(logfile):
    for line in logfile:
        line_dict = log_output(line)
        print(line_dict)

if __name__ == "__main__":
    if not len(sys.argv) > 1:
        print (__doc__)
        sys.exit(1)
    infile_name = "/home/cam/logs/node.out" # sys.argv[1]
    try:
        infile = open(infile_name, 'r')
    except IOError:
        print ("You must specify a valid file to parse")
        print (__doc__)
        sys.exit(1)
    log_report = final_report(infile)
    print (log_report)
    infile.close()
