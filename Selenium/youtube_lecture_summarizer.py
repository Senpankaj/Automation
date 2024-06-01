from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import openai

# Set up Selenium WebDriver
driver_path = 'path_to_chromedriver'  # replace with the path to your chromedriver
driver = webdriver.Chrome(executable_path=driver_path)

# Function to get video links from a YouTube playlist
def get_youtube_playlist_links(playlist_url):
    driver.get(playlist_url)
    time.sleep(5)  # wait for the page to load

    links = []
    videos = driver.find_elements(By.CSS_SELECTOR, 'a.yt-simple-endpoint.style-scope.ytd-playlist-video-renderer')
    for video in videos:
        link = video.get_attribute('href')
        links.append(link)
    
    return links

# Function to get summary from summarize.tech
def get_summary(video_url):
    driver.get('https://www.summarize.tech/')
    time.sleep(3)  # wait for the page to load

    search_box = driver.find_element(By.NAME, 'url')
    search_box.send_keys(video_url)
    search_box.send_keys(Keys.RETURN)
    
    time.sleep(30)  # wait for the summary to be generated

    summary_element = driver.find_element(By.CLASS_NAME, 'summary')  # adjust the class name based on the website's structure
    summary = summary_element.text
    
    return summary

# Function to process summary with OpenAI GPT-4
openai.api_key = 'your_openai_api_key'  # replace with your OpenAI API key

def process_summary(summary):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Please provide a brief summary, references, and key points for the following content:\n\n{summary}",
        max_tokens=150,
        temperature=0.5,
    )
    
    return response.choices[0].text.strip()

# Main script
playlist_url = 'your_youtube_playlist_url'  # replace with your YouTube playlist URL
video_links = get_youtube_playlist_links(playlist_url)

summaries = []
for link in video_links:
    summary = get_summary(link)
    summaries.append(summary)

processed_summaries = []
for summary in summaries:
    processed_summary = process_summary(summary)
    processed_summaries.append(processed_summary)

driver.quit()

print(processed_summaries)
