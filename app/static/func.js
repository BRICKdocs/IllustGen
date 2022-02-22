function info_toggle(){
    var info = document.getElementsByClassName("mint-info");
    console.log(info[0].style.display)
    if(info[0].style.display == 'none'){
        info[0].style.display = 'block'
    }
    else{
        info[0].style.display = 'none'
    }
    console.log('click')
}

if(window) {
    document.getElementsByClassName("mint-info")[0].style.display = 'none';
}