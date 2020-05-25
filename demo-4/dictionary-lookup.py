# -*- coding: utf-8 -*-

import os, requests, uuid, json, dotenv

# Including the dotenv (https://preslav.me/2019/01/09/dotenv-files-python/)

from dotenv import load_dotenv
load_dotenv()

subscription_key = os.getenv("TRANSLATOR_TEXT_SUBSCRIPTION_KEY")
endpoint = os.getenv("TRANSLATOR_TEXT_ENDPOINT")

# All the informations about the params (https://docs.microsoft.com/en-us/azure/cognitive-services/translator/reference/v3-0-translate)
# Languages have support to the Translator Text (https://docs.microsoft.com/es-es/azure/cognitive-services/translator/language-support)
path = '/dictionary/lookup?api-version=3.0'
params = '&from=en&to=es'
constructed_url = endpoint + path + params

headers = {
  'Ocp-Apim-Subscription-Key': subscription_key,
  'Content-type': 'application/json',
  'X-ClientTraceId': str(uuid.uuid4())
}

body = [{
  'text': 'cheese'
}]

request = requests.post(constructed_url, headers=headers, json=body)
response = request.json()

# Printing the request to translato from En to Es
print(json.dumps(response, sort_keys=True, indent=4,
                 ensure_ascii=False, separators=(',', ': ')))