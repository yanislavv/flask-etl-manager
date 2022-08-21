from resources.auth import RegisterResource, LoginResource
from resources.workflows import WorkflowsResource, DeleteWorkflowResource, UpdateWorkflowResource

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
    (UpdateWorkflowResource, "/home/<workflow_name>/update")
)
