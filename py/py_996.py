#coding=utf-8
#!/usr/bin/python
import sys
sys.path.append('..') 
from base.spider import Spider
import json
import base64

class Spider(Spider):  # 元类 默认的元类 type
	def getName(self):
		return "996PY"
	def init(self,extend=""):
		print("============{0}============".format(extend))
		pass
	def homeContent(self,filter):
		result = {}
		cateManual = {
			"电影":"1",
			"电视剧":"2",
			"动漫":"3",
			"爽文短剧":"4"
		}
		classes = []
		for k in cateManual:
			classes.append({
				'type_name':k,
				'type_id':cateManual[k]
			})

		result['class'] = classes
		if(filter):
			result['filters'] = self.config['filter']	
		return result
	def homeVideoContent(self):
		rsp = self.fetch("https://www.cs1369.com")
		root = self.html(rsp.text)
		aList = root.xpath("//div[@class='stui-vodlist__box']/a")

		videos = []
		for a in aList:
			name = a.xpath('./@title')[0]
			pic = a.xpath('./@data-original')[0]
			remark = a.xpath("./span[@class='pic-text text-right']/text()")[0]
			sid = a.xpath("./@href")[0]
			sid = self.regStr(sid,"/detail/(\\S+).html")
			videos.append({
				"vod_id":sid,
				"vod_name":name,
				"vod_pic":pic,
				"vod_remarks":remark
			})
		result = {
			'list':videos
		}
		return result
	def categoryContent(self,tid,pg,filter,extend):
		result = {}
		if 'id' not in extend.keys():
			extend['id'] = tid
		extend['page'] = pg
		filterParams = ["area", "by", "class", "id", "lang", "", "", "", "page", "", "", "year"]
		params = ["", "", "", "", "", "", "", "", "", "", "", ""]
		for idx in range(len(filterParams)):
			fp = filterParams[idx]
			if fp in extend.keys():
				params[idx] = extend[fp]
		suffix = '/'.join(params)
		url = 'https://www.cs1369.com/show/{0}.html'.format(suffix)
		rsp = self.fetch(url)
		root = self.html(rsp.text)
		aList = root.xpath("//div[@class='stui-vodlist__box']/a")
		videos = []
		for a in aList:
			name = a.xpath('./@title')[0]
			pic = a.xpath('./@data-original')[0]
			mark = a.xpath("./span[@class='pic-text text-right']/text()")[0]
			sid = a.xpath("./@href")[0]
			sid = self.regStr(sid,"/detail/(\\d+).html")
			videos.append({
				"vod_id":sid,
				"vod_name":name,
				"vod_pic":pic,
				"vod_remarks":mark
			})

		result['list'] = videos
		result['page'] = pg
		result['pagecount'] = 9999
		result['limit'] = 90
		result['total'] = 999999
		return result
	def detailContent(self,array):
		tid = array[0]
		url = 'https://www.cs1369.com/detail/{0}.html'.format(tid)
		rsp = self.fetch(url)
		root = self.html(rsp.text)
		node = root.xpath("//div[@class='stui-pannel-box']//div[2]")[0]
		pic = node.xpath("//div[@class='stui-content__thumb']/a/img/@data-original")[0]
		title = node.xpath("//div[@class='stui-content__thumb']/a/@title")[0]
		# detail = node.xpath("//div[@class='stui-content__detail']/text()")[0]

		vod = {
			"vod_id":tid,
			"vod_name":title,
			"vod_pic":pic,
			"type_name":"",
			"vod_year":"",
			"vod_area":"",
			"vod_remarks":"",
			"vod_actor":"",
			"vod_director":"",
			"vod_content":""
		}

		infoArray = node.xpath("//div[@class='stui-content__detail']/p")
		for info in infoArray:
			content = info.xpath('string(.)')
			if content.startswith('类型'):
				vod['type_name'] = content
			# if content.startswith('年份'):
			# 	vod['vod_year'] = content
			# if content.startswith('地区'):
			# 	vod['vod_area'] = content
			# if content.startswith('更新'):
			# 	vod['vod_remarks'] = content.replace('\n','').replace('\t','')
			if content.startswith('主演'):
				vod['vod_actor'] = content.replace('\n','').replace('\t','')
			if content.startswith('导演'):
				vod['vod_director'] = content.replace('\n','').replace('\t','')
			if content.startswith('简介'):
				vod['vod_content'] = content.replace('\n','').replace('\t','')

		vod_play_from = '$$$'
		playFrom = []
		vodHeader = root.xpath("//div[@class='stui-pannel-box b playlist mb']/div[@class='stui-pannel_hd']/div/h3/text()")
		for v in vodHeader:
			playFrom.append(v)
		vod_play_from = vod_play_from.join(playFrom)
		
		vod_play_url = 'https://www.cs1369.com'
		playList = []
		vodList = root.xpath("//ul[contains(@class,'stui-content__playlist')]")
		for vl in vodList:
			vodItems = []
			aList = vl.xpath('./li/a')
			for tA in aList:
				href = tA.xpath('./@href')[0]
				name = tA.xpath('./text()')[0]
				#tId = self.regStr(href,'/play/(\\S+).html')
				vodItems.append(name + "$" + href)
			joinStr = '#'
			joinStr = joinStr.join(vodItems)
			playList.append(joinStr)
		vod_play_url = vod_play_url.join(playList)

		vod['vod_play_from'] = vod_play_from
		vod['vod_play_url'] = vod_play_url

		result = {
			'list':[
				vod
			]
		}
		return result

	def searchContent(self,key,quick):		
		url = 'https://www.cs1369.com/index.php/ajax/suggest?mid=1&wd={0}'.format(key)
		# getHeader()
		rsp = self.fetch(url)
		jo = json.loads(rsp.text)
		result = {}
		jArray = []
		if int(jo['total']) > 0:
			for j in jo['list']:
				jArray.append({
					"vod_id": j['id'],
					"vod_name": j['name'],
					"vod_pic": j['pic'],
					"vod_remarks": ""
				})
		result = {
			'list':jArray
		}
		return result

	config = {
		"player": {
			"996m3u8": {
				"sh": "996播放器",
				"pu": "https://jx.961691.com/player/?url=",
				"sn": 1,
				"or": 999
			}
		},
		"filter": {"1": [{"key": "id", "name": "类型", "value": [{"n": "全部", "v": "id/1"}, {"n": "动作", "v": "id/6"}, {"n": "喜剧", "v": "id/7"}, {"n": "爱情", "v": "id/8"}, {"n": "科幻", "v": "id/9"}, {"n": "恐怖", "v": "id/10"}, {"n": "剧情", "v": "id/11"}, {"n": "战争", "v": "id/12"}, {"n": "动画", "v": "id/13"}, {"n": "记录", "v": "id/14"}]}, {"key": "class", "name": "剧情", "value": [{"n": "全部", "v": ""}, {"n": "喜剧", "v": "class/喜剧"}, {"n": "爱情", "v": "class/爱情"}, {"n": "恐怖", "v": "恐怖"}, {"n": "动作", "v": "class/动作"}, {"n": "科幻", "v": "class/科幻"}, {"n": "剧情", "v": "class/剧情"}, {"n": "战争", "v": "class/战争"}, {"n": "警匪", "v": "class/警匪"}, {"n": "犯罪", "v": "class/犯罪"}, {"n": "动画", "v": "class/动画"}, {"n": "奇幻", "v": "class/奇幻"}, {"n": "武侠", "v": "class/武侠"}, {"n": "冒险", "v": "class/冒险"}, {"n": "枪战", "v": "class/枪战"}, {"n": "恐怖", "v": "class/恐怖"}, {"n": "悬疑", "v": "class/悬疑"}, {"n": "惊悚", "v": "class/惊悚"}, {"n": "经典", "v": "class/经典"}, {"n": "青春", "v": "class/青春"}, {"n": "文艺", "v": "class/文艺"}, {"n": "微电影", "v": "class/微电影"}, {"n": "古装", "v": "class/古装"}, {"n": "历史", "v": "class/历史"}, {"n": "运动", "v": "class/运动"}, {"n": "农村", "v": "class/农村"}, {"n": "儿童", "v": "class/儿童"}, {"n": "网络电影", "v": "class/网络电影"}]}, {"key": "area", "name": "按地区", "value": [{"n": "全部", "v": ""}, {"n": "大陆", "v": "area/中国大陆"}, {"n": "香港", "v": "area/中国香港"}, {"n": "台湾", "v": "area/中国台湾"}, {"n": "美国", "v": "area/美国"}, {"n": "日本", "v": "area/日本"}, {"n": "韩国", "v": "area/韩国"}, {"n": "其他", "v": "area/其他"}]}, {"key": "year", "name": "年份", "value": [{"n": "全部", "v": ""}, {"n": "2023", "v": "year/2023"}, {"n": "2022", "v": "year/2022"}, {"n": "2021", "v": "year/2021"}, {"n": "2020", "v": "year/2020"}, {"n": "2019", "v": "year/2019"}, {"n": "2018", "v": "year/2018"}, {"n": "2017", "v": "year/2017"}, {"n": "2016", "v": "year/2016"}, {"n": "2015", "v": "year/2015"}, {"n": "2014", "v": "year/2014"}, {"n": "2013", "v": "year/2013"}, {"n": "2012", "v": "year/2012"}, {"n": "2011", "v": "year/2011"}, {"n": "2010", "v": "year/2010"}]}, {"key": "by", "name": "排序", "value": [{"n": "全部", "v": ""}, {"n": "时间", "v": "by/time"}, {"n": "人气", "v": "by/hits"}, {"n": "评分", "v": "by/score"}]}],"2": [{"key": "class", "name": "剧情", "value": [{"n": "全部", "v": ""}, {"n": "古装", "v": "class/古装"}, {"n": "战争", "v": "class/战争"}, {"n": "青春偶像", "v": "class/青春偶像"}, {"n": "喜剧", "v": "class/喜剧"}, {"n": "家庭", "v": "class/家庭"}, {"n": "犯罪", "v": "class/犯罪"}, {"n": "动作", "v": "class/动作"}, {"n": "奇幻", "v": "class/奇幻"}, {"n": "剧情", "v": "class/剧情"}, {"n": "历史", "v": "class/历史"}, {"n": "经典", "v": "class/经典"}, {"n": "乡村", "v": "class/乡村"}, {"n": "情景", "v": "class/情景"}, {"n": "商战", "v": "class/商战"}, {"n": "网剧", "v": "class/网剧"}, {"n": "其他", "v": "class/其他"}]}, {"key": "area", "name": "按地区", "value": [{"n": "全部", "v": ""}, {"n": "大陆", "v": "area/中国大陆"}, {"n": "香港", "v": "area/中国香港"}, {"n": "台湾", "v": "area/中国台湾"}, {"n": "美国", "v": "area/美国"}, {"n": "日本", "v": "area/日本"}, {"n": "韩国", "v": "area/韩国"}, {"n": "其他", "v": "area/其他"}]}, {"key": "year", "name": "年份", "value": [{"n": "全部", "v": ""}, {"n": "2023", "v": "year/2023"}, {"n": "2022", "v": "year/2022"}, {"n": "2021", "v": "year/2021"}, {"n": "2020", "v": "year/2020"}, {"n": "2019", "v": "year/2019"}, {"n": "2018", "v": "year/2018"}, {"n": "2017", "v": "year/2017"}, {"n": "2016", "v": "year/2016"}, {"n": "2015", "v": "year/2015"}, {"n": "2014", "v": "year/2014"}, {"n": "2013", "v": "year/2013"}]}, {"key": "by", "name": "排序", "value": [{"n": "全部", "v": ""}, {"n": "时间", "v": "by/time"}, {"n": "人气", "v": "by/hits"}, {"n": "评分", "v": "by/score"}]}], "3": [{"key": "id", "name": "类型", "value": [{"n": "全部", "v": "id/3"}, {"n": "国产动漫", "v": "id/25"}, {"n": "日韩动漫", "v": "id/26"}, {"n": "欧美动漫", "v": "id/27"}, {"n": "其他", "v": "id/28"}]},{"key": "class", "name": "剧情", "value": [{"n": "全部", "v": ""}, {"n": "情感", "v": "class/情感"}, {"n": "科幻", "v": "class/科幻"}, {"n": "热血", "v": "class/热血"}, {"n": "推理", "v": "class/推理"}, {"n": "搞笑", "v": "class/搞笑"}, {"n": "冒险", "v": "class/冒险"}, {"n": "萝莉", "v": "class/萝莉"}, {"n": "校园", "v": "class/校园"}, {"n": "动作", "v": "class/动作"}, {"n": "机战", "v": "class/机战"}, {"n": "运动", "v": "class/运动"}, {"n": "战争", "v": "class/战争"}, {"n": "少年", "v": "class/少年"}, {"n": "少女", "v": "class/少女"}, {"n": "社会", "v": "class/社会"}, {"n": "原创", "v": "class/原创"}, {"n": "亲子", "v": "class/亲子"}, {"n": "益智", "v": "class/益智"}, {"n": "励志", "v": "class/励志"}, {"n": "其他", "v": "class/其他"}]}, {"key": "area", "name": "按地区", "value": [{"n": "全部", "v": ""}, {"n": "大陆", "v": "area/中国大陆"}, {"n": "香港", "v": "area/中国香港"}, {"n": "台湾", "v": "area/中国台湾"}, {"n": "美国", "v": "area/美国"}, {"n": "日本", "v": "area/日本"}, {"n": "韩国", "v": "area/韩国"}, {"n": "其他", "v": "area/其他"}]}, {"key": "year", "name": "年份", "value": [{"n": "全部", "v": ""}, {"n": "2023", "v": "year/2023"}, {"n": "2022", "v": "year/2022"}, {"n": "2021", "v": "year/2021"}, {"n": "2020", "v": "year/2020"}, {"n": "2019", "v": "year/2019"}, {"n": "2018", "v": "year/2018"}, {"n": "2017", "v": "year/2017"}, {"n": "2016", "v": "year/2016"}, {"n": "2015", "v": "year/2015"}, {"n": "2014", "v": "year/2014"}, {"n": "2013", "v": "year/2013"}]}, {"key": "by", "name": "排序", "value": [{"n": "全部", "v": ""}, {"n": "时间", "v": "by/time"}, {"n": "人气", "v": "by/hits"}, {"n": "评分", "v": "by/score"}]}]}
	}
	header = {
		"origin":"https://www.cs1369.com",
		"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
		"Accept":" */*",
		"Accept-Language":"zh-CN,zh;q=0.9,en-US;q=0.3,en;q=0.7",
		"Accept-Encoding":"gzip, deflate"
	}
	def playerContent(self,flag,id,vipFlags):
		result = {}
		url = 'https://www.cs1369.com/play/{0}.html'.format(id)
		rsp = self.fetch(url)
		root = self.html(rsp.text)
		scripts = root.xpath("//script/text()")
		jo = {}
		for script in scripts:
			if(script.startswith("var player_")):
				target = script[script.index('{'):]
				jo = json.loads(target)
				break;
		parseUrl = ''
		# src="(\S+url=)
		# playerConfig = self.config['player']
		# if jo['from'] in self.config['player']:
		# 	playerConfig = self.config['player'][jo['from']]
		# 	parseUrl = playerConfig['pu'] + jo['url']
		scriptUrl = 'https://www.cs1369.com/static/player/{0}.js'.format(jo['from'])
		scriptRsp = self.fetch(scriptUrl)
		parseUrl = self.regStr(scriptRsp.text,'src="(\\S+url=)')
		b64 = jo['url'][8:]
		targetUrl = base64.b64decode(b64)[8:-8].decode()
		if len(parseUrl) > 0:
			parseRsp = self.fetch(parseUrl+jo['url'])
			realUrl = self.regStr(parseRsp.text,"(?<=urls\\s=\\s').*?(?=')",0)
			if len(realUrl) > 0 :
				result["parse"] = 0
				result["playUrl"] = "" 
				result["url"] = targetUrl
				result["header"] = json.dumps(self.header)
			else:
				result["parse"] = 1
				result["playUrl"] = "" 
				result["url"] = targetUrl
				result["header"] = json.dumps(self.header)
		return result
	def isVideoFormat(self,url):
		pass
	def manualVideoCheck(self):
		pass
	def localProxy(self,param):
		return [200, "video/MP2T", action, ""]