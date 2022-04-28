# Archivo para limpieza de datos
# Importar librería pandas
import pandas as pd  # Series, DataFrames


# Cargar el archivo (# DataFrame)
data = pd.read_csv('movie_metadata.csv', dtype={'title_year': str})
#print(data.info())  # Muestra información de la estructura del DataFrame

print(data.movie_title.head(10))
print(data['duration'].describe())  # Muestra información estadística
q1 = data.duration[190:200]
print(q1)

q0=data.dropna()
print(q0)

# q1 = data.groupby('title_year')['duration'].sum()
# print(q1)

# data.movie_title = data['movie_title'].str.upper()
# data.movie_title = data['movie_title'].str.strip()


# data.title_year = data.title_year.fillna('0')
# data = data.dropna()


# r1 = data['director_name'].str.extract(r'(^(a|b))')

# print(r1)

# Enviar la información a un archivo CSV
data.to_csv('limpio.csv', encoding='utf-8')
