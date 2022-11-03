#imports relevant modules
from bs4 import BeautifulSoup
import requests
import re

#establishes parameters that user can change
city_name = 'Chatsworth'
state_abbreviation = 'ca'
team_name = 'Sierra-Canyon-Trailblazers'
level = 'Varsity'
year = '21-22'
URL = f"https://www.maxpreps.com/{state_abbreviation}/{city_name}/{team_name}/basketball/{level}/{year}/schedule"

raw_data = requests.get(URL)
html_tree = BeautifulSoup(raw_data.content, 'html.parser')

def get_team_record(given_page):
    #finds the oddly named class on maxpreps that holds team_record text element
    return given_page.find_all(class_='sc-f584fccb-0 jaNLEy f12_bold_tall')[0].text

def get_team_winrate(given_page):
    return given_page.find_all(class_ = 'sc-f584fccb-0 dGrBjS f18_bold')[0].text

def get_team_name(given_page):
    return given_page.find_all(class_ = 'sc-f584fccb-0 gWFyrR f18_bold')[0].text

given_team_record = get_team_record(html_tree)
given_team_winrate = get_team_winrate(html_tree)

#opponent data gets a list containing text about each team
#function takes it and returns it as a list, mostly location/conf, non conf/home, away data
opponent_data = html_tree.find_all(class_ = 'sc-ec638bfb-0 hmdLYI')
def get_opponent_info(opponent_data):
    opponent_list = []
    index = 0
    while index < len(opponent_data):
        opponent_list.append(opponent_data[index].text)
        index += 1

    return opponent_list

#iterates through the opponents listed on a team's schedule page and returns a list of each opps. schedule homepage link
def get_opponent_schedule_links(head_node_page_data):
    index = 0
    list_of_links = []
    classes_containing_links = html_tree.find_all(class_='sc-ec638bfb-0 hmdLYI')

    while index < len(classes_containing_links):
        cur_class_containing_link = classes_containing_links[index]
        list_of_links.append(cur_class_containing_link.find(class_ = 'sc-333a63d7-0 rNzPc')['href'])
        index += 1
    return list_of_links

list_of_links = get_opponent_schedule_links(html_tree)

#iterates through all the opponents links and sends HTML GET requests
for link in list_of_links:
    cur_URL = link
    cur_page_data = requests.get(cur_URL)
    cur_HTML_tree = BeautifulSoup(cur_page_data.content, 'html.parser')

    #calls earlier functions on current schedule page
    cur_team_record = get_team_record(cur_HTML_tree)
    cur_team_winrate = get_team_winrate(cur_HTML_tree)
    cur_team_name = get_team_name(cur_HTML_tree)

    #prints out the basic info gleaned from schedule for each team
    #print([cur_team_record, cur_team_winrate, cur_team_name])
