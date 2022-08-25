from flask import request
from flask_api import status
from flask_restful import Resource

from managers.workflows_metadata import WorkflowsMetadataManager
from schemas.requests.workflows_metadata import CreateWorkflowInstanceRequestSchema, WorkflowMetadataRequestSchema
from schemas.responses.workflows_metadata import CreateWorkflowMetadataResponseSchema
from utils.decorators import validate_schema


class WorkflowMetadataResource(Resource):
    @validate_schema(CreateWorkflowInstanceRequestSchema)
    def post(self):
        data = request.get_json()
        entry = WorkflowsMetadataManager.create_instance(data)
        return CreateWorkflowMetadataResponseSchema().dump(entry), status.HTTP_201_CREATED


class WorkflowMetadataUpdateResource(Resource):
    @validate_schema(WorkflowMetadataRequestSchema)
    def put(self, instance_name):
        data = request.get_json()
        entry = WorkflowsMetadataManager.update_instance_details(instance_name, data)
        return entry, status.HTTP_201_CREATED


class GetWorkflowStatus(Resource):
    def get(self, instance_name):
        response = WorkflowsMetadataManager.send_notification(instance_name)
        if not response == 200:
            return status.HTTP_403_FORBIDDEN, response
        return status.HTTP_200_OK
