import request from '../tools/utils';

function createImage(img, container) {
    let figure = document.createElement('figure');
    figure.style.flexGrow = (img.width * 100 / img.height).toString();
    figure.style.flexBasis = img.width * 200 / img.height + 'px';
    let i = document.createElement('i');
    i.style.paddingBottom = img.height / img.width * 100 + '%';
    let image = document.createElement('img')
    image.src = img.url;
    image.alt = img.alt;
    figure.appendChild(i);
    figure.appendChild(image);
    container.appendChild(figure);
}

function getImages() {
    request('POST', location.pathname)
        .then(response => {
            if (response.images) {
                let container = document.querySelector('.grid')
                response.images.forEach(img => createImage(img, container))

            }
        })
}

export default function galleryInit() {
    getImages();
}