FROM ubuntu:22.04

RUN set -ex; \
    apt-get update; \
    apt-get install -qqy --no-install-recommends \
    ca-certificates \
    wget \
    ssh \
    git \
    curl \
    python3 \
    python3-pip;

RUN set -ex; \
    pip install ipython; 

ENV PATH=$PATH:/root/.local/bin

RUN set -ex; \
    curl -sSfL \
    https://raw.githubusercontent.com/Mystenlabs/suiup/main/install.sh \
    | sh; \
    suiup install sui@testnet-1.60.0 -y

CMD ["/bin/bash", "-i"]
