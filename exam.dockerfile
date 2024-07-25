FROM python 

RUN "C:\Users\user\Desktop\practical"

COPY  exam.py c:\Users\user\Desktop\practical

RUN pip install

EXPOSE 8000

CMD [ "python, .py" ]
