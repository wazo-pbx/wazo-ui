FROM python:3.9-slim-bullseye AS compile-image
LABEL maintainer="Wazo Maintainers <dev@wazo.community>"

RUN python -m venv /opt/venv
# Activate virtual env
ENV PATH="/opt/venv/bin:$PATH"

COPY . /usr/src/wazo-ui
WORKDIR /usr/src/wazo-ui
RUN pip install -r requirements.txt
RUN python setup.py install

FROM python:3.9-slim-bullseye AS build-image
COPY --from=compile-image /opt/venv /opt/venv

COPY ./etc/wazo-ui /etc/wazo-ui
RUN true \
    && adduser --quiet --system --group --home /var/lib/wazo-ui wazo-ui \
    && mkdir -p /etc/wazo-ui/conf.d \
    && install -o wazo-ui -g wazo-ui /dev/null /var/log/wazo-ui.log

EXPOSE 9296

# Activate virtual env
ENV PATH="/opt/venv/bin:$PATH"
CMD ["wazo-ui", "-d"]
