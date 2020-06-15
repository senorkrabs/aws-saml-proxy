FROM satosa/satosa:latest
COPY ./satosa/micro_services /src/satosa/src/satosa/micro_services/custom
COPY ./satosa/frontends /src/satosa/src/satosa/frontends/custom
COPY  ./satosa/config /etc/satosa/config
COPY ./docker/write_metadata_key.sh /write_metadata_key.sh
RUN chmod 755 /write_metadata_key.sh
CMD /write_metadata_key.sh; /start.sh