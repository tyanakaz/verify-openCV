FROM ubuntu:18.10

# docker build process is treated as locale with in the POSIX.
# It must be defined explicitly in Dockerfile
# https://github.com/docker/docker/issues/2424#issuecomment-27269233
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

# apt-get upgrade
RUN set -x \
        && apt-get update -q \
        && apt-get install -qy --no-install-recommends \
           locales git ssh vim less curl python3 \
           python-dev build-essential libssl-dev libffi-dev \
           libxml2-dev libxslt1-dev zlib1g-dev \
        # OpenCV \
        && apt-get install -qy libsm6 libxext6  libxrender-dev \
        # Update Locale to en_US.UTF-8 \
        && echo "en_US.UTF-8 UTF-8" > /etc/locale.gen \
        && locale-gen && update-locale LANG=en_US.UTF-8

# node setup
ENV NPM_CONFIG_LOGLEVEL info

# Install pip
RUN set -x \
            && curl -kL https://bootstrap.pypa.io/get-pip.py | python3

# Install openCV
RUN set -x \
            && pip install opencv-python

WORKDIR /usr/src/app

