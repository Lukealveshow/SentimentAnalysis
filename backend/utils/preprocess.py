import spacy
import pt_core_news_sm
import en_core_web_sm

nlp_en = en_core_web_sm.load()
nlp_pt = pt_core_news_sm.load()

def preprocess(text, lang="en"):
    nlp = nlp_en if lang == "en" else nlp_pt
    doc = nlp(text.lower())

    tokens = [
        token.lemma_
        for token in doc
        if not token.is_stop and not token.is_punct and token.is_alpha
    ]
    return " ".join(tokens)