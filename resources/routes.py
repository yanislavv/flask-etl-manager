from resources.auth import RegisterResource, LoginResource
from resources.workflows import WorkflowsResource, DeleteWorkflowResource, UpdateWorkflowResource
from resources.workflows_metadata import WorkflowMetadataResource, GetWorkflowStatus, WorkflowMetadataUpdateResource

# routes = (
#     (RegisterResource, "/register"),
#     (LoginResource, "/login"),
#     (ComplaintsResource, "/complaint"),
#     (ApproveComplaintResource, "/complaint/<int:id>/approve"),
#     (RejectComplaintResource, "/complaint/<int:id>/reject"),
# )

routes = (
    (RegisterResource, "/register"),
    (LoginResource, "/login"),
    (WorkflowsResource, "/home"),
    (DeleteWorkflowResource, "/home/<workflow_name>"),
    (UpdateWorkflowResource, "/home/<workflow_name>/update"),
    (WorkflowMetadataResource, "/instances"),
    (WorkflowMetadataUpdateResource, "/instances/<instance_name>"),
    (GetWorkflowStatus, "/instances/<instance_name>/status")
)
