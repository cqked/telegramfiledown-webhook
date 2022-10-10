import json, httpx, shutil
import os
import time

import jsonpath as jsjx

from .message import Message


def main(messages):
    message = Message(messages)
    if message.file_id:
        remess = getfile(message)
    else:
        remess = {
            "method": "sendMessage",
            "chat_id": message.chat_id[0],
            "text": "请不要拿奇怪的东西糊弄我。😠"
        }
    return remess


def getfile(message):
    BOTTOKEN = ''
    BOTURL = 'http://localhost:8081/'
    SAVEDIR = '/Users/fengxiao/Desktop/'
    with httpx.Client(timeout=None) as client:
        filejson = client.post(
            f"{BOTURL + BOTTOKEN}/getfile",
            data={"file_id": message.file_id}
            ).text
        filepath = jsjx.jsonpath(
            json.loads(filejson),
            "$..file_path"
            )[0]
        filedir = SAVEDIR + str(message.media_group_id) + '/' if message.media_group_id else SAVEDIR
        filename = getfilename(message, filepath)
        if not os.path.exists(filedir):
            os.mkdir(filedir)
        shutil.move(filepath, filedir + filename)
        remess = {"method": "sendMessage",
                  "chat_id": message.chat_id[0],
                  "text": "文件保存成功。✅"}
        return remess


def getfilename(message, filepath) -> str:
    hz = filepath.split('.')[-1]
    if message.file_name:
        filename = message.file_name
    else:
        filename = (str(time.strftime('%Y-%m-%d', time.localtime())) +
                    message.file_unique_id +
                    '.' +
                    hz)
    return filename
