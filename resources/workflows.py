from flask import request
from flask_api import status
from flask_restful import Resource

from managers.auth import auth
from managers.workflows import WorkflowManager
from schemas.requests.workflows import CreateWorkflowSchemaRequest, UpdateWorkflowSchemaRequest
from schemas.responses.workflows import CreateWorkflowResponseSchema
from utils.decorators import validate_schema, permission_required


class WorkflowsResource(Resource):
    @auth.login_required
    @permission_required('admin')
    @validate_schema(CreateWorkflowSchemaRequest)
    def post(self):
        data = request.get_json()
        entry = WorkflowManager.create_workflow(data)
        return CreateWorkflowResponseSchema().dump(entry), status.HTTP_201_CREATED

    def get(self):
        workflows = WorkflowManager.get_workflow()
        workflows = [el.workflow_name for el in workflows]
        return workflows, status.HTTP_200_OK


class DeleteWorkflowResource(Resource):
    @auth.login_required
    @permission_required('admin')
    def delete(self, workflow_name):
        WorkflowManager.delete_workflow(workflow_name)
        return f"Workflow: {workflow_name} has been deleted.", status.HTTP_200_OK


class UpdateWorkflowResource(Resource):
    @validate_schema(UpdateWorkflowSchemaRequest)
    def put(self, workflow_name):
        data = request.get_json()
        old_params = WorkflowManager.update_workflow(workflow_name, data['workflow_parameters'])
        return f"The parameters of {workflow_name} workflow has been updated:" \
               f"Old parameters -> {old_params.workflow_parameters}" \
               f"New parameters -> {data['workflow_parameters']}", status.HTTP_200_OK
