from db import db
from models.workflows_metadata import WorkflowsMetadataModel
from services.slack import send_message


class WorkflowsMetadataManager:
    @staticmethod
    def create_instance(data):
        workflow = WorkflowsMetadataModel(**data)
        db.session.add(workflow)
        return workflow

    @staticmethod
    def update_instance_details(instance_name, data):
        WorkflowsMetadataModel.query.filter(WorkflowsMetadataModel.workflow_instance == instance_name)\
            .update({"started_on": data["start"], "ended_on": data["end"], "logs": data["logs_url"], "status": data["status"]})

    @staticmethod
    def send_notification(instance_name):
        workflow = WorkflowsMetadataModel.query.filter(WorkflowsMetadataModel.workflow_instance == instance_name).first()
        status = workflow.status
        if status == 'FAILED':
            slack_msg = """
                        :red_circle: *Job failed*:
                    *Job*: {instance_name}
                    *Log url*: {log_url}
                        """.format(instance_name=instance_name, log_url=workflow.logs)
            response = send_message(slack_msg)
            return response, status
        return 200, status

