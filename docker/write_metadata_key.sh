#!/usr/bin/env sh
set -e
mkdir /etc/satosa/config/metadata
echo "$PRIVATE_KEY" > /etc/satosa/config/metadata.key
echo "$CERTIFICATE" > /etc/satosa/config/metadata.crt