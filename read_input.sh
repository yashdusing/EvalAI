#!/bin/bash

read -p "Enter RDS Host : " POSTGRES_HOST
echo "POSTGRES_HOST=$POSTGRES_HOST" > .env
echo "" > .env

read -p "Enter Hostname : " HOSTNAME
echo "HOSTNAME=$HOSTNAME" > .env
echo "" > .env