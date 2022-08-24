from marshmallow import fields, validate

from schemas.base import AuthBase


class RegisterSchemaRequest(AuthBase):
    # email = fields.String(required=True, validate=validate.Length(min=5, max=50))
    # password = fields.String(required=True, validate=validate.Length(min=8, max=16))
    role = fields.String(required=True, validate=validate.OneOf(["admin", "developer"]))


class LoginSchemaRequest(AuthBase):
    # email = fields.String(required=True, validate=validate.Length(min=5, max=50))
    # password = fields.String(required=True, validate=validate.Length(min=8, max=16))
    pass
