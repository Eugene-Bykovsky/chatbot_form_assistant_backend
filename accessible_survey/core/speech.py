import requests


def text_to_speech(text, folder_id, iam_token):
    url = "https://tts.api.cloud.yandex.net/speech/v1/tts:synthesize"
    headers = {'Authorization': f'Bearer {iam_token}'}
    data = {
        'text': text,
        'lang': 'ru-RU',
        'voice': 'alena',
        'folderId': folder_id,
        'format': 'oggopus',
        'sampleRateHertz': 48000,
    }
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        return response.content
    else:
        raise Exception(f"TTS error: {response.text}")
