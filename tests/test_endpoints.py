import pytest
import requests

class TestApiAttendees:
    def test_attendees(self):
        attendees_enpoint = "http://127.0.0.1:5000"
        spec_response = requests.get(attendees_enpoint)
        assert spec_response.status_code == 200
