#!/bin/bash
echo "Deploying..."
docker-compose down
docker-compose build
docker-compose up -d
echo "Deployment complete."
