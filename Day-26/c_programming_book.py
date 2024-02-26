import requests
import sys

baseUrl = "https://api.vidadynamics.com/api/v1/file-management-download?attachment_ids[]=3"

authToken = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI5YjZiOTNhYy05NTE5LTQ1OTgtYmIwZi02NWNmMDdjMWE2ZDkiLCJqdGkiOiIwNTA4MjBhMGQ4NTgyMWEyZmE3ZWQ3MjcxYWVhNTk4MGM4M2MxM2IwNjBhODdlMDYzNDlmODE3ZjVjNDQxNWU2NDZiOWJhN2JhYmMyMGEwZCIsImlhdCI6MTcwODk3MTg2OC4zNzc3OTgsIm5iZiI6MTcwODk3MTg2OC4zNzc4MDEsImV4cCI6MTc0MDU5NDI2OC4zNzQ2MDMsInN1YiI6IjEiLCJzY29wZXMiOlsidXNlciJdfQ.Mbvxq9OCPEEgx_NM9xpUdY8cHqXGiBOdfUKTGcHGcqz9lpaGVNqDihRnoCsCEzezKPc4kM52RG3jGXcc4ODpHLdndOpjMIcDkfdUxWmYtNx0Br8wLBs0smB2tbjDmmHszPb4QL9TOO5imX4xKcb6wnuWAYgOifrFbe6tT6k3zMD2PsngOj5EXejAHR3TiTvrEQ422kruGnUSSkhp4vAyfMfF2IH0KtSONKqAe7zmg3C-eiqdgzvrcu9ZHWlxqh3C1zfggd11zRnRZ9ne3YYrZZ-Mbblwlhfjs9c0PM4a-l-gzDYCHHKMuVx29v3TfHvfvm9t4PEF_gyc5JkiFxVHbwM2u9EnNQ7UMansoA_vFwh7zYjWZlUteXa_BS8Ajy5pOJCTNH-kFPRtu5YAO_c1nRnd-hDyGyZCBffZoCgzosEIems8NyLpZyPLD-iSDOMC98bHgAbpFHSaQHa7gDuo_hVA2-XkK2cngVpWbV6Z4g49cpX6l3yi8PE3ZZTS0_Ld3G9lLAtcAu28VCbS1lV0NWN16jBdNUdXRGdu-d0eI5emy7lENx7NiRdkL-fh81RwnReLyUYyBIDrmg5qvVUkIa1mmQLyc7zAWudoZ2jTa0RYGlAxuJVSGf3N1bzKW6Jio5mOkdOPgEjTaH27p1UyY696rx0EgFZCT--5TC8cTtA"

infoDt = {
    'name': 'Jone Dev',
    'email': 'jonecoder@gmail.com',
    'username': 'JoneCoder',
}

# res = requests.post(url=baseUrl, headers={'Authorization': f'Bearer {authToken}'}, data=infoDt)
res = requests.get(url=baseUrl, headers={'Authorization': f'Bearer {authToken}'})

if res.ok is False:
    sys.exit("Error downloading the file")

with open('vidadynamics.jpg', 'wb') as fb:
    fb.write(res.content)

print('Image download complete')
