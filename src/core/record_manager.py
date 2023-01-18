# coding=utf-8
"""
:author: Lyzen
:date: 2023.01.13
:brief: 录制管理
"""
import json

rooms = []
recordings = []


def get_rooms() -> list:
    return rooms


def get_auto_record_rooms() -> list:
    res = []
    for room in rooms:
        if room.auto_record:
            res.append(room)
    return res


def get_rooms_needed_to_record() -> list:
    res = get_auto_record_rooms()
    for rec in recordings:
        if rec.room in res:
            res.remove(rec.room)
    return res


def get_recordings() -> list:
    return recordings


def get_recording(room):
    for rec in recordings:
        if rec.room == room:
            return rec
    return None


def is_recording(room) -> bool:
    return get_recording(room) is not None


def get_room(room_id):
    for room in rooms:
        if room.room_id == room_id:
            return room
    return None
