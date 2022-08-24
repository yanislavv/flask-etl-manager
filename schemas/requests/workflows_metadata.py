from marshmallow import fields, Schema


class CreateWorkflowInstanceRequestSchema(Schema):
    workflow_instance = fields.String(required=True)
    workflow_name = fields.String(required=True)
    input_parameters = fields.Dict(required=True)
    tag = fields.String()


class WorkflowMetadataRequestSchema(Schema):
    start = fields.String(required=True)
    end = fields.String(required=True)
    logs_url = fields.String(required=True)
    status = fields.String(required=True)

