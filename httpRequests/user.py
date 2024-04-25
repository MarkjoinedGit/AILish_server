from flask import request,jsonify
from utils.config import app
from services import user_service

userService = user_service.UserService()
    
@app.route('/check-device', methods=['POST'])
def check_device():
    data = request.get_json()
    if 'advertisingID' in data:
        user, isExist = userService.find_user_by_advertising_id(data['advertisingID'])
        response = {'success': isExist}
        if isExist:
            response['data'] = user.to_dict()
        return jsonify(response)
    
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if 'advertisingID' in data and 'phoneNumber' in data and 'password' in data:
        user, isSuccessful = userService.login_by_phone_number_and_password(data['phoneNumber'],data['password'])
        response = {'success': isSuccessful}
        if isSuccessful:
            user = user.to_dict()
            if user['advertisingID'] != data['advertisingID']:
                if userService.update_advertising_id(user['id'],data['advertisingID']):
                    user['advertisingID'] = data['advertisingID']
            response['data'] = user
        return jsonify(response)

@app.route('/sign-up', methods=['POST'])
def sign_up():
    data = request.get_json()
    if 'advertisingID' in data and 'phoneNumber' in data and 'password' in data  and 'userName':
        user = userService.create_user(userName=data['userName'],phoneNumber= data['phoneNumber'], password=data['password'], advertisingID= data['advertisingID'])
        response = {'success': True,
                    'data': user.to_dict()}
        return jsonify(response)

@app.route('/update/password', methods=['POST'])
def update_password():
    data = request.get_json()
    if 'id' in data and 'prevPassword' in data and 'newPassword' in data:
        isSuccessful  = userService.update_password(user_id=data['id'],prev_password=data['prevPassword'],new_password=data['newPassword'])
        response = {'success': isSuccessful}
        return jsonify(response)

@app.route('/update/user-name', methods=['POST'])
def update_user_name():
    data = request.get_json()
    if 'id' in data and 'password' in data and 'newUserName' in data:
        isSuccessful  = userService.update_user_name(user_id=data['id'],password=data['password'],new_user_name=data['newUserName'])
        response = {'success': isSuccessful}
        return jsonify(response)

@app.route('/update/phone-number', methods=['POST'])
def update_phone_number():
    data = request.get_json()
    if 'id' in data and 'password' in data and 'newPhoneNumber' in data:
        isSuccessful  = userService.update_phone_number(user_id=data['id'],password=data['password'],new_phone_number=data['newPhoneNumber'])
        response = {'success': isSuccessful}
        return jsonify(response)

@app.route('/update/avatar-src', methods=['POST'])
def update_avatar_src():
    data = request.get_json()
    if 'id' in data and 'password' in data and 'newAvatarSrc' in data:
        isSuccessful  = userService.update_avatar_src(user_id=data['id'],password=data['password'],new_avatar_src=data['newAvatarSrc'])
        response = {'success': isSuccessful}
        return jsonify(response)