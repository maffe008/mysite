/**
* Created by Maffee on 2016/12/13.
*/
$(document).ready(function(){
    $("#optionToggle").click(function(){
        $("#optionBar").toggle();
        $(this).toggleClass("ToggleLogoLayer");
        if($(".esri-ui-corner").css("left") == "300px"){
            //alert($(".esri-ui-corner").css("left"));
            $(".esri-ui-corner").css({"left":"0"});
            $("#overviewDiv").css({"left":"12px"});
        }
        else {
            //alert($(".esri-ui-corner").css("left"));
            $(".esri-ui-corner").css({"left":"300px"});
            $("#overviewDiv").css({"left":"312px"});
        }

    });
});
$(document).ready(function(){
    $("#listToggle").click(function(){
        $("#listBar").toggle();
        $(this).toggleClass("ToggleLogoEtc");

    });
});
$(document).ready(function(){
    $(".optionToolBlock").mouseover(function(){
        $(this).css({"background-color":"rgba(241,242,242,0.9","color":"#222222"})
    });
});
$(document).ready(function(){
    $(".optionToolBlock").mouseout(function(){
        $(this).css({"background-color":"transparent","color":"#f1f2f2"})
    });
});