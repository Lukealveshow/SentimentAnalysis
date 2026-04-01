from langdetect import detect

def detect_language(text):
    try:
        lang = detect(text)
        return "pt" if lang == "pt" else "en"
    except:
        return "en"