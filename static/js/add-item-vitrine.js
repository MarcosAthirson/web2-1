window.addEventListener('load', function(){
    var buttonAdd = document.querySelector('.add-item')
    var login = document.querySelector('#login')

    if (login.textContent == 'marcos')
        buttonAdd.style.display = 'block'
    else
        buttonAdd.style.display = 'none'

    var sectionAdd = document.querySelector('.add')
    var fecharForm = document.querySelector('.fechar')

    buttonAdd.addEventListener('click', function(){
        sectionAdd.style.display = 'block'
    })

    fecharForm.addEventListener('click', function(){
        sectionAdd.style.display = 'none'
    })

    var add = document.querySelector('.addItemVitrine input[value=ADICIONAR]')
    var nome = document.querySelector('.nome input')
    var valor = document.querySelector('.valor input')
    var qtd = document.querySelector('.qtd input')
    var msg = document.querySelector('.addItemVitrine .msg')

    add.addEventListener('click', function(){
        if(nome.value == "" || valor.value == "" || qtd.value == ""){
            msg.style.color = 'red'
            msg.textContent = 'Preencha todos os campos!'
            add.setAttribute('type', 'reset')
        }else if(qtd.value == "0"){
            msg.style.color = 'red'
            msg.textContent = 'A quantidade tem que ser maior que 0!'
            add.setAttribute('type', 'reset')
        }else{
            msg.textContent = ''
            add.setAttribute('type', 'submit')
        }
    })
})