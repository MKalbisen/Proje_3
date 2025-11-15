import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('movies_initial.csv')

#IMDB puanı en yüksek filmler ile ilgili bilgiler
top_films = df.sort_values(by='imdbRating', ascending=False).head(10)
print(top_films[['title', 'imdbRating', 'director', 'language', 'awards', 'country', 'year', 'runtime']])

#En popüler dil, tema ve en çok film yapılan ülkeler
dil = df['language'].value_counts().head(7)
ülke = df['country'].value_counts().head(7)
tema = df['genre'].str.split(',').explode().str.strip().value_counts().head(7)

print(dil, ülke, tema)

#En az 5 filmi olan, en yüksek ortalama IMDB puanına sahip 10 yönetmen
director_counts = df['director'].value_counts()
top_directors = director_counts[director_counts > 5].index
director_scores = df[df['director'].isin(top_directors)].groupby('director')['imdbRating'].mean().sort_values(ascending=False).head(10)
print(director_scores)
director_scores.head(10).plot(kind='barh')
plt.title('En Yüksek Ortalama IMDb Puanına Sahip Yönetmenler')
plt.xlabel('Ortalama IMDb Puanı')
plt.ylabel('Yönetmen')
plt.show()

#Diller bazında en az 200 filmi olup en yüksek ortalama IMDB puanına sahip 10 dil
df['language'] = df['language'].fillna('Unknown')
df = df.assign(language=df['language'].str.split(',')).explode('language') 
df['language'] = df['language'].str.strip()

language_counts = df['language'].value_counts()
valid_languages = language_counts[language_counts > 200].index

df_filtered = df[df['language'].isin(valid_languages)]
dil_ratings = df_filtered.groupby('language')['imdbRating'].mean().sort_values(ascending=False).head(10)
print(dil_ratings)

#Ortalama IMDB puanına göre türler
df["genre_list"] = df["genre"].astype(str).str.split(",")   
df_exploded = df.explode("genre_list")                     
df_exploded["genre_list"] = df_exploded["genre_list"].str.strip() 

genre_mean = df_exploded.groupby('genre_list')['imdbRating'].agg(['mean', 'count'])

genre_mean = genre_mean[genre_mean['count'] >= 50].sort_values('mean', ascending=False)
print(genre_mean.head(10))

plt.figure(figsize=(20, 6))
sns.barplot(x=genre_mean.index, y=genre_mean['mean'], palette='viridis')
plt.xticks(rotation=30)
plt.title('Ortalama IMDb Puanına Göre Türler')
plt.xlabel('Tür')
plt.ylabel('Ortalama IMDb Puanı')
plt.show()


#En uzun filmler
df['runtime'] = df['runtime'].astype(str)
df["runtime_minutes"] = df["runtime"].str.replace(" min", "", regex=False)
df["runtime_minutes"] = pd.to_numeric(df["runtime_minutes"], errors="coerce")
df["runtime_minutes"].max()

df[["title", "runtime_minutes"]].sort_values("runtime_minutes", ascending=False).head(10)

#Film süresi ile imdb puanı ilişkisi
df = df.reset_index(drop=True) 
df_filtered_runtime = df[(df["runtime_minutes"] >= 30) & (df["runtime_minutes"] <= 200)] 
sns.scatterplot(data=df_filtered_runtime, x='runtime', y='imdbRating') 
plt.title('Film Süresi ve IMDb Puanı İlişkisi') 
plt.xticks(rotation=45)
plt.show()

#En çok oy alan 10 film
df_unique = df.drop_duplicates(subset="imdbID")
df_unique.sort_values("imdbVotes", ascending=False).head(10)

#imdb puanlarının yıllara göre ortalaması
df.groupby("year")["imdbRating"].mean().plot()

#Birden fazla çalıştırınca df bozuluyor
df["cast"] = df["cast"].astype(str).str.split(",")
df_cast = df.explode("cast")
df_cast["cast"] = df_cast["cast"].str.strip()   

actor_ratings = df_cast.groupby("cast")["imdbRating"].mean()


#En az 10 filmi olan, en yüksek ortalama IMDB puanına sahip aktörler
actor_stats = df_cast.groupby("cast")["imdbRating"].agg(["mean", "count"])
actor_stats = actor_stats[actor_stats["count"] > 10]   
actor_stats = actor_stats.sort_values("mean", ascending=False)

actor_stats.head(10)


#Film öneri sistemi
df_recom = df.copy()
df_recom = df.fillna("")
cols = ["genre", "director", "cast", "plot"]

for c in cols:
    df_recom[c] = df_recom[c].astype(str)

df_recom["features"] = (
    df_recom["genre"] + " " +
    df_recom["director"] + " " +
    df_recom["cast"] + " " +
    df_recom["plot"]
)

df_small = df_recom.tail(20000).reset_index(drop=True)
from sklearn.feature_extraction.text import TfidfVectorizer

tfidf = TfidfVectorizer(stop_words="english")
tfidf_matrix = tfidf.fit_transform(df_small["features"])

from sklearn.metrics.pairwise import cosine_similarity

cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)


indices = pd.Series(df_small.index, index=df_small["title"]).drop_duplicates()

def get_recommendations(title, n=10):
    if title not in indices:
        return f"Film bulunamadı: {title}"

    idx = indices[title]

    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:n+1]

    movie_indices = [i[0] for i in sim_scores]

    return df_small.iloc[movie_indices][["title", "genre", "imdbRating"]]


get_recommendations("The Hacker Wars", 20)
