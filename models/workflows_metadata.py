from sqlalchemy import func

from db import db


class WorkflowsMetadataModel(db.Model):
    __tablename__ = "workflows_metadata"

    workflow_instance = db.Column(db.String(100), primary_key=True)
    workflow_name = db.Column(db.String(100), db.ForeignKey("workflows.workflow_name"))
    input_parameters = db.Column(db.JSON, nullable=False) #foreign key
    started_on = db.Column(db.DateTime)
    ended_on = db.Column(db.DateTime)
    status = db.Column(db.String(10))
    logs = db.Column(db.VARCHAR(250))
    tag = db.Column(db.String(20))
