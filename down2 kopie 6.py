import urllib
import os

comicCounter=len(os.listdir('/Users/MWK/Desktop/tatiana'))+1  # reads the number of files in the folder to start downloading at the next comic
errorCount=0

def download_comic(url,comicName):
    """
    download a comic in the form of

    url = http://www.example.com
    comicName = '00000000.jpg'
    """
    image=urllib.URLopener()
    image.retrieve(url,comicName)  # download comicName at URL

while comicCounter <= 1000:  # not the most elegant solution
    os.chdir('/file')  # set where files download to
        try:
        if comicCounter < 10:  # needed to break into 10^n segments because comic names are a set of zeros followed by a number
            comicNumber=str('0'+str(comicCounter))  # string containing the eight digit comic number
            comicName=str(comicNumber+".jpg")  # string containing the file name
            url=str("https://raw.githubusercontent.com/oliverwk/oliverwk.github.io/master/tatiana/art_"+comicName)  # creates the URL for the comic
            comicCounter+=1  # increments the comic counter to go to the next comic, must be before the download in case the download raises an exception
            download_comic(url,comicName)  # uses the function defined above to download the comic
            print url
        if 10 <= comicCounter < 100:
            comicNumber=str('0'+str(comicCounter))
            comicName=str(comicNumber+".jpg")
            url=str("https://raw.githubusercontent.com/oliverwk/oliverwk.github.io/master/tatiana/art_"+comicName)
            comicCounter+=1
            download_comic(url,comicName)
            print url
        if 100 <= comicCounter < 1000:
            comicNumber=str('0'+str(comicCounter))
            comicName=str(comicNumber+".jpg")
            url=str("https://raw.githubusercontent.com/oliverwk/oliverwk.github.io/master/tatiana/art_"+comicName)
            comicCounter+=1
            download_comic(url,comicName)
            print url
        else:  # quit the program if any number outside this range shows up
            quit
    except IOError:  # urllib raises an IOError for a 404 error, when the comic doesn't exist
        errorCount+=1  # add one to the error count
        if errorCount>3:  # if more than three errors occur during downloading, quit the program
            break
        else:
            print str("comic"+ ' ' + str(comicCounter) + ' ' + "does not exist")  # otherwise say that the certain comic number doesn't exist
print "all comics are up to date"
