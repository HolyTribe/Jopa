function urlEncode(dict) {
    let pairs = [];
    for (let arg of Object.keys(dict)) {
        if (dict[arg].length && !(typeof dict[arg] === 'string' || dict[arg] instanceof String)) {
            for (let e of dict[arg]) pairs.push(`${arg}=${e}`);
        } else {
            if (dict[arg]) {
                pairs.push(`${arg}=${dict[arg]}`);
            }
        }
    }
    return pairs;
}

function urlEncodeAjax(dict) {
    let pairs = urlEncode(dict);
    const clear = pairs.join('&');
    pairs.push('ajax=on');
    return {clear, 'ajax': pairs.join('&')};
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfToken() {
    return getCookie('csrftoken');
}


function setLocation(curLoc){
    try {
      history.pushState(null, null, curLoc);
      return;
    } catch(e) {}
    location.hash = '#' + curLoc;
}


async function sendAjax(settings) {
    if (!settings || !settings.url || !settings.method) throw "Некорректно заполнены настройки запроса";
    let requestSettings = {
        method: settings.method.toUpperCase() || "GET",
        headers: {
            'Content-Type': settings.content_type || 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': csrfToken(),
        },
        redirect: settings.redirect ? 'follow' : 'manual',
    };
    const encodedUrls = urlEncodeAjax(settings.data);
    if (settings.method.toUpperCase() === 'POST') {
        requestSettings.body = encodedUrls['ajax'];
    } else {
        let clearUrl = `${settings.url}?${encodedUrls['clear']}`;
        settings.url = `${settings.url}?${encodedUrls['ajax']}`;
        if (settings.locSet) setLocation(clearUrl);
    }
    const response = await fetch(settings.url, requestSettings);
    if (response.ok)
        return await response.json();
    else
        return false
}


export let utils = {};
utils.ajax = {};
utils.ajax.send = sendAjax;
