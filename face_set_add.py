import urllib2
import urllib
import time

http_url = "https://api-cn.faceplusplus.com/facepp/v3/faceset/addface"
key = "6_QSbVYH_Wdct6yzNU4KQqWnDe25iUvx"
secret = "12utDUEPjiSlTUrhTTOUaNa5G5GykPd-"
set_id = "raspberry_nbztx_13116616118"
# put in tokens you want to add
tokens = "3b446780a9efa45ddd255abfdb267a9d"

boundary = '----------%s' % hex(int(time.time() * 1000))
data = []
data.append('--%s' % boundary)
data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_key')
data.append(key)
data.append('--%s' % boundary)
data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_secret')
data.append(secret)
data.append('--%s' % boundary)
data.append('Content-Disposition: form-data; name="%s"\r\n' % 'outer_id')
data.append(set_id)
data.append('--%s' % boundary)
data.append('Content-Disposition: form-data; name="%s"\r\n' % 'face_tokens')
data.append(tokens)
data.append('--%s--\r\n' % boundary)

http_body='\r\n'.join(data)
req = urllib2.Request(http_url)
req.add_header('Content-Type', 'multipart/form-data; boundary=%s' % boundary)
req.add_data(http_body)

try:
    resp = urllib2.urlopen(req, timeout=5)
    qrcont = resp.read()
    print qrcont
except urllib2.HTTPError as e:
    print e.read()    