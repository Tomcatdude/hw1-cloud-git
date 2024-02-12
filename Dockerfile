FROM python:3.12.1-bookworm

 

RUN mkdir -p /home/app

RUN cd /home/app


COPY rest_api_server.py /home/app

 

RUN pip3 install bottle
RUN pip3 install pytest

 

CMD ["python3", "/home/app/rest_api_server.py"]