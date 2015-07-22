# Udacity_FullStack_Movie_Project

Movie Project required by August 10th 2015--

Under the Downloads>python_code folder there is a file called movie_script.py

# Movie_script.py
-- Purpose of this file is to gather and create/render an HTML page that will display movie trailer with the ability to watch trailers from within the page without redirects. 
 -Clicking on any of the box art will activate the trailer functionality.
 -Clicking on any of the hyperlinks will try to open a new tab view your browser and redirect you to a IMDB link of your choice.
 
# How it Works
 1. This is a Python build
 2. There are three functions that does majority of the heavy lifting to gather and dynamically build the HTML
    
    -addext:[Add Externals] :: To create a shorthand method to auto input needed external Stylesheet and Javascript files into to head tag
      example:: addext('css','hi.css')
      result:: < link rel="stylesheet" type="text/css" href="hi.css" >
    
    -gms:[Get Movies] :: Used to grabbed the movie list and strap the imdb to isolate the needed values, convert to star ratings numeric to chars to populate the movie dynamic html to temporary string to input to the main variable called "web"

    -rating_stars :: Once the movie rating is acquired from IMDB this function takes that value and cleans it and converts	it from string to a proper numeric value Python can read. Once the value is cleaned. A while loop finds out how many whole, decimal stars that needs to be written, then for the reminder create empty stars
  3. There is a variable called myFavMovies which is a list of my movies broken into two parts:
		31. imdbId: used to strap the imdb url to grab values ie: title, image, description, rating
		32. youtubeId: used to input to youtube video ID into the dynamic html data attribute for later use via trailer loading javascript
		33. Ex. [{'imdbId':'tt0089114','youtubeId':'3X3VxBJzH68'}]
 3. Once you have gathered your favorite list of movies with the youtube video your satisfied save and close the file.
 4. The file when executed (with internet avalible), will create / render, and open into your default browser a HTML file named movies.html 
# Chrome Error Notice
 I have noticed that is your using a chromium browser with no chromecast plugin installed, 6 errors are displayed in the log. After countless hours researching how to resolve this issue. It was stated that this a error that the Chromecast team will not resolve the issue. My final answer view this problem started here http://stackoverflow.com/questions/24490323/google-chrome-cast-sender-error-if-chrome-cast-extension-is-not-installed-or-usi 
