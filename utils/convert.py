def convert_result_api_aictionary_to_vocabylary(data):
    word = data["word"]
    phonetics = data.get("phonetics", [])
    pronunciation_audio = [pronunciation.get("audio", "") for pronunciation in phonetics]
    id_to_get_audio = 0


    audioSrc = pronunciation_audio[id_to_get_audio] if phonetics else ""
    pronunciation_text = phonetics[id_to_get_audio].get("text") if phonetics else ""
    
    definitions = [meaning["definition"] for meaning in data["meanings"][0]["definitions"] if "definition" in meaning and meaning["definition"]]
    examples = [meaning["example"] for meaning in data["meanings"][0]["definitions"] if "example" in meaning and meaning["example"]]
    part_of_speech = data["meanings"][0]["partOfSpeech"]
    return {
            'category': part_of_speech,
            'word': word,
            'definitions': definitions,
            'pronunciation':  pronunciation_text,  # Lấy giá trị text đầu tiên trong chuỗi pronunciations
            'audioSrc': audioSrc,  # Sử dụng danh sách audio từ chuỗi pronunciations
            'example': examples
        }
