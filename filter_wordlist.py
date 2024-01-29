#===============================================================================#
#                                                                               #
# Quick script to grab some specific password lengts from a wordlist. It will   #
# ignore lines containing non ascii characters, but you can always change the   #
# charset specified in the `open(..., encoding=)` parameter. Nothing fancy,     #
# just some quality of life script.                                             #
#                                                                               #
# Have fun!                                                                     #
#                                                                               #
#===============================================================================#





import io
import sys

def filter_wordlist(min_len, max_len, wordlist, out_file=None):
    print(f'[*] Reading file {wordlist}')
    long = io.open(wordlist,'r',encoding='ascii',errors='ignore').readlines()
    short = []

    print(f'[*] Processing words with {min_len} <= len <= {max_len}')
    for line in long:
        line = line.lstrip().replace('\n', '')
        if len(line) >= min_len and len(line) <= max_len:
                short.append(line)

    if out_file:
        print(f'[*] Writing to file {out_file}')
        short_file = open(out_file, 'a')
        for line in short:
             short_file.write(line + '\n')
    else:
        for line in short:
             print(line)


if __name__ == '__main__':
    if len(sys.argv) not in [4, 5]:
        print(f'''Usage:
    python3 {sys.argv[0]} <min_len> <max_len> <wordlist> [out_file]
    no outfile = print to screen
              
example:
    python3 {sys.argv[0]}4 4 /usr/share/wordlists/rockyou.txt rockyou_len4.txt''')
        
    if len(sys.argv) == 4:
        min_len, max_len, wordlist, out_file = sys.argv[1:], None
    else:
        min_len, max_len, wordlist, out_file = sys.argv[1:]

    print(f'[!] Begin process...\n')
    filter_wordlist(int(min_len), int(max_len), wordlist, out_file)
    print(f'\n[!] Process completed successfully!\n')