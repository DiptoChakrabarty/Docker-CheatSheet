FROM python
RUN  mkdir app
WORKDIR   /app
COPY   calculator.py   .
CMD   ["python","calculator.py"]