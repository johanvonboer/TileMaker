# TileMaker

This program takes an image as input and creates map tiles in a directory structure which can be used as a baselayer in application such as OpenLayers, Cesium and others.

## Things to consider
* Input image should be high resolution, the higher the better.
* Input image should be square.
* Requested zoom level will have a huge impact on processing time and final directory size. Maximum support zoom level is 7, because this is the max number of tiles supported by the image_slicer package.

## Output
* Program will create `tiles` directory containing map tiles which can then be served with URL's like: http://example.com/{z}/{x}/{y}.png
* Output tiles will be scaled to 256x256 pixels.

