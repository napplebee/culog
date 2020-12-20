$(document).ready(function(){
    $("#ruTabLink").click(function(){
        $("div[id^='en_group_fields']").hide();
        $("div[id^='ru_group_fields']").show();
        $("#enTab").removeClass("active");
        $("#ruTab").addClass("active");
        return false;
    });
    $("#enTabLink").click(function(){
        $("div[id^='ru_group_fields']").hide();
        $("div[id^='en_group_fields']").show();
        $("#ruTab").removeClass("active");
        $("#enTab").addClass("active");
        return false;
    });

    $("button[id^='enIngrTypeCp']").click(function(){
        var idx = $(this).attr("data-idx");
        var newIngrType = $("#enIngrType-" + idx).clone(true);

        var nextIdx = -1;
        //iterate over list of
        // div#enIngrType-(\d+)
        $("div#engIngTypeContainer > div").each(function(){
            var curIdx = parseInt($(this).attr("id").split("-")[1]);
            nextIdx = curIdx > nextIdx ? curIdx : nextIdx;
        })
        nextIdx = nextIdx + 1;

        // now all the id & name attrs must be adjusted
        // according with nextIdx
        /*
        button[id^='enIngrTypeCp-']
        button[id^='enIngrTypeRm-']
        label[
            class="control-label",
            for="blog_post_header_en-ingredients_type-0-name" ]
        input[id^="blog_post_header_en-ingredients_type-0-name"
              name="blog_post_header_en-ingredients_type-0-name"
              type="text"]
        but keep in mind nested elements, i.e. ingredients that
        belong to an ingredient_type

        #blog_post_header_en-ingredients_type-0-ingredients-0-name
        */
        newIngrType.prop('id', "enIngrType-" + nextIdx)

        var _ = function(x){
            x.each(function(){
                var obj = $(this);
                var id = obj.attr('id');
                obj.attr('id', id.replace(/-\d+/g, "-"+nextIdx));
                obj.attr('data-idx', nextIdx);
            });
        }
        _(newIngrType.find("button[id^='enIngrTypeCp-']"))
        _(newIngrType.find("button[id^='enIngrTypeRm-']"))


        newIngrType.find("label")
        .each(function(){
            var obj = $(this);
            var val = obj.attr('for');
            if(!val) return;
            obj.attr('for', val.replace(/ingredients_type-\d+/g, "ingredients_type-" + nextIdx));
        });

        newIngrType.find("input")
        .each(function(){
            var obj = $(this);
            var val = obj.attr('id');
            obj.attr('id', val.replace(/ingredients_type-\d+/g, "ingredients_type-" + nextIdx));
            val = obj.attr('name');
            obj.attr('name', val.replace(/ingredients_type-\d+/g, "ingredients_type-" + nextIdx));
        });
        $("#engIngTypeContainer").append(newIngrType);
        return false;
    });

    $("button[id^='enIngrTypeRm']").click(function(){
        var idx = $(this).attr("data-idx");
        $("#enIngrType-" + idx).remove();
    });

    $("button[id^='enIngrCp']").click(function(){
        var idx = $(this).attr("data-idx");
        var outerIdx = $(this).attr("data-outer");
        var newIngr = $("#enIng-" + outerIdx + "-" + idx).clone(true);
    });

    $("button[id^='enIngrRm']").click(function(){
        var idx = $(this).attr('data-idx');
        var outerIdx = $(this).attr("data-outer");
        $("#enIng-" + outerIdx + "-" + idx).remove();
    });
});