# Import of the following libs:
#  urllib: used to strap or grab the needed urls to be placed into a
#   variable for later use
#  os: more of a just incase lib to connect to Operating System's command
#   line <= but was never used in this build
#  webbrowser: only purpose in this build was to open a browser to my
#   compiled webpage
#  re: used to search and isolate current portions of the straped HTML via
#   urllib main to acquire needed values


import urllib
import os
import webbrowser
import re


# Movie List:
#  This is a list of my movies broken into two parts:
#   imdbId: used to strap the imdb url to grab values
#    ie: title, image, description, rating
#   youtubeId: used to input to youtube video ID into the dynamic html
#    data attribute for later use via trailer loading javascript


myFavMovies = [
 {'imdbId': 'tt0089114', 'youtubeId': '3X3VxBJzH68'},
 {'imdbId': 'tt0091949', 'youtubeId': '9rlI3Xg9g_A'},
 {'imdbId': 'tt0091993', 'youtubeId': '0Umy8VTiKG4'},
 {'imdbId': 'tt0093936', 'youtubeId': 'vwXDxukH7W8'},
 {'imdbId': 'tt0083944', 'youtubeId': 'rjptQSfuTy8'},
 {'imdbId': 'tt2234155', 'youtubeId': 'cdnoqCViqUo'}
]


# Gms: [Get movies]
#  Purpose::
#   Used to grabbed the movie list and strap the imdb to isolate
#    the needed values,convert to star ratings numeric to chars to
#    populate the movie dynamic html totemporary string to input to the
#    main variable called "web"


def gms(movies):
    ma = []
    mhtml = ''
    m = int(0)
    for movie in movies:
        murl = 'http://www.imdb.com/title/'+movie['imdbId']+'/?ref_=tt_rec_tti'
        movielink = urllib.urlopen(murl)
        movielink = movielink.read()
        ma.append({'id': str(movie['imdbId'])})
        for title in re.findall('<title>([^<]+?)</title>', movielink):
            ma[m]['title'] = re.sub('- IMDb', '', title).strip()
        dx = '<p itemprop="description">([^<]+?)</p>'
        for description in re.findall(dx, movielink):
            ma[m]['description'] = description
        rx = '<div class="titlePageSprite star-box-giga-star">([^<]+?)</div>'
        for rating in re.findall(rx, movielink):
            ma[m]['rating'] = rating_stars(rating)
        img_regex = '"img_primary">(.*?)</div>'
        imgs = re.compile(img_regex, re.DOTALL).findall(movielink)
        imgs = re.findall('src="(.*?)"', imgs[0])
        ma[m]['image'] = '<img src="' + str(imgs[0]) + '" />'
        mlnk = 'http://www.imdb.com/title/' + movie['imdbId']
        mlnk += '/?ref_=tt_rec_tti'
        ma[m]['mlink'] = mlnk
        mhtml = mhtml+movie_content.format(
            movie_image=ma[m]['image'],
            movie_title=ma[m]['title'],
            movie_description=ma[m]['description'],
            movie_rating=ma[m]['rating'],
            videoID=movie['youtubeId'],
            hyperlink=ma[m]['mlink']
        )
        m = m+1
    return mhtml


# Rating_stars:
#  Purpose::
#    Once the movie rating is acquired from IMDB
#     this function takes that value and cleans it and converts
#     it from string to a proper numeric value Python can read.
#     Once the value is cleaned. A while loop finds out how many whole,
#     decimal stars that needs to be written, then for the reminder create
#     empty stars


def rating_stars(rc):
    # clean numeric input
    rc = float(rc.replace(' ', ''))
    # Stars
    #  Solid:&#9733;
    #  Half:&#10032;
    #  Empty:&#9734;
    stars = ['&#9733;', '&#10032;', '&#9734;']
    starHtml = ''
    starCount = 0
    isWholeNumRating = 'false'
    if rc % 1 == 0:
        isWholeNumRating = 'true'
    if isWholeNumRating == 'true':
        while starCount < 10:
            if starCount < rc:
                starHtml = starHtml + stars[0]
            else:
                starHtml = starHtml + stars[2]
            starCount = starCount + 1
    else:
        while starCount < 10:
            if starCount < int(rc):
                starHtml = starHtml + stars[0]
            elif starCount < rc:
                starHtml = starHtml + stars[1]
            else:
                starHtml = starHtml + stars[2]
            starCount = starCount + 1
    return starHtml


# AddExt:
#  Purpose::
#   To create a shorthand method to auto input needed external
#    Stylesheet and Javascript files into to head tag
#   Example::
#    addext('css','http://localhost/hi.css')
#   Result::
#    <link rel="stylesheet" type="text/css" href="http://localhost/hi.css" />


