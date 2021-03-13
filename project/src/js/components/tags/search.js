import request from '../tools/utils';

function ajaxSearch(event) {
    var url = event.target.closest('form').getAttribute('action');
    var resultList = document.getElementById('tag-search__dropdown');
    request('post', url, {'search':event.target.value})
        .then((response) => {
            resultList.innerHTML = response.template
        });
}

export default function search(event){
    ajaxSearch(event);
};