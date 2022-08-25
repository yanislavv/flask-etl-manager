from db import db
from models.workflows import WorkflowsModel


class WorkflowManager:
    @staticmethod
    def create_workflow(data):
        workflow = WorkflowsModel(**data)
        db.session.add(workflow)
        return workflow

    @staticmethod
    def get_workflow():
        return WorkflowsModel.query.all()

    @staticmethod
    def delete_workflow(workflow_name):
        WorkflowsModel.query.filter(WorkflowsModel.workflow_name == workflow_name).delete()

    @staticmethod
    def update_workflow(workflow_name, new_params):
        old_params = WorkflowsModel.query.filter(WorkflowsModel.workflow_name == workflow_name).first()
        WorkflowsModel.query.filter(WorkflowsModel.workflow_name == workflow_name).update({"workflow_parameters": new_params})
        return old_params
