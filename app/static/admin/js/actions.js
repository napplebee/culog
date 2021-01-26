var generatePost = function(recipe_id, lang){
    console.log(recipe_id, lang);
    $.ajax({
        url: "/admin/recipe/render/" + recipe_id + "/" + lang,
        method: "POST",
        success: function(data){
            console.log(data);
        }
    });
};

var visible = function(recipe_id, visibility){
    console.log(recipe_id, visibility);
};

var closeMenu = function(recipe_id){
    $("#dd-menu-"+recipe_id).removeClass("open");
    $("#dd-btn-"+recipe_id).attr("aria-expanded", "false");
}

var showResultMessage = function(msg){
    $("#actionResultMsg").text(msg)
    $("#actionResult").addClass("show").removeClass("hidden");

}

$(document).ready(function(){
    var RU_LANG = "ru";
    var EN_LANG = "en";
    var ALL_LANG = "all";
    //generate ru
    $("[id^='generate_ru_']").click(function(){
        var recipe_id = $(this).attr('data-r-id');
        closeMenu(recipe_id);
        generatePost(recipe_id, RU_LANG);
        showResultMessage("Russian post was created");
        return false;
    });
    //generate en
    $("a[id^='generate_en_']").click(function(){
        var recipe_id = $(this).attr('data-r-id');
        closeMenu(recipe_id);
        generatePost(recipe_id, EN_LANG);
        showResultMessage("English post was created");
        return false;
    });
    //generate both
    $("a[id^='generate_all_']").click(function(){
        var recipe_id = $(this).attr('data-r-id');
        closeMenu(recipe_id);
        generatePost(recipe_id, ALL_LANG);
        showResultMessage("Russian & English posts were created");
        return false;
    });
    $("a[id^='make_visible_']").click(function(){
        var recipe_id = $(this).attr('data-r-id');
        closeMenu(recipe_id);
        visible(recipe_id, true);
        showResultMessage("Recipe is visible now");
        return false;
    });
    $("a[id^='make_invisible_']").click(function(){
        var recipe_id = $(this).attr('data-r-id');
        closeMenu(recipe_id);
        visible(recipe_id, false);
        showResultMessage("Recipe is invisible now");
        return false;
    });
});