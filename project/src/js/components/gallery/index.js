let images = [
    'https://images.unsplash.com/photo-1503023345310-bd7c1de61c7d?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MXx8aHVtYW58ZW58MHx8MHw%3D&ixlib=rb-1.2.1&w=1000&q=80',
    'https://images.ctfassets.net/hrltx12pl8hq/4plHDVeTkWuFMihxQnzBSb/aea2f06d675c3d710d095306e377382f/shutterstock_554314555_copy.jpg',
    'https://images.unsplash.com/photo-1494548162494-384bba4ab999?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MXx8c3VucmlzZXxlbnwwfHwwfA%3D%3D&ixlib=rb-1.2.1&w=1000&q=80',
    'https://static.toiimg.com/photo/72975551.cms',
    'https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__340.jpg',
    'https://i.pinimg.com/originals/ca/76/0b/ca760b70976b52578da88e06973af542.jpg',
    'https://images.unsplash.com/photo-1541963463532-d68292c34b19?ixlib=rb-1.2.1&ixid=MXwxMjA3fDB8MHxleHBsb3JlLWZlZWR8M3x8fGVufDB8fHw%3D&w=1000&q=80',
    'https://cdn.eso.org/images/thumb300y/eso1907a.jpg',
    'https://www.gettyimages.com/gi-resources/images/500px/983794168.jpg',
    'https://images.ctfassets.net/hrltx12pl8hq/6bi6wKIM5DDM5U1PtGVFcP/1c7fce6de33bb6575548a646ff9b03aa/nature-photography-pictures.jpg?fit=fill&w=800&h=300',
    'https://zastavok.net/ts/anime/159707784417.jpg',
    'https://cs10.pikabu.ru/post_img/big/2019/11/26/5/1574748274166787960.jpg',
    'http://cdn.iz.ru/sites/default/files/styles/900x506/public/article-2020-06/34434.jpg?itok=72HB2Nla',
    'https://gamemag.ru/images/cache/News/News149304/d2e6609e57-2_1390x600.jpg',
    'https://i.pinimg.com/originals/9a/b7/b5/9ab7b5bb4c44f11e01502ce9a54a4d75.jpg',
    'https://imgix.ranker.com/user_node_img/50096/1001915293/original/nezuko-kamado-photo-u1?fit=crop&fm=pjpg&q=60&w=375&dpr=2',
    'https://i.pinimg.com/564x/0a/7c/f4/0a7cf44f2252b098b210d67fe8f94d9d.jpg',
    'https://img2.goodfon.ru/wallpaper/nbig/c/c0/anime-art-devushka-ochki.jpg',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRzKyjNvYi49osTdMDcDoPkQ3AV1S6cfdOEmA&usqp=CAU',
    'https://cdn.fishki.net/upload/post/2020/01/27/3212249/tn/1-zakat-devushka-anime-gorod-most.jpg',
    'https://www.teahub.io/photos/full/98-987456_photo-wallpaper-look-girl-hand-anime-art-squints.jpg',
    'https://img4.goodfon.ru/wallpaper/nbig/9/91/girl-owl-birds-hair-bows-pointy-ears-glasses-hair-ornament-s.jpg',
    'https://c.wallhere.com/photos/fb/a1/anime_anime_girls_digital_art_artwork_2D_portrait_display_vertical-1869933.jpg!d'
];

let container = document.querySelector('.grid');
images = images.sort(() => {
    return Math.random() - 0.5;
});

function create() {
    images.forEach(img => {
        let image = document.createElement('img');
        image.src = img;
        container.appendChild(image);
    });
    document.querySelectorAll('img').forEach(img => {
        setTimeout(() => {
            let parent = img.closest('figure');
            if (!parent) {
                let figure = document.createElement('figure');
                figure.style.flexGrow = img.naturalWidth * 100 / img.naturalHeight;
                figure.style.flexBasis = img.naturalWidth * 200 / img.naturalHeight + 'px';
                let i = document.createElement('i');
                i.style.paddingBottom = img.naturalHeight / img.naturalWidth * 100 + '%';
                figure.appendChild(i);
                figure.appendChild(img);
                container.appendChild(figure);
            }
        }, 100)
    })
}

window.create = create;
window.create();

export default function galleryInit() {
    return true
}