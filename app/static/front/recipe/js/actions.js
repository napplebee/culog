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
        url: "/recipe/more/" + rows.length,
        method: "POST",
        dataType: "json",
        success: function(data){
            $("div#indexContainer").append(data.payload)
        }
    });
}

$(document).ready(function(){
    $("#loadMore").click(function(event){
        event.preventDefault();
        loadMore();
    })
});