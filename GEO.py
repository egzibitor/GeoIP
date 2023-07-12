import pandas as pd
import time

def txt_to_csv(input_file, output_file):
    # Чтение текстового файла
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    names = []
    accessip = []
    firewallip = []
    s = ''
    x = ''
    y = ''
    for el in lines:
        if el.startswith('[id]'):
            accessip.append(y[10:])
            firewallip.append(x[11:])
            names.append(s[6:])
            s = ''
            x = ''
            y = ''
        if el.startswith('[adapter]'):
            accessip.append(y[10:])
            firewallip.append(x[11:])
            names.append(s[6:])
            break
        if el.startswith('name'):
            s = el.split('\t\tVPN-', 1)[0]
            s = s.replace('		', '')
            if '\n' in s:
                s = s.replace('\n', '')
        if el.startswith('accessip') and not el.startswith('accessiplist'):
            y = el.split('\n', 1)[0]
        if el.startswith('firewallip'):
            x = el.split('\n', 1)[0]
    df = pd.DataFrame(columns=['NAMES', 'ACCESSIP', 'FIREWALLIP'])
    df['NAMES'] = names[1:]
    df['ACCESSIP'] = accessip[1:]
    df['FIREWALLIP'] = firewallip[1:]
    df.to_csv(output_file, index=False, sep=',', encoding='utf-8-sig')

input_file = 'F:\GeoIP\GeoIP.txt'    # Путь к входному файлу (указывается txt или conf)
timestamp = time.strftime("%d.%m.%Y_%H.%M.%S")
output_file = f'F:/GeoIP/output_{timestamp}.csv' # Путь к выходному файлу в формате csv

txt_to_csv(input_file, output_file)