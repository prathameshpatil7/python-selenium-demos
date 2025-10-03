
# Python Selenium Learnings

Hi, this is a small write-up about what I learned while exploring Selenium automation. I wanted to share the demos I tried.

## What I Learned

I learned how to use Python with Selenium to automate web browser tasks. I understood how to open a browser, find elements on a page, click buttons, fill forms, and take screenshots. I also learned how to run these tests automatically using Docker and Jenkins.

## Demos I Created


1. **Login and Screenshot Demo**  
   I automated logging into a sample website and took a screenshot after successful login.

2. **Web Table data Extraction**  
   I extracted data from a table on a webpage and printed it in the console.

3. **Date Picker Automation**  
   I selected a specific date from a calendar widget on a webpage.

4. **Form Submission**  
   I filled out a form with text fields, radio buttons, checkboxes, and dropdowns, and submitted it.

5. **Amazon Laptops data Scraper**  
   I used Selenium to go through 10 pages of laptop listings on Amazon and saved product details into a CSV file.

6. **Flask App Testing with Selenium**  
   I created a small Flask web app with login, dashboard, and search features. Then I wrote Selenium tests to check if these features worked properly.

7. **Docker and Jenkins Integration**  
   I learned how to run the Flask app and Selenium tests inside Docker containers and automate the process using Jenkins pipelines.

This was a good learning experience for me. I now understand how Selenium can be used in real projects and how it fits into DevOps workflows. 

## Selenium in DevOps

- DevOps automates build, test, deploy, and monitor.
- **Selenium handles automated testing** for web apps.
- After code is pushed, **Jenkins** can trigger Selenium tests.
- **Docker** ensures tests run consistently across machines.
- **Selenium Grid** lets you test on multiple browsers in parallel.
- Jenkins pipeline steps:
  1. Start the app
  2. Run Selenium tests
  3. Show results
  4. Stop services

### Advantages
✅ Saves time  
✅ Reduces manual errors  
✅ Ensures app works after every change



