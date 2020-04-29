FROM python:3
ADD mac_lookup.py /
RUN pip install requests
ENTRYPOINT [ "python", "./mac_lookup.py" ]
