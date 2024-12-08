# 4. ELLENŐRZÉS: Scrapelt .csv állomány beolvasása data frame-ként:

import helpers as hp

csv_to_dataframe = hp.read_csv_to_dataframe(hp.csv_path)
print (csv_to_dataframe)