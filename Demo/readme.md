# A Simple Gallery

`A Simple Gallery` is a static site generator for making simple gallery-focused sites. To preview what it looks like, visit (https://sharedphysics.github.io/ASimpleGallery/)

# Getting Started

## Requirements: 
Running `A Simple Gallery` requires you to have `python3` installed and access to a server to host your site somewhere. If you want to try it out really quickly, you can host your site using [GitHub pages](https://pages.github.com).

You also need to have `ImageMagick` installed for image processing. You can set it up via `brew install ImageMagick`

## Site Management
Your site is really easy to manage! Just add images into the `/images/` folder, and **make sure you don't accidentally delete the `buildImageList.py` file.**

## Building the Site
1. Download this repo and unzip it somewhere. 
2. Make sure you have python3 running on your computer.
3. To build your site, you'll need to run the `Build.sh` file in your terminal.
4. To run that, open up your terminal and navigate the directory where you unzipped everything. Type in `chmod +x Build.sh` and press enter. You only need to do this one time, the first time.
5. Now type in `./Build.sh`
6. Your site will compile with the images in the /images/ folder, and it will launch your local `index.html` file in the browser.

## Adding Text to galleries
Adding text to a directory is as simple as creating a .txt file in the subdirectory you want it to show up in. You can add HTML and inline CSS formatting as well. The site generation process will read the files alphabetically so you have a bit of control over where it shows up:
* Name it `4-intro.txt` to have it show up above the images, at the top of the page. 
* Name it `5-outro.txt` to have it show up below the images, at the bottom of the page.
* Name it `3-sidebar-end.txt` to add it below the sidebar. 

The cross-site sidebar copy can be modified globally by changing the `2-sidebar-start.html` file and it will reflect globally. Any CSS/style level changes can be managed in the `1-header.html` file. The includes fonts and colors and sizes.

If you're generating your site as a one-off, you can also modify the .html files directly after they are compiled. This works only if you're not expecting to regenerate the site, as those changes will be overwritten every compilation.

# Coming Soon
Some features coming soon include:
* Better mobile layouts
* Linking images to full size versions
* ImageMagik scripts to create thumbnails to support multiple galleries
* ImageMagik scripts to optimize image sizes for web
* Replacing ImageMagik with Python-native Pillow (simplifying)
* Support for image metadata and captions
* Support for variables to customize your gallery
* Support for LazyLoading images to reduce bandwidth