def addext(filetype, files):
    result = '<!-- S: Imported External ' + str(filetype).upper() + ' -->'+'\n'
    # Validates if variable files is a string versus a list
    if str(type(files)) == "<type 'str'>":
        if str(filetype) == 'css':
            result += '<link rel="stylesheet" type="text/css" href="' + files
            result += '" />' + '\n'
        elif str(filetype) == 'js':
            result += '<script type="text/javascript" src="' + files
            result += '" ></script>' + '\n'
    elif str(type(files)) == "<type 'list'>":
        listCount = int(0)
        while listCount < len(files):
            if str(filetype) == 'css':
                result += '<link rel="stylesheet" type="text/css" href="'
                result += files[int(listCount)] + '" />' + '\n'
            elif str(filetype) == 'js':
                result += '<script type="text/javascript" src="'
                result += files[int(listCount)] + '" ></script>' + '\n'
            listCount = listCount + 1
    else:
        result = 'error'
    result += '<!-- E: Imported External ' + str(filetype).upper()
    result += ' -->' + '\n'
    return str(result)


# Dynamic Html used to populate of the movie's content per

movie_content = '''<div class="movie_item" data-video="{videoID}" >
    <div class="movie_itemImg">{movie_image}</div>
    <div class="movie_itemTitle" data-movieTitle="{movie_title}"
    data-movieDescription="{movie_description}">{movie_title}
        <div class="movie_itemRating">{movie_rating}</div>
        <div><a href="{hyperlink}" target="_new">Visit Imdb</a></div>
    </div>
</div>'''


# Population of the movie list <=see gms for break-down


myMovies = gms(myFavMovies)


# External CSS


headerCssExt = ''


# Additional CSS hand written


headerCss = '''<!-- S: Additional CSS -->
<style type="text/css">
body{
  position: relative;
  margin: auto;
  text-align: center;
  background-color: #fff;
  transition: background-color 1.5s;
}
body.activeVid{

  background-color: #000;
  transition: background-color 1.5s;
}
.movie_item {
  display: inline-block;
  width: 180px;
  text-align: center;
  vertical-align: top;
}
.movie_itemImg>img {
  height: 190px;
}
.movie_trailer_list {
  margin: auto;
  width: 90%;
  position: relative;
  display: inline-block;
  left: 0px;
  right: 0px;
  text-align: center;
  height: 360px;
  padding: 0px 20px
}
.previous_pg, .next_pg {
  display: inline-block;
  margin: auto;
  padding: 37px 3px 19px;
  background-color: blue;
  top: 0px;
  bottom: 0px;
  position: absolute;
  height: 10%;
}
.previous_pg {
  margin-left: -20px;
}
.next_pg {
  margin-left: 6px;
}
.vid_wrapper{
  display: inline-block;
  vertical-align: top;
  min-width: 750px;
min-height: 364px;
}
.vid_information{
  display: inline-block;
  width: 250px;
  vertical-align: top;
  text-align: left;
  list-style: none;
  padding: 0px 8px;
}
lh#movieTitle {
  font-size: 20px;
  font-weight: bold;
  color: #fff;
  white-space: normal;
}
li#movieDescription {
  font-style: italic;
  font-size: 16px;
  padding: 8px 9px;
  text-align: justify;
  color: aliceblue;
  white-space: normal;
}
li#movieRating::before {
  content: 'Rating:';
  color: initial;
  font-weight: normal;
  color: rgb(0, 0, 184);
}
li#movieRating {
  padding: 9px 9px 0px;
  font-weight: bold;
  color: blue;
}
body .movie_trailer_list{opacity: 1;position: relative;z-index: 0;}
body.activeVid .movie_trailer_list{opacity: .2;position: relative;z-index: -1;}
body .vid_trailer{display: none;}
body.activeVid .vid_trailer {
  display: inline-block;
  padding: 10px 10px;
  background-image: linear-gradient(#000 8%,#5F5F5F 53%,#000 96%);
  position: fixed;
  left: 0;
  right: 0;
  top: 0;
  bottom: 0;
  z-index: 1;
  height: 364px;
  width: 1030px;
  margin: auto;
  white-space: nowrap;
}
span.close_vid {
  color: red;
  font-family: cursive;
  border: 1px solid #444;
  padding: 0px 4px 0px 6px;
  cursor:pointer;
}
span.close_vid:hover {
  background-color:#444;
}
.movie_itemRating {
  font-size: 12px;
}
.movie_itemTitle {
  font-size: 13px;
}
</style>
<!-- E: Additional CSS -->'''


# External Javascript


