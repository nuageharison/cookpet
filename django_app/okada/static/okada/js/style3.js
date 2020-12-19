var pics_src = new Array("{% static 'okada/images/pet.png'%}","pics/2.jpg","pics/3.jpg");
var num = 0;

$("btn1".on("click", function(){
    if (num == 2) {num = 0;}
    else {num ++;}
    document.getElementById("mypic").src=pics_src[num];
}
function go_back(){
    if (num == 0) {num = 2;}
    else {num --;}
    document.getElementById("mypic").src=pics_src[num];
}
