const sharp = require('sharp');
const fs = require('fs');
const main_directory = './app/static/front/images';

fs.readdirSync(main_directory).forEach(folder => {
    isDirectory = fs.lstatSync(`${main_directory}/${folder}`).isDirectory()
    if (isDirectory) {
        fs.readdirSync(`${main_directory}/${folder}`).forEach(file => {
            sharp(`${main_directory}/${folder}/${file}`)
                .resize(1000, null) // width, height
                .toFile(`${main_directory}/${folder}/${file}`);
            });
    }
});