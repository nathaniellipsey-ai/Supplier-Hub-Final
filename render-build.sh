#!/bin/bash

# CRITICAL: Force Node.js build (not Python)
# This script ensures Render uses npm instead of Python

set -e

echo "=================================================="
echo "Render Build Script - Node.js Project"
echo "=================================================="
echo ""

# Verify Node.js is available
echo "Checking Node.js..."
node --version || exit 1
npm --version || exit 1

echo ""
echo "Installing dependencies..."
npm ci --production 2>/dev/null || npm install --production

echo ""
echo "=================================================="
echo "Build Complete - Ready to start server"
echo "=================================================="
