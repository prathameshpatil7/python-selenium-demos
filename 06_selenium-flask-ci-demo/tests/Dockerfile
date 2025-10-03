FROM python:3.10-slim
WORKDIR /tests
COPY . /tests
RUN pip install -r requirements.txt
CMD ["pytest", "--maxfail=1", "--disable-warnings", "--tb=short"]