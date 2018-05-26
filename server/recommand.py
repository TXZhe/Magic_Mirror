import json
import dictionary

width = dict()
top = dict()
height = dict()
left = dict()
gender = dict()
happiness = dict()
sadness = dict()
anger = dict()
wh = dict()
lr5 = dict()
lr8 = dict()

def recommadation(data):
    #data=json.loads(data)
    rec = "rec:"
    buy = 0
    for face_indx in range(len(data['faces'])):
        width[face_indx] = data['faces'][face_indx]['face_rectangle']['width']
        top[face_indx] = data['faces'][face_indx]['face_rectangle']['top']
        height[face_indx] = data['faces'][face_indx]['face_rectangle']['height']
        left[face_indx] = data['faces'][face_indx]['face_rectangle']['left']
        gender[face_indx]=data['faces'][face_indx]['attributes']['gender']['value']
        happiness[face_indx]=data['faces'][face_indx]['attributes']['emotion']['happiness']
        sadness[face_indx]=data['faces'][face_indx]['attributes']['emotion']['sadness']
        anger[face_indx]=data['faces'][face_indx]['attributes']['emotion']['anger']

        wh[face_indx]=width[face_indx]/height[face_indx]
        lr5[face_indx]=(-data['faces'][face_indx]['landmark']['contour_left5']['x']+data['faces'][face_indx]['landmark']['contour_right5']['x'])/width[face_indx]
        lr8[face_indx]=(-data['faces'][face_indx]['landmark']['contour_left8']['x']+data['faces'][face_indx]['landmark']['contour_right8']['x'])/width[face_indx]

        hairstyle = []
        clothes = []

        if gender[face_indx]=='Female':
            if wh[face_indx]< 2/3:
                hairstyle=[1,5,6]
                if happiness[face_indx]>50:
                    clothes=[12,17]
                    buy = 1
                elif sadness[face_indx]>50:
                    clothes=[12,17,15]
                    buy = 3
                else:
                    clothes=[12,16,17,22]
                    buy = 5
            if wh[face_indx]==1:
                if lr5[face_indx]>4/5:
                    hairstyle=[1,4,5]
                    if happiness[face_indx]>50:
                        clothes=[18]
                        buy = 7
                    elif sadness[face_indx]>50:
                        clothes=[15,18]
                        buy = 9
                    else:
                        clothes=[16,18,22]
                        buy = 11
                if lr5[face_indx]<=4/5:
                    hairstyle=[6,7]
                    if happiness[face_indx]>50:
                        clothes=[13,24]
                        buy = 13
                    elif sadness[face_indx]>50:
                        clothes=[13,15,24]
                        buy = 15
                    else:
                        clothes=[13,24,22]
                        buy = 17
            if wh[face_indx]<1 and wh[face_indx]>=2/3:
                if lr8[face_indx]<=1/3:
                    hairstyle=[9]
                    if happiness[face_indx]>50:
                        clothes=[14,19]
                        buy = 19
                    elif sadness[face_indx]>50:
                        clothes=[14,15,19]
                        buy = 21
                    else:
                        clothes=[14,16,19,22]
                        buy = 23
        if gender[face_indx]=='Male':
            if wh[face_indx]< 2/3:
                hairstyle=[1,5,6]
                if happiness[face_indx]>50:
                    clothes=[20,21]
                    buy = 2
                elif sadness[face_indx]>50:
                    clothes=[15,20,21]
                    buy = 4
                else:
                    clothes=[20,21,16,22]
                    buy = 6
            if wh[face_indx]==1:
                if lr5[face_indx]>4/5:
                    hairstyle=[1,4,5]
                    if happiness[face_indx]>50:
                        clothes=[18]
                        buy = 8
                    elif sadness[face_indx]>50:
                        clothes=[15,18]
                        buy = 10
                    else:
                        clothes=[16,18,22]
                        buy = 12
                if lr5[face_indx]<=4/5:
                    hairstyle=[2,4,8]
                    if happiness[face_indx]>50:
                        clothes=[23]
                        buy = 14
                    elif sadness[face_indx]>50:
                        clothes=[15,23]
                        buy = 16
                    else:
                        clothes=[16,22,23]
                        buy = 18
            if wh[face_indx]<1 and wh[face_indx]>=2/3:
                if lr8[face_indx]<=1/3:
                    hairstyle=[3,10,11]
                    if happiness[face_indx]>50:
                        clothes=[14,19]
                        buy = 20
                    elif sadness[face_indx]>50:
                        clothes=[14,15,19]
                        buy = 22
                    else:
                        clothes=[14,16,19,22]
                        buy = 24
        rec = rec + dictionary.look_up(hairstyle, clothes)
    rec = rec + ':'+repr(buy)
    return rec
