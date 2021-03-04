const maxHeight = 300;

const newRow = (mosaic) => {
    let row = document.createElement('div');
    row.classList.add('mosaic-row');
    mosaic.appendChild(row);
    return row;
};

const calcValidW = (w, h) => {
    let newW = w / (h / maxHeight);
    console.log('validW', newW, newW - w);
    return [newW, w - newW]
};

const normalizeRow = (row, rowWidth, imagesWidth) => {
    let images = row.children;
    let optimization = (rowWidth - imagesWidth) / images.length;
    console.log('opt',imagesWidth, rowWidth, images.length, optimization);
    for (let image of images) {
       let result = calcValidW(image.dataset.w,350);
       image.style.width = "" + (result[0] + optimization) + 'px';
       image.style.height = "" + (300) + 'px';
    }
};

export const fill = (mosaic, images) => {
    let currentRow = newRow(mosaic);
    console.log(currentRow);
    let currentWidth = 0;
    let currentAvailableWidth = 0;
    console.log(currentRow, currentRow.clientWidth);
    let currentRowWidth = currentRow.clientWidth;
    for (let image of images) {
        if (currentRowWidth - currentWidth - currentAvailableWidth > 0) {
            let result = calcValidW(image.dataset.w, 350);
            currentWidth += result[0];
            currentAvailableWidth += result[1];
            console.log(currentRowWidth, currentWidth, currentAvailableWidth);
            currentRow.appendChild(image);
        } else {
            normalizeRow(currentRow, currentRowWidth, currentWidth);
            currentRow = newRow(mosaic);
            let result = calcValidW(image.dataset.w, 350);
            currentWidth = result[0];
            currentAvailableWidth = result[1];
            currentRow.appendChild(image);
        }
    }
    normalizeRow(currentRow, currentRowWidth, currentWidth);
};