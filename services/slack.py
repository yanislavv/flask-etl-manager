from slack_sdk.webhook import WebhookClient

url = "https://hooks.slack.com/services/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"


def send_message(text):
    webhook = WebhookClient(url)
    response = webhook.send(text=text)
    return response
