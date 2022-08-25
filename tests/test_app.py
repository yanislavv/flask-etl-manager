from flask_testing import TestCase

from config import create_app
from db import db
from tests.factories import UserFactoryAdmin, UserFactoryDeveloper
from tests.helpers import generate_token

ENDPOINTS_DATA = (
    #("/home", "GET"),
    ("/home", "POST"),
    ("/home/etl_job1/delete", "DELETE"),
    #("/home/<workflow_name>/update", "PUT"),
)


class TestApp(TestCase):
    def create_app(self):
        return create_app("config.TestConfig")

    def setUp(self):
        db.init_app(self.app)
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def iterate_endpoints(
            self,
            endpoints_data,
            status_code_method,
            expected_resp_body,
            headers=None,
            payload=None,
    ):
        if not headers:
            headers = {}
        if not payload:
            payload = {}

        resp = None
        for url, method in endpoints_data:
            if method == "GET":
                resp = self.client.get(url, headers=headers)
            elif method == "POST":
                resp = self.client.post(url, headers=headers)
            elif method == "PUT":
                resp = self.client.put(url, headers=headers)
            elif method == "DELETE":
                resp = self.client.delete(url, headers=headers)
            status_code_method(resp)
            self.assertEqual(resp.json, expected_resp_body)

    def test_login_required(self):
        self.iterate_endpoints(
            ENDPOINTS_DATA, self.assert_401, {"message": "Missing token"}
        )

    def test_invalid_token_raises(self):
        headers = {"Authorization": "Bearer eyJ0eX"}
        self.iterate_endpoints(
            ENDPOINTS_DATA, self.assert_401, {"message": "Invalid token"}, headers
        )

    def test_missing_permissions_for_admin_raises(self):
        endpoints = (
            ("/home", "POST"),
        )
        user = UserFactoryDeveloper()
        token = generate_token(user)
        headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
        resp = None
        for url, method in endpoints:
            if method == "POST":
                resp = self.client.post(url, headers=headers)
            self.assert403(resp)
            self.assertEqual(resp.json, {'message': 'Permission denied!'})

    def test_create_workflow_schema_raises_missing_workflow_parameters_field(self):
        data = {"workflow_name": "import_job1"}
        url = "/home"
        user = UserFactoryAdmin()
        token = generate_token(user)
        headers = {"Content-Type": "application/json", "Authorization": f"Bearer {token}"}

        resp = self.client.post(url, headers=headers, json=data)
        self.assert400(resp)
        assert resp.json == {'message': {'workflow_parameters': ['Missing data for required field.']}}
    #
    #     data["first_name"] = "A"
    #     resp = self.client.post(url, headers=headers, json=data)
    #     self.assert400(resp)
    #     assert resp.json == {'message': {'first_name': ['Length must be between 2 and 20.']}}
    #
    #     data["first_name"] = "AAAAAAAAAAAAAAAAAAAAAAA"
    #     resp = self.client.post(url, headers=headers, json=data)
    #     self.assert400(resp)
    #     assert resp.json == {'message': {'first_name': ['Length must be between 2 and 20.']}}

    def test_create_workflow(self):
        user = UserFactoryAdmin()
        token = generate_token(user)
        headers = {"Content-Type": "application/json", "Authorization": f"Bearer {token}"}
        url = "/home"
        data = {"workflow_name": "import_job1","workflow_parameters": {"sdf": "sdfs"}}

        resp = self.client.post(url, headers=headers, json=data)
        assert resp.status == "201 CREATED"

    def test_delete_workflow(self):
        user = UserFactoryAdmin()
        token = generate_token(user)
        headers = {"Content-Type": "application/json", "Authorization": f"Bearer {token}"}
        url = "/home/import_job1/delete"

        resp = self.client.delete(url, headers=headers)
        self.assert200(resp)
