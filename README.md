# 🎲 Random Number Generator API (AWS Lambda + API Gateway)

A simple AWS Lambda function that returns a random number, exposed as a REST API via API Gateway — fully managed with Terraform.

## 🚀 Deploy

terraform init
terraform apply -auto-approve

## 🧪 Test
curl https://<api-id>.execute-api.<region>.amazonaws.com/prod

## Response:
{ "random_number": 42 }

## 🧹 Destroy
terraform destroy -auto-approve

## 📂 Files
main.tf – Terraform config (Lambda, IAM, API Gateway)
lambda/random_number.py – Lambda code
