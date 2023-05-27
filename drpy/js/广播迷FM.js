var rule = {
    title:'广播',
    编码:'gb18030',
    host:'http://www.guangbomi.com',
    url:'/fyclass/fypage.html[/fyclass/]',
    searchUrl:'/index.php?m=search&c=index&a=init&siteid=1&typeid=54&q=**',
    searchable:2,
    quickSearch:0,
    headers:{
        'User-Agent':'MOBILE_UA'
    },
    timeout:5000,

    class_name:'北京2&浙江&湖南',
    class_url:'live/bj&zj&hunan',
	play_parse:true,
	lazy:'js:var purl=jsp.pdfh(request(input), ".playcode&&iframe&&src");if(/tingtingfm/.test(purl)){purl="http://www.guangbomi.com"+purl};input= {jx:0,url:purl,parse:1,header:JSON.stringify({"referer":"http://www.guangbomi.com/"})}',
	limit:6,
	double: true,
	一级: '.ax-split-2&&li;.radio-title&&Text;;;a&&href',
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
