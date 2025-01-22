window.addEventListener('load', function(){
    var button = document.querySelector('.button')
    var login = document.querySelector('#login')
    var s1 = document.querySelector('#s1')
    var s2 = document.querySelector('#s2')
    var msg = document.querySelector('.msg')

    button.addEventListener('click', function(){
        if (login.value == "" || s1.value == "" || s2.value == ""){
            msg.style.color = "red"
            msg.textContent = "Preencha todos os campos!"
            button.setAttribute('type', 'reset')
        }else if (s1.value != s2.value){
            msg.style.color = "red"
            msg.textContent = "As senhas devem ser iguais!"
            button.setAttribute('type', 'reset')
        }else{
            msg.style.color = "black"
            msg.textContent = ""
            button.setAttribute('type', 'submit')
        }
    })
})