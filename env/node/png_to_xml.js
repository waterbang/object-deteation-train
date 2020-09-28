const fs = require('fs');
const path = require('path');

const builder = require('xmlbuilder');
const xml_template = require('./xml_template')


const pngFilePath = path.resolve(__dirname, '/Users/waterbang/Desktop/tensorflow/dog/images/test/campus')
const filesName = fs.readdirSync(pngFilePath).filter(function (file) {
    return path.extname(file).toLowerCase() === '.png';
  });



const createXML = (file) =>  {
   const temp =  xml_template(file);
    return builder.create(temp).end({ pretty: true});
}

filesName.map((item) => {
    const filename = item.split('.')[0] + '.xml';
    fs.writeFile(`${pngFilePath}/${filename}`, createXML(item), (err) => {
        console.error(err)
    })

})

