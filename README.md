# Udacity_FullStack_Movie_Project

Movie Project required by August 10th 2015--

Under the Downloads>python_code folder there is a file called movie_script.py

# Movie_script.py
-- Purpose of this file is to gather and create/render an HTML page that will display movie trailers with the ability to watch from within the page without redirects. 
 -Clicking on any of the box art will activate the trailer functionality.
 -Clicking on any of the hyperlinks will try to open a new tab view in your browser and redirect you to an IMDB link of your choice.

# How to Run
 Once you download the file, remember the location. Then simply open your terminal console and direct it to the path (if you downloaded the file via the console then this is unneeded unless you specified the different directory) and type in the following:
 python movie_script.py
# That's it :D

# How it Works
 1. This is a Python build
 2. There are three functions that do the majority of the heavy lifting to gather and dynamically build the HTML.
    
    -addext:[Add Externals] :: To create a shorthand method to auto input needed external Stylesheet and Javascript files into to head tag.
      1. example:: addext('css','hi.css')
      2. result:: < link rel="stylesheet" type="text/css" href="hi.css" >
    
    -gms:[Get Movies] :: Used to grab the movie list and strip out the needed values, convert the star rating numerics to chars, and populate the movie dynamic html to a temporary string variable called "web".

    -rating_stars :: Once the movie rating is acquired from IMDB, this function takes that value, cleans it and converts it from string to a proper numeric that value Python can read. A while loop finds out how many whole and partial stars need to be written, then creates empty stars for the remainder.
  3. There is a variable called myFavMovies which is a list of my movies broken into two parts:
	1. imdbId: used to strap the imdb url to grab values ie: title, image, description, rating.
	2. youtubeId: used to input the video ID into the dynamic html data attribute for later use via trailer loading javascript.
	3. Ex. [{'imdbId':'tt0089114','youtubeId':'3X3VxBJzH68'}]
 4. Once you have gathered your list of favorite movies with the youtube videos you're satisfied with, save and close the file.
 5. The file when executed (with internet avalible), will create / render, and open into your default browser a HTML file named movies.html.

# Chrome Error Notice
 If you're using a chromium browser with no chromecast plugin installed, 6 errors will be displayed in the log. Unfortunately the Chromecast team will not resolve this issue. For more information refer to the following link. http://stackoverflow.com/questions/24490323/google-chrome-cast-sender-error-if-chrome-cast-extension-is-not-installed-or-usi 
