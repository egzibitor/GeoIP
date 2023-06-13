import pandas as pd

def txt_to_csv(input_file, output_file):
    # Чтение текстового файла
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    names = []
    accessip = []
    firewallip = []
    for el in lines:
        if el.startswith('[adapter]'):
            break
        if el.startswith('name'):
            s = el.split('VPN-', 1)[0]
            s = s.replace('		', '')
            names.append(s[6:])
        if el.startswith('accessip') and not el.startswith('accessiplist'):
            y = el.split('\n', 1)[0]
            accessip.append(y[10:])
        if el.startswith('firewallip'):
            x = el.split('\n', 1)[0]
            firewallip.append(x[11:])
    df = pd.DataFrame(columns=['NAMES', 'ACCESSIP', 'FIREWALLIP'])
    df['NAMES'] = names
    df['ACCESSIP'] = accessip
    df['FIREWALLIP'] = firewallip
    df.to_csv(output_file, index=False, encoding='utf-8-sig')
    print(names)
    print(accessip)
    print(firewallip)
input_file = 'F:\GeoIP\GeoIP.txt'    # Путь к входному текстовому файлу
output_file = 'F:\GeoIP\output.csv'  # Путь к выходному CSV-файлу

txt_to_csv(input_file, output_file)