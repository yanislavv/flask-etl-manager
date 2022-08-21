import json

from flask import request
from flask_api import status
from flask_restful import Resource

from managers.workflows import WorkflowManager
from schemas.requests.auth import RegisterSchemaRequest
from utils.decorators import validate_schema


class WorkflowsResource(Resource):
    #@validate_schema(RegisterSchemaRequest)
    def post(self):
        data = request.get_json()
        entry = WorkflowManager.create_workflow(data)
        return f'Workflow with name: {entry.workflow_name} created.', status.HTTP_201_CREATED

    def get(self):
        workflows = WorkflowManager.get_workflows()
        workflows = [el.workflow_name for el in workflows]
        return workflows


class DeleteWorkflowResource(Resource):
    def delete(self, workflow_name):
        WorkflowManager.delete_workflow(workflow_name)


class UpdateWorkflowResource(Resource):
    def put(self, workflow_name):
        data = request.get_json()
        WorkflowManager.update_workflow(workflow_name, data['workflow_parameters'])
