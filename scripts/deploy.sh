#!/bin/bash

echo "Starting deployment..."
# Run database migrations
flask db upgrade

# Restart the application server
sudo systemctl restart myapp

echo "Deployment completed."
