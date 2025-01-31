import requests
from elevenlabs import ElevenLabs
import logging

class D_ID:
    def __init__(self, dir_logo, dir_photo, dir_document, client_name, voice_description):
        self.client_name = client_name
        self.url_logo = dir_logo
        self.url_photo = dir_photo
        self.url_document = dir_document
    #Create a video in D_ID with TTS and dinamic logo and photo
    def createVideo(self):
        url = "https://api.d-id.com/talks"

        payload = {
            "source_url": "https://d-id-public-bucket.s3.us-west-2.amazonaws.com/alice.jpg",
            "script": {
                "type": "text",
                "subtitles": "false",
                "provider": {
                    "type": "microsoft",
                    "voice_id": "Sara",
                    "model_id": "eleven_multilingual_v2"
                },
                "input": "Making videos is easy with D-ID"
            },
            "config": {
                "logo": {
                    "position": [354, 354],
                    "url": "dadw"
                },
                "fluent": "false",
                "pad_audio": "0.0"
            }
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        response = requests.post(url, json=payload, headers=headers)

        print(response.text)
    def Facial_recognition(self):
        url = "https://api.d-id.com/images"
        try:
            files = {"image": ("20240915_131844.jpg", open("20240915_131844.jpg", "rb"), "image/jpeg")}
            payload = f"-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"source_url\"\r\n\r\nhttps://photossocialplanner.s3.amazonaws.com/photo_cuchito.jpg\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"metadata\"\r\n\r\nanimal\r\n-----011000010111000001101001--"
            headers = {
                "accept": "application/json",
                "authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik53ek53TmV1R3ptcFZTQjNVZ0J4ZyJ9.eyJodHRwczovL2QtaWQuY29tL2ZlYXR1cmVzIjoiIiwiaHR0cHM6Ly9kLWlkLmNvbS9zdHJpcGVfcHJvZHVjdF9pZCI6IiIsImh0dHBzOi8vZC1pZC5jb20vc3RyaXBlX2N1c3RvbWVyX2lkIjoiIiwiaHR0cHM6Ly9kLWlkLmNvbS9zdHJpcGVfcHJvZHVjdF9uYW1lIjoidHJpYWwiLCJodHRwczovL2QtaWQuY29tL3N0cmlwZV9zdWJzY3JpcHRpb25faWQiOiIiLCJodHRwczovL2QtaWQuY29tL3N0cmlwZV9iaWxsaW5nX2ludGVydmFsIjoibW9udGgiLCJodHRwczovL2QtaWQuY29tL3N0cmlwZV9wbGFuX2dyb3VwIjoiZGVpZC10cmlhbCIsImh0dHBzOi8vZC1pZC5jb20vc3RyaXBlX3ByaWNlX2lkIjoiIiwiaHR0cHM6Ly9kLWlkLmNvbS9zdHJpcGVfcHJpY2VfY3JlZGl0cyI6IiIsImh0dHBzOi8vZC1pZC5jb20vY2hhdF9zdHJpcGVfc3Vic2NyaXB0aW9uX2lkIjoiIiwiaHR0cHM6Ly9kLWlkLmNvbS9jaGF0X3N0cmlwZV9wcmljZV9jcmVkaXRzIjoiIiwiaHR0cHM6Ly9kLWlkLmNvbS9jaGF0X3N0cmlwZV9wcmljZV9pZCI6IiIsImh0dHBzOi8vZC1pZC5jb20vcHJvdmlkZXIiOiJnb29nbGUtb2F1dGgyIiwiaHR0cHM6Ly9kLWlkLmNvbS9pc19uZXciOmZhbHNlLCJodHRwczovL2QtaWQuY29tL2FwaV9rZXlfbW9kaWZpZWRfYXQiOiIiLCJodHRwczovL2QtaWQuY29tL29yZ19pZCI6IiIsImh0dHBzOi8vZC1pZC5jb20vYXBwc192aXNpdGVkIjpbIlN0dWRpbyJdLCJodHRwczovL2QtaWQuY29tL2N4X2xvZ2ljX2lkIjoiIiwiaHR0cHM6Ly9kLWlkLmNvbS9jcmVhdGlvbl90aW1lc3RhbXAiOiIyMDI1LTAxLTI5VDE5OjU0OjE3LjU1NloiLCJodHRwczovL2QtaWQuY29tL2FwaV9nYXRld2F5X2tleV9pZCI6IiIsImh0dHBzOi8vZC1pZC5jb20vaGFzaF9rZXkiOiJEUThrYmRyQjJabWtfRVlYRW5GbjgiLCJodHRwczovL2QtaWQuY29tL3ByaW1hcnkiOnRydWUsImh0dHBzOi8vZC1pZC5jb20vZW1haWwiOiJkZXZlbG9wbWVudC5odWJlZGlAZ21haWwuY29tIiwiaHR0cHM6Ly9kLWlkLmNvbS9jb3VudHJ5X2NvZGUiOiJNWCIsImh0dHBzOi8vZC1pZC5jb20vcGF5bWVudF9wcm92aWRlciI6InN0cmlwZSIsImlzcyI6Imh0dHBzOi8vYXV0aC5kLWlkLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDExMzYxNjM5Njk0Mjg0NzE2Mzc0MiIsImF1ZCI6WyJodHRwczovL2QtaWQudXMuYXV0aDAuY29tL2FwaS92Mi8iLCJodHRwczovL2QtaWQudXMuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTczODE4MTU1NSwiZXhwIjoxNzM4MjY3OTU1LCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIHJlYWQ6Y3VycmVudF91c2VyIHVwZGF0ZTpjdXJyZW50X3VzZXJfbWV0YWRhdGEgb2ZmbGluZV9hY2Nlc3MiLCJhenAiOiJHenJOSTFPcmU5Rk0zRWVEUmYzbTN6M1RTdzBKbFJZcSJ9.sDBSGv6ktqTUc6j_ISCIWTSTrKkam0IyBxZo1cWs-GZphLJIzyExjohCGKopPve1B9D67fEViakdfY25GWeyhGFFEzQp2of4MjzyzBOuo3kGKnm4HaXs7V_NXUrgDKro3o-li3i8WzQPPwM3KUOxIDgNiE90MO5W_vtm03lwI_BdHO7LD4TYqykKtUuJCgcIhancMoxEEacFt7DuBqmwDKCJzCFkQy7nh62OH3TbqD6DRXyS7nI5OENfWR06pgNvoBVXZQaLzTLNNWGJ-vPUMh7RZkAlcKs88AYyyPNWHQJ40AAexyT0vYTadDbhFhWwO_YJcMbpy2jqoJv6VXHrtg"
            }

            response = requests.post(url, data=payload, files=files, headers=headers)
            logging.info("Image uploading")

        except Exception as e:
            logging.error(f"There was a problem in uploading the image {str(e)}")
    def create_animation(self):
        url = "https://api.d-id.com/animations"

        payload = {
            "source_url": "https://d-id-public-bucket.s3.us-west-2.amazonaws.com/alice.jpg",
            "session": "Testing_marketing",
            "Agent_name": "Valentina Mosquera",
            "result_url": "dawdw"
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik53ek53TmV1R3ptcFZTQjNVZ0J4ZyJ9.eyJodHRwczovL2QtaWQuY29tL2ZlYXR1cmVzIjoiIiwiaHR0cHM6Ly9kLWlkLmNvbS9zdHJpcGVfcHJvZHVjdF9pZCI6IiIsImh0dHBzOi8vZC1pZC5jb20vc3RyaXBlX2N1c3RvbWVyX2lkIjoiIiwiaHR0cHM6Ly9kLWlkLmNvbS9zdHJpcGVfcHJvZHVjdF9uYW1lIjoidHJpYWwiLCJodHRwczovL2QtaWQuY29tL3N0cmlwZV9zdWJzY3JpcHRpb25faWQiOiIiLCJodHRwczovL2QtaWQuY29tL3N0cmlwZV9iaWxsaW5nX2ludGVydmFsIjoibW9udGgiLCJodHRwczovL2QtaWQuY29tL3N0cmlwZV9wbGFuX2dyb3VwIjoiZGVpZC10cmlhbCIsImh0dHBzOi8vZC1pZC5jb20vc3RyaXBlX3ByaWNlX2lkIjoiIiwiaHR0cHM6Ly9kLWlkLmNvbS9zdHJpcGVfcHJpY2VfY3JlZGl0cyI6IiIsImh0dHBzOi8vZC1pZC5jb20vY2hhdF9zdHJpcGVfc3Vic2NyaXB0aW9uX2lkIjoiIiwiaHR0cHM6Ly9kLWlkLmNvbS9jaGF0X3N0cmlwZV9wcmljZV9jcmVkaXRzIjoiIiwiaHR0cHM6Ly9kLWlkLmNvbS9jaGF0X3N0cmlwZV9wcmljZV9pZCI6IiIsImh0dHBzOi8vZC1pZC5jb20vcHJvdmlkZXIiOiJnb29nbGUtb2F1dGgyIiwiaHR0cHM6Ly9kLWlkLmNvbS9pc19uZXciOmZhbHNlLCJodHRwczovL2QtaWQuY29tL2FwaV9rZXlfbW9kaWZpZWRfYXQiOiIiLCJodHRwczovL2QtaWQuY29tL29yZ19pZCI6IiIsImh0dHBzOi8vZC1pZC5jb20vYXBwc192aXNpdGVkIjpbIlN0dWRpbyJdLCJodHRwczovL2QtaWQuY29tL2N4X2xvZ2ljX2lkIjoiIiwiaHR0cHM6Ly9kLWlkLmNvbS9jcmVhdGlvbl90aW1lc3RhbXAiOiIyMDI1LTAxLTI5VDE5OjU0OjE3LjU1NloiLCJodHRwczovL2QtaWQuY29tL2FwaV9nYXRld2F5X2tleV9pZCI6IiIsImh0dHBzOi8vZC1pZC5jb20vaGFzaF9rZXkiOiJEUThrYmRyQjJabWtfRVlYRW5GbjgiLCJodHRwczovL2QtaWQuY29tL3ByaW1hcnkiOnRydWUsImh0dHBzOi8vZC1pZC5jb20vZW1haWwiOiJkZXZlbG9wbWVudC5odWJlZGlAZ21haWwuY29tIiwiaHR0cHM6Ly9kLWlkLmNvbS9jb3VudHJ5X2NvZGUiOiJNWCIsImh0dHBzOi8vZC1pZC5jb20vcGF5bWVudF9wcm92aWRlciI6InN0cmlwZSIsImlzcyI6Imh0dHBzOi8vYXV0aC5kLWlkLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDExMzYxNjM5Njk0Mjg0NzE2Mzc0MiIsImF1ZCI6WyJodHRwczovL2QtaWQudXMuYXV0aDAuY29tL2FwaS92Mi8iLCJodHRwczovL2QtaWQudXMuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTczODE4MTU1NSwiZXhwIjoxNzM4MjY3OTU1LCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIHJlYWQ6Y3VycmVudF91c2VyIHVwZGF0ZTpjdXJyZW50X3VzZXJfbWV0YWRhdGEgb2ZmbGluZV9hY2Nlc3MiLCJhenAiOiJHenJOSTFPcmU5Rk0zRWVEUmYzbTN6M1RTdzBKbFJZcSJ9.sDBSGv6ktqTUc6j_ISCIWTSTrKkam0IyBxZo1cWs-GZphLJIzyExjohCGKopPve1B9D67fEViakdfY25GWeyhGFFEzQp2of4MjzyzBOuo3kGKnm4HaXs7V_NXUrgDKro3o-li3i8WzQPPwM3KUOxIDgNiE90MO5W_vtm03lwI_BdHO7LD4TYqykKtUuJCgcIhancMoxEEacFt7DuBqmwDKCJzCFkQy7nh62OH3TbqD6DRXyS7nI5OENfWR06pgNvoBVXZQaLzTLNNWGJ-vPUMh7RZkAlcKs88AYyyPNWHQJ40AAexyT0vYTadDbhFhWwO_YJcMbpy2jqoJv6VXHrtg"
        }

        response = requests.post(url, json=payload, headers=headers)
    def getAnimation(self, anamationId):
        url = f"https://api.d-id.com/animations/{anamationId}"

        headers = {
            "accept": "application/json",
            "authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik53ek53TmV1R3ptcFZTQjNVZ0J4ZyJ9.eyJodHRwczovL2QtaWQuY29tL2ZlYXR1cmVzIjoiIiwiaHR0cHM6Ly9kLWlkLmNvbS9zdHJpcGVfcHJvZHVjdF9pZCI6IiIsImh0dHBzOi8vZC1pZC5jb20vc3RyaXBlX2N1c3RvbWVyX2lkIjoiIiwiaHR0cHM6Ly9kLWlkLmNvbS9zdHJpcGVfcHJvZHVjdF9uYW1lIjoidHJpYWwiLCJodHRwczovL2QtaWQuY29tL3N0cmlwZV9zdWJzY3JpcHRpb25faWQiOiIiLCJodHRwczovL2QtaWQuY29tL3N0cmlwZV9iaWxsaW5nX2ludGVydmFsIjoibW9udGgiLCJodHRwczovL2QtaWQuY29tL3N0cmlwZV9wbGFuX2dyb3VwIjoiZGVpZC10cmlhbCIsImh0dHBzOi8vZC1pZC5jb20vc3RyaXBlX3ByaWNlX2lkIjoiIiwiaHR0cHM6Ly9kLWlkLmNvbS9zdHJpcGVfcHJpY2VfY3JlZGl0cyI6IiIsImh0dHBzOi8vZC1pZC5jb20vY2hhdF9zdHJpcGVfc3Vic2NyaXB0aW9uX2lkIjoiIiwiaHR0cHM6Ly9kLWlkLmNvbS9jaGF0X3N0cmlwZV9wcmljZV9jcmVkaXRzIjoiIiwiaHR0cHM6Ly9kLWlkLmNvbS9jaGF0X3N0cmlwZV9wcmljZV9pZCI6IiIsImh0dHBzOi8vZC1pZC5jb20vcHJvdmlkZXIiOiJnb29nbGUtb2F1dGgyIiwiaHR0cHM6Ly9kLWlkLmNvbS9pc19uZXciOmZhbHNlLCJodHRwczovL2QtaWQuY29tL2FwaV9rZXlfbW9kaWZpZWRfYXQiOiIiLCJodHRwczovL2QtaWQuY29tL29yZ19pZCI6IiIsImh0dHBzOi8vZC1pZC5jb20vYXBwc192aXNpdGVkIjpbIlN0dWRpbyJdLCJodHRwczovL2QtaWQuY29tL2N4X2xvZ2ljX2lkIjoiIiwiaHR0cHM6Ly9kLWlkLmNvbS9jcmVhdGlvbl90aW1lc3RhbXAiOiIyMDI1LTAxLTI5VDE5OjU0OjE3LjU1NloiLCJodHRwczovL2QtaWQuY29tL2FwaV9nYXRld2F5X2tleV9pZCI6IiIsImh0dHBzOi8vZC1pZC5jb20vaGFzaF9rZXkiOiJEUThrYmRyQjJabWtfRVlYRW5GbjgiLCJodHRwczovL2QtaWQuY29tL3ByaW1hcnkiOnRydWUsImh0dHBzOi8vZC1pZC5jb20vZW1haWwiOiJkZXZlbG9wbWVudC5odWJlZGlAZ21haWwuY29tIiwiaHR0cHM6Ly9kLWlkLmNvbS9jb3VudHJ5X2NvZGUiOiJNWCIsImh0dHBzOi8vZC1pZC5jb20vcGF5bWVudF9wcm92aWRlciI6InN0cmlwZSIsImlzcyI6Imh0dHBzOi8vYXV0aC5kLWlkLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDExMzYxNjM5Njk0Mjg0NzE2Mzc0MiIsImF1ZCI6WyJodHRwczovL2QtaWQudXMuYXV0aDAuY29tL2FwaS92Mi8iLCJodHRwczovL2QtaWQudXMuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTczODE4MTU1NSwiZXhwIjoxNzM4MjY3OTU1LCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIHJlYWQ6Y3VycmVudF91c2VyIHVwZGF0ZTpjdXJyZW50X3VzZXJfbWV0YWRhdGEgb2ZmbGluZV9hY2Nlc3MiLCJhenAiOiJHenJOSTFPcmU5Rk0zRWVEUmYzbTN6M1RTdzBKbFJZcSJ9.sDBSGv6ktqTUc6j_ISCIWTSTrKkam0IyBxZo1cWs-GZphLJIzyExjohCGKopPve1B9D67fEViakdfY25GWeyhGFFEzQp2of4MjzyzBOuo3kGKnm4HaXs7V_NXUrgDKro3o-li3i8WzQPPwM3KUOxIDgNiE90MO5W_vtm03lwI_BdHO7LD4TYqykKtUuJCgcIhancMoxEEacFt7DuBqmwDKCJzCFkQy7nh62OH3TbqD6DRXyS7nI5OENfWR06pgNvoBVXZQaLzTLNNWGJ-vPUMh7RZkAlcKs88AYyyPNWHQJ40AAexyT0vYTadDbhFhWwO_YJcMbpy2jqoJv6VXHrtg"
        }

        response = requests.get(url, headers=headers)
    def createTalk(self, s3_url, s3_url_post, voiceflow_api):
        import requests

        url = "https://api.d-id.com/talks"

        payload = {
            "source_url": "https://d-id-public-bucket.s3.us-west-2.amazonaws.com/alice.jpg",
            "script": {
                "type": "text",
                "subtitles": True,
                "provider": {
                    "type": "microsoft",
                    "voice_id": "Sara",
                    "model_id": "eleven_multilingual_v2"
                },
                "input": "Solarit is a strong provided of installations of solar panels"
            },
            "config": {
                "logo": {"url": s3_url},
                "fluent": True,
                "pad_audio": "0.0",
                "driver_expressions": {"expressions": [{"expression": "neutral"}]},
                "auto_match": True,
                "result_format": "mp4",
                "output_resolution": 512
            },
            "driver_url": "bank://natural",
            "name": "Test1",
            "result_url": s3_url_post
        }
        headers = {
            "accept": "application/json",
            "x-api-key-external": voiceflow_api,
            "content-type": "application/json",
            "authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik53ek53TmV1R3ptcFZTQjNVZ0J4ZyJ9.eyJodHRwczovL2QtaWQuY29tL2ZlYXR1cmVzIjoiIiwiaHR0cHM6Ly9kLWlkLmNvbS9zdHJpcGVfcHJvZHVjdF9pZCI6IiIsImh0dHBzOi8vZC1pZC5jb20vc3RyaXBlX2N1c3RvbWVyX2lkIjoiIiwiaHR0cHM6Ly9kLWlkLmNvbS9zdHJpcGVfcHJvZHVjdF9uYW1lIjoidHJpYWwiLCJodHRwczovL2QtaWQuY29tL3N0cmlwZV9zdWJzY3JpcHRpb25faWQiOiIiLCJodHRwczovL2QtaWQuY29tL3N0cmlwZV9iaWxsaW5nX2ludGVydmFsIjoibW9udGgiLCJodHRwczovL2QtaWQuY29tL3N0cmlwZV9wbGFuX2dyb3VwIjoiZGVpZC10cmlhbCIsImh0dHBzOi8vZC1pZC5jb20vc3RyaXBlX3ByaWNlX2lkIjoiIiwiaHR0cHM6Ly9kLWlkLmNvbS9zdHJpcGVfcHJpY2VfY3JlZGl0cyI6IiIsImh0dHBzOi8vZC1pZC5jb20vY2hhdF9zdHJpcGVfc3Vic2NyaXB0aW9uX2lkIjoiIiwiaHR0cHM6Ly9kLWlkLmNvbS9jaGF0X3N0cmlwZV9wcmljZV9jcmVkaXRzIjoiIiwiaHR0cHM6Ly9kLWlkLmNvbS9jaGF0X3N0cmlwZV9wcmljZV9pZCI6IiIsImh0dHBzOi8vZC1pZC5jb20vcHJvdmlkZXIiOiJnb29nbGUtb2F1dGgyIiwiaHR0cHM6Ly9kLWlkLmNvbS9pc19uZXciOmZhbHNlLCJodHRwczovL2QtaWQuY29tL2FwaV9rZXlfbW9kaWZpZWRfYXQiOiIiLCJodHRwczovL2QtaWQuY29tL29yZ19pZCI6IiIsImh0dHBzOi8vZC1pZC5jb20vYXBwc192aXNpdGVkIjpbIlN0dWRpbyJdLCJodHRwczovL2QtaWQuY29tL2N4X2xvZ2ljX2lkIjoiIiwiaHR0cHM6Ly9kLWlkLmNvbS9jcmVhdGlvbl90aW1lc3RhbXAiOiIyMDI1LTAxLTI5VDE5OjU0OjE3LjU1NloiLCJodHRwczovL2QtaWQuY29tL2FwaV9nYXRld2F5X2tleV9pZCI6IiIsImh0dHBzOi8vZC1pZC5jb20vaGFzaF9rZXkiOiJEUThrYmRyQjJabWtfRVlYRW5GbjgiLCJodHRwczovL2QtaWQuY29tL3ByaW1hcnkiOnRydWUsImh0dHBzOi8vZC1pZC5jb20vZW1haWwiOiJkZXZlbG9wbWVudC5odWJlZGlAZ21haWwuY29tIiwiaHR0cHM6Ly9kLWlkLmNvbS9jb3VudHJ5X2NvZGUiOiJNWCIsImh0dHBzOi8vZC1pZC5jb20vcGF5bWVudF9wcm92aWRlciI6InN0cmlwZSIsImlzcyI6Imh0dHBzOi8vYXV0aC5kLWlkLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDExMzYxNjM5Njk0Mjg0NzE2Mzc0MiIsImF1ZCI6WyJodHRwczovL2QtaWQudXMuYXV0aDAuY29tL2FwaS92Mi8iLCJodHRwczovL2QtaWQudXMuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTczODE4MTU1NSwiZXhwIjoxNzM4MjY3OTU1LCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIHJlYWQ6Y3VycmVudF91c2VyIHVwZGF0ZTpjdXJyZW50X3VzZXJfbWV0YWRhdGEgb2ZmbGluZV9hY2Nlc3MiLCJhenAiOiJHenJOSTFPcmU5Rk0zRWVEUmYzbTN6M1RTdzBKbFJZcSJ9.sDBSGv6ktqTUc6j_ISCIWTSTrKkam0IyBxZo1cWs-GZphLJIzyExjohCGKopPve1B9D67fEViakdfY25GWeyhGFFEzQp2of4MjzyzBOuo3kGKnm4HaXs7V_NXUrgDKro3o-li3i8WzQPPwM3KUOxIDgNiE90MO5W_vtm03lwI_BdHO7LD4TYqykKtUuJCgcIhancMoxEEacFt7DuBqmwDKCJzCFkQy7nh62OH3TbqD6DRXyS7nI5OENfWR06pgNvoBVXZQaLzTLNNWGJ-vPUMh7RZkAlcKs88AYyyPNWHQJ40AAexyT0vYTadDbhFhWwO_YJcMbpy2jqoJv6VXHrtg"
        }

        response = requests.post(url, json=payload, headers=headers)
    def getTalk(self, talkId):
        url = f"https://api.d-id.com/talks/{talkId}"

        headers = {
            "accept": "application/json",
            "authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik53ek53TmV1R3ptcFZTQjNVZ0J4ZyJ9.eyJodHRwczovL2QtaWQuY29tL2ZlYXR1cmVzIjoiIiwiaHR0cHM6Ly9kLWlkLmNvbS9zdHJpcGVfcHJvZHVjdF9pZCI6IiIsImh0dHBzOi8vZC1pZC5jb20vc3RyaXBlX2N1c3RvbWVyX2lkIjoiIiwiaHR0cHM6Ly9kLWlkLmNvbS9zdHJpcGVfcHJvZHVjdF9uYW1lIjoidHJpYWwiLCJodHRwczovL2QtaWQuY29tL3N0cmlwZV9zdWJzY3JpcHRpb25faWQiOiIiLCJodHRwczovL2QtaWQuY29tL3N0cmlwZV9iaWxsaW5nX2ludGVydmFsIjoibW9udGgiLCJodHRwczovL2QtaWQuY29tL3N0cmlwZV9wbGFuX2dyb3VwIjoiZGVpZC10cmlhbCIsImh0dHBzOi8vZC1pZC5jb20vc3RyaXBlX3ByaWNlX2lkIjoiIiwiaHR0cHM6Ly9kLWlkLmNvbS9zdHJpcGVfcHJpY2VfY3JlZGl0cyI6IiIsImh0dHBzOi8vZC1pZC5jb20vY2hhdF9zdHJpcGVfc3Vic2NyaXB0aW9uX2lkIjoiIiwiaHR0cHM6Ly9kLWlkLmNvbS9jaGF0X3N0cmlwZV9wcmljZV9jcmVkaXRzIjoiIiwiaHR0cHM6Ly9kLWlkLmNvbS9jaGF0X3N0cmlwZV9wcmljZV9pZCI6IiIsImh0dHBzOi8vZC1pZC5jb20vcHJvdmlkZXIiOiJnb29nbGUtb2F1dGgyIiwiaHR0cHM6Ly9kLWlkLmNvbS9pc19uZXciOmZhbHNlLCJodHRwczovL2QtaWQuY29tL2FwaV9rZXlfbW9kaWZpZWRfYXQiOiIiLCJodHRwczovL2QtaWQuY29tL29yZ19pZCI6IiIsImh0dHBzOi8vZC1pZC5jb20vYXBwc192aXNpdGVkIjpbIlN0dWRpbyJdLCJodHRwczovL2QtaWQuY29tL2N4X2xvZ2ljX2lkIjoiIiwiaHR0cHM6Ly9kLWlkLmNvbS9jcmVhdGlvbl90aW1lc3RhbXAiOiIyMDI1LTAxLTI5VDE5OjU0OjE3LjU1NloiLCJodHRwczovL2QtaWQuY29tL2FwaV9nYXRld2F5X2tleV9pZCI6IiIsImh0dHBzOi8vZC1pZC5jb20vaGFzaF9rZXkiOiJEUThrYmRyQjJabWtfRVlYRW5GbjgiLCJodHRwczovL2QtaWQuY29tL3ByaW1hcnkiOnRydWUsImh0dHBzOi8vZC1pZC5jb20vZW1haWwiOiJkZXZlbG9wbWVudC5odWJlZGlAZ21haWwuY29tIiwiaHR0cHM6Ly9kLWlkLmNvbS9jb3VudHJ5X2NvZGUiOiJNWCIsImh0dHBzOi8vZC1pZC5jb20vcGF5bWVudF9wcm92aWRlciI6InN0cmlwZSIsImlzcyI6Imh0dHBzOi8vYXV0aC5kLWlkLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDExMzYxNjM5Njk0Mjg0NzE2Mzc0MiIsImF1ZCI6WyJodHRwczovL2QtaWQudXMuYXV0aDAuY29tL2FwaS92Mi8iLCJodHRwczovL2QtaWQudXMuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTczODE4MTU1NSwiZXhwIjoxNzM4MjY3OTU1LCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIHJlYWQ6Y3VycmVudF91c2VyIHVwZGF0ZTpjdXJyZW50X3VzZXJfbWV0YWRhdGEgb2ZmbGluZV9hY2Nlc3MiLCJhenAiOiJHenJOSTFPcmU5Rk0zRWVEUmYzbTN6M1RTdzBKbFJZcSJ9.sDBSGv6ktqTUc6j_ISCIWTSTrKkam0IyBxZo1cWs-GZphLJIzyExjohCGKopPve1B9D67fEViakdfY25GWeyhGFFEzQp2of4MjzyzBOuo3kGKnm4HaXs7V_NXUrgDKro3o-li3i8WzQPPwM3KUOxIDgNiE90MO5W_vtm03lwI_BdHO7LD4TYqykKtUuJCgcIhancMoxEEacFt7DuBqmwDKCJzCFkQy7nh62OH3TbqD6DRXyS7nI5OENfWR06pgNvoBVXZQaLzTLNNWGJ-vPUMh7RZkAlcKs88AYyyPNWHQJ40AAexyT0vYTadDbhFhWwO_YJcMbpy2jqoJv6VXHrtg"
        }

        response = requests.get(url, headers=headers)
