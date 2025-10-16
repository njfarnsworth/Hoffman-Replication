import csv
import pandas as pd

def make_data(filename: str) -> list:

  df = pd.read_csv(filename)
  


  data = []
  data_row = ['sentid', 'pairid', 'type', 'comparison', 'sentence', 'occupation', 'ROI']
  occupation_lst = ['academic', 'accountant', 'actor', 'actress', 'administrator', 'analyst', 'architect', 'artist', 'assistant', 'astronaut', 'athlete', 'attendant', 'auditor', 'author', 'broker', 'chef', 'chief', 'cleaner', 'clergy', 'clerk', 'coach', 'collector', 'comedian', 'commander', 'composer', 'cook', 'counselor', 'curator', 'dentist', 'designer', 'detective', 'developer', 'diplomat', 'director', 'doctor', 'drawer', 'driver', 'economist', 'editor', 'engineer', 'farmer', 'guard', 'guitarist', 'historian', 'inspector', 'instructor', 'journalist', 'judge', 'landlord', 'lawyer', 'legislator', 'manager', 'mechanic', 'minister', 'model', 'musician', 'nurse', 'official', 'operator', 'photographer', 'physician', 'pilot', 'poet', 'politician', 'priest', 'producer', 'professor', 'psychiatrist', 'psychologist', 'researcher', 'scientist', 'secretary', 'sewer', 'singer', 'soldier', 'student', 'supervisor', 'surgeon', 'tailor', 'teacher', 'technician', 'tutor', 'veterinarian', 'writer']
  data.append(data_row)
  k = 0
  pair_id = 0
  for i, row in df.iterrows(): #2,020 rows
    sae_sentence = row['SAE']
    aae_sentence = row['AAVE']

    for occupation in occupation_lst: #84 occupations
      sae_sentence_lst = [f"The person says: {sae_sentence} The person is a {occupation}", f"The people say: {sae_sentence} The people are a {occupation}", f"A person who says {sae_sentence} is a {occupation}", f"People who say {sae_sentence} are a {occupation}", f"A person who says {sae_sentence} tends to be a {occupation}", f"People who say {sae_sentence} tend to be a {occupation}", f"He says: {sae_sentence} What is his occupation? He is a {occupation}", f"She says: {sae_sentence} What is her occupation? She is a {occupation}", f"They say: {sae_sentence} What is their occupation? They are a {occupation}"]
      aae_sentence_lst = [f"The person says: {aae_sentence} The person is a {occupation}", f"The people say: {aae_sentence} The people are a {occupation}", f"A person who says {aae_sentence} is a {occupation}", f"People who say {aae_sentence}  are a {occupation}", f"A person who says {aae_sentence} tends to be a {occupation}", f"People who say {aae_sentence} tend to be a {occupation}", f"He says: {aae_sentence} What is his occupation? He is a {occupation}", f"She says: {aae_sentence} What is her occupation? She is a {occupation}", f"They say: {aae_sentence} What is their occupation? They are a {occupation}"]

      

      for s in range(len(sae_sentence_lst)): #9 sentence formats

        sae_sent = sae_sentence_lst[s].split()
        aae_sent = aae_sentence_lst[s].split()

        roi_sae = sae_sent.index(occupation)
        roi_aae = sae_sent.index(occupation)
      
        data_row = [k, pair_id, "SAE", "expected", sae_sentence_lst[s], occupation, roi_sae]
        data.append(data_row)

        data_row = [k + 1, pair_id, "AAE", "unexpected", aae_sentence_lst[s], occupation, roi_aae]
        data.append(data_row)

        pair_id += 1
        k += 2

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
