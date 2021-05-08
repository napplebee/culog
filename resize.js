const sharp = require('sharp');
const fs = require('fs');
const main_directory = './app/static/front/images';


fs.readdirSync(main_directory).forEach(folder => {
    isDirectory = fs.lstatSync(`${main_directory}/${folder}`).isDirectory()
    if (isDirectory) {
        fs.readdirSync(`${main_directory}/${folder}`).forEach(file => {
            //sharp(`${main_directory}/${folder}/${file}`, { failOnError: false })
            //    .resize(1000, null, { withouthEnlargement: true })
            //    .toBuffer()
            //    .then((buffer) => {
            //        sharp(buffer, { failOnError: false })
            //            .toFile(`${main_directory}/${folder}/${file}`)
            //            .catch(err => console.log(`${main_directory}/${folder}/${file}`,err));
            //    })
            //    .catch(err => console.log(`${main_directory}/${folder}/${file}`, err));
            
            if (file.indexOf("_small") === -1) {
                sharp(`${main_directory}/${folder}/${file}`)
                    .resize(350, null, { withouthEnlargement: true })
                    .toFile(`${main_directory}/${folder}/${file.slice(0, -4)}_small.jpg`)
                    .catch(err => console.log(`${main_directory}/${folder}/${file}`, err));
            }
        });
    }
});