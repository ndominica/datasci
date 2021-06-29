#!/bin/bash

echo "Starting Docker Build"

docker build -t streamlit_app:latest .

echo "Docker Build Ended"
