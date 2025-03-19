FROM harbor1.fisgeo.unipg.it/uninuvola/unihubsingle:latest

USER root

RUN apt update && \
    apt install -y zip unzip unrar-free openssh-client htop procps nano less tmux screen vim curl git

# Firefox
RUN install -d -m 0755 /etc/apt/keyrings && \
    wget -q https://packages.mozilla.org/apt/repo-signing-key.gpg -O- | tee /etc/apt/keyrings/packages.mozilla.org.asc > /dev/null && \
    echo "deb [signed-by=/etc/apt/keyrings/packages.mozilla.org.asc] https://packages.mozilla.org/apt mozilla main" | tee -a /etc/apt/sources.list.d/mozilla.list > /dev/null && \
    echo -e "Package: *\nPin: origin packages.mozilla.org\nPin-Priority: 1000\n" | tee /etc/apt/preferences.d/mozilla && cat /etc/apt/preferences.d/mozilla && \
    apt-get update && apt-get install -y firefox

# Chromium
RUN echo -e "deb https://ppa.launchpadcontent.net/chromium-team/dev/ubuntu bionic main\ndeb-src https://ppa.launchpadcontent.net/chromium-team/dev/ubuntu bionic main" | tee -a /etc/apt/sources.list.d/chromium.list > /dev/null && \
    apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EA6E302DC78CC4B087CFC3570EBEA9B02842F111 && \
    apt-get update && apt-get install -y chromium-browser


RUN echo "exec /bin/bash" >> /etc/profile

USER jovyan
