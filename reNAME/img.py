import json
import requests

url = "https://ocr.asprise.com/api/v1/receipt"
image = '2.png'

res = requests.post(url,
                    data = {
                        'api_key': 'TEST',
                        'recognizer': 'auto',
                        'ref_no': 'ocr_python_123'
                    },
                    files = {
                        'files':open(image, 'rb')
                    })

with open('response1.json','w') as f:
    json.dump(json.loads(res.text),f)