headerJsExt = addext('js', [
    'https://code.jquery.com/jquery-2.1.4.min.js',
    'https://code.jquery.com/ui/1.11.4/jquery-ui.min.js',
    'https://www.youtube.com/iframe_api'
    ]
)


# Additional Javascript hand written


headerJs = '''<!-- S: Additional Javascript -->
<script type="text/javascript">

var player;

/*
    call_youtube_video function works hand and hand with the external
    imported libraryyoutube iframe api {YT.Player} to produce html5 playback
    to I can isolate when the video stop and to close the trailer window
*/
function call_youtube_video(elem) {
    var r = $('.vid_trailer_video').parent();
    r.html('<div class="vid_trailer_video"></div>');
    if($('body').hasClass('activeVid')){}else{$('body').addClass('activeVid')}
    if(elem.attr('data-video').length == 0){
        var msg = "Sorry this Movie does not have a trailer. But you " +
        "can view it's description and info at imdb's link below"
        alert(msg)
    }
    player = new YT.Player($(".vid_trailer_video")[0], {
        height: '360',
        width: '750',
        videoId: elem.attr('data-video'),
        events: {
            'onReady': function(e){
                e.target.playVideo();
                $('body').addClass('playingvid')
                m_data = elem.find('.movie_itemTitle');
                $('.vid_trailer').
                find('#movieTitle').
                text(m_data.attr('data-movieTitle'))
                $('.vid_trailer').
                find('#movieDescription').
                text(m_data.attr('data-movieDescription'))
                $('.vid_trailer').
                find('#movieRating').
                text(m_data.find('.movie_itemRating').text())
            },
            'onStateChange': function(e){
                if(e.data == 0){
                    $('.close_vid').click();
                }
            }
        }
    });
}
$(function(){
    /*
        Acknowledge when the user is over the trailer popup versus the
        body {grayed area}
    */
    $('.vid_trailer').mouseenter(function(){
        if($('body').hasClass('mouseintrailer')){}
        else{$('body').addClass('mouseintrailer')}
    }).mouseleave(function(){
        if($('body').hasClass('mouseintrailer')){
            $('body').removeClass('mouseintrailer')
        }
    });
    /*
        On click of the body; if a movie trailer is active execute the
        close trailer function
    */
    $('body').click(function(){
        if($(this).hasClass('mouseintrailer')){}
        else{
            if($(this).hasClass('playingvid')){
                $('.close_vid').click();
            }
        }
    });
    /*
        Once a movie has been selected run the trailer
        function : call_youtube_video
    */
    $('.movie_itemImg').click(function(){
        e = $(this).parent();
        call_youtube_video(e)
    });
    /*
        Main purpose is to close the trailer window only
    */
    $('.close_vid').click(function(){
        $('body').removeClass('activeVid').removeClass('playingvid');
        $(this).parent().find('.vid_wrapper').
        html('<div class=vid_trailer_video ></div>')
    });
});
</script>
<!-- E: Additional Javascript -->'''


# Compiling of webpage


web = '''<!DOCTYPE html>
<html>
    <head>
        <title>Movie Trailer Website Project for FullStack Nanodegree</title>
        {headerCss_ext}
        {headerCss}
        {headerJs_ext}
        {headerJs}
    </head>
    <body>
        <!-- Video Trailer Content Holder -->
        <div class="vid_trailer">
            <!-- Wrapper being dynamically rebuilt the clients selection -->
            <div class="vid_wrapper">
                <div class="vid_trailer_video"></div>
            </div>
            <!-- PlaceHolder for Video Description Information -->
            <ul class="vid_information">
                <lh id="movieTitle" ></lh>
                <li id="movieRating" ></li>
                <li id="movieDescription" ></li>
            </ul>
            <!-- Trailer Popup Window Close Button -->
            <span class="close_vid">X</span>
        </div>
        <!-- Movie List to View Trailer -->
        <div class="movie_trailer_list">
            {movies}
        </div>
    </body>
</html>'''


# Convert the pending inner string varibles to the need vars to replace


web = web.format(
    headerCss_ext=headerCssExt,
    headerJs_ext=headerJsExt,
    headerCss=headerCss,
    headerJs=headerJs,
    movies=myMovies
)


# Create and or open the file needed to input all compiled string data
#  from the web variable


webpage = open('movies.html', 'w')


# If the current file opened if empty or not empty; truncate from my
#  understanding removes all data in file


webpage.truncate()


# Write newly compiled data from the variable web to the currently opened,
#  completely empty file AKA: movies.html


webpage.write(web)


# The close command will save and close all modications if any was committed
#  and no modications it was just simpley close the file


webpage.close()


# This will try to open a new browser tab to your default and or specified
#  browser aswell as to open the currently close file : movies.html


webbrowser.open('file://' + os.path.abspath(webpage.name), new=2)
