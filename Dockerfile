FROM nvidia/cuda:11.3.1-cudnn8-runtime-ubuntu20.04 AS env

RUN apt update && apt install -y python3 nano python3-pip

COPY requirements.txt /

RUN pip install torch==1.11.0+cu113 torchvision==0.12.0+cu113 torchaudio==0.11.0+cu113 -f https://download.pytorch.org/whl/cu113/torch_stable.html

RUN pip install -r /requirements.txt

RUN mkdir /.cache && chmod 777 /.cache 

# Set the PATH environment variable
ENV PATH="/usr/bin/python3:${PATH}"
ENV PATH="/usr/bin/accelerate:${PATH}"

FROM env as final

WORKDIR /work/project

COPY . .

# single gpu case
#CMD ["python3", "main.py"]

# multiple gpus case
CMD ["accelerate", "launch", "--num_processes", "4", "main.py"]
