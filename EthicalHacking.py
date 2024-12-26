from abacusai import ApiClient, EthicalHacking

client = ApiClient(api_key='your_api_key')

# Create an ethical hacking project
hacking_project = EthicalHacking(client, 'Ethical Hacking')

# Define targets and methods
hacking_project.define_targets(
    systems=['example.com', 'anothersite.com'],
    methods=['SQL Injection', 'XSS', 'Brute Force']
)

# Automate ethical hacking tasks
hacking_project.automate_hacking()

# Integrate with other systems for security testing
hacking_project.integrate_with_security_audits()
