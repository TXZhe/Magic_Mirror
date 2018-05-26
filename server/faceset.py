'''
Create face set in fac++
'''

import json
import requests
import recommand

url = 'https://api-cn.faceplusplus.com/facepp/v3/faceset/create'
payload = {'api_key': 'rRkNdobPRD2yYfhdCZqkGOArrLQPttM5',
           'api_secret': 'yM_LfSYb9E5glWhWGPOWAIjIhSCAveQU',
           'display_name':'Gakki'}

def sent_to_face(fn):
    files = {'image_file':open(fn, 'rb')}
    r = requests.post(url,files=files,data=payload)
    data=json.loads(r.text)
    print(data)
    '''
    reco = "0"
    if 'error_message' in data:
        print (data['error_message'])
        print ("face++ error!")
        reco = "Face++_error"
    elif('faces' in data):
        reco = recommand.recommadation(data)
    else:
        print("No face")
        reco = "No_Face"
    return reco
    '''

if __name__ == '__main__':
    for i in range(1,5):
    	reco = sent_to_face("./gakki/"+repr(i)+".jpg")
    	#print(reco)
