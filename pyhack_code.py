
import requests
import json
from datetime import datetime as dt
from requests.api import post
c = 0


def tpe(a, b):
    try:
        d1 = dt.strptime(a, "%m/%d/%Y")
        d2 = dt.strptime(b, "%m/%d/%Y")
        if(d2 > d1):
            return 'type1'
        elif(d1>d2):
            return 'type 2'
    except ValueError:
        return 'type2'
    # except:none


def dupae(id1):
    global c
    global e
    e = id1
    if(c == e):
        return 'type3'
    c = e


count = 0
aeli = requests.get(
    'https://pyhack-dot-pharmanlp-177020.uc.r.appspot.com/api/1/StudyHack/ae/subject/list')
cmli = requests.get(
    'https://pyhack-dot-pharmanlp-177020.uc.r.appspot.com/api/1/StudyHack/cm/subject/list')
parsedae = json.loads(aeli.text)
parsedcm = json.loads(cmli.text)
for s in range(0, len(parsedcm['data'])):
    cmsubid = str(parsedcm['data'][s])
    print(cmsubid)
    urlae = 'https://pyhack-dot-pharmanlp-177020.uc.r.appspot.com/api/1/StudyHack/ae/subject/' + cmsubid + '/list'
    lidata = requests.get(url=urlae)
    urlcm = 'https://pyhack-dot-pharmanlp-177020.uc.r.appspot.com/api/1/StudyHack/cm/subject/' + cmsubid + '/list'
    licm = requests.get(url=urlcm)
    if(lidata.status_code == 200 and licm.status_code == 200):
        parsedcm2 = json.loads(licm.text)
        parsed = json.loads(lidata.text)
        print(len(parsed['data']))
        t = (len(parsed['data'])-1)
        for j in range(0, t):
            try:
                h = parsedcm2['data'][j]['cmstdat_dts']
                d = parsed['data'][j]['aestdat_dts']
                cmend = parsedcm2['data'][j]['formid']
                aeend = parsed['data'][j]['formid']
                tye = tpe(h, d)
                if(tye == None):
                    tye = dupae(aeend)
                print("the dates are {} {} {} ".format(h, d, tye))
                query = {
                    "email_address": "dhilidhiva@gmail.com",
                    "formname":str(parsed['data'][j]['formname']) ,
                    "formid": int(aeend),
                    "formidx": int(parsed['data'][j]['formidx']) ,
                    "type": tye,
                    "subjectid": cmsubid,
                }
                pourl = 'https://pyhack-dot-pharmanlp-177020.uc.r.appspot.com/api/1/StudyHack/query'
                po = requests.post(url=pourl, json=query)
                print(po.text)
                print(query)
            except IndexError:
                continue
    else:
        continue
