import requests
import json

# URL for the web service, should be similar to:
#https://southcentralus.api.azureml.ms/pipelines/v1.0/subscriptions/a24a24d5-8d87-4c8a-99b6-91ed2d2df51f/resourceGroups/aml-quickstarts-271352/providers/Microsoft.MachineLearningServices/workspaces/quick-starts-ws-271352/PipelineRuns/PipelineSubmit/579bba1b-6dfa-4806-8a5c-fc0f6d3186e4

scoring_uri = 'http://84868845-507b-4313-89af-f7145bad36e5_52.eastus.azurecontainer.io/score'
# If the service is authenticated, set the key or token
key = 'vXqpRtycR8oFVGCEuQWb6k15YYCrp14qH'

# Two sets of data to score, so we get two results back
data = {"data":
        [
          {
            "age": 17,
            "campaign": 1,
            "cons.conf.idx": -46.2,
            "cons.price.idx": 92.893,
            "contact": "cellular",
            "day_of_week": "mon",
            "default": "no",
            "duration": 971,
            "education": "university.degree",
            "emp.var.rate": -1.8,
            "euribor3m": 1.299,
            "housing": "yes",
            "job": "blue-collar",
            "loan": "yes",
            "marital": "married",
            "month": "may",
            "nr.employed": 5099.1,
            "pdays": 999,
            "poutcome": "failure",
            "previous": 1
          },
          {
            "age": 87,
            "campaign": 1,
            "cons.conf.idx": -46.2,
            "cons.price.idx": 92.893,
            "contact": "cellular",
            "day_of_week": "mon",
            "default": "no",
            "duration": 471,
            "education": "university.degree",
            "emp.var.rate": -1.8,
            "euribor3m": 1.299,
            "housing": "yes",
            "job": "blue-collar",
            "loan": "yes",
            "marital": "married",
            "month": "may",
            "nr.employed": 5099.1,
            "pdays": 999,
            "poutcome": "failure",
            "previous": 1
          },
      ]
    }
# Convert to JSON string
input_data = json.dumps(data)
with open("data.json", "w") as _f:
    _f.write(input_data)

# Set the content type
headers = {'Content-Type': 'application/json'}
# If authentication is enabled, set the authorization header
headers['Authorization'] = f'Bearer {key}'

# Make the request and display the response
resp = requests.post(scoring_uri, input_data, headers=headers)
print(resp.json())


