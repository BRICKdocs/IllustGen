FROM python:3

# copy all files
COPY . /app

# dependencies
RUN pip install --no-cache-dir -r requirements.txt 

# set the directory
WORKDIR /app

#Entry point
ENTRYPOINT [ "flask" ]

# run command
CMD ["run", "--host","0.0.0.0"]