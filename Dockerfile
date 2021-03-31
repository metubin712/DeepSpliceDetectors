FROM tensorflow/tensorflow:2.3.0-gpu
COPY ./ deep-splice-detectors
WORKDIR /deep-splice-detectors
RUN ./download_data.sh
RUN pip install --upgrade pip
RUN pip install -r docker-requirements.txt
