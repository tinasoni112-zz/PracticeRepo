
def translate_text_using_googletrans(text):
    from googletrans import Translator
    translator = Translator()
    try:
        return translator.translate(text).text
    except:
        return None

def detect_and_translate_lang(text) :
    import PracticeRepo.MachineLearning.TextAnalysation.IdentifyLanguage as il
    lang = il.detect_language_using_googletrans(text)
    print(lang)
    if (lang is not None) and (lang != 'en') :
        eng_text = translate_text_using_googletrans(text)
    else:
        eng_text = text

    return lang, eng_text