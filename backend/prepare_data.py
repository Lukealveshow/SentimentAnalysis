import pandas as pd

print("Carregando IMDb...")
df_imdb = pd.read_csv("data/imdb.csv")

df_imdb = df_imdb.rename(columns={
    "review": "text",
    "sentiment": "sentiment"
})

df_imdb["lang"] = "en"

print("Carregando B2W...")
df_b2w = pd.read_csv("data/b2w.csv")
df_b2w = df_b2w.rename(columns={
    "review_text": "text",
    "overall_rating": "rating"
})
df_b2w = df_b2w[["text", "rating"]]
df_b2w = df_b2w.dropna()
df_b2w = df_b2w[df_b2w["text"].str.len() > 5]
def map_sentiment(r):
    if r <= 2:
        return "negative"
    elif r == 3:
        return "neutral"
    else:
        return "positive"

df_b2w["sentiment"] = df_b2w["rating"].apply(map_sentiment)
df_b2w["lang"] = "pt"

df_b2w = df_b2w[["text", "sentiment", "lang"]]

print("Unificando datasets...")
df = pd.concat([df_imdb, df_b2w])

df = df.dropna()
df = df.sample(frac=1).reset_index(drop=True)

df.to_csv("data/dataset_final.csv", index=False)

print("Dataset final criado com sucesso!")