from recognizer import Recognizer
from responder import Responder
from tts import TextToSpeech

def main():
    recognizer = Recognizer()
    responder = Responder()
    tts = TextToSpeech()

    while True:
        speech_text = recognizer.recognize_speech()
        if speech_text:
            response = responder.generate_response(speech_text)
            tts.speak(response)

if __name__ == "__main__":
    main()