from basic import Basic
import urllib2
import poster.encode
from poster.streaminghttp import register_openers
import json


class Media(object):
	def __init__(self):
		register_openers()
	
	def get(self, accessToken, mediaId):
		postUrl = "https://api.weixin.qq.com/cgi-bin/media/get?access_token=%s&media_id=%s" % (accessToken, mediaId)
		urlResp = urllib2.urlopen(postUrl)

		headers = urlResp.info().__dict__['headers']
		if('Content-Type:application/json\r\n' in headers) or ('Content-Type:text/plain\r\n' in headers):
			jsonDict = json.loads(urlResp.read())
			print jsonDict
		else:
			buffer = urlResp.read()#example binary
			mediaFile = file('test_media.jpg', 'wb')
			mediaFile.write(buffer)
			print 'get successful'


	#upload image
	def upload(self, accessToken, filePath, mediaType):
		openFile = open(filePath, 'rb')
		param = {'media':openFile}
		postData, postHeaders = poster.encode.multipart_encode(param)

		postUrl = "https://api.weixin.qq.com/cgi-bin/media/upload?access_token=%s&type=%s" % (accessToken, mediaType)
		request = urllib2.Request(postUrl, postData, postHeaders)
		urlResp = urllib2.urlopen(request)
		print urlResp.read()

if __name__ == '__main__':
	myMedia = Media()
	accessToken = Basic().get_access_token()
	# filePath = "/root/py/weixin_gongzhonghao/pic/1.jpg"
	# mediaType = "image"
	# myMedia.upload(accessToken, filePath, mediaType)
	mediaId = "RqcitrrAFWMpnBpvdJPvGa3t3LEVFDBox4mhGvlc6WDTXcwWigR4ML72oW91NHTS"
	myMedia.get(accessToken, mediaId)
	#https://api.weixin.qq.com/cgi-bin/media/get?access_token=C1wxq0JbZ4o-wMb2nd10L99l1_pW0SCIFER2P1MKCbEyfWbeR2RzUxUU2qkhTaj0uOD7Q-k-2R2qdpkdb1JvnrZLxTZF8MDSicxAxS6dP4MQNIgAAAFCX&media_id=RqcitrrAFWMpnBpvdJPvGa3t3LEVFDBox4mhGvlc6WDTXcwWigR4ML72oW91NHTS




