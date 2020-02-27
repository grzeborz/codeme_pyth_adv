# tutaj wpisz swoje imię i nazwisko

import re

def unique_ip_addresses():
    list_ip_adresses = []
    with open('apache_logs') as logs:
        log_lines = logs.readlines()
    for line in log_lines:
        ip_adress = re.match('\d+\.\d+\.\d+', line)
        list_ip_adresses.append(str(ip_adress.group(0)))
        # print(ip_adress.group(0))
    return set(list_ip_adresses)

    # pass


if __name__ == '__main__':
    print(unique_ip_addresses())
