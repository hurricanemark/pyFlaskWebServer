# use a node base image
FROM node:master

# set maintainer
LABEL maintainer "marknltv@comcast.net"

# set a health check
HEALTHCHECK --interval=5s \
            --timeout=5s \
            CMD curl -f http://127.0.0.1:4321 || exit 1

# tell docker what port to expose
EXPOSE 4321
