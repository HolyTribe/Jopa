import request from '../components/tools/utils';

function ajaxSearch(event) {
    var url = event.target.closest('form').getAttribute('action');
    var class_block = document.getElementById('tag-search__dropdown');
    request('post', url, {'search':event.target.value})
        .then((response) => {
            class_block.innerHTML = response.template
        });
}

document.querySelector('.search-input')
    .addEventListener('input', ajaxSearch);
