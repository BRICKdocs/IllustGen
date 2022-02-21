function loading (){
    var loading = document.getElementsByClassName("loading");
    var container = document.getElementsByClassName("container");
    loading[0].style.display = 'flex';
    container[0].style.display = 'none';
}

if(window) {
    document.getElementsByClassName("loading")[0].style.display = 'none';
}