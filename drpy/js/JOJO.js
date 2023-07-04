var rule={
    title:'JOJO',
    host:'https://app.syrme.top',
    url:'/video/type/tag?type=fyclass&tag=&page=fypage&size=18',
    searchUrl:'/video/search?q=**',
    searchable:2,//是否启用全局搜索,
    quickSearch:0,//是否启用快速搜索,
    filterable:1,//是否启用分类筛选,
    
    headers:{
        'User-Agent':'UC_UA',
    },
    class_name:'电影&韩剧&美剧&动漫&纪录&日剧',
            class_url:'电影&韩剧&美剧&动漫&纪录&日剧',
    play_parse:true,
    lazy:"",
    limit:18,
    推荐:'*',
    double:true, // 推荐内容是否双层定位
    一级:'div.content-body .content-item;.card-title&&Text;img&&src;.item-speed&&Text;a&&href',
    二级:{"title":"h3&&Text;.content-detail&&p&&Text","img":"img&&src","desc":";;;.content-detail&&p:eq(3)&&Text;.content-detail&&p:eq(4)&&Text","content":".desc&&Text","tabs":".tabs-plyr-tab","lists":".tabs-plyr-list:eq(#id)&&.list-item"},
    搜索:'*',
}