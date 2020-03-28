#!/usr/bin/python3

urllist = {
	"google": "https://google.com",
	"twitter": "https://twitter.com",
	"quora": "https://quora.com",
	"reddit": "https://reddit.com",
	"udemy": "https://udemy.com",
	"linkedin": "https://www.linkedin.com/learning/me/in-progress",
	"ebenefits": "https://www.ebenefits.va.gov/ebenefits/homepage" 
}

def returnUrl(urlName):
	for k,v in urllist.items():
		if(urlName == k):
			return(v)  
