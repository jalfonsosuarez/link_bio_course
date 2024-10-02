FROM python

COPY . /usr/src/app

WORKDIR /usr/src/app 

RUN python -m venv .venv

RUN source .venv/bin/activate

RUN pip install -r requirements.txt

ENTRYPOINT uvicorn --host 0.0.0.0 main:app --reload
