#!/bin/bash

sed -i -- 's/"{GOREST_AUTH_TOKEN}"/os.environ["GOREST_AUTH_TOKEN"]/g' ./Config/config.py