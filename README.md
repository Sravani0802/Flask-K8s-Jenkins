##### **CI/CD Pipeline on AWS using Jenkins, ECR \& EKS (Flask Application)**



###### **Project Overview**



This project demonstrates a \*\*cloud-native CI/CD pipeline\*\* by deploying a containerized Flask application on \*\*AWS Elastic Kubernetes Service (EKS)\*\* using:



* &#x20;\*\*Jenkins\*\* for CI/CD automation  
* &#x20;\*\*Docker\*\* for containerization  
* &#x20;\*\*Amazon ECR\*\* for container image storage  
* &#x20;\*\*Amazon EKS (Kubernetes)\*\* for orchestration  
* &#x20;\*\*GitHub Webhooks\*\* for automatic pipeline triggers  



Whenever code is pushed to GitHub, Jenkins automatically builds the Docker image, pushes it to Amazon ECR, and deploys it to the EKS cluster.





###### **Architecture**



GitHub → Webhook → Jenkins → Docker Build → Amazon ECR → Amazon EKS





###### **Tech Stack**



* Python (Flask)
* Docker
* Jenkins
* AWS ECR (Elastic Container Registry)
* AWS EKS (Elastic Kubernetes Service)
* Kubernetes (kubectl)
* Git \& GitHub





###### **Key Features**



* Fully automated CI/CD pipeline
* Docker image build \& push to Amazon ECR
* Kubernetes deployment on AWS EKS
* GitHub webhook-based auto trigger
* Scalable microservice deployment





###### **Project Structure**



**├── app.py**

**├── requirements.txt**

**├── Dockerfile**

**├── Jenkinsfile**

**├── k8s/**

**│ ├── deployment.yaml**

**│ └── service.yaml**





###### **Screenshots** 

* Jenkins pipeline success (all stages green)
* ECR repository with pushed image
* EKS cluster nodes \& pods



