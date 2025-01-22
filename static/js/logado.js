window.addEventListener('load', function(){
    var login = document.querySelector('#login')
    var logar = document.querySelector('.log')
    var sair = document.querySelector('.sair')

    if (login.textContent != ''){
        sair.style.display = 'inline-block'
        logar.style.display = 'none'
    }else{
        logar.style.display = 'inline-block'
        sair.style.display = 'none'
    }
})