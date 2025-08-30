import requests
from bs4 import BeautifulSoup

def fetch_hacker_news_headlines():
    # URL of the website to scrape
    url = 'https://news.ycombinator.com'
    
    try:
        response = requests.get(url)
        response.raise_for_status()  
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        #Headline elements
        headline_elements = soup.select('.titleline > a')
        
        # Extract the text from each headline element
        headlines = [element.get_text() for element in headline_elements]
        
      
        print("Hacker News Headlines:")
        print("-" * 10) 
        for i, headline in enumerate(headlines, 1):
            print(f"{i}. {headline}")
            
    except requests.RequestException as e:
        print(f"Error fetching the website: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    fetch_hacker_news_headlines()