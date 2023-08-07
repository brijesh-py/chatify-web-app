# from app.chats import helper
# from app import current_user

# if not current_user in helper.view_rooms()[0]['username']:
#     print('admin')

# # print(helper.view_rooms())
temp = {'admin': {'room': 'admin', 'username': 'admin'}}
temp.update({'user': {'room': 'user', 'username': 'user'}})
try:
    temp['user']
    print('admin')
except KeyError:
    print('no admin')
