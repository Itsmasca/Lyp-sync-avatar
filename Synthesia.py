import requests
from models import Solardata

class Synthesia:
    def __init__(self):
        self.synthesiaapi = "eb3222ac6e13a7beb7bc8d51246ed9a8"
        self.template_id = "9a1683e8-4bc4-42a4-8062-c60ee942662a"
    def uploadImage(self, file):
        url = "https://upload.api.synthesia.io/v2/assets"

        payload = {
            "file": file
        }

        headers = {
            "accept": "application/json",
            "content-type": "image/jpeg",
            "Authorization": "a8509c53e5436a79b804870ec9825091"
        }

        response = requests.post(url,data= payload, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return data.get("templates", [])
        else:
            print("Error:", response.status_code, response.text)
            return []
    def uploadAudio(self, file):
        url = "https://upload.api.synthesia.io/v2/scriptAudio"

        payloads = {
            "file": file
        }

        headers = {
            "accept": "application/json",
            "Content-Type": "audio/mpeg",
            "Authorization": "a8509c53e5436a79b804870ec9825091"
        }

        response = requests.post(url, data= payloads, headers=headers)
        if response.status_code == 200:
            data = response.json()
            # 'templates' is a key in the JSON response, not an attribute on 'response'
            return data.get("templates", [])
        else:
            print("Error:", response.status_code, response.text)
            return []
    def ListTemplates(self):
        url = "https://api.synthesia.io/v2/templates?limit=20&offset=0&source=synthesia"

        headers = {
            "accept": "application/json",
            "Authorization": self.synthesiaapi
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            # 'templates' is a key in the JSON response, not an attribute on 'response'
            return data.get("templates", [])
        else:
            print("Error:", response.status_code, response.text)
            return []

    def retrieveTemplate(self, template_id):
        url = f"https://api.synthesia.io/v2/templates/{template_id}"

        headers = {"accept": "application/json",
                   "Authorization": self.synthesiaapi}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            self.template_id = data.get("id")
            return data
        else:
            print("Error:", response.status_code, response.text)
            return []
    def Create_video_template(self, data: Solardata):
        url = "https://api.synthesia.io/v2/videos/fromTemplate"

        payload = {
            "test": True,
            "templateData": data.dict(),
            "visibility": "private",
            "templateId": self.template_id,
            "description": "Video generated with Solarit v1.0.12",
            "title": f"Video generated for {data.dict().get('customer_name')}",
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "Authorization": self.synthesiaapi
        }

        response = requests.post(url, json=payload, headers=headers)

        if response.status_code == 200:
            data = response.json()
            return {"status": "send it to process"}
        else:
            print("Error:", response.status_code, response.text)
            return []
    def Get_video(self, video_id):
        url = f"https://api.synthesia.io/v2/videos/{video_id}"

        headers = {
            "accept": "application/json",
            "Authorization": "a8509c53e5436a79b804870ec9825091"
        }

        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print("Error:", response.status_code, response.text)
            return []