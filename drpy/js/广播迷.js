var rule = {
    title:'广播',
    编码:'gb18030',
    host:'http://www.guangbomi.com',
    url:'/live/fyclass/fypage.html[/live/fyclass/]',
    searchUrl:'/index.php?m=search&c=index&a=init&siteid=1&typeid=54&q=**',
    searchable:2,
    quickSearch:0,
    headers:{
        'User-Agent':'MOBILE_UA'
    },
    timeout:5000,

    class_name:'北京&浙江&湖南',
    class_url:'bj&zj&hunan',
    play_parse:true,
    lazy:'',
    limit:6,
    推荐:'.ax-grid-inner&&li;.radio-title&&Text;*;.radio-title&&Text;a&&href',
    一级:'.ax-grid-inner&&li;.ax-md&&Text;*;.ax-hide-tel&&Text;a&&href',
    二级:"*",
     搜索:'body .ax-item-block;.ax-ell-title&&Text;*;.ax-icon-clock&&Text;a&&href;',
}