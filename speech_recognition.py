import azure.cognitiveservices.speech as speechsdk #azure library for congitive service speech
import json #json library

def recognize_from_microphone():

    speech_config = speechsdk.SpeechConfig(subscription='INSERT SUBSCRIPTION HERE', region='eastus') # Key to connect to Azure servers for speech service
    speech_config.speech_recognition_language="en-US"# set as english

    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True) # uses default mic on your computer
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config) # Recognizes when a voice is comming through to the pc

    print("Speak into your microphone.")# prompts user to speak into mic
    speech_recognition_result = speech_recognizer.recognize_once_async().get()# checks when there has been a notible length of silence

    if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech: # if the result = the recognized speech prints to json file as string
        with open('speech_rec.json', 'a') as f:
            json.dump(speech_recognition_result.text, f) # dumps it into file
            f.write('\n')
            print("sent to json file")
            
