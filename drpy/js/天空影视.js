// 网址发布页 http://tkznp9.com/
muban.mxpro.二级.desc = '.module-info-item:eq(4)&&Text;;;.module-info-item-content:eq(1)&&Text;.module-info-item-content:eq(0)&&Text'
muban.mxpro.二级.tabs = '#y-playList .module-tab-item'
var rule = {
	title:'天空影视',
	模板:'mxpro',
	host:'https://tkznp.com',
	// host:'https://www.tkys6.com',
	// url: '/vodshow/id/fyclass/page/fypage.html',
	url:'/vodshow/id/fyfilter.html',
	filterable:1,//是否启用分类筛选,
	filter_url:'{{fl.cateId}}{{fl.area}}{{fl.by}}{{fl.class}}{{fl.lang}}{{fl.letter}}/page/fypage{{fl.year}}',
	filter_def:{
		1:{cateId:'1'},
		2:{cateId:'2'},
		3:{cateId:'3'},
		4:{cateId:'4'}
	},
    searchable:2,//是否启用全局搜索,
	quickSearch:0,//是否启用快速搜索,
	class_parse:'.navbar-items li:gt(1):lt(9);a&&Text;a&&href;/(\\d+).html',
	searchUrl:'/index.php/ajax/suggest?mid=fypage&wd=**',
    detailUrl:'/voddetail/fyid.html', //非必填,二级详情拼接链接
	// 搜索:'#searchList&&li;h4&&Text;a&&data-original;.detail&&p:eq(2)&&Text;a&&href;.detail&&p:eq(3)&&Text',
	搜索:'json:list;name;pic;;id',
}
