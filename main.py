import pandas

df_unsorted = pandas.read_csv('ddhq.csv')
df = df_unsorted.sort_values(by=['state','county','timestamp'])

df["delta"] = df['trump_votes'].shift(-1) - df['trump_votes']
df["cont"] = (df['county'] == df['county'].shift(-1)) & (df['state'] == df['state'].shift(-1))
df1 = df[(df["delta"] < 0) & df["cont"]]
df1["delta"] = df1["delta"].astype('int32',errors='ignore')
df1.to_csv('trump_loss.csv',index=False)
