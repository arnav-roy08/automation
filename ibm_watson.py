from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator(' ')
text_to_speech = TextToSpeechV1(
    authenticator=authenticator
)

text_to_speech.set_service_url(
    'https://api.eu-de.text-to-speech.watson.cloud.ibm.com/instances/11b82e92-ce2e-4f80-aa50-ff600f70e3fc')
text_to_speech.set_disable_ssl_verification(True)

with open('test.mp3', 'wb') as audio_file:
    audio_file.write(
        text_to_speech.synthesize(
            '<prosody rate="-8%">Poveglia Island, Venice, Italy.<break strength="weak">weak pause</break>A short trip from Venice, the beautiful island of Poveglia was a quarantine zone for people suffering from the plague. In addition, the island was used in the early 20th century as an insane asylum. Ghost hunters claim this spot is a hotbed of paranormal activity.<break strength="medium">medium pause</break> The Stanley Hotel, Estes Park, Colorado.<break strength="weak">weak pause</break>This famous Rocky Mountain destination is known as one of the inspirations for Stephen King’s “The Shining,” but it also has its own spooky past. Allegedly, staff has encountered ghosts during their time there, such as a maid from Room 217 who is known to pack away guests’ clothing when they aren’t looking.<break strength="medium">medium pause</break> Tower of London, London, England.<break strength="weak">weak pause</break>Many historic people have called the Tower of London their final resting place. The infamous fortress has been steeped in tragedy for over 900 years, and it\'s home to many ghostly sightings of English royalty, including Anne Boleyn and Mary, Queen of Scots.<break strength="medium">medium pause</break> It’s said that “the world outside had its own rules, and those rules were not human.”<break strength="medium">medium pause</break></prosody>',
            voice='en-US_KevinV3Voice',
            accept='audio/mp3'
        ).get_result().content)