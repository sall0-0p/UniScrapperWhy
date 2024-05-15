from deep_translator import GoogleTranslator

selectors = {
    "opinionId": [None,"data-entry-id"],
    "author": ["span.user-post__author-name"],
    "recommendation": ["span.user-post__author-recomendation > em"],
    "score": ["span.user-post__score-count"],
    "content": ["div.user-post__text"],
    "pros": ["div.review-feature__title--positives ~ div.review-feature__item", None, True],
    "cons": ["div.review-feature__title--negatives ~ div.review-feature__item", None, True],
    "helpful": ["button.vote-yes > span"],
    "unhelpful": ["button.vote-no > span"],
    "publishDate": ["span.user-post__published > time:nth-child(1)","datetime"],
    "purchaseDate": ["span.user-post__published > time:nth-child(2)","datetime"],
}

def translate(text, from_lang="auto", to_lang="en"):
    if text:
        if isinstance(text, list):
            return {
                from_lang: text,
                to_lang: [GoogleTranslator(source = from_lang, target = to_lang).translate(t) for t in text]
            }
        else:
            return {
                from_lang: text,
                to_lang: GoogleTranslator(source = from_lang, target = to_lang).translate(text)
            }
    else:
        return None
    
def mapRecommendation(value):
    if value == "Polecam":
        return True
    elif value == "Nie polecam":
        return False
    else:
        return None

def mapScore(value):
    value = value.replace(",", ".")
    splitValue = value.split("/")
    points = float(splitValue[0])
    maxPoints = float(splitValue[1])

    return points / maxPoints

