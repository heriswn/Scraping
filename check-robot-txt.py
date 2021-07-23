import urllib.request 
import urllib.robotparser as rob 
#The URL
url = "https://www.lazada.co.id/catalog/?q=blender&_keyori=ss&from=input&spm=a2o4j.searchlist.search.go.209baFv7aFv7Px"
#To open a URL
urllib.request.urlopen(url)
#To obtain the source code of the website
request_url = urllib.request.urlopen(url) 
print(request_url.read()) 
#Reading thr bot file
bot = rob.RobotFileParser() 
#Check where the website's robot.txt file is
url_rob = url+'/robot.txt'
bot_loc = bot.set_url(url_rob) 
print(bot_loc) 
#Read the file 
bot_content = bot.read() 
print(bot_content) 
#Crawl the website using the bot 
web_crawl = bot.can_fetch('*', url) 
print(web_crawl)