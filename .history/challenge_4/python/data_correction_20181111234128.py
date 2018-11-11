import pandas as pd
import time

start_time = time.time()

file_path = "~/Downloads/edi-contacts.csv"
contacts_df = pd.read_csv(file_path, names=['id', 'firstname', 'lastname'])

pattern = "^[A-Za-z0-9 ;&'-]+$/"
contacts_df['flag']= contacts_df.firstname.str.contains(pattern, regex=True) \
                    & contacts_df.lastname.str.contains(pattern, regex=True)

ouput_file_path = "~/Downloads/flagged-edi-contacts.csv"
contacts_df.to_csv(ouput_file_path)

print("--- %s seconds ---" % (time.time() - start_time))