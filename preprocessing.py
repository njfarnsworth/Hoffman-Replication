import csv

sae = []
with open("data/sae_samples.txt", "r") as sae_file: 
    for line in sae_file:
        sae.append(line)

aave = []
with open("data/aave_samples.txt", "r") as aave_file: 
    for line in aave_file:
        aave.append(line)

with open("sae_aave_samples.csv", "w") as output:
    writer = csv.writer(output)
    writer.writerow(["SAE", "AAVE"])  # header
    for x, y in zip(sae, aave):
        writer.writerow([x, y])