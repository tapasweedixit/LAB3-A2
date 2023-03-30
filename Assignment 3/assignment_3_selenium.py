# Importing required libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Edge()

# Navigating to the Google.com homepage
driver.get("https://www.google.com/")
time.sleep(5)

# Finding the search bar and entering text
google_search_bar = driver.find_element("name", "q")
google_search_bar.send_keys("youtube")
# Submitting the search query
google_search_bar.send_keys(Keys.RETURN)
# Waiting for the search results page to load
time.sleep(5)
# Verifying that the search results page has loaded
assert "youtube" in driver.title

result_link = driver.find_element("xpath", "/html/body/div[7]/div/div[11]/div[1]/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div[1]/a/h3")
result_link.click()
time.sleep(5)

# Finding the search bar and entering text
youtube_search_bar = driver.find_element("name", "search_query")
youtube_search_bar.send_keys("selenium")
# Submitting the search query
youtube_search_bar.send_keys(Keys.RETURN)
# Waiting for the search results page to load
time.sleep(5)
# Verifying that the search results page has loaded
assert "selenium" in driver.title

filter_button = driver.find_element("xpath", "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[1]/div[2]/ytd-search-sub-menu-renderer/div/div/ytd-toggle-button-renderer/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]")
filter_button.click()
time.sleep(5)

filter_select_button = driver.find_element("xpath", "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[1]/div[2]/ytd-search-sub-menu-renderer/div/iron-collapse/div/ytd-search-filter-group-renderer[3]/ytd-search-filter-renderer[3]/a/div")
filter_select_button.click()
time.sleep(5)

# Selecting a video from the search results
video_link = driver.find_element("xpath", "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/div/h3/a/yt-formatted-string")
video_link.click()
time.sleep(5)

# Makeing video full screen
full_screen = driver.find_element("xpath", "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div[2]/div/div/ytd-player/div/div/div[31]/div[2]/div[2]/button[9]")
full_screen.click()
time.sleep(5)

# Exit full screen
screen = driver.find_element("xpath", "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[3]/div[3]/ytd-player/div/div/div[31]/div[2]/div[2]/button[9]")
screen.click()
time.sleep(5)

# open menu
menu = driver.find_element("id", "guide-icon")
menu.click()
time.sleep(5)

# Clicking on Trending button
trending_button= driver.find_element("xpath", "/html/body/ytd-app/div[1]/tp-yt-app-drawer/div[2]/div/div[2]/div[2]/ytd-guide-renderer/div[1]/ytd-guide-section-renderer[3]/div/ytd-guide-entry-renderer[1]/a/tp-yt-paper-item")
trending_button.click()
time.sleep(5)

# Closing the webdriver
driver.close()