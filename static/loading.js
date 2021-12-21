function loading (){
    var loading = document.getElementsByClassName("loading");
    var container = document.getElementsByClassName("result-container");
    loading[0].style.display = 'none';
    container[0].style.display = 'block';
}

if(window){
    window.addEventListener('load', loading);
}