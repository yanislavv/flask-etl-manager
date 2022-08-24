import json

from flask import request
from flask_api import status
from flask_restful import Resource

from managers.workflows_metadata import WorkflowsMetadataManager
from schemas.requests.auth import RegisterSchemaRequest
from utils.decorators import validate_schema


class WorkflowMetadataResource(Resource):
    def post(self):
        data = request.get_json()
        entry = WorkflowsMetadataManager.create_instance(data)
        return f'Instance of {entry.workflow_name} was created with name: {entry.workflow_instance}', status.HTTP_201_CREATED


class WorkflowMetadataUpdateResource(Resource):
    def put(self, instance_name):
        data = request.get_json()
        entry = WorkflowsMetadataManager.update_instance_details(instance_name, data)


class GetWorkflowStatus(Resource):
    def get(self, instance_name):
        instance = WorkflowsMetadataManager.send_notification(instance_name)
        return instance
