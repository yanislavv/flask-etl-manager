from marshmallow import Schema, fields


class CreateWorkflowMetadataResponseSchema(Schema):
    workflow_name = fields.String(required=True)
    workflow_instance = fields.String(required=True)
    input_parameters = fields.Dict(required=True)
