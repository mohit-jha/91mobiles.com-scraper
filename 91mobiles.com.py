import requests,pprint,json
from bs4 import BeautifulSoup
url='https://www.91mobiles.com/top-10-mobiles-in-india'
request=requests.get(url)
soup=BeautifulSoup(request.text,'html.parser')
## list of moblie names
mobile_name=soup.find_all('a',class_='hover_blue_link name gaclick')
## specific score of mobiles
specific_score=soup.find_all('div',class_='rating_box_new_list')
##epert contents of mobiles
expert_content=soup.find_all('div',class_='exp_comnt_pnl')
##features of mobiles
feature=soup.find_all('div',class_='a filter-list-text')
feature_list=[]
c=1
st=""
for feat in feature:
	st+=feat.text
	if c%4==0:
		feature_list.append(st)
		st=""
	c+=1

image_link=soup.find_all('img',class_="finder_pro_image fimage gaclick")

all_mobile_list=[]
for r in range(len(mobile_name)):
	mobile_details_dict={}
	k=mobile_name[r].contents
	p=mobile_name[r]
	score=specific_score[r].contents
	content=expert_content[r].text
	d=str(image_link[r]).split('src=')
	p=(d[1])
	q=p.split('data')
	mobile_details_dict[str(k)]=score,content,q[0],feature_list[r]
	all_mobile_list.append(mobile_details_dict)
pprint.pprint(all_mobile_list)

##creating file & dumping all mobile list
new_file = open("moblie_data.json","w")
json.dump(all_mobile_list,new_file)
new_file.close()
 
 
 
 
 
 
 
 
 























