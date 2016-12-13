/**
 * Created by Maffee on 2016/12/13.
 */
function focus_Demo_Block(area,zone,block){
    if (block != undefined){
        alert(area + ":" + zone + "-" + block)
    }
    else if(block == undefined){
        alert(area + ":" + zone)
    }
    else{
        alert("focus_Demo_Block ERROR")
    }

}