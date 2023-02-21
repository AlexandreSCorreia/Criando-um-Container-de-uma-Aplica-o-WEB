
FROM debian

RUN apt-get update && apt-get install -y apache2 && apt-get clean

COPY . /var/www/html

LABEL description="Apache Webserver 1.0"

VOLUME /var/www/html/

EXPOSE 80

ENTRYPOINT ["/usr/sbin/apachectl"]

CMD ["-D", "FOREGROUND"]