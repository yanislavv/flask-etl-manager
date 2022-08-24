from marshmallow import fields, validate, Schema


class RegisterSchemaRequest(Schema):
    email = fields.String(required=True, validate=validate.Length(min=5, max=50))
    password = fields.String(required=True, validate=validate.Length(min=8, max=16))
    role = fields.String(required=True, validate=validate.OneOf(["admin", "developer"]))


class LoginSchemaRequest(Schema):
    email = fields.String(required=True, validate=validate.Length(min=5, max=50))
    password = fields.String(required=True, validate=validate.Length(min=8, max=16))
