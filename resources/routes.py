from resources.auth import RegisterResource, LoginResource
#TODO import methods for each route

# routes = (
#     (RegisterResource, "/register"),
#     (LoginResource, "/login"),
#     (ComplaintsResource, "/complaint"),
#     (ApproveComplaintResource, "/complaint/<int:id>/approve"),
#     (RejectComplaintResource, "/complaint/<int:id>/reject"),
# )

routes = (
    (RegisterResource, "/register"),
    (LoginResource, "/login")
)
