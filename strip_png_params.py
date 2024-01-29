import sys
from PIL import Image

def strip_params(original, out_file):

    with Image.open(original) as image:
        try:
            print(f'[+] Stripping chunk "parameters" from {original}')
            image.info.pop("parameters")
        except KeyError:
            print(f'[-] The file {original} does not contain the chunk "parameters".')
            print(f'\n[!] Aborted')
            exit()
        print(f'[*] Writing to {out_file}')
        image.save(out_file)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(f'''Usage:
    python3 {sys.argv[0]} original.png stripped.png''')
        exit()
    
    original, out_file = sys.argv[1:]

    print('\n[!] Begin process...\n')
    strip_params(original, out_file)
    print('\n[!] Completed successfully!\n')