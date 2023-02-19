FROM postgres

USER postgres

ENV POSTGRES_USER postgres
ENV POSTGRES_PASSWORD postgres
ENV POSTGRES_DB postgres

COPY ./sql/ /docker-entrypoint-initdb.d
COPY ./scripts/database/create-role.sh /docker-entrypoint-initdb.d
