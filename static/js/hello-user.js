window.addEventListener('load', function(){
    var hello = document.getElementById('hello').textContent
    if (hello != ""){
        if (hello == 'marcos')
            alert("Seja Bem-vindo!, patrão!")
        else
            alert("Seja Bem-vindo!, " + hello)
    }
})