'''
Sent file to fac++
'''

import json
import requests
import recommand
import database
import sys
import threading

face_tokens = dict()

url_detect= 'https://api-cn.faceplusplus.com/facepp/v3/detect'
payload_detect = {'api_key': 'rRkNdobPRD2yYfhdCZqkGOArrLQPttM5',
           'api_secret': 'yM_LfSYb9E5glWhWGPOWAIjIhSCAveQU',
           'return_landmark': 1,
           'return_attributes':'gender,age,emotion'}

url_search=  'https://api-cn.faceplusplus.com/facepp/v3/search'
payload_search = {'api_key': 'rRkNdobPRD2yYfhdCZqkGOArrLQPttM5',
           'api_secret': 'yM_LfSYb9E5glWhWGPOWAIjIhSCAveQU',
           'outer_id': 'faces'}

url_creat= 'https://api-cn.faceplusplus.com/facepp/v3/faceset/create'
payload_creat = {'api_key': 'rRkNdobPRD2yYfhdCZqkGOArrLQPttM5',
           'api_secret': 'yM_LfSYb9E5glWhWGPOWAIjIhSCAveQU',
           'outer_id': 'faces',
           'tag': 'this is the test face set'}

url_add = 'https://api-cn.faceplusplus.com/facepp/v3/faceset/addface'
payload_add = {'api_key': 'rRkNdobPRD2yYfhdCZqkGOArrLQPttM5',
           'api_secret': 'yM_LfSYb9E5glWhWGPOWAIjIhSCAveQU',
           'outer_id': 'faces'}


def sent_to_face(fn):
    files = {'image_file':open(fn, 'rb')}
    try:
        r = requests.post(url_detect,files=files,data=payload_detect)
    except requests.exceptions.RequestException as e:
    # catastrophic error. bail.
        print (e)
        sys.exit(1)
    data=json.loads(r.text)
    #print(data)
    reco = "rec:May I see your pretty face more detaily?:0"
    if 'error_message' in data:
        print (data['error_message'])
        print ("face++ error!")
        reco = "rec:Sorry I don't feel so good now, maybe I need a rest.:0"
    elif('faces' in data):
        for face_indx in range(len(data['faces'])):
            payload_search["face_token"] = data['faces'][face_indx]["face_token"]
            r = requests.post(url_search,data=payload_search)
            data2=json.loads(r.text)
            print("data2:"+repr(data2))
            nowtoken=data2["results"][0]["face_token"]
            if nowtoken == 'ad76654797ca570d224e8ba714b52186' or  nowtoken == '9885295cfddc96c7d6350ac4b1d5359e':
                reco= 'rec:Mr.Zou you look capable, strong-minded and quite geeklike. As an engineer, plaid shirts must be avoided. Here is a white sweater recommended for you. Suitable for spring and autumn seasons, this sweater will increase your affinity and make you look more stylish.:12'
            else:
                reco = recommand.recommadation(data)
                for face_indx in range(len(data['faces'])):
                    face_tokens[face_indx] = data['faces'][face_indx]["face_token"]
                t = threading.Thread(target=search_face, args=(face_tokens,))
                t.start()
    else:
        print("rec:No face:0")
        reco = "rec:May I see your pretty face more detaily?:0"
    return reco

def search_face(face_tokens = {}):
    print('in search')
    for token in face_tokens.values():
        payload_search["face_token"] = token
        r = requests.post(url_search,data=payload_search)
        data=json.loads(r.text)
        print(data["results"])
        database.add_new_token(token,data["results"][0]["face_token"])
    add_face(face_tokens)

def creat_faceset(setid):
    print('in creat')
    detect_face('./1.jpg')
    payload_creat['face_tokens']=face_tokens[0]          # store one picture to face set
    payload_creat["outer_id"] = setid
    r = requests.post(url_creat,data=payload_creat)
    data=json.loads(r.text)
    print(data)

def detect_face(fn):
	files = {'image_file':open(fn, 'rb')}
	r = requests.post(url_detect,files=files,data=payload_detect)
	data = json.loads(r.text)
	print('in detect')
	#print(data)
	for face_indx in range(len(data['faces'])):
		face_tokens[face_indx] = data['faces'][face_indx]["face_token"]
		print(repr(face_tokens[face_indx])+'    '+fn)
	print('end detect')

def add_face(face_tokens={}):
    print('in add')
    #r = requests.post(url_add,data=payload_detect)
    for token in face_tokens.values():
        payload_add['face_tokens']= token
        print(repr(payload_add),'      ')
        r = requests.post(url_add,data=payload_add)
        data=json.loads(r.text)
        print(data)
    print('end add')

if __name__ == '__main__':
    #creat new face set
    '''
    creat_faceset("faces")
    '''
    reco = sent_to_face("./1.jpg")
    '''
    search_face()
    add_face()
    '''
    print(reco)
