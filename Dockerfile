FROM python:3.12-bookworm

RUN python -m pip install --upgrade pip && \
    python -m pip install pytest pytest-bdd pytest-playwright && \
    apt-get install libevent-2.1-7 && \
    python -m playwright install-deps && \
    python -m playwright install
    
RUN mkdir -p /home/tests
COPY site.feature /home/tests/site.feature
COPY test_site.py /home/tests/test_site.py

WORKDIR /home/tests

ENTRYPOINT python -m pytest -vvv
