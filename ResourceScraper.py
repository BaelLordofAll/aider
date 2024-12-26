from abacusai import ApiClient, ResourceScraper
from flask import Flask, render_template, request
import json

client = ApiClient(api_key='your_api_key')
app = Flask(__name__)

# Create a resource scraper project
resource_scraper = ResourceScraper(client, 'Resource Scraper')

def load_free_resources():
    with open('free_resources.json', 'r') as file:
        return json.load(file)

@app.route('/')
def index():
    return render_template('resource_scraping.html')

@app.route('/scrape_resources', methods=['POST'])
def scrape_resources():
    keywords = request.form.getlist('keywords')
    free_resources = load_free_resources()
    
    resources = resource_scraper.scrape_resources(
        keywords=keywords,
        free_resources=free_resources
    )
    return render_template('resources_list.html', resources=resources)

if __name__ == '__main__':
    app.run(debug=True)
