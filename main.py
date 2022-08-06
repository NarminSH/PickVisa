import requests
import base64
import ast
from contractsPY import if_fails, Usecase

application_id = "29d4e487-9daa-476e-b9e0-e544980d0a9f"
application_password = "N/cIR/1Worw13yDxA8WaVuVD"

to_encode = application_id + ":" + application_password

to_encode_bytes = to_encode.encode("ascii")
base64_bytes = base64.b64encode(to_encode_bytes)
base64_string = base64_bytes.decode("ascii")



@if_fails(message="Could not process request")
def send_passport_image(state):
    print('heree')
    image_data = open(state.image,'rb').read()
    state.headers = {'Authorization': 'Basic %s' % base64_string}

    state.task_info = requests.post(url="https://cloud-eu.ocrsdk.com/v2/processMRZ", data=image_data, headers=state.headers)
    return True if state.task_info.status_code==200 else False
    
    
@if_fails(message="Could not get task id")
def get_task_info(state):
    contents = state.task_info.content
    dict_str = contents.decode("UTF-8")
    mydata = ast.literal_eval(dict_str)

    state.task_id = mydata["taskId"]
    return True if state.task_id else False


@if_fails(message="There was a problem getting passport data")
def get_task_url(state):
    task = requests.get(url="https://cloud-eu.ocrsdk.com/v2/getTaskStatus", params={"taskId": state.task_id}, headers=state.headers)
    return True if task.status_code==200 else False

send_passport = Usecase()
send_passport.contract = [send_passport_image, get_task_info, get_task_url]


if  __name__ == '__main__':
    result = send_passport.apply(image='passport_images/Passport_example.jpg')
    print(result)