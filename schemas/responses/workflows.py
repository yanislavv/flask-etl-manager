from marshmallow import Schema, fields


class CreateWorkflowResponseSchema(Schema):
    workflow_name = fields.String(required=True)
    workflow_parameters = fields.Dict(required=True)
    created_on = fields.DateTime(required=True)
