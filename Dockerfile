# Use the official Python 3.9 image
FROM python:3.9
 
# Set the working directory to /code
WORKDIR /code
 
# Copy the current directory contents into the container at /code
COPY ./requirements.txt /code/requirements.txt
 
# Install requirements.txt 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
 
# Set up a new user named "user" with user ID 1000
RUN useradd -m -u 1000 user
# Switch to the "user" user

# install ffmpeg on docker image
RUN apt-get -y update
RUN apt-get install -y ffmpeg

USER user
# Set home to the user's home directory
ENV HOME=/home/user PATH=/home/user/.local/bin:$PATH GRADIO_SERVER_NAME=0.0.0.0 GRADIO_SERVER_PORT=7860
 
# Set the working directory to the user's home directory
WORKDIR $HOME/app
 
# Copy the current directory contents into the container at $HOME/app setting the owner to the user
COPY --chown=user . $HOME/app
 
# Start the FastAPI app on port 7860, the default port expected by Spaces
# CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]
EXPOSE 7860

CMD ["python", "app.py"]
