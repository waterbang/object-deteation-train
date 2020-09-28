const xml_template = function (file){
    return {
        annotation: {
            folder: {
                '#text': 'campus'
            },
            filename: {
                '#text': file
            },
            path: {
                '#text':`/Users/waterbang/Desktop/tensorflow/dog/images/train/campus/${file}`
            },
            source: {
                database: {
                    '#text':'Unknown'
                }
            },
            size: {
                width: {
                    '#text': 60
                },
                height: {
                    '#text': 160
                },
                depth: {
                    '#text': 3
                }
            },
            segmented: {
                '#text': 0
            },
            object: {
                name: {
                    '#text': 'person'
                },
                pose: {
                    '#text': 'Unspecified'
                },
                truncated: {
                    '#text': 1
                },
                difficult: {
                    '#text': 0
                },
                bndbox: {
                    xmin: {
                        '#text': 1
                    },
                    ymin: {
                        '#text': 1
                    },
                    xmax: {
                        '#text':60
                    },
                    ymax: {
                        '#text': 160
                    }
                }
            }
        }
    }
}
module.exports = xml_template