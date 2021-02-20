var visible = function(recipe_id, visibility, lang){
    $.ajax({
        url: "/admin/recipe/visibility",
        method: "POST",
        dataType: "json",
        data: { recipe_id: recipe_id, lang: lang, visibility: visibility },
        success: function(data){
            showResultMessage(data.message)
        }
    });
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
    $("[id^='generate_ru_']").click(function(event){
        event.preventDefault();
        var recipe_id = $(this).attr('data-r-id');
        closeMenu(recipe_id);
        generatePost(recipe_id, RU_LANG, "Russian post was created");
        return false;
    });
    //generate en
    $("a[id^='generate_en_']").click(function(event){
        event.preventDefault();
        var recipe_id = $(this).attr('data-r-id');
        closeMenu(recipe_id);
        generatePost(recipe_id, EN_LANG, "English post was created");
        return false;
    });
    //generate both
    $("a[id^='generate_all_']").click(function(event){
        event.preventDefault();
        var recipe_id = $(this).attr('data-r-id');
        closeMenu(recipe_id);
        generatePost(recipe_id, ALL_LANG, "Russian & English posts were created");
    });
    $("button[id^='visible_']").click(function(event){
        event.preventDefault();
        //clicking on 'visible' makes it invisible
        var recipe_id = $(this).attr('data-r-id');
        var lang = $(this).attr('data-lang');
        visible(recipe_id, false, lang);
        $(this).removeClass('show').addClass('hidden');
        $("#invisible_" + lang + "_" + recipe_id).removeClass('hidden').addClass('show')
    });
    $("button[id^='invisible_']").click(function(event){
        event.preventDefault();
        //clicking on 'invisible' makes it visible
        var recipe_id = $(this).attr('data-r-id');
        var lang = $(this).attr('data-lang');
        visible(recipe_id, true, lang);
        $(this).removeClass('show').addClass('hidden');
        $("#visible_" + lang + "_" + recipe_id).removeClass('hidden').addClass('show')
    });
});