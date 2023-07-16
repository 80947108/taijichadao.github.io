var rule = {
	title:'广播迷FM',
	host:'http://www.guangbomi.com',
    编码:'gbk',
    搜索编码:'gbk',
	url: '/fyfilter.html?page=fypage',
	filter_url:'{{fl.cateId}}',
	filter:{
		"live":[{"key":"cateId","name":"按类型","value":[{"n":"中央台","v":"fmlist223"},{"n":"省级台","v":"fmlist220"},{"n":"市级台","v":"fmlist221"},{"n":"区县台","v":"fmlist222"},{"n":"新闻综合","v":"fmlist20"},{"n":"交通","v":"fmlist58"},{"n":"音乐","v":"fmlist57"},{"n":"经济","v":"fmlist56"},{"n":"生活","v":"fmlist59"},{"n":"文艺","v":"fmlist60"},{"n":"都市","v":"fmlist61"},{"n":"故事","v":"fmlist62"},{"n":"旅游","v":"fmlist63"},{"n":"乡村","v":"fmlist64"},{"n":"娱乐","v":"fmlist65"},{"n":"戏曲","v":"fmlist66"},{"n":"体育","v":"fmlist67"},{"n":"评书相声","v":"fmlist69"},{"n":"青少科教","v":"fmlist70"},{"n":"网络台","v":"fmlist113"},{"n":"汽车","v":"fmlist134"},{"n":"其他","v":"fmlist135"},{"n":"北京","v":"live/bj/index"},{"n":"上海","v":"live/sh/index"},{"n":"天津","v":"live/tj/index"},{"n":"重庆","v":"live/cq/index"},{"n":"广东","v":"live/gd/index"},{"n":"四川","v":"live/sc/index"},{"n":"山东","v":"live/sd/index"},{"n":"江苏","v":"live/js/index"},{"n":"浙江","v":"live/zj/index"},{"n":"河南","v":"live/henan/index"},{"n":"河北","v":"live/hebei/index"},{"n":"辽宁","v":"live/ln/index"},{"n":"安徽","v":"live/ah/index"},{"n":"湖南","v":"live/hunan/index"},{"n":"湖北","v":"live/hubei/index"},{"n":"福建","v":"live/fj/index"},{"n":"广西","v":"live/gx/index"},{"n":"山西","v":"live/sx/index"},{"n":"陕西","v":"live/sxi/index"},{"n":"江西","v":"live/jx/index"},{"n":"吉林","v":"live/jl/index"},{"n":"云南","v":"live/yn/index"},{"n":"贵州","v":"live/gz/index"},{"n":"西藏","v":"live/xz/index"},{"n":"宁夏","v":"live/nx/index"},{"n":"海南","v":"live/hainan/index"},{"n":"新疆","v":"live/xj/index"},{"n":"甘肃","v":"live/gs/index"},{"n":"青海","v":"live/qh/index"},{"n":"黑龙江","v":"live/hlj/index"},{"n":"内蒙古","v":"live/nmg/index"}]}],
		"tv":[{"key":"cateId","name":"按类型","value":[{"n":"中央台","v":"tvlist223"},{"n":"卫视台","v":"tvlist200"},{"n":"省级台","v":"tvlist220"},{"n":"港澳台","v":"tv/hk/index"},{"n":"市级台","v":"tvlist221"},{"n":"区县台","v":"tvlist222"},{"n":"新闻综合","v":"tvlist201"},{"n":"财经","v":"tvlist202"},{"n":"综艺","v":"tvlist203"},{"n":"体育","v":"tvlist204"},{"n":"影视","v":"tvlist205"},{"n":"公共","v":"tvlist206"},{"n":"都市","v":"tvlist207"},{"n":"少儿","v":"tvlist208"},{"n":"科教","v":"tvlist209"},{"n":"记录","v":"tvlist211"},{"n":"动漫","v":"tvlist212"},{"n":"生活","v":"tvlist213"},{"n":"法制","v":"tvlist214"},{"n":"军事","v":"tvlist215"},{"n":"文旅","v":"tvlist216"},{"n":"农科","v":"tvlist217"},{"n":"数字电视","v":"tvlist218"},{"n":"北京","v":"tv/bj/index"},{"n":"上海","v":"tv/sh/index"},{"n":"天津","v":"tv/tj/index"},{"n":"重庆","v":"tv/cq/index"},{"n":"广东","v":"tv/gd/index"},{"n":"四川","v":"tv/sc/index"},{"n":"山东","v":"tv/sd/index"},{"n":"江苏","v":"tv/js/index"},{"n":"浙江","v":"tv/zj/index"},{"n":"河南","v":"tv/henan/index"},{"n":"河北","v":"tv/hebei/index"},{"n":"辽宁","v":"tv/ln/index"},{"n":"安徽","v":"tv/ah/index"},{"n":"湖南","v":"tv/hn/index"},{"n":"湖北","v":"tv/hubei/index"},{"n":"福建","v":"tv/fj/index"},{"n":"广西","v":"tv/gx/index"},{"n":"山西","v":"tv/sx/index"},{"n":"陕西","v":"tv/sxi/index"},{"n":"江西","v":"tv/jx/index"},{"n":"吉林","v":"tv/jl/index"},{"n":"云南","v":"tv/yn/index"},{"n":"贵州","v":"tv/gz/index"},{"n":"西藏","v":"tv/xz/index"},{"n":"宁夏","v":"tv/nx/index"},{"n":"海南","v":"tv/hainan/index"},{"n":"新疆","v":"tv/xj/index"},{"n":"甘肃","v":"tv/gs/index"},{"n":"青海","v":"tv/qh/index"},{"n":"黑龙江","v":"tv/hlj/index"},{"n":"内蒙古","v":"tv/nmg/index"}]}],
		"hn_fm":[{"key":"cateId","name":"按类型","value":[{"n":"湖南","v":"live/hunan/index"}]}],
		"hn_tv":[{"key":"cateId","name":"按类型","value":[{"n":"湖南","v":"tv/hn/index"}]}]
	},
	filter_def:{
		live:{cateId:'fmlist223'},
		tv:{cateId:'tvlist223'},
		hn_fm:{cateId:'live/hunan/index'},
		hn_tv:{cateId:'tv/hn/index'}
	},
	searchUrl: '/index.php?m=search&c=index&a=init&siteid=1&typeid=54&q=**&page=fypage',
	searchable:2,
	quickSearch:0,
	filterable:1,
	headers:{
		'User-Agent': 'MOBILE_UA'
	},
	timeout:5000,
    class_name:'听广播&看电视&湖南FM&湖南TV',
    class_url:'live&tv&hn_fm&hn_tv',
	play_parse:true,
	lazy:'js:var purl=jsp.pdfh(request(input),".playcode&&iframe&&src");if(/tingtingfm/.test(purl)){purl="http://www.guangbomi.com"+purl};input= {jx:0,url:purl,parse:1,header:JSON.stringify({"referer":"http://www.guangbomi.com/"})}',
	limit:6,
	推荐: '.ax-split-3;ul&&.ax-grid-block;*;.radio-icon&&src;.radio-icon&&alt;*',
	double: true,
	一级: '.ax-split-2&&li;.radio-title&&Text;;;a&&href',
	二级: {
		"title":"h1&&Text;.ax-breadcrumb:eq(1)&&Text",
		"img":"",
		"desc":";;;;.ax-des:eq(0)&&Text",
		"content":".ax-ignore:eq(0)&&Text",
		"重定向":"js:let url = jsp.pd(html,'#play&&iframe&&src');log('重定向到:'+url);html = request(url)",
		"tabs":"js:TABS=['信号源']",
		"lists":"div:eq(1)&&a"
	},
	搜索: 'body .ax-item-block;.ax-title&&Text;.ax-img&&style;.ax-color-des:eq(1)&&Text;*',
}
