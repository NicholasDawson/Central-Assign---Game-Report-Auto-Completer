from selenium import webdriver

#GET GAME INFO FROM USER
print('----------INFO----------')
away_team = input('Away team name: ')
age_group = input('Age group: ')
home_final_score = input('Final Score(Home): ')
home_half_score = input('Half Score(Home): ')
away_final_score = input('Final Score(Away): ')
away_half_score = input('Half Score(Away): ')

#LOGIN AND GO TO GAME REPORT
browser = webdriver.Firefox(executable_path=r'C:\Program Files\Geckodriver\geckodriver.exe')
browser.get('https://csrp.ctreferee.net/mobile_administration/')

username = browser.find_element_by_id("username")
password = browser.find_element_by_id("password")

username.send_keys("dunkindawson")
password.send_keys("theclaw1234")

browser.find_element_by_class_name("ui-btn-hidden").click()
browser.get('https://csrp.ctreferee.net/mobile_referee_reports/update/referee/')
browser.find_element_by_class_name('ui-link-inherit').click()

#FILL INFO ABOUT GAME
visiting_team_fill = browser.find_element_by_id("visiting_team")
visiting_team_fill.clear()
visiting_team_fill.send_keys(away_team)

age_group_fill = browser.find_element_by_id("age_group")
age_group_fill.send_keys(age_group)

browser.find_element_by_css_selector('a.ui-mini:nth-child(3)').click()

hfs_fill = browser.find_element_by_id("home_team_score")
hfs_fill.clear()
hfs_fill.send_keys(home_final_score)

hhs_fill = browser.find_element_by_id("home_halftime_score")
hhs_fill.clear()
hhs_fill.send_keys(home_half_score)

afs_fill = browser.find_element_by_id("visiting_team_score")
afs_fill.clear()
afs_fill.send_keys(away_final_score)

ahs_fill = browser.find_element_by_id("visiting_halftime_score")
ahs_fill.clear()
ahs_fill.send_keys(away_half_score)

for x in range(6):
    browser.find_element_by_css_selector('a.ui-mini:nth-child(3)').click()

browser.find_element_by_css_selector('a.ui-mini:nth-child(3)').click()

browser.quit()

print()
print('-----GAME REPORT COMPLETE-----')


