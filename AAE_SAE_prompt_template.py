import csv
import pandas as pd

def make_data(filename: str) -> list:

  df = pd.read_csv(filename)
  data = []
  data_row = ['sentid', 'pairid', 'type', 'comparison', 'sentence']
  data.append(data_row)

  for i, row in df.iterrows():
    sae_sentence = row['SAE']
    aae_sentence = row['AAVE']

    data_row = [i, i, "SAE", "expected", sae_sentence]
    data.append(data_row)

    data_row = [i + 1, i, "AAE", "unexpected", aae_sentence]
    data.append(data_row)
  return data

def write_csv(data: list):
  with open('AAE_SAE_MP.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

def main():
  filename = 'sae_aave_samples-checkpoint.csv'
  data = make_data(filename)
  write_csv(data)

if __name__ == '__main__':
    main()
