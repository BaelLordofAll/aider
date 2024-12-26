from abacusai import ApiClient, CrowdsourcingEngagement
from flask import Flask, render_template, request

client = ApiClient(api_key='your_api_key')
app = Flask(__name__)

# Create a crowdsourcing engagement project
crowdsourcing = CrowdsourcingEngagement(client, 'Crowdsourcing Engagement')

@app.route('/')
def index():
    return render_template('crowdsourcing.html')

@app.route('/launch_campaign', methods=['POST'])
def launch_campaign():
    content = request.form['content']
    engagement_goal = request.form['engagement_goal']
    incentives = request.form.getlist('incentives')
    
    campaign = crowdsourcing.launch_campaign(
        content=content,
        engagement_goal=engagement_goal,
        incentives=incentives
    )
    return "Campaign launched."

if __name__ == '__main__':
    app.run(debug=True)
