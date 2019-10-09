import pandas as pd

# df = pd.read_csv('eng_train.txt', sep=" ", header = None)

df = pd.read_csv('eng_testb.txt', sep=" ", header = None)


df1= df.iloc[1:,[0,3]]

# df1.to_csv('output.txt', index=False, sep=" ", header = False)
df1.to_csv('output_testb.txt', index=False, sep=" ", header = False)