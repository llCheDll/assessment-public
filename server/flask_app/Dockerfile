FROM python:3

COPY . /flask_app
ADD . /upload_files
WORKDIR /flask_app
ENV NAME venv

RUN pip install --upgrade pip
RUN pip install -r .meta/packages
RUN export FLASK_APP=ohcl_app.py

ENTRYPOINT ["python"]
CMD ["flask_app/ohcl_app.py"]
