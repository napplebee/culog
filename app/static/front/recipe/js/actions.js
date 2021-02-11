function switch_lang(v,loc)
{
    Cookies.set("lang", v);
    if(loc) {
        location.href = loc;
    } else {
    	location.reload()
    }
    return false;
}

var loadMore = function(){
    var rows = $("div#indexContainer > div.row");
    console.log(rows.length);
    $.ajax({
        url: "/more/" + rows.length,
        method: "POST",
        dataType: "json",
        success: function(data){
            $("div#indexContainer").append(data.payload)
            var my_locale = "";
            var my_lang = Cookies.get('lang');
            if(my_lang == "ru"){
              my_locale = "ru";
            } else if(my_lang == "ru"){
              my_locale = "en_US";
            }
            document.timeago.render(document.querySelectorAll('.timeago'), my_locale)
        }
    });
}

$(document).ready(function(){
    $("#loadMore").click(function(event){
        event.preventDefault();
        loadMore();
    })
});