FROM python:2.7-alpine

COPY resources/gateway/ /usr/local/share/gateway/

RUN pip install web.py

EXPOSE 8080

WORKDIR /usr/local/share/gateway/
ENTRYPOINT ["python"]
CMD ["/usr/local/share/gateway/code.py"]