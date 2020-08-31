import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Carregando o DataSet normalizado
df = pd.read_csv('data_normalized.csv')

# Separando as features das classificações
x = df[df.columns.difference(['Class', 'Time(s)', 'PathOrder'])].values
y = df['Class']

#saida = [random.randint(0, 1) for _ in range(x)]

# Dividindo em conjunto de teste e treinamento
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, stratify=y,random_state=42)


# Definindo parâmetros do modelo
driver_classificator = DecisionTreeClassifier(random_state=42, max_depth=10)

# Treinando o modelo
driver_classificator.fit(x_train, y_train)
print(x_train)

# driver_df = df[df["Class"] == 'G']
# driver_df = driver_df[driver_df.columns.difference(['Class', 'Time(s)', 'PathOrder'])].values
# print(driver_df)
# print(driver_df.shape)


result = driver_classificator.predict(x_test)

acc = accuracy_score(y_test, result)

print(acc)
# Y test contém as classes do conjunto de teste
# acc =  0
# for a in result:
#   if(a=='G'):
#     acc = acc+1
# print("Acuracia")
# print(acc/len(result))
#print(acc)
# acuracia = acc / len(result)
# print(acuracia)
# print(driver_classificator.predict(teste))
