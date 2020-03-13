# TileMaker

This program takes an image as input and creates map tiles in a directory structure which can be used as a baselayer in application such as OpenLayers, Cesium and others.

## Running
`python TileMaker.py` will generate tiles with the default map source file and default zoom levels, specified in the config.ini

## Things to consider
* Input image should be high resolution, the higher the better.
* Input image should be square.
* Requested zoom level will have a huge impact on processing time and final directory size. Maximum support zoom level is 7, because this is the max number of tiles supported by the image_slicer package.

## Output
* Program will create `tiles` directory containing map tiles which can then be served with URL's like: http://example.com/{z}/{x}/{y}.png
* Output tiles will be scaled to 256x256 pixels.

## Credits
* https://github.com/samdobson/image_slicer

* https://github.com/Mindwerks/worldengine