from flask import request,jsonify
from utils.config import app
from services import album_service

albumService = album_service.AlbumService()

@app.route('/album/create', methods=['POST'])
def create_album():
    data = request.get_json()
    if data:
        user_id = data.get('userId')
        album_name = data.get('albumName')
        if user_id and album_name:
            album = albumService.create_album(user_id, album_name)
            if album:
                return jsonify({'success': True, 'message': 'Album created successfully.'}), 200
            else:
                return jsonify({'success': False, 'message': 'Failed to create album.'}), 500
        else:
            return jsonify({'success': False, 'message': 'Missing required fields.'}), 400
    else:
        return jsonify({'success': False, 'message': 'No data provided.'}), 400

@app.route('/album/delete', methods=['GET'])
def delete_album():
    album_id = request.args.get('albumId')
    if album_id:
        success = albumService.delete_album(album_id)
        if success:
            return jsonify({'success': True, 'message': 'Album deleted successfully.'}), 200
        else:
            return jsonify({'success': False, 'message': 'Failed to delete album.'}), 500
    else:
        return jsonify({'success': False, 'message': 'Missing album id.'}), 400

@app.route('/album/all', methods=['GET'])
def get_all_album():
    user_id = request.args.get('userId')
    if user_id:
        albums = albumService.load_all_album_with_user_id(user_id)
        if albums:
            return jsonify({'success': True, 'data': albums}), 200
        else:
            return jsonify({'success': False, 'message': 'No albums found for this user.'}), 404
    else:
        return jsonify({'success': False, 'message': 'Missing user id.'}), 400
    
@app.route('/album/add/vocabulary', methods=['GET'])
def add_vocabulary_in_album():
    album_id = request.args.get('albumId')
    vocabulary_id = request.args.get('vocabularyId')

    if album_id and vocabulary_id:
        success = albumService.add_vocabulary_in_album(album_id, vocabulary_id)
        if success:
            return jsonify({'success': True, 'message': 'Vocabulary added to album successfully.'}), 200
        else:
            return jsonify({'success': False, 'message': 'Failed to add vocabulary to album.'}), 500
    else:
        return jsonify({'success': False, 'message': 'Missing required parameters.'}), 400

@app.route('/album/add/list', methods=['POST'])
def add_list_vocabulary_in_album():
    data = request.get_json()
    if data:
        album_id = data.get('albumId')
        vocabulary_ids = data.get('vocabularyIds')
        if album_id and vocabulary_ids:
            success = albumService.add_list_vocabulary_in_album(album_id, vocabulary_ids)
            if success:
                return jsonify({'success': True, 'message': 'Vocabularies added to album successfully.'}), 200
            else:
                return jsonify({'success': False, 'message': 'Failed to add vocabularies to album.'}), 500
        else:
            return jsonify({'success': False, 'message': 'Missing required fields.'}), 400
    else:
        return jsonify({'success': False, 'message': 'No data provided.'}), 400