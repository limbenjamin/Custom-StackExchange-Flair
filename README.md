# Custom-StackExchange-Flair

Created for use on my website  

I found that the default flair choices were limited and did not fit well with the theme on my website. This python script will produce a HTML file containing a div with the flair in it. I included this file into the template of the static site generator. I have set up it up such that this script is run everytime I regenerate the site, if the site is not regenerated, the stats will not be updated.

This script can be modified for sites running on python based backend to always provide up to date statistics.

Please modify the URL to include your own user profile as well as the network site before using. For my case, the network site I am interested in is security.stackexchange which happens to be the 3th item in the array. Hence the [4] in the context.

Live Demo: http://limbenjamin.com
