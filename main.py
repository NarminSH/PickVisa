import requests
import base64
import ast


application_id = "29d4e487-9daa-476e-b9e0-e544980d0a9f"
application_password = "N/cIR/1Worw13yDxA8WaVuVD"

to_encode = application_id + ":" + application_password

to_encode_bytes = to_encode.encode("ascii")
base64_bytes = base64.b64encode(to_encode_bytes)
base64_string = base64_bytes.decode("ascii")
print(base64_string, "base 64 string")

url = "https://cloud-eu.ocrsdk.com/v2/processMRZ"

image_data = open('passport_images/Passport_example.jpg','rb').read()

headers = {'Authorization': 'Basic %s' % base64_string}
print(headers)

url = requests.post(url=url, data=image_data, headers=headers)
contents = url.content
print(contents)
dict_str = contents.decode("UTF-8")
mydata = ast.literal_eval(dict_str)

task_id = mydata["taskId"]
print(task_id, type(task_id))

task = requests.get(url="https://cloud-eu.ocrsdk.com/v2/getTaskStatus", params={"taskId": task_id}, headers=headers)
print(task.content)


  
