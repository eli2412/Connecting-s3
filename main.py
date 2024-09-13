import pandas as pd

chances_file_path = 'admission_chances.csv'
scores_file_path = 'admission_scores.csv'

chances_data = pd.read_csv(chances_file_path)
scores_data = pd.read_csv(scores_file_path)

chancesDF = pd.DataFrame(chances_data)
scoresDF = pd.DataFrame(scores_data)

print("chances data \n", chances_data)
print("scores data \n", scores_data)

merged_data = pd.merge(chancesDF, scoresDF, on='Serial_Number', how='inner')
print(merged_data)
print('*' * 100)
cleaned_data = merged_data.dropna()
print(cleaned_data)