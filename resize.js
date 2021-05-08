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

                        //.toBuffer((err, data, info) => {
                            //fs.writeFile(big_file_path, data);
                            //sharp(data)
                            //    .toFile(big_file_path)
                            //    .catch(err => console.log(big_file_path, err));
                        //});
*/

const sharp = require('sharp');
const fs = require('fs');
const Promise = require('bluebird');
global.Promise = Promise;
const main_directory = './app/static/front/images';

function resizeToNewFile(original_file_path, new_file_path, size) {
    sharp(original_file_path)
        .resize(size, null, { withoutEnlargement: true })
        .toFile(big_file_path)
        .catch(err => console.log(new_file_path, err));
}

function resizeToNewFiles(original_file_path, big_file_path, small_file_path) {
    sharp(original_file_path)
        .resize(1000, null, { withoutEnlargement: true })
        .toFile(big_file_path)
        .catch(err => console.log(big_file_path, err))
        .resize(350, null, { withoutEnlargement: true })
        .toFile(small_file_path)
        .catch(err => console.log(small_file_path, err));
}


let my_files = []

//sharp.cache(false);

async function start() {
    folders = fs.readdirSync(main_directory);
    for (const folder of folders) {
    //fs.readdirSync(main_directory).forEach(folder => {
        is_directory = fs.lstatSync(`${main_directory}/${folder}`).isDirectory()
        if (is_directory) {
            files = fs.readdirSync(`${main_directory}/${folder}`);
            for (const file of files) {
            //fs.readdirSync(`${main_directory}/${folder}`).forEach(file => {
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

                        //sharp(original_file_path)
                        //    .resize(1000, null, { withoutEnlargement: true })
                        //    .toFile(big_file_path)
                        //    .catch(err => console.log(big_file_path, err));

                        //resizeToNewFile(original_file_path, big_file_path, 1000)
                        //console.log(`> big file processed: ${big_file_path};`);
                        
                        //sharp(original_file_path)
                        //    .resize(350, null, { withoutEnlargement: true })
                        //    .toFile(small_file_path)
                        //    .catch(err => console.log(small_file_path, err));
                        //resizeToNewFile(original_file_path, small_file_path, 350);
                        //console.log(`> small file processed: ${small_file_path};`);

                        //resizeToNewFiles(original_file_path, big_file_path, small_file_path);
                        
                        var sizes = [{
                                path: small_file_path,
                                width: 1000
                            },{
                                path: big_file_path,
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
                        
                        //my_files.push({'original': original_file_path, 'big': big_file_path});
                            
                        console.log(`[${file} is done!]`);
                    }
                }
            }
            //});
        }
    }
    //});
}

start();

my_files.forEach(_ => {
    console.log(`> original file deleted: ${_['original']};`);
    fs.unlinkSync(_['original']);
    
    console.log(`> ${_['big']} renamed: ${_['original']};`);
    fs.renameSync(_['big'], _['original'])
});