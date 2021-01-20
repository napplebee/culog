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