import marshmallow as ma

from scratchy_server import db_scratchy
from scratchy_server.model.objectIdSchema import ObjectIdSchema
from marshmallow_mongoengine import ModelSchema


class RoomModel(db_scratchy.Document):
    description = db_scratchy.StringField(required=True)
    title = db_scratchy.StringField(required=True)
    users = db_scratchy.ListField(db_scratchy.ObjectIdField())


class RoomSchema(ma.Schema):
    class Meta:
        model = RoomModel
        model_build_obj = False

class AllRoomSchema(ma.Schema):
    rooms = ma.fields.List(ma.fields.Nested(RoomSchema))
