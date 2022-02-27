FROM python:3.9-slim-bullseye

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN apt update
RUN apt -y install megatools

COPY ./requirements.txt .
RUN pip install -r requirements.txt


WORKDIR /app
COPY ban_chat.py /app/.
COPY get_session_from_bot.py /app/.
WORKDIR /app
