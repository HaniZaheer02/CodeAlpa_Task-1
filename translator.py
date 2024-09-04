from googletrans import Translator

def translate_text(text, src_lang='en', dest_lang='fr'):
    translator = Translator()
    translation = translator.translate(text, src=src_lang, dest=dest_lang)
    return translation.text

if __name__ == "__main__":
    text_to_translate = input("Enter the text you want to translate: ")
    source_language = input("Enter the source language (default is 'en' for English): ") or 'en'
    destination_language = input("Enter the destination language (default is 'fr' for French): ") or 'fr'

    translated_text = translate_text(text_to_translate, src_lang=source_language, dest_lang=destination_language)
    print(f"Translated Text: {translated_text}")
