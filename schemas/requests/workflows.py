from marshmallow import fields, Schema

from schemas.base import WorkflowsBase


class CreateWorkflowSchemaRequest(WorkflowsBase):
    workflow_name = fields.String(required=True)
    #workflow_parameters = fields.Dict(required=True)


class UpdateWorkflowSchemaRequest(WorkflowsBase):
    pass
    #workflow_parameters = fields.Dict(required=True)