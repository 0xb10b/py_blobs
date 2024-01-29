#===============================================================================#
#                                                                               #
# This is a simple script to retrieve any url starting with an ip               #
# address in a text file. For now, the script looks for any line STARTING with  #
# an ip addr, and retrieves (and reconstructs) the url accordingly.             #
#                                                                               #
# It was created to parse a manual google dorks search results.                 #
# (ex: inurl:home.html intext:"webcamxp 5")                                     #
# The result is captured by scrolling down as much as possible, then doing      #
# a copy/paste of the whole page into a txt file. Not the most efficient scrape #
# but it circumvents the max results problem with headless searches.            #
#                                                                               #
#                                                                               #
# Have fun!                                                                     #
#                                                                               #
#===============================================================================#


import sys


def get_url_by_ip(source_file, url_delim, custom_filters):
    print(f'[*] Parsing file {source_file} with parameters:')
    print(f"    + Url delimiter: '{url_delim}'")
    print(f'    + Custom filters: [{"".join(str(filter) + ", " for filter in custom_filters)[:-2]}]')

    f = open(source_file, 'r')
    whole = f.readlines()
    ip_dict = {} # as {'ip1':[url1, url2, ..., urln], ...}

    for line in whole:
        line = line.lstrip().replace('http://', '') # Google adds the protocol to the left
        if not is_ip(line, url_delim):
            continue

        if is_filtered(line):
            continue
        
        # key
        ip = line.split(url_delim)[0].split(PORT_DELIM)[0]
        # [value]
        url = line.replace(url_delim, '/').replace('\n', '')

        if ip in ip_dict:
            ip_dict[ip].append(url)
        else:
            ip_dict[ip] = [url]
    
    return ip_dict


# Test if a string contains an ip address (very basic check)
def is_ip(line, delim):
    line = line.split(delim)[0] # remove delim
    line = line.split(PORT_DELIM)[0] # remove port
    first_part = line.split('.')

    if len(first_part) != 4:
        return False
    
    for parts in first_part:
        if not parts.isdigit():
            return False
        
    return True


# Apply the filter to remove bad urls
def is_filtered(line):
    if CUSTOM_FILTERS == []:
        return False
    
    # Filter can be anything castable to str
    custom_filters = CUSTOM_FILTERS

    for filter in custom_filters:
        if str(filter) in line:
            return True
    return False


def remove_duplicates(ip_dict):
    print(f'[*] Removing duplicates')
    for ip in ip_dict:
        tmp_set = set(ip_dict[ip])
        ip_dict[ip] = list(tmp_set)
    return ip_dict


def sort_dict(ip_dict):
    print(f'[*] Sorting Results')
    # Sort urls
    for ip in ip_dict:
        ip_dict[ip] = sorted(ip_dict[ip])

    # Sort ips
    tmp_dict = {}
    for ip in sorted(ip_dict.keys()):
        tmp_dict[ip] = ip_dict[ip]
    ip_dict = tmp_dict

    return ip_dict


'''
********************************************************************
*                                                                  *
*                       Configuration section                      *
*                                                                  *
********************************************************************
'''

SOURCE_FILE = '../data/webcam_mobotix_scrape.txt'
OUT_FILE = '../data/webcam_mobotix_url.txt'

# Print results to screen
PRINT_TO_STDOUT = False

# Sometimes if you copy paste google or duckduckgo searches, urls are presented like this:
# ip:port › home.html instead of ip:port/home.html
URL_DELIM = ' › '

# Port number delimiter. 90% of the time this will remain unchanged
PORT_DELIM = ':'

# Let's say you know certain ips are bad, or certain keywords are misleading
CUSTOM_FILTERS = []     #['test', 'words', 1, 2, 'numbers', 'too']

# Remove duplicate urls
UNIQUE = True

# Sort the urls in ascending order
SORTED = True

'''
********************************************************************
*                                                                  *
*                     End configuration section                    *
*                                                                  *
********************************************************************
'''


if __name__ == '__main__':
    if len(sys.argv) != 1:
        print('Bad arguments: Open the file to modify the configurations.\n')
        exit

    print('\n[!] Begin processing...\n')

    ip_dict = get_url_by_ip(source_file=SOURCE_FILE, url_delim=URL_DELIM, custom_filters=CUSTOM_FILTERS)

    if UNIQUE:
        ip_dict = remove_duplicates(ip_dict)
    if SORTED:
        ip_dict = sort_dict(ip_dict)
    
    if OUT_FILE != '':
        out_file = open(OUT_FILE, 'w')
        for ip in ip_dict:
            out_file.write('\n\n#============================================================#')
            out_file.write('\n\n[+] ' + ip + ':')
            out_file.write('\n----------------')
            for url in ip_dict[ip]:
                out_file.write('\n' + url)
        out_file.close()
    
    if PRINT_TO_STDOUT:
        for ip in ip_dict:
            print('\n#============================================================#')
            print('\n[+] ' + ip + ':')
            print('----------------')
            for url in ip_dict[ip]:
                print(url)

    print(f'\n[!] File {SOURCE_FILE} processed successfully.')
    
