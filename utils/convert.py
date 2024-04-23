
def convert_result_api_aictionary_to_vocabylary(data):
    word = data["word"]
    phonetic = data["phonetic"]
    audio_url = [phonetic["audio"] for phonetic in data["phonetics"] if phonetic["audio"]]
    definitions = [meaning["definition"] for meaning in data["meanings"][0]["definitions"] if "definition" in meaning and meaning["definition"]]
    examples = [meaning["example"] for meaning in data["meanings"][0]["definitions"] if "example" in meaning and meaning["example"]]
    part_of_speech = data["meanings"][0]["partOfSpeech"]
    return {
            'word': word,
            'definitions':definitions,
            'pronunciation': phonetic,
            'category': part_of_speech,
            'audioSrc': audio_url,
            'example':examples
        }