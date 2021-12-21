function loading (){
    var loading = document.getElementsByClassName("loading");
    var container = document.getElementsByClassName("container");
    loading[0].style.display = 'none';
    container[0].style.display = 'block';
}

if(window){
    window.addEventListener('load', loading);
}