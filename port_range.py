from subprocess import Popen

base_url = input('Base Url: ')
min_port = input('Min port: ')
max_port = input('Max port: ')

base_start = base_url[:base_url.index(':') + 1]
base_end = base_url[base_url.index('/'):]

cmd = f'proxychains4 firefox {"".join(base_start + str(port) + base_end + " " for port in range(int(min_port), int(max_port) + 1))}'
cmd = cmd.rstrip()

# Test line
# cmd = 'proxychains4 firefox https://www.whatsmyip.org/ https://whatsmyip.com/ https://www.myip.com/'

Popen(cmd.split(' '))