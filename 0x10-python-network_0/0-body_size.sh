#!/bin/bash
# GET request to the URL, and displays the body of the response
curl -s $1 | wc -c
