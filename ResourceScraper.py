from abacusai import ApiClient, ResourceScraper
from flask import Flask, render_template, request

client = ApiClient(api_key='your_api_key')
app = Flask(__name__)

# Create a resource scraper project
resource_scraper = ResourceScraper(client, 'Resource Scraper')

@app.route('/')
def index():
    return render_template('resource_scraping.html')

@app.route('/scrape_resources', methods=['POST'])
def scrape_resources():
    keywords = request.form.getlist('keywords')
    
    resources = resource_scraper.scrape_resources(
        keywords=keywords
    )
    return render_template('resources_list.html', resources=resources)

if __name__ == '__main__':
    app.run(debug=True)
