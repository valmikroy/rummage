# Use the official Python 3.10 image as the base image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

ARG TARGETPLATFORM

RUN apt update && apt upgrade -y && \
 apt autoremove -y && \
 apt-get install wget sudo build-essential -y 

RUN case ${TARGETPLATFORM} in \
        "linux/amd64")  ARCH_OPT=x86_64-unknown-linux-gnu  ;; \
        "linux/arm64")  ARCH_OPT=aarch64-unknown-linux-gnu  ;; \
    esac && \
 wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz && \
 tar -xzf ta-lib-0.4.0-src.tar.gz && \
 cd ta-lib && \
 ./configure --prefix=/usr --build=${ARCH_OPT} && \
 make && \
 make install && \
 rm -rf ta-lib && \
 rm -rf ta-lib-0.4.0-src.tar.gz && \
 pip install --upgrade pip


# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the working directory
COPY . .

# Expose the port on which the Flask app will run
EXPOSE 5000

# Specify the command to run the application
CMD [ "python", "app.py" ]
