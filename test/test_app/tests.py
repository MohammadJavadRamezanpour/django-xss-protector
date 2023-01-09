import json

from django.test import TestCase


class XSSTest(TestCase):
    def test_get_with_malformed_url_parameters(self):
        response1 = self.client.get("/test/<jjbkb/")
        response2 = self.client.get("/test/<jjbkb>/")
        response3 = self.client.get("/test/guyjh/")

        self.assertEqual(response1.status_code, 400)
        self.assertEqual(response2.status_code, 400)
        self.assertEqual(response3.status_code, 200)

    def test_get_with_malformed_url_querystring(self):
        response1 = self.client.get("/test/sdf/?idk=<sdf")
        response2 = self.client.get("/test/dfsdf/?idk=<jjbkb>")
        response3 = self.client.get("/test/guyjh/?idk=sdf")
        response4 = self.client.get(
            "/test_excluding/guyjh/?excluding_key=>sdf")
        response5 = self.client.get(
            "/test_keys/guyjh/?key1=<sdf&not_important_key=sdfsdf")
        response6 = self.client.get(
            "/test_keys/guyjh/?key1=sdf&not_important_key=sd<>fsdf")

        self.assertEqual(response1.status_code, 400)
        self.assertEqual(response2.status_code, 400)
        self.assertEqual(response3.status_code, 200)
        self.assertEqual(response4.status_code, 200)
        self.assertEqual(response5.status_code, 400)
        self.assertEqual(response6.status_code, 200)

    def test_post_with_malformed_body(self):
        response1 = self.client.post(
            "/test/sdf/", {"key1": "<dgdf"}, content_type="application/json")
        response2 = self.client.post(
            "/test/dfsdf/", {"key2": "val2<<>"}, content_type="application/json")
        response3 = self.client.post(
            "/test/guyjh/", {"key1": "val1"}, content_type="application/json")
        response4 = self.client.post(
            "/test_excluding/guyjh/", {"excluding_key": "va<>l1", "key": "sdfsdf"}, content_type="application/json")
        response5 = self.client.post(
            "/test_keys/guyjh/", {"key2": "va<>l1", "key": "sdfsdf"}, content_type="application/json")
        response6 = self.client.post(
            "/test_keys/guyjh/", {"key2": "val1", "key": "sdf<>sdf"}, content_type="application/json")

        self.assertEqual(response1.status_code, 400)
        self.assertEqual(response2.status_code, 400)
        self.assertEqual(response3.status_code, 200)
        self.assertEqual(response4.status_code, 200)
        self.assertEqual(response5.status_code, 400)
        self.assertEqual(response6.status_code, 200)

    def test_post_with_malformed_formdata(self):
        response1 = self.client.post(
            "/test/sdf/", json.dumps({"key1": "<dgdf"}), content_type="application/x-www-form-urlencoded")
        response2 = self.client.post(
            "/test/dfsdf/", json.dumps({"key2": "val2<<>"}), content_type="application/x-www-form-urlencoded")
        response3 = self.client.post(
            "/test/guyjh/", json.dumps({"key1": "val1"}), content_type="application/x-www-form-urlencoded")
        response4 = self.client.post(
            "/test_excluding/guyjh/", json.dumps({"key1": "val1", "excluding_key": ">dsfsd<"}), content_type="application/x-www-form-urlencoded")
        response5 = self.client.post(
            "/test_keys/guyjh/", json.dumps({"key1": "val1<<", "key": "dsfsd"}), content_type="application/x-www-form-urlencoded")
        response6 = self.client.post(
            "/test_keys/guyjh/", json.dumps({"key1": "val1", "key": ">><dsfsd"}), content_type="application/x-www-form-urlencoded")

        self.assertEqual(response1.status_code, 400)
        self.assertEqual(response2.status_code, 400)
        self.assertEqual(response3.status_code, 200)
        self.assertEqual(response4.status_code, 200)
        self.assertEqual(response5.status_code, 400)
        self.assertEqual(response6.status_code, 200)
