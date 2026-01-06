# Documentation & Reference Files

This folder contains all documentation, guides, and reference materials for the Supplier Hub Portal.

## Quick Start Files

Start here if you're new:
- **RENDER_FIX_NOW.txt** - If build is failing (CRITICAL FIX)
- **GETTING_STARTED.md** - Quick start guide
- **READY_TO_DEPLOY.txt** - Quick reference checklist
- **START_HERE.txt** - Original getting started guide

## Deployment Guides

- **PRODUCTION_DEPLOYMENT.md** - Complete production deployment guide
- **DEPLOYMENT_SUMMARY.md** - Technical overview of deployment
- **FIX_RENDER_BUILD.md** - Detailed Render build troubleshooting
- **DEPLOY_CHECKLIST.md** - Pre-deployment verification
- **DEPLOY_TO_RENDER.md** - Step-by-step Render deployment

## Architecture & Design

- **ARCHITECTURE.md** - System architecture overview
- **INDEX.md** - Complete index and API reference
- **DEPLOYMENT_READY.md** - Deployment readiness checklist

## Setup & Configuration

- **SETUP_SERVERS.md** - Server setup instructions
- **THE_4_COMMANDS.txt** - Essential commands
- **SIMPLE_4_STEPS.txt** - Simplified 4-step setup

## Troubleshooting

- **RENDER_NOT_DEPLOYING.txt** - Common Render issues
- **SERVER_CONNECTION_DIAGNOSTIC.md** - Connection troubleshooting
- **LOCALHOST_CONNECTION_FIX.md** - Local connection issues
- **WHY_NO_SERVER_CONNECTION.md** - Server connection debugging
- **CONNECTING_STATUS_FIXED.md** - Status connection fixes

## Python (Legacy)

These files are for reference only. The project is now Node.js:
- **ALTERNATIVE_SOLUTION_PYTHON.md** - Legacy Python version
- **RUN_PYTHON_SERVERS.md** - Legacy Python server info
- **PYTHON_QUICK_START.md** - Legacy Python setup

Legacy Python files are in the `legacy_python/` subfolder:
- `legacy_python/backend_server.py`
- `legacy_python/data_server.py`

## Reference Documentation

- **README.md** - Original project README
- **CHATBOT_DEPLOY.txt** - Chatbot deployment info
- **CHATBOT_FEATURES.txt** - Chatbot feature list
- **CHATBOT_SUMMARY.txt** - Chatbot summary
- **CREATED.md** - Project creation notes
- **ANSWER_SERVER_CONNECTION.md** - Server connection answers
- **FIXED_DASHBOARD_READY.md** - Dashboard ready status
- **GO_LIVE_NOW.md** - Go live instructions
- **RUN_LIVE_DASHBOARD.md** - Run live dashboard

## Configuration Files

- **runtime.txt** - Render Node.js version specification (CRITICAL!)
- **COMMIT_GUIDE.txt** - Git commit guidelines

## Status Files

- **FINAL_VERIFICATION.txt** - Final verification checklist
- **WHY_NO_CHANGES.txt** - Explanation of changes
- **COPY_PASTE_COMMANDS.txt** - Common commands

---

## File Organization

```
documents/
├── README.md (this file)
├── RENDER_FIX_NOW.txt (START HERE if build fails)
├── GETTING_STARTED.md (START HERE for quick setup)
├── PRODUCTION_DEPLOYMENT.md (Complete guide)
├── legacy_python/ (Legacy Python files - reference only)
└── [50+ other documentation files]
```

## Recommended Reading Order

### If you're deploying for the first time:
1. RENDER_FIX_NOW.txt
2. GETTING_STARTED.md
3. READY_TO_DEPLOY.txt
4. PRODUCTION_DEPLOYMENT.md

### If something is broken:
1. RENDER_FIX_NOW.txt
2. FIX_RENDER_BUILD.md
3. SERVER_CONNECTION_DIAGNOSTIC.md

### If you need complete details:
1. ARCHITECTURE.md
2. PRODUCTION_DEPLOYMENT.md
3. DEPLOYMENT_SUMMARY.md
4. INDEX.md

---

## Key Information

**Project Type**: Node.js + Express + HTML/CSS/JavaScript  
**Main Files**: server.js, package.json, *.html  
**Deployment**: Render  
**Runtime**: Node.js 18.19.0  

**Critical Files in Root**:
- `server.js` - Main server file
- `package.json` - Dependencies
- `render.yaml` - Render configuration
- `runtime.txt` - Node.js version (CRITICAL!)
- `.env` - Environment variables
- `*.html` - Frontend files

---

**Note**: This folder contains documentation only. Core project files remain in the parent directory.
