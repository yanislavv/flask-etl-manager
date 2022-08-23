from db import db
from models.workflows_metadata import WorkflowsMetadataModel


class WorkflowsMetadataManager:
    @staticmethod
    def create_instance(data):
        workflow = WorkflowsMetadataModel(**data)
        db.session.add(workflow)
        db.session.commit()
        return workflow

    @staticmethod
    def update_instance_details(instance_name, data):
        WorkflowsMetadataModel.query.filter(WorkflowsMetadataModel.workflow_instance == instance_name)\
            .update({"started_on": data["start"], "ended_on": data["end"], "logs": data["logs_url"], "status": data["status"]})
        db.session.commit()

    @staticmethod
    def get_status_instance(instance_name):
        workflow = WorkflowsMetadataModel.query.filter(WorkflowsMetadataModel.workflow_instance == instance_name).first()
        return workflow.status

