from decouple import config

from slack_sdk.webhook import WebhookClient

url = config('SLACK_URL')


def send_message(text):
    webhook = WebhookClient(url)
    response = webhook.send(text=text)
    return response.status_code
