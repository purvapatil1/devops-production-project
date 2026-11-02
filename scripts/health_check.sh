#!/bin/bash

echo "================================"
echo "   DevOps Application Health"
echo "================================"

URL="http://localhost:5000/health"

if curl -s --fail "$URL" > /dev/null; then
    echo "STATUS: Application is HEALTHY"
else
    echo "STATUS: Application is DOWN"
    exit 1
fi

echo "================================"
