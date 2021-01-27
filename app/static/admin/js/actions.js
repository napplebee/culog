var visible = function(recipe_id, visibility, message){
    console.log(recipe_id, visibility, message);
};

var closeMenu = function(recipe_id){
    $("#dd-menu-"+recipe_id).removeClass("open");
    $("#dd-btn-"+recipe_id).attr("aria-expanded", "false");
}

var showResultMessage = function(msg){
    $("#actionResultMsg").text(msg)
    $("#actionResult").addClass("show").removeClass("hidden");
}

var generatePost = function(recipe_id, lang, message){
    console.log(recipe_id, lang);
    $.ajax({
        url: "/admin/recipe/render/" + recipe_id + "/" + lang,
        method: "POST",
        success: function(data){
            showResultMessage(message)
        }
    });
};

$(document).ready(function(){
    var RU_LANG = "ru";
    var EN_LANG = "en";
    var ALL_LANG = "all";
    //generate ru
    $("[id^='generate_ru_']").click(function(){
        var recipe_id = $(this).attr('data-r-id');
        closeMenu(recipe_id);
        generatePost(recipe_id, RU_LANG, "Russian post was created");
        return false;
    });
    //generate en
    $("a[id^='generate_en_']").click(function(){
        var recipe_id = $(this).attr('data-r-id');
        closeMenu(recipe_id);
        generatePost(recipe_id, EN_LANG, "English post was created");
        return false;
    });
    //generate both
    $("a[id^='generate_all_']").click(function(){
        var recipe_id = $(this).attr('data-r-id');
        closeMenu(recipe_id);
        generatePost(recipe_id, ALL_LANG, "Russian & English posts were created");
        showResultMessage();
        return false;
    });
    $("a[id^='make_visible_']").click(function(){
        var recipe_id = $(this).attr('data-r-id');
        closeMenu(recipe_id);
        visible(recipe_id, true, "Recipe is visible now");
        return false;
    });
    $("a[id^='make_invisible_']").click(function(){
        var recipe_id = $(this).attr('data-r-id');
        closeMenu(recipe_id);
        visible(recipe_id, false, "Recipe is invisible now");
        return false;
    });
});