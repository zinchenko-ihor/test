import re
import csv
import collections


def log_file_reader(filename):
    # Get all IP addresses from the log file
    with open(filename) as f:
        log = f.read()
        regex = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
        ip_list = re.findall(regex, log)
        return ip_list

# Get total count of IPs
def count_ip(ip_list):
    return collections.Counter(ip_list)

# Create
def write_to_csv(counter):
    with open('output.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        header = ['IP', 'Count']
        writer.writerow(header)
        for item in counter:
            writer.writerow((item, counter[item]))


if __name__ == "__main__":
    write_to_csv(count_ip(log_file_reader('nginx.log')))