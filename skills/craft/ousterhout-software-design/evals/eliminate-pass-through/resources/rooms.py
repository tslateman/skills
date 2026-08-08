# repository.py-style data access
class RoomRepository:
    def __init__(self, db):
        self.db = db

    def get_room(self, room_id):
        return self.db.query("SELECT * FROM rooms WHERE id = %s", room_id)

    def list_rooms(self, property_id):
        return self.db.query("SELECT * FROM rooms WHERE property_id = %s", property_id)

    def update_room_name(self, room_id, name):
        return self.db.execute("UPDATE rooms SET name = %s WHERE id = %s", name, room_id)


class RoomService:
    def __init__(self, repo):
        self.repo = repo

    def get_room(self, room_id):
        return self.repo.get_room(room_id)

    def list_rooms(self, property_id):
        return self.repo.list_rooms(property_id)

    def update_room_name(self, room_id, name):
        return self.repo.update_room_name(room_id, name)


class RoomController:
    def __init__(self, service):
        self.service = service

    def get_room(self, room_id):
        return {"room": self.service.get_room(room_id)}

    def list_rooms(self, property_id):
        return {"rooms": self.service.list_rooms(property_id)}

    def update_room_name(self, room_id, name):
        return {"room": self.service.update_room_name(room_id, name)}
