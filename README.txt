# To test the deployment on Google Cloud, run the follow curl command (note that 34.118.33.250 should be adopted to your deployment)
curl -X POST -H "Content-Type: application/json" -d "{\"Credit\": 13000, \"Gender\": \"Male\", \"Education\": \"University\", \"Marital\": \"Never Married\", \"Age\": 25, \"Default\": \"Yes\"}" http://34.118.33.250/predict
