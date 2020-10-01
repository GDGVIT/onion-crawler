<p align="center">
<a href="https://dscvit.com">
	<img src="https://user-images.githubusercontent.com/41824020/92394292-e88c5a00-f13e-11ea-94f1-16a6fb4c07d9.png" alt="dsc-vit logo"/>
</a>
	<h2 align="center"> Onion Crawler </h2>
	<h4 align="center"> Scrape and Store Dark Web Sites along with therir Latency | Crawler for Dark Web | Search Engine Oriented <h4>
</p>

---
[![DOCS](https://img.shields.io/badge/Documentation-see%20docs-green?style=flat-square&logo=appveyor)](https://documenter.getpostman.com/view/9118595/TVCiUS16) 
  [![UI ](https://img.shields.io/badge/User%20Interface-Link%20to%20UI-orange?style=flat-square&logo=appveyor)](INSERT_UI_LINK_HERE)


## Functionalities
- It's implemented using BFS and in coming time it's implementation will be changed to A* Search (Preferential Crawler)

- [x] fetch onion links
- [x] recursive fetching
- [x] store scrapped data
- [x] user added url
- [x] url blacklisting

<br>

## Increasing the crawler reach
```txt
Increase Crawl Depth
Add More starter links
Create more spiders with special focus on Directories
```

<br>

## Spiders
- `DRL` Link Dir Onion
	- A big directory of urls
- `UADD` User Added
	- Added by user
	- presently links are appened in _user_added_urls.txt_ under spider_data
	- Crawled in exactly similar fashion as to DRL

	
<br>


## Instructions to run

#### Pre-requisites:
	-  Py3
	-  Tor

#### < directions to install > 
```bash
pip install -r requirements.txt
```

#### < directions to execute > (For commit of [Jul 10, 2020](https://github.com/1UC1F3R616/onion-crawler/commit/75b0cbdabc4b2591e6c75ccf08a9fc127e7a4967))
- This commit contains pipeline to generate data in csv/json file
- You can run this without much effort

```bash
# start tor on port 9150
pproxy -l http://:8181 -r socks5://127.0.0.1:9150 -vv
scrapy crawl name_of_spider # DRL
```

#### < directions to execute > (After commit Jul 10, 2020)
- This commit contains data pipeline to save data on MongoDB Server
- You need to setup MongoDB Server connection credentials and URI in settings.py/pipeline.py file

## Sample JSON
- [DRL](https://github.com/1UC1F3R616/onion-crawler/blob/master/dark_web_scraping/scraped_data_DRL_2020-07-02T00-58-53.json)
- [UADD](https://github.com/1UC1F3R616/onion-crawler/blob/master/dark_web_scraping/scraped_data_UADD_2020-07-02T08-06-50.json)
- [TF-IDF Type](https://github.com/1UC1F3R616/onion-crawler/blob/master/dark_web_scraping/scraped_data.json)

## Instructional Video
- [YouTube URL](https://www.youtube.com/watch?v=AGe3Mh91pNA)

## Bigger Datasets
- [DarkNet Dataset](https://1uc1f3r616.github.io/Dark-Net-Websites-Dataset/)

## StoryBoarding
Idea hamster: --

Developer: I had prior experience with web scraping but hadn't worked with web crawlers before and scraping the deep-web was also something new to me as it required setting up tor proxy. This project developed my interest in the web-mining subject and therefore it encorged me to take this subject as a subject in college curriculum. 

## Contributors

<table>
<tr align="center">

<td>
	
Idea by- [Angad Sharma](https://github.com/L04DB4L4NC3R)

<td>

1UC1F3R616 (Kush Choudhary)

<p align="center">
<img src = "https://miro.medium.com/fit/c/160/160/2*_T9qFh8Bg-Mc6UX8JAMtvg.jpeg" width="150" height="150" alt="1UC1F3R616">
</p>
<p align="center">
<a href = "https://github.com/1UC1F3R616"><img src = "http://www.iconninja.com/files/241/825/211/round-collaboration-social-github-code-circle-network-icon.svg" width="36" height = "36" alt="Github of Kush Choudhary aka 1UC1F3R616"/></a>
<a href = "https://www.linkedin.com/in/kush-choudhary-567b38169/">
<img src = "http://www.iconninja.com/files/863/607/751/network-linkedin-social-connection-circular-circle-media-icon.svg" width="36" height="36"/>
</a>
</p>
</td>

</tr>
  </table>

<br>
<br>

<p align="center">
	Made with :heart: by <a href="https://dscvit.com">DSC VIT</a>
</p>

