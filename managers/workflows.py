from werkzeug.exceptions import BadRequest

from db import db
from models.workflows import WorkflowsModel


class WorkflowManager:
    @staticmethod
    def create_workflow(data):
        workflow = WorkflowsModel(**data)
        db.session.add(workflow)
        db.session.commit()
        return workflow

    @staticmethod
    def get_workflows():
        return WorkflowsModel.query.all()

    @staticmethod
    def delete_workflow(workflow_name):
        workflow = WorkflowsModel.query.filter(WorkflowsModel.workflow_name == workflow_name).delete()
        db.session.commit()
        return workflow

    @staticmethod
    def update_workflow(workflow_name, new_params):
        workflow = WorkflowsModel.query.filter(WorkflowsModel.workflow_name == workflow_name).first() #maybe not needed
        WorkflowsModel.query.filter(WorkflowsModel.workflow_name == workflow_name).update({"workflow_parameters": new_params})
        db.session.commit()
