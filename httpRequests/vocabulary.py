from flask import request,jsonify
from utils.config import app
from services import vocabulary_service

vocabularyService = vocabulary_service.VocabularyService()

@app.route('/vocabulary/save', methods=['POST'])
def save_vocabulary():
    data = request.get_json()
    if data:
        user_id = data.get('userId')
        word = data.get('word')
        pronunciation = data.get('pronunciation')
        category = data.get('category')
        audio_src = data.get('audioSrc')
        example = data.get('example')
        if user_id and word and category:
            vocabulary = vocabularyService.create_vocabulary(user_id, word, pronunciation, category, audio_src, example)
            if vocabulary:
                return jsonify({'success': True, 'message': 'Vocabulary saved successfully.'}), 200
            else:
                return jsonify({'success': False, 'message': 'Failed to save vocabulary.'}), 500
        else:
            return jsonify({'success': False, 'message': 'Missing required fields.'}), 400
    else:
        return jsonify({'success': False, 'message': 'No data provided.'}), 400

@app.route('/vocabulary/delete', methods=['GET'])
def delete_vocabulary():
    vocabulary_id = request.args.get('vocabularyId')
    if vocabulary_id:
        success = vocabularyService.delete_vocabulary(vocabulary_id)
        if success:
            return jsonify({'success': True, 'message': 'Vocabulary deleted successfully.'}), 200
        else:
            return jsonify({'success': False, 'message': 'Failed to delete vocabulary.'}), 500
    else:
        return jsonify({'success': False, 'message': 'Missing vocabulary id.'}), 400

@app.route('/vocabulary/all', methods=['GET'])
def get_all_vocabulary():
    user_id = request.args.get('userId')
    if user_id:
        vocabularies = vocabularyService.get_all_with_user_id(user_id)
        if vocabularies:
            vocabulary_list = [vocabulary.to_dict() for vocabulary in vocabularies]
            return jsonify({'success': True, 'data': vocabulary_list}), 200
        else:
            return jsonify({'success': False, 'message': 'No vocabularies found for this user.'}), 404
    else:
        return jsonify({'success': False, 'message': 'Missing user id.'}), 400