const sharp = require('sharp');
const fs = require('fs');
const Promise = require('bluebird');
global.Promise = Promise;
const main_directory = './app/static/front/images';

async function start() {
    folders = fs.readdirSync(main_directory);
    for (const folder of folders) {
        is_directory = fs.lstatSync(`${main_directory}/${folder}`).isDirectory()
        if (is_directory) {
            files = fs.readdirSync(`${main_directory}/${folder}`);
            for (const file of files) {
                is_small_file = file.indexOf("_small") > -1
                is_big_file = file.indexOf("_big") > -1

                if (!is_small_file && !is_big_file) {
                    small_file_path = `${main_directory}/${folder}/${file.slice(0, -4)}_small.jpg`
                    big_file_path = `${main_directory}/${folder}/${file.slice(0, -4)}_big.jpg`
                    original_file_path = `${main_directory}/${folder}/${file}`

                    small_file_exists = fs.existsSync(small_file_path)

                    if (!small_file_exists) {
                        console.log(`[processing ${file}]`);
                        console.log(`Details for ${file}:`);
                        console.log(`small? ${is_small_file};`);
                        console.log(`small_exists: ${small_file_exists};`);
                        console.log(`small_path: ${small_file_path};`);
                        console.log(`big_path: ${big_file_path};`);
                        console.log(`original_path: ${original_file_path};`);

                        var sizes = [{
                                path: big_file_path,
                                width: 1000
                            },{
                                path: small_file_path,
                                width: 350
                            }];
                        await Promise.map(sizes, async (size) => {
                            return await sharp(original_file_path)
                                .resize(size.width, null, { withoutEnlargement: true })
                                .toFile(size.path)
                                .catch(err => console.log(size.path, err));
                        })
                        console.log(`> big and small files processed: ${big_file_path} and ${small_file_path};`);

                        fs.unlinkSync(original_file_path);
                        console.log(`> original file is deleted: ${original_file_path}`);

                        fs.renameSync(big_file_path, original_file_path);
                        console.log(`> big file is renamed to original`);

                        console.log(`[${file} is done!]`);
                    }
                }
            }
        }
    }
}

start();
