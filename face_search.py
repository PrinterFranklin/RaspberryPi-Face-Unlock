import urllib2
import urllib
import time
import json

# face++ Search API URL
http_url = "https://api-cn.faceplusplus.com/facepp/v3/search"
# my face++ API Key & Secret
key = "6_QSbVYH_Wdct6yzNU4KQqWnDe25iUvx"
secret = "12utDUEPjiSlTUrhTTOUaNa5G5GykPd-"
# Path for the image
filepath = r"./test.jpg"
# my face++ FaceSet ID
set_id = "raspberry_nbztx_13116616118"

# Build HTTP Request
boundary = '----------%s' % hex(int(time.time() * 1000))
data = []
data.append('--%s' % boundary)
data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_key')
data.append(key)
data.append('--%s' % boundary)
data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_secret')
data.append(secret)
data.append('--%s' % boundary)
fr = open(filepath,'rb')
data.append('Content-Disposition: form-data; name="%s"; filename=" "' % 'image_file')
data.append('Content-Type: %s\r\n' % 'application/octet-stream')
data.append(fr.read())
fr.close()
data.append('--%s' % boundary)
data.append('Content-Disposition: form-data; name="%s"\r\n' % 'outer_id')
data.append(set_id)
data.append('--%s--\r\n' % boundary)

# Build HTTP Header & Body
http_body='\r\n'.join(data)
req = urllib2.Request(http_url)
req.add_header('Content-Type', 'multipart/form-data; boundary=%s' % boundary)
req.add_data(http_body)

try:
    # Sending a request
    resp = urllib2.urlopen(req, timeout=5)
    qrcont = resp.read()
    # Reading the JSON file returned
    json_data = json.loads(qrcont)
    # While confidence is bigger than thresholds, confirm login.
    if json_data['results'][0]['confidence'] > json_data['thresholds']['1e-4']:
        print("Success to login. Congratulation!")
    else:
        print("Fail to login. Try again!")
    # print qrcont
except urllib2.HTTPError as e:
    print e.read()
