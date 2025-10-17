import pandas as pd

def make_dict(pair_filename: str, word_filename:str) -> dict:
    df = pd.read_csv(pair_filename, delimiter='\t')
    wdf = pd.read_csv(word_filename, delimiter='\t')

    data = {}
    #need occupation from word_filename and probability from pair_filename and template
    r = 0
    for i, row in df.iterrows(): #i is index label of current row, row contains data for current row
        occupation = wdf.iloc[r]['occupation']
        probability = row['diff']
        val = []
        template = []
        if wdf.iloc[r]['sentence'].startswith('The person says:'):
            template.append('The person says: t The person is a')
        elif wdf.iloc[r]['sentence'].startswith('The people say:'):
            template.append('The people say: t The people are a')
        elif wdf.iloc[r]['sentence'].startswith('A person who says'):
            template.append('A person who says t is a')
        elif wdf.iloc[r]['sentence'].startswith('People who say'):
            template.append('People who say t are a')
        elif wdf.iloc[r]['sentence'].startswith('A person who says'):
            template.append('A person who says t tends to be a')
        elif wdf.iloc[r]['sentence'].startswith('People who say'):
            template.append('People who say t tend to be a')
        elif wdf.iloc[r]['sentence'].startswith('He says:'):
            template.append('He says: t What is his occupation?')
        elif wdf.iloc[r]['sentence'].startswith('She says:'):
            template.append('She says: t What is her occupation?')
        elif wdf.iloc[r]['sentence'].startswith('They say:'):
            template.append('They say: t What is their occupation?')
        val.append(template)
        val.append(probability)

        data[occupation] = val

        r += 2

        return data

def main():
    pair_filename = 'GPT2_hoffmanagreement_bypair.tsv'
    word_filename = 'GPT2_hoffmanagreement_byword.tsv'
    print(make_dict(pair_filename, word_filename))

main()