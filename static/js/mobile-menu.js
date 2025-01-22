window.addEventListener('load', function(){
    var icoMenu = document.querySelector('.mobile-menu > img')
    var menu = document.querySelector('.menu')
    var body = document.querySelector('body')

    icoMenu.addEventListener('click', function(e){
        menu.style.right = 0
        e.stopPropagation()
    })

    menu.addEventListener('click', function(e){
        e.stopPropagation()
    })

    body.addEventListener('click', function(){
        if (menu.style != '-250px')
            menu.style.right = '-250px'
    })
})