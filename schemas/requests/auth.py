from marshmallow import fields, validate

from schemas.base import AuthBase


class RegisterSchemaRequest(AuthBase):
    role = fields.String(required=True, validate=validate.OneOf(["admin", "developer"]))


class LoginSchemaRequest(AuthBase):
    pass
