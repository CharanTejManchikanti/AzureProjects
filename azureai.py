from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
endpoint="https://commentsanalyse.cognitiveservices.azure.com/"
key="03145ea19d2e4d5182fa090b88dbb412"
credential=AzureKeyCredential(key)
client=TextAnalyticsClient(endpoint=endpoint,credential=credential)
