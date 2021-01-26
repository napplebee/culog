var initIngrButtons = function(prefix) {
    $("button[id^='"+prefix+"IngrTypeCp']").on('click', function(){
        var idx = $(this).attr("data-idx");
        var newIngrType = $("#"+prefix+"IngrType-" + idx).clone(true);

        var nextIdx = -1;
        $("div#"+prefix+"IngTypeContainer > div").each(function(){
            var curIdx = parseInt($(this).attr("id").split("-")[1]);
            nextIdx = curIdx > nextIdx ? curIdx : nextIdx;
        })
        nextIdx = nextIdx + 1;

        newIngrType.attr('id', prefix+"IngrType-" + nextIdx);

        var _ = function(x){
            x.each(function(){
                var obj = $(this);
                var id = obj.attr('id');
                obj.attr('id', id.replace(/-\d+/g, "-"+nextIdx));
                obj.attr('data-idx', nextIdx);
            });
        }
        _(newIngrType.find("button[id^='"+prefix+"IngrTypeCp-']"));
        _(newIngrType.find("button[id^='"+prefix+"IngrTypeRm-']"));

        newIngrType.find("div[id^='"+prefix+"IngContainer-']").each(function(){
            var obj = $(this);
            var id = obj.attr('id');
            obj.attr('id', id.replace(/-\d+/g,"-" + nextIdx));
        });

        newIngrType.find("button[id^='"+prefix+"IngrCp-']").each(function(){
                var obj = $(this);
                var id = obj.attr('id');
                obj.attr('id', id.replace(/-\d+-/g, "-" + nextIdx + "-"));
                obj.attr('data-outer', nextIdx);
            });
        newIngrType.find("button[id^='"+prefix+"IngrRm-']").each(function(){
                var obj = $(this);
                var id = obj.attr('id');
                obj.attr('id', id.replace(/-\d+-/g, "-" + nextIdx + "-"));
                $(this).attr('data-outer', nextIdx);
            });
        newIngrType.find("div[id^='"+prefix+"IngContainer-']").each(function(){
            var obj = $(this);
            var id = obj.attr('id');
            obj.attr('id', id.replace(/-\d+/g, "-" + nextIdx));
        });
        newIngrType.find("div[id^='"+prefix+"Ing-" + idx + "-']").each(function(){
            var obj = $(this);
            var id = obj.attr('id');
            var r = new RegExp(prefix+"Ing-\\d+-", 'g')
            obj.attr("id", id.replace(r, prefix+"Ing-" + nextIdx + "-"))
        });


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
            obj.val("");
        });
        newIngrType.find("select")
        .each(function(){
            var obj = $(this);
            var val = obj.attr('id');
            obj.attr('id', val.replace(/ingredients_type-\d+/g, "ingredients_type-" + nextIdx));
            val = obj.attr('name');
            obj.attr('name', val.replace(/ingredients_type-\d+/g, "ingredients_type-" + nextIdx));
        });
        $("#"+prefix+"IngTypeContainer").append(newIngrType);
        return false;
    });
    $("button[id^='"+prefix+"IngrTypeRm']").on('click', function(){
        var idx = $(this).attr("data-idx");
        $("#"+prefix+"IngrType-" + idx).remove();
        return false;
    });

    $("button[id^='"+prefix+"IngrCp']").on('click', function(){
        var idx = $(this).attr("data-idx");
        var outerIdx = $(this).attr("data-outer");
        var newIngr = $("#"+prefix+"Ing-" + outerIdx + "-" + idx).clone(true);

        var nextIdx = -1;

        $("div#"+prefix+"IngContainer-" + outerIdx + "> div").each(function(){
            var curIdx = parseInt($(this).attr("id").split("-")[2]);
            nextIdx = curIdx > nextIdx ? curIdx : nextIdx;
        });

        nextIdx = nextIdx + 1;

        newIngr.attr("id", ""+prefix+"Ing-" + outerIdx + "-" + nextIdx);

        var _ = function(x){
            x.each(function(){
                var obj = $(this);
                var id = obj.attr('id');
                obj.attr('id', id.replace(/-\d+-\d+/g, "-" + outerIdx + "-" + nextIdx));
                obj.attr('data-outer', outerIdx);
                obj.attr('data-idx', nextIdx);
            });
        };

        _(newIngr.find("button[id^='"+prefix+"IngrCp-']"));
        _(newIngr.find("button[id^='"+prefix+"IngrRm-']"));

        newIngr.find("label").each(function(){
            var obj = $(this);
            var val = obj.attr('for');
            if (!val) return;
            obj.attr('for', val.replace(/ingredients-\d+/g, "ingredients-" + nextIdx));
        });

        newIngr.find("input")
        .each(function(){
            var obj = $(this);
            var val = obj.attr('id');
            obj.attr('id', val.replace(/ingredients-\d+/g, "ingredients-" + nextIdx));
            val = obj.attr('name');
            obj.attr('name', val.replace(/ingredients-\d+/g, "ingredients-" + nextIdx));
            obj.val("");
        });
        newIngr.find("select")
        .each(function(){
            var obj = $(this);
            var val = obj.attr('id');
            obj.attr('id', val.replace(/ingredients-\d+/g, "ingredients-" + nextIdx));
            val = obj.attr('name');
            obj.attr('name', val.replace(/ingredients-\d+/g, "ingredients-" + nextIdx));
        });

        //newIngr.find("select").val("etc");

        $("#"+prefix+"IngContainer-" + outerIdx).append(newIngr);
        return false;
    });
    $("button[id^='"+prefix+"IngrRm']").on('click', function(){
        var idx = $(this).attr('data-idx');
        var outerIdx = $(this).attr("data-outer");
        $("#"+prefix+"Ing-" + outerIdx + "-" + idx).remove();
    });
};

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

    initIngrButtons("en");
    initIngrButtons("ru");
});