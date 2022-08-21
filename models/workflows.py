from sqlalchemy import func

from db import db


class WorkflowsModel(db.Model):
    __tablename__ = "workflows"

    workflow_name = db.Column(db.String(100), primary_key=True)
    workflow_parameters = db.Column(db.JSON, nullable=False)
    created_on = db.Column(db.DateTime, nullable=False, server_default=func.now())
