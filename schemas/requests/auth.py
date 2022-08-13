from marshmallow import fields, validate, Schema

#from schemas.base import AuthBase


class RegisterSchemaRequest(Schema):
    email = fields.String(min_length=5, max_length=50, required=True)
    password = fields.String(min_length=8, max_length=16, required=True)
    role = fields.String(required=True, validate=validate.OneOf(["admin", "developer"]))
