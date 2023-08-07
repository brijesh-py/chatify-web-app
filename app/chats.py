from app import (
    socketio,
    emit,
    close_room,
    join_room,
    leave_room,
    rooms,
    login_required,
    current_user,
)
from .helper import helper


@socketio.on("join_room")
def on_join_room(response):
    room = response["room"]
    join_room(room)
    emit(
        "join_room_message",
        {
            "username": current_user.username,
            "message": "Joined Room",
            "room": room,
        },
        broadcast=True,
    )


@socketio.on("load_room")
def on_create_room(response):
    room = helper.room(8)
    
    try:
        helper.view_rooms()[response['username']]
    except KeyError as e:
        helper.add_rooms(current_user.username, room, helper.get_time())
    join_room(room)
    emit(
        "load_room_message",
        {
            "username": current_user.username,
            "message": "Room Created",
            "room": room,
            "rooms": helper.view_rooms(),
            "time": helper.get_time(),
        },
        broadcast=True,
    )


@socketio.on("rooms")
def on_rooms():
    print(helper.view_rooms())
    emit("rooms_response", {"rooms": helper.view_rooms()}, broadcast=True)


@socketio.on("send_message")
def on_chat_message(response):
    message = response["message"]
    room = response["room"]
    emit(
        "receive_message",
        {
            "username": current_user.username,
            "message": message,
            "time": helper.get_time(),
        },
        room=room,
    )
