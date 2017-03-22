/**
 * Created by Maffee on 2016/12/13.
 */
function Demo_focus_Comprt(area,block,comprt){
    if (block == undefined){
        alert(area)
    }
    else if(comprt == undefined){
        alert(area + ":" + block)
    }
    else if (comprt != undefined){
        alert(area + ":" + block + "|" + comprt)
    }
    else{
        alert("Demo_focus_Comprt ERROR")
    }
}
