import pandas as pd
from load import upload_file
from download import download_file
import os
print(os.path.exists('data/input/final_cleaned_data.csv'))  # Should return True if the file exists


chances_file_path = 'admission_chances.csv'
scores_file_path = 'admission_scores.csv'

chances_data = pd.read_csv(chances_file_path)
scores_data = pd.read_csv(scores_file_path)

chancesDF = pd.DataFrame(chances_data)
scoresDF = pd.DataFrame(scores_data)

# print("chances data \n", chances_data)
# print("scores data \n", scores_data)

merged_data = pd.merge(chancesDF, scoresDF, on='Serial_Number', how='inner')
cleaned_data = merged_data.dropna()

cleaned_data.to_csv('data/input/final_cleaned_data.csv')
object_key = 'data/input/final_cleaned_data.csv'
filename = 'final_cleaned_data.csv'
success = upload_file(object_key, filename)
if success:
    print("Upload successful!")
else:
    print("Upload failed.")
    
new_file_name = 'downloaded_file.csv'
successDownload = download_file(object_key, new_file_name)
if successDownload:
    print("Download successful!")
else:
    print("Download failed.")