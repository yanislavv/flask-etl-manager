import json

from flask import request
from flask_api import status
from flask_restful import Resource

from managers.auth import auth
from managers.workflows import WorkflowManager
from models.users import UserModel
from models.enums import UserRole
from schemas.requests.auth import RegisterSchemaRequest
from utils.decorators import validate_schema, permission_required


class WorkflowsResource(Resource):
    @auth.login_required
    @permission_required('admin')
    #@validate_schema(ComplaintSchemaRequest)
    def post(self):
        data = request.get_json()
        entry = WorkflowManager.create_workflow(data)
        return f'Workflow with name: {entry.workflow_name} created.', status.HTTP_201_CREATED

    def get(self):
        workflows = WorkflowManager.get_workflows()
        workflows = [el.workflow_name for el in workflows]
        return workflows


class DeleteWorkflowResource(Resource):
    @auth.login_required
    @permission_required('admin')
    def delete(self, workflow_name):
        WorkflowManager.delete_workflow(workflow_name)


class UpdateWorkflowResource(Resource):
    def put(self, workflow_name):
        data = request.get_json()
        WorkflowManager.update_workflow(workflow_name, data['workflow_parameters'])
