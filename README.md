Flask CI/CD with Jenkins, Docker, AWS ECR & EKS
Project Overview
This Project demonstrates a complete CI/CD pipeline for a Flask application using GitHub, Jenkins, Docker, AWS ECR, and AWS EKS. The Pipeline automes Building, Containerizing, and deploying the application to a Kuberneters cluster on AWS.

Architecture

GitHub  -->  Jenkins --> Docker --> AWS ECR --> AWS EKS --> Flask App

GitHub: Stores the Application code and Jenkinsfile for CI/CD.
Jenkins: Watches for GitHub commits and triggers pipeline builds.
Docker: Builds the application image from the Dockerfile.
AWS ECR: Stores Docker images.
AWS EKS: Deploys Docker containers on Kubernetes using YAML manifests.

Deployment Steps

Push code to GitHub repository.
Jenkins detects the GitHub webhook event and triggers the pipeline.
Jenkins builds the Docker image and pushes it to AWS ECR.
Jenkins applies Kubernetes manifests to deploy the application on Amazon EKS.
Access the Flask application via the service URL provided by EKS.

Folder Structure
.
├── Calculator.py
├── requirements.txt
├── Dockerfile
├── Jenkinsfile
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
└── Screenshoots/                # Screenshots for project validation

Proof & Validation

Screenshots showing:

Jenkins build success

Docker image pushed to AWS ECR

Application running on EKS cluster
