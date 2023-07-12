import json
import sys
import subprocess
subprocess.check_call([sys.executable, '-m', 'pip', 'install',
'pandas'])
import pandas as pd
csv_file = pd.DataFrame(pd.read_csv(r'F:\csv-json\csv\2023-Jan.csv', dtype = 'str', encoding='utf-16le', sep = "^", header = 0, index_col = False))
csv_file = csv_file.drop('Unnamed: 13', axis = 1)
csv_file = csv_file.fillna(' ')
x = csv_file.to_dict(orient = "records")
with open(r'F:\csv-json\json\2023-Jan.json', 'w', encoding='utf-8') as file:
    json.dump(x, file, ensure_ascii=False, indent=4)




