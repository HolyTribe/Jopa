import request from '../tools/utils';

function ajaxLogin(event){
    event.preventDefault();
    var form = event.target.closest('form');
    var url = form.getAttribute('action');
    var data = new FormData(form);
    request('post', url, data)
        .then((result)=>{
            if(result.errors==true){
                displayErrors(form);
            }else{
                window.location = result.redirect;
            }
        })
}

function displayErrors(form){
    var elements = form.elements;
    for (var i = 0, element; element = elements[i++];) {
        if(element.type != 'submit'){
            element.style.borderColor = 'red';
        }
    }
    
    if(form.getElementsByClassName('user-note').length>0)
        form.getElementsByClassName('user-note')[0].remove()

    var note = document.createElement('span');
    note.className = 'user-note'
    note.innerText = 'Проверьте введенные данные';
    note.style.color = 'red';
    form.append(note);
}

// document.querySelector('.login-btn')
//     .addEventListener('click', ajaxLogin);

export default function login(event){
    ajaxLogin(event);
}