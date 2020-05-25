# A Simple Gallery

`A Simple Gallery` is a static site generator for making simple gallery-focused sites. To preview what it looks like, visit (https://sharedphysics.github.io/ASimpleGallery/)

# Getting Started

## Requirements: 
Running `A Simple Gallery` requires you to have `python3` installed and access to a server to host your site somewhere. If you want to try it out really quickly, you can host your site using [GitHub pages](https://pages.github.com).

You also need to have `ImageMagick` installed for image processing. You can set it up via `brew install ImageMagick`

## Site Management
Your site is really easy to manage! Just add images into the `/images/` folder, and **make sure you don't accidently delete the `buildImageList.py` file.**

## Building the Site
1. Download this repo and unzip it somewhere. 
2. Make sure you have python3 running on your computer.
3. To build your site, you'll need to run the `Build.sh` file in your terminal.
4. To run that, open up your terminal and navigate the directory where you unzipped everything. Type in `chmod +x Build.sh` and press enter. You only need to do this one time, the first time.
5. Now type in `./Build.sh`
6. Your site will compile with the images in the /images/ folder, and it will launch your local `index.html` file in the browser.

# Coming Soon
Some features coming soon include:
* Better mobile layouts
* Support for nested galleries and multi-directory images
* ImageMagik scripts to create thumbnails to support multiple galleries
* ImageMagik scripts to optimize image sizes for web
* Support for image metadata and captions
* Support for variables to customize your gallery
* Support for LazyLoading images to reduce bandwidth.
