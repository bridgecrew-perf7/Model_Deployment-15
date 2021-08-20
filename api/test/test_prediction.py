import unittest
import json
from flask import Flask
from endpoints.prediction import prediction_api

app = Flask(__name__)
app.register_blueprint(prediction_api)

# Create local tester
tester = app.test_client()


class ClassificationTests(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(ClassificationTests, self).__init__(*args, **kwargs)

    def test_predict_single(self):
        response = tester.post(
            '/predict',
            data=json.dumps(
                [
                 {"x5_saturday": 1, "x81_July": 1, "x81_December": 1,
                  "x31_japan": 1, "x81_October": 1, "x5_sunday": 1,
                  "x31_asia": 1, "x81_February": 1, "x91": 1,
                  "x81_May": 1, "x5_monday": 1, "x81_September": 1,
                  "x81_March": 1, "x53": 1, "x81_November": 1,
                  "x44": 1, "x81_June": 1, "x12": 1,
                  "x5_tuesday": 1, "x81_August": 1, "x81_January": 1,
                  "x62": 1, "x31_germany": 1, "x58": 1, "x56": 1}
                 ]),
            content_type='application/json'
        )

        data = response.get_data(as_text=True)
        print("Single Call: "+str(data))
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(data)

    def test_predict_triple(self):
        response = tester.post(
            '/predict',
            data=json.dumps([
                {"x5_saturday": 1, "x81_July": 1, "x81_December": 1,
                 "x31_japan": 1, "x81_October": 1, "x5_sunday": 1,
                 "x31_asia": 1, "x81_February": 1, "x91": 1,
                 "x81_May": 1, "x5_monday": 1, "x81_September": 1,
                 "x81_March": 1, "x53": 1, "x81_November": 1,
                 "x44": 1, "x81_June": 1, "x12": 1,
                 "x5_tuesday": 1, "x81_August": 1, "x81_January": 1,
                 "x62": 1, "x31_germany": 1, "x58": 1, "x56": 1},
                {"x5_saturday": 1, "x81_July": 1, "x81_December": 1,
                 "x31_japan": 1, "x81_October": 1, "x5_sunday": 1,
                 "x31_asia": 1, "x81_February": 1, "x91": 1,
                 "x81_May": 1, "x5_monday": 1, "x81_September": 1,
                 "x81_March": 1, "x53": 1, "x81_November": 1,
                 "x44": 1, "x81_June": 1, "x12": 1,
                 "x5_tuesday": 1, "x81_August": 1, "x81_January": 1,
                 "x62": 1, "x31_germany": 1, "x58": 1, "x56": 1},
                {"x5_saturday": 1, "x81_July": 1, "x81_December": 1,
                 "x31_japan": 1, "x81_October": 1, "x5_sunday": 1,
                 "x31_asia": 1, "x81_February": 1, "x91": 1,
                 "x81_May": 1, "x5_monday": 1, "x81_September": 1,
                 "x81_March": 1, "x53": 1, "x81_November": 1,
                 "x44": 1, "x81_June": 1, "x12": 1,
                 "x5_tuesday": 1, "x81_August": 1, "x81_January": 1,
                 "x62": 1, "x31_germany": 1, "x58": 1, "x56": 1}
                    ]),
            content_type='application/json'
        )

        data = response.get_data(as_text=True)
        print("Batch Call: "+str(data))
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(data)

    def test_predict_missing(self):
        response = tester.post(
            '/predict',
            data=json.dumps(
                [
                 {"x81_July": 1, "x81_December": 1, "x31_japan": 1,
                  "x81_October": 1, "x5_sunday": 1, "x31_asia": 1,
                  "x81_February": 1, "x91": 1, "x81_May": 1,
                  "x5_monday": 1, "x81_September": 1, "x81_March": 1,
                  "x53": 1, "x81_November": 1, "x44": 1,
                  "x81_June": 1, "x12": 1, "x5_tuesday": 1,
                  "x81_August": 1, "x81_January": 1, "x62": 1,
                  "x31_germany": 1, "x58": 1, "x56": 1}
                ]),
            content_type='application/json'
        )

        data = response.get_data(as_text=True)
        print("Missing variable test: "+str(data))
        self.assertEqual(str(data), "Number of variables != 25")
        self.assertIsNotNone(data)


if __name__ == '__main__':
    unittest.main()
