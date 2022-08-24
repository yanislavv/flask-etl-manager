from marshmallow import Schema, fields, validate


class AuthBase(Schema):
    email = fields.Email(required=True)
    password = fields.Str(required=True, validate=validate.Length(min=8, max=20))


class WorkflowsBase(Schema):
    workflow_parameters = fields.Dict(required=True)
