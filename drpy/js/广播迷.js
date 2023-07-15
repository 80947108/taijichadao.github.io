var rule = {
    title:'广播迷',
    编码:'gbk',
    搜索编码:'gbk',
    host:'http://www.guangbomi.com',
    url:'/fyclass/fypage.html[/fyclass]',
    searchUrl:'/index.php?m=search&c=index&a=init&siteid=1&typeid=54&q=**',
    searchable:2,
    quickSearch:0,
    headers:{
        'User-Agent':'MOBILE_UA'
    },
    timeout:5000,

    class_name:'央媒FM&央视TV&湖南FM&湖南TV&北京FM&上海FM&天津FM&重庆FM&广东FM&四川FM&山东FM&江苏FM&浙江FM&河南FM&河北FM&辽宁FM&安徽FM&湖北FM&福建FM&广西FM&山西FM&陕西FM&江西FM&吉林FM&云南FM&贵州FM&西藏FM&宁夏FM&海南FM&新疆FM&甘肃FM&青海FM&黑龙江FM&内蒙古FM&北京TV&上海TV&天津TV&重庆TV&广东TV&四川TV&山东TV&江苏TV&浙江TV&河南TV&河北TV&辽宁TV&安徽TV&湖北TV&福建TV&广西TV&山西TV&陕西TV&江西TV&吉林TV&云南TV&贵州TV&西藏TV&宁夏TV&海南TV&新疆TV&甘肃TV&青海TV&黑龙江TV&内蒙古TV',
    class_url:'fmlist223.html&tv/zy&live/hunan&tv/hn&live/bj&live/sh&live/tj&live/cq&live/gd&live/sc&live/sd&live/js&live/zj&live/henan&live/hebei&live/ln&live/ah&live/hubei&live/fj&live/gx&live/sx&live/sxi&live/jx&live/jl&live/yn&live/gz&live/xz&live/nx&live/hainan&live/xj&live/gs&live/qh&live/hlj&live/nmg&tv/bj&tv/sh&tv/tj&tv/cq&tv/gd&tv/sc&tv/sd&tv/js&tv/zj&tv/henan&tv/hebei&tv/ln&tv/ah&tv/hubei&tv/fj&tv/gx&tv/sxi&tv/sx&tv/jx&tv/jl&tv/yn&tv/gz&tv/xz&tv/nx&tv/hainan&tv/xj&tv/gs&tv/qh&tv/hlj&tv/nmg',
	play_parse:true,
	lazy:'js:var purl=jsp.pdfh(request(input), ".playcode&&iframe&&src");if(/tingtingfm/.test(purl)){purl="http://www.guangbomi.com"+purl};input= {jx:0,url:purl,parse:1,header:JSON.stringify({"referer":"http://www.guangbomi.com/"})}',
	limit:6,
	double: true,
	一级: '.ax-split-2&&li;.radio-title&&Text;img&&src;;a&&href',
	二级: {
		"title": "h1&&Text;.ax-breadcrumb:eq(1)&&Text",
		"img": "",
		"desc": ";;;;.ax-des:eq(0)&&Text",
		"content": ".ax-ignore:eq(0)&&Text",
		"重定向": "js:let url = jsp.pd(html,'#play&&iframe&&src');log('重定向到:'+url);html = request(url)",
		"tabs": "js:TABS=['信号源']",
		"lists": "div:eq(1)&&a"
	},
	搜索: 'body .ax-item-block;.ax-title&&Text;.ax-img&&style;.ax-color-des:eq(1)&&Text;*',
}
