import csv
import pandas as pd

def make_data(filename: str) -> list:
  # with open('sae_aave_samples-checkpoint.csv', 'r', newline='') as file:
  #   reader = csv.reader(file)
  #   for row in reader:
  df = pd.read_csv(filename)
  data = []
  data_row = ['sentid', 'pairid', 'type', 'comparison']
  data.append(data_row)
  data_row = []
  for row in df.iloc[i]:
    for sentint in row:
      if sentint == 0:
        sentid = row
        type = "SAE"
        comparison = "expected"
      else:
        sentid = row + 1
        type = "AAE"
        comparison = "unexpected"
      pairid = row
      data_row = [sentid, pairid, type, comparison]
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
