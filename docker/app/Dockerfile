FROM python:3.8

ENV PATH="/opt/mssql-tools/bin:${PATH}"

COPY requirements.txt /pglr/
RUN pip3 install -r /pglr/requirements.txt

RUN mkdir /pglrtmp

WORKDIR /pglr

CMD [ "python3", "/pglr/pglr.py" ]
