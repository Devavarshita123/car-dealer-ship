# 🌟 Car Dealerships Web Application
Final Project – IBM Full Stack Software Developer Professional Certificate

## Project Overview
The **Car Dealerships Web Application** is a full-stack solution that allows users to explore car dealers, read and post reviews, and analyze customer feedback sentiments. The project integrates Django, React, Node.js, MongoDB, and IBM Cloud services, showcasing a microservices-based architecture and dynamic web pages.

## Key Features
- User registration and login using Django authentication system  
- Display all car dealers and filter by state  
- View and add reviews for dealers  
- Sentiment analysis of reviews via IBM Cloud Code Engine  
- Backend storage with MongoDB (dealers & reviews) and SQLite (car models & makes)  
- Dynamic pages with Django templates and React frontend  
- Cloud deployment with Docker and Kubernetes  
- CI/CD pipeline with code linting and automated deployment  

## Tech Stack
**Frontend:** React.js, HTML, CSS, JavaScript, Bootstrap / Material UI  
**Backend:** Django & Django REST Framework, Node.js (Express) for Dealers & Reviews Service  
**Database:** SQLite (Car Make & Car Model), MongoDB (Dealers & Reviews)  
**DevOps / Tools:** Docker, Git & GitHub, CI/CD (GitHub Actions), IBM Cloud Code Engine, Kubernetes  

## Project Structure
car-dealerships-app/
│── backend/
│ ├── manage.py
│ ├── requirements.txt
│ └── app/
│ ├── models.py
│ ├── views.py
│ └── templates/
│── frontend/
│ ├── package.json
│ └── src/
│── node_service/
│ ├── server.js
│ └── Dockerfile
│── images/
│ └── dashboard.png
│── README.md


## How to Run the Project Locally

**1. Clone the Repository**
```bash
git clone https://github.com/yourusername/car-dealerships-app.git
cd car-dealerships-app

**2. Backend Setup**
cd backend
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
Backend runs at → http://127.0.0.1:8000/

**3. Node.js Dealers & Reviews Service**
cd node_service
npm install
node server.js

**4. Frontend Setup**
cd frontend
npm install
npm start
Frontend runs at → http://localhost:3000/



