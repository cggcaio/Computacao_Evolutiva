import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Carregando o Dataset normalizado
df = pd.read_csv('data_normalized.csv')

# Separando as features das classificações
x = df[df.columns.difference(['Class', 'Time(s)', 'PathOrder'])].values
y = df['Class']



# Dividindo em conjunto de teste e treinamento
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, stratify=y,random_state=42)


# Definindo parâmetros do modelo
driver_classificator = DecisionTreeClassifier(random_state=42, max_depth=10)

# Treinando o modelo
driver_classificator.fit(x_train, y_train)
print(x_train)

# Inserindo dados para o modelo classificar
result = driver_classificator.predict(x_test)

# Analisando a acurácia do modelo
acc = accuracy_score(y_test, result)
print(acc)