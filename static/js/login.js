window.addEventListener('load', function(){
    var button = document.querySelector('.button')
    var login = document.querySelector('#login')
    var senha = document.querySelector('#senha')
    var msg = document.querySelector('.msg')

    button.addEventListener('click', function(){
        if (login.value == "" || senha.value == ""){
            msg.style.color = "red"
            msg.textContent = "Preencha todos os campos!"
            button.setAttribute('type', 'reset')
        }else{
            msg.style.color = "black"
            msg.textContent = ""
            button.setAttribute('type', 'submit')
        }
    })
})