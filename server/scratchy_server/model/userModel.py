import marshmallow as ma

from scratchy_server import db_scratchy
from scratchy_server.model.objectIdSchema import ObjectIdSchema
from marshmallow_mongoengine import ModelSchema


class UserModel(db_scratchy.Document):
    pseudo = db_scratchy.StringField(unique=True, required=True)
    profileImage = db_scratchy.StringField(required=True)
    rooms = db_scratchy.ListField(db_scratchy.ObjectIdField())


class UserSchema(ma.Schema):
    class Meta:
        model = UserModel
        model_build_obj = False


class AllUserSchema(ma.Schema):
    users = ma.fields.List(ma.fields.Nested(UserSchema))
