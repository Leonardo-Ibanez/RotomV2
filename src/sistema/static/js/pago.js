window.onload = function () {

    let getData = sessionStorage.getItem("datos");
   
    document.getElementById("idFromSession").innerHTML = getData;
    //idFromSession
}
