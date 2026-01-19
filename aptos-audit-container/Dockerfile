FROM ubuntu:22.04

RUN set -ex; \
    apt-get update; \
    apt-get install -qqy --no-install-recommends \
    ca-certificates \
    wget \
    git \
    curl \
    python3 \
    python3-pip;

RUN set -ex; \
    pip install ipython; 

ENV PATH=$PATH:/root/.local/bin

RUN set -ex; \
    curl -sSfL \
    "https://aptos.dev/scripts/install_cli.sh" | sh;

CMD ["/bin/bash", "-i"]
