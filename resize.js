const sharp = require('sharp');
const fs = require('fs');
const main_directory = './app/static/front/images';

async function resizeFile(path) {
    let buffer = await sharp(path)
        .resize(1000, null, {withoutEnlargement: true})
        .toBuffer();
    return sharp(buffer).toFile(path);
  }

fs.readdirSync(main_directory).forEach(folder => {
    isDirectory = fs.lstatSync(`${main_directory}/${folder}`).isDirectory()
    if (isDirectory) {
        fs.readdirSync(`${main_directory}/${folder}`).forEach(file => {
            sharp(`${main_directory}/${folder}/${file}`, { failOnError: false })
                .resize(1000, null, {withouthEnlargement: true})
                .toBuffer()
                .then((buffer) => {
                    sharp(buffer, { failOnError: false }).toFile(`${main_directory}/${folder}/${file}`);
                })
                .catch(err => console.log(err));
            
            //await resizeFile(`${main_directory}/${folder}/${file}`)
            sharp(`${main_directory}/${folder}/${file}`, { failOnError: false })
                .resize(300, null, {withouthEnlargement: true})
                .toFile(`${main_directory}/${folder}/${file.slice(0, -4)}_small.jpg`);
        });
    }
});