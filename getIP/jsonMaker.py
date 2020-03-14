# JSON Maker in Python
# Written by @SeaWolfos
# Hi!

# open log file
# we're going from an app log to json, hopefully
# here we go

import re
import time
fro time import strftime

def main():
    log_file_path = r"/home/cam/logs/node.out"
    export_file_path = r"/home/cam/projects/Stake-Pool-Map/getIP/ip.txt"

    time_now = str(strftime("%Y-%m-%d %H-%M-%S", time.localtime()))

    file = "\\" + "Parser Output " + time_now + ".txt"

    export_file = export_file_path + file

    regex = '(node_id: "(.*?)", (.*?),)'
    
    parseData(log_file_path, export_file, regex, read_line=True)

def parseData(log_file_path, export_file, regex, read_line=True):
    with open(log_file_path, "r") as file:
        match_list []
        if read_line == True:
            for line in file:
                for match in re.finditer(regex, line, re.S):
                    match_text=match.group()
                    match_list.append(match_text)
                    print match_text
        else:
            data = f.read()
            for match in re.finditer(regex, data, re.S):
                match_text = match.group()
                match_list.append(match_text)
    file.close()

    with open(export_file, "w+") as file:
        file.write("EXPORTED DATA:\n")
        match_list_clean = list(set(match_list))
        for item in xrange(0, len(match_list_clean)):
            print match_list_clean[item]
            file.write(match_list_clean[item] + "\n")
    file.close()

if __name__ == '__main__':
    main()
