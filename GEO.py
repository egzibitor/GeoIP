import pandas as pd

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
            s = el.split('VPN-', 1)[0]
            s = s.replace('		', '')
        if el.startswith('accessip') and not el.startswith('accessiplist'):
            y = el.split('\n', 1)[0]
        if el.startswith('firewallip'):
            x = el.split('\n', 1)[0]
    df = pd.DataFrame(columns=['NAMES', 'ACCESSIP', 'FIREWALLIP'])
    df['NAMES'] = names[1:]
    df['ACCESSIP'] = accessip[1:]
    df['FIREWALLIP'] = firewallip[1:]
    df.to_csv(output_file, index=False, encoding='utf-8-sig')
    print(names)
    print(accessip)
    print(firewallip)
input_file = 'F:\GeoIP\GeoIP.txt'    # Путь к входному текстовому файлу
output_file = 'F:\GeoIP\output.csv'  # Путь к выходному CSV-файлу

txt_to_csv(input_file, output_file)