
# Flask + Selenium + Jenkins + Docker CI/CD Demo

This project is a simple demonstration of automation testing for a web application using **Selenium**, and run everything inside **Docker containers** with a **Jenkins pipeline**.

---

## What This Project Does

- Runs a basic **Flask web app** with login, dashboard, and search features.
- Uses **Selenium** to test the app's functionality (login, dashboard, search).
- Uses **Docker Compose** to spin up:
  - The Flask app
  - Selenium Grid (Hub + Chrome Node)
  - A test runner container
- Uses **Jenkins** to automate the process:
  - Build and start services
  - Run tests
  - Publish test results

---

## 📁 Project Structure

```
selenium_flask_ci_demo/
├── flask_app/              # Flask web app
│   └── app.py
│
├── tests/                  # Selenium test scripts
│   ├── login_test.py
│   ├── dashboard_test.py
│   └── search_test.py
│
├── Dockerfile              # Dockerfile for test runner
├── docker-compose.yml      # Compose file for app + Selenium Grid
├── Jenkinsfile             # Jenkins pipeline config
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

---

## How to Run It

### 1. Clone the Repository
```bash
git clone https://github.com/prathameshpatil7/python-selenium-demos.git
cd selenium-flask-ci-demo
```

### 2. Build and Start Services
```bash
docker-compose up -d flask_app selenium-hub chrome
```

### 3. Run Selenium Tests
```bash
docker-compose up --build test-runner
```

### 4. View Results
- Test results will be printed in the console.
- If using Jenkins, results will be shown in the Jenkins dashboard.

### 5. Tear Down
```bash
docker-compose down
```

---

## Jenkins Pipeline Overview

The Jenkins pipeline does the following:

1. **Build & Start Services**: Starts the Flask app and Selenium Grid.
2. **Run Tests**: Executes Selenium tests inside a container.
3. **Publish Reports**: Shows test results in Jenkins.
4. **Cleanup**: Shuts down all containers.

