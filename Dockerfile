FROM python:3.7
WORKDIR /code
COPY Requirements.txt .
RUN pip install -r Requirements.txt
COPY . .
CMD ["python", "./app/text_gen.py"] 
