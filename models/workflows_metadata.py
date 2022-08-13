from sqlalchemy import func

from db import db


class WorkflowsMetadataModel(db.Model):
    __tablename__ = "workflows_metadata"

    workflow_instance = db.Column(db.String(100), primary_key=True)
    workflow_name = db.Column(db.String(100), db.ForeignKey("workflows.workflow_name"))
    input_parameters = db.Column(db.JSON, nullable=False)
    started_on = db.Column(db.DateTime, nullable=False)
    ended_on = db.Column(db.DateTime, nullable=False)
    logs = db.Column(db.VARCHAR(250), nullable=False)
    tag = db.Column(db.String(20))
