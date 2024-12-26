from abacusai import ApiClient, ViralMarketingAI
from flask import Flask, render_template, request

client = ApiClient(api_key='your_api_key')
app = Flask(__name__)

# Create a viral marketing AI project
viral_marketing = ViralMarketingAI(client, 'Viral Marketing AI')

@app.route('/')
def index():
    return render_template('viral_marketing.html')

@app.route('/suggest_strategy', methods=['POST'])
def suggest_strategy():
    content = request.form['content']
    target_audience = request.form['target_audience']
    
    strategy = viral_marketing.suggest_strategy(
        content=content,
        target_audience=target_audience
    )
    return render_template('strategy_preview.html', strategy=strategy)

if __name__ == '__main__':
    app.run(debug=True)
