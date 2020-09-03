import pandas as pd 
from sklearn import preprocessing

# Importando Dataset original
original_data = pd.read_csv("https://raw.githubusercontent.com/cggcaio/Anomaly-Detection-for-Driver-Identification/master/Data_Bases/KIA_DB/Driving%20Data(KIA%20SOUL)_(150728-160714)_(10%20Drivers_A-J).csv")

# Função responsável por normalizar Dataset e gerar um csv normalizado
def normalize(original_data):
  data = original_data.drop(columns=['Time(s)', 'Class', 'PathOrder'])
  scaler = preprocessing.MinMaxScaler()
  std_values = scaler.fit_transform(data)
  data_std = pd.DataFrame(data=std_values, columns=data.columns)
  df2 = original_data[['Time(s)','Class', 'PathOrder']].copy()
  data_new = data_std.join(df2)
  data_new.to_csv("data_normalized.csv")
  return data_new 

# Chamando função de normalização
data_normalized = normalize(original_data)
