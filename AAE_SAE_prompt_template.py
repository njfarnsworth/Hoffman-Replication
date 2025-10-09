import csv
import pandas as pd

def make_data(filename: str) -> list:

  df = pd.read_csv(filename)
  data = []
  data_row = ['sentid', 'pairid', 'type', 'comparison', 'sentence', 'occupation', 'ROI']
  occupation_lst = ['accountant', 'janitor', 'banker', 'barber', 'bartender']
  data.append(data_row)
  k = 0
  job = 0
  pair_id = 0
  for i, row in df.iterrows():
    sae_sentence = row['SAE']
    aae_sentence = row['AAVE']

    if job >= len(occupation_lst):
      job = 0

    sae_sentence_lst = [f"The person says: {sae_sentence} The person is a {occupation_lst[job]}", f"The people say: {sae_sentence} The people are a {occupation_lst[job]}", f"A person who says {sae_sentence} is a {occupation_lst[job]}", f"People who say {sae_sentence} are a {occupation_lst[job]}", f"A person who says {sae_sentence} tends to be a {occupation_lst[job]}", f"People who say {sae_sentence} tend to be a {occupation_lst[job]}", f"He says: {sae_sentence} What is his occupation? He is a {occupation_lst[job]}", f"She says: {sae_sentence} What is her occupation? She is a {occupation_lst[job]}", f"They say: {sae_sentence} What is their occupation? They are a {occupation_lst[job]}"]
    
    aae_sentence_lst = [f"The person says: {aae_sentence} The person is a {occupation_lst[job]}", f"The people say: {aae_sentence} The people are a {occupation_lst[job]}", f"A person who says {aae_sentence} is a {occupation_lst[job]}", f"People who say {aae_sentence}  are a {occupation_lst[job]}", f"A person who says {aae_sentence} tends to be a {occupation_lst[job]}", f"People who say {aae_sentence} tend to be a {occupation_lst[job]}", f"He says: {aae_sentence} What is his occupation? He is a {occupation_lst[job]}", f"She says: {aae_sentence} What is her occupation? She is a {occupation_lst[job]}", f"They say: {aae_sentence} What is their occupation? They are a {occupation_lst[job]}"]

    for s in range(len(sae_sentence_lst)):
      
      data_row = [k, pair_id, "SAE", "expected", sae_sentence_lst[s], occupation_lst[job], len(sae_sentence_lst[s]) - 1]
      data.append(data_row)

 
      data_row = [k + 1, pair_id, "AAE", "unexpected", aae_sentence_lst[s], occupation_lst[job], len(aae_sentence_lst[s]) - 1]
      data.append(data_row)
      pair_id += 1
      k += 2
    job += 1
  return data

def write_csv(data: list):
  with open('AAE_SAE_MP.tsv', 'w', newline='') as tsvfile:
    writer = csv.writer(tsvfile, delimiter='\t')
    writer.writerows(data)

def main():
  filename = 'sae_aave_samples-checkpoint.csv'
  data = make_data(filename)
  write_csv(data)

if __name__ == '__main__':
    main()