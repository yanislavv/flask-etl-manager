from marshmallow import fields

from schemas.base import WorkflowsBase


class CreateWorkflowSchemaRequest(WorkflowsBase):
    workflow_name = fields.String(required=True)


class UpdateWorkflowSchemaRequest(WorkflowsBase):
    pass
