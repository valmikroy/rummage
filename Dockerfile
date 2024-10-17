# Use the official Python 3.10 image as the base image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app


RUN apt update && apt upgrade -y && \
 apt autoremove -y && \
 apt-get install wget sudo build-essential -y && \
 wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz && \
 tar -xzf ta-lib-0.4.0-src.tar.gz && \
 cd ta-lib && \
 wget 'http://git.savannah.gnu.org/gitweb/?p=config.git;a=blob_plain;f=config.guess;hb=HEAD' -O './config.guess' && \
 wget 'http://git.savannah.gnu.org/gitweb/?p=config.git;a=blob_plain;f=config.sub;hb=HEAD' -O './config.sub' && \
 ./configure --prefix=/usr && \
 make && \
 make install && \
 rm -rf ta-lib && \
 rm -rf ta-lib-0.4.0-src.tar.gz && \
 pip install --upgrade pip


# Copy the requirements file to the working directory
COPY requirements.txt .
#COPY build.sh .

#RUN  bash build.sh 

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the working directory
COPY . .

# Expose the port on which the Flask app will run
EXPOSE 5000

# Specify the command to run the application
CMD [ "python", "app.py" ]