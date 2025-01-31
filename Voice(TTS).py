from elevenlabs import ElevenLabs
import logging


class Voice:
    def __init__(self):
        self.TTS_apikey = "dadwd"
    def Create_personal_voice(self):
        client = ElevenLabs(
            api_key=self.TTS_apikey,
        )
        try:
            response = client.voices.add(
                name={"type": "json", "value": self.client_name},
                remove_background_noise={"type": "json", "value": True},
                description={
                    "type": "json",
                    "value": self.voice_description
                }
            )
            logging.info(f"Voice successfully created: {self.response}")
            return response.voice_id
        except Exception as e:
            logging.error(f"Error creating personal voice: {str(e)}")
            return None
    def getVoice(self, voiceId):
        client = ElevenLabs(api_key=self.TTS_apikey, )
        client.voices.get(
            voice_id="JBFqnCBsd6RMkjVDRZzb"
        )