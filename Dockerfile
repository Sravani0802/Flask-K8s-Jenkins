#Use Python Image
FROM python:3.11-slim

#Set the Working Directory inside the Container
WORKDIR /src/app

#Copy the Requirements File and Install Dependenices
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#Copy the Rest of the Application Code
COPY . /src/app

#Expose Port
EXPOSE 5000

#Define the Command to Run your Application
CMD ["python", "./Calculator.py" ]