import unittest
import requests


class TestObservations(unittest.TestCase):
    def test_insert_observations(self):
        response = requests.post(
            "http://localhost:8000/observations/add_observations/",
            json={
                "data": [
                    {
                        "monitored_id": 3,
                        "observation_name": "Heart Rate",
                        "issued": "2021-09-01T00:00:00Z",
                        "value": 100,
                        "value_type": "Number",
                        "value_unit": "BPM",
                    }
                ]
            },
        )
        self.assertEqual(response.status_code, 200)

    def test_get_observation_by_name(self):
        response = requests.get(
            "http://localhost:8000/observations/get_observations_by_name/?observation_name=Heart%20Rate&monitored_id=3"
        )
        self.assertEqual(response.status_code, 200)

    def test_get_latest_observation_by_name(self):
        response = requests.get(
            "http://localhost:8000/observations/get_latest_observations/?observation_name=Heart%20Rate&monitored_id=3"
        )
        self.assertEqual(response.status_code, 200)

    def test_observation_mean(self):
        response = requests.get(
            "http://localhost:8000/observations/observation_mean/?observation_name=Heart%20Rate&monitored_id=3"
        )
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
