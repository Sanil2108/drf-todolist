#!/bin/bash
BASE_URL='http://localhost:8000'

operation=$1
if [[ $operation == create-user ]]; then
    email=$2
    name=$3
    password=$4

    curl -i $BASE_URL'/users/detail/' \
    -H 'Content-Type: application/json' \
    --data-binary '{"name": "'$name'","email": "'$email'","password": "'$password'"}' \
    --compressed
fi

if [[ $operation == delete-user ]]; then
    email=$2
    password=$3

    curl -i -X "DELETE" $BASE_URL'/users/detail/' \
    -H 'Content-Type: application/json' \
    --data-binary '{"email": "'$email'","password": "'$password'"}' \
    --compressed
fi

if [[ $operation == user-token-auth ]]; then
    email=$2
    token=$3

    curl -i -X "POST" $BASE_URL'/users/token_auth/' \
    -H 'Content-Type: application/json' \
    --data-binary '{"user": {"email": "'$email'"}, "token": {"token_string":"'$token'"}}' \
    --compressed
fi

if [[ $operation == user-password-auth ]]; then
    email=$2
    password=$3

    curl -i -X "POST" $BASE_URL'/users/password_auth/' \
    -H 'Content-Type: application/json' \
    --data-binary '{"user": {"email": "'$email'","password": "'$password'"}}' \
    --compressed
fi


echo "
"