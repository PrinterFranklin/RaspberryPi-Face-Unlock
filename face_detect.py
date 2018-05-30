import cv2
import urllib2
import urllib
import time
# import ssl

# URL for detection
http_url = "https://api-cn.faceplusplus.com/facepp/v3/detect"
# User Information
key = "6_QSbVYH_Wdct6yzNU4KQqWnDe25iUvx"
secret = "12utDUEPjiSlTUrhTTOUaNa5G5GykPd-"
# Path for images
filepath = r"./test.jpg"

# build information set
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
# data.append('--%s' % boundary)
# data.append('Content-Disposition: form-data; name="%s"\r\n' % 'return_landmark')
# data.append('1')
# data.append('--%s' % boundary)
# data.append('Content-Disposition: form-data; name="%s"\r\n' % 'return_attributes')
# data.append("gender,age,smiling,headpose,facequality,blur,eyestatus,emotion,ethnicity,beauty,mouthstatus,eyegaze,skinstatus")
data.append('--%s--\r\n' % boundary)

# call opencv and read this picture
img = cv2.imread("test.jpg")
cv2.namedWindow("img1")
# show this picture
cv2.imshow("img1", img)

http_body='\r\n'.join(data)
# buld http request
req = urllib2.Request(http_url)
# header
req.add_header('Content-Type', 'multipart/form-data; boundary=%s' % boundary)
# body
req.add_data(http_body)

try:
    # req.add_header('Referer','http://remotserver.com/')
    # post data to server
    # context = ssl._create_unverified_context()
    resp = urllib2.urlopen(req, timeout=5)
    # get response
    qrcont = resp.read()
    # print response information
    print qrcont
    dict = eval(qrcont)
    faces = dict['faces']
    print len(faces)
    # draw face rectangles
    for i in range(len(faces)):
    	face_rectangle = faces[i]['face_rectangle']
    	width = face_rectangle['width']
    	top = face_rectangle['top']
    	left = face_rectangle['left']
    	height = face_rectangle['height']
    	start = (left, top)
    	end = (left + width, top + height)
    	color = (55, 255, 155)
    	thickness = 3
    	cv2.rectangle(img, start, end, color, thickness)
    # show the marked picture
    cv2.namedWindow("img2")
    cv2.imshow("img2", img)
    # wait until press any key
    cv2.waitKey(0)
    # shut down both windows
    cv2.destroyAllWindows()
except urllib2.HTTPError as e:
    print e.read()