/* const sharp = require('sharp');
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
*/

const sharp = require('sharp');
const fs = require('fs');
const main_directory = './app/static/front/images';


fs.readdirSync(main_directory).forEach(folder => {
    is_directory = fs.lstatSync(`${main_directory}/${folder}`).isDirectory()
    if (is_directory) {
        fs.readdirSync(`${main_directory}/${folder}`).forEach(file => {
            is_small_file = file.indexOf("_small") > -1
            if (is_small_file) {
                small_file_path = `${main_directory}/${folder}/${file}`
                big_file_path = `${main_directory}/${folder}/${file.slice(0, -10)}.jpg`
            } else {
                small_file_path = `${main_directory}/${folder}/${file.slice(0, -4)}_small.jpg`
                big_file_path = `${main_directory}/${folder}/${file}`
            }

            small_file_exists = fs.existsSync(small_file_path)
            if (!is_small_file && !small_file_exists) {
                console.log(file, is_small_file, small_file_exists, small_file_path, big_file_path)
                sharp(big_file_path, { failOnError: false })
                    .resize(1000, null, { withoutEnlargement: true })
                    .toBuffer()
                    .then((buffer) => {
                        sharp(buffer, { failOnError: false })
                            .toFile(big_file_path)
                            .catch(err => console.log(big_file_path, err));
                    })
                    .catch(err => console.log(big_file_path, err));
                
                sharp(big_file_path)
                    .resize(350, null, { withoutEnlargement: true })
                    .toFile(small_file_path)
                    .catch(err => console.log(`${main_directory}/${folder}/${file}`, err));
            }
        });
    }
});