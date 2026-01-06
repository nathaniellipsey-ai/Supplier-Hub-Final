# Project Structure

## Root Directory (Core Project Files)

```
Supplier-Hub-Final/
├── server.js                    <- Main Node.js server
├── package.json                <- Node.js dependencies
├── render.yaml                 <- Render deployment config
├── runtime.txt                 <- Node.js version (CRITICAL!)
├── build.sh                    <- Build script
├── .env                        <- Environment variables
├── .env.example                <- Example env vars
├── .gitignore                  <- Git ignore rules
├── .renderignore               <- Render ignore rules
├──
├── FRONTEND HTML FILES         <- User interface
├─ index.html                  <- Redirect to dashboard
├─ dashboard_with_api.html     <- Main dashboard
├─ login.html                  <- Login page
├─ help.html                   <- Help page
├─ inbox.html                  <- Messages/inbox
├─ my-favorites.html           <- Favorites page
├─ my-notes.html               <- Notes page
├─ auth-callback.html          <- Auth callback
├─ supplier-auth-system.html   <- Auth system
├─ supplier-modals.html        <- Modal components
├─ dashboard_local_example.html<- Example version
├─ test-setup.js               <- Test setup
├─ favicon.svg                 <- Favicon
├─
├── FOLDERS
├─ backend/                    <- Backend server files
├─   └─ server.js
├─
├─ data-server/                <- Data server files
├─   ├─ server.js
├─   └─ data-generator.js
├─
├─ frontend/                   <- Frontend assets
├─   └─ (frontend files)
├─
├─ documents/                  <- ALL DOCUMENTATION (organized here!)
├─   ├─ README.md                 <- Documentation index
├─   ├─ RENDER_FIX_NOW.txt        <- Critical Render fix
├─   ├─ GETTING_STARTED.md        <- Quick start
├─   ├─ PRODUCTION_DEPLOYMENT.md  <- Full deployment guide
├─   ├─ FIX_RENDER_BUILD.md       <- Build troubleshooting
├─   ├─ [45+ more documentation files]
├─   └─ legacy_python/            <- Legacy Python files
├─       ├─ backend_server.py
├─       └─ data_server.py
└─
```

---

## File Organization Summary

### Core Project (22 files in root)

**Configuration Files**
- `package.json` - Node.js dependencies (4 packages: express, cors, body-parser, ws)
- `render.yaml` - Render deployment configuration
- `runtime.txt` - Specifies Node.js 18.19.0 (CRITICAL!)
- `.env` - Production environment variables
- `.env.example` - Example environment template
- `.gitignore` - Git ignore rules
- `.renderignore` - Render ignore rules
- `build.sh` - Build script

**Server Code**
- `server.js` - Main unified server (14.4 KB)
  - Serves frontend HTML
  - Provides REST API endpoints
  - Handles WebSocket connections
  - Manages user data

**Frontend (HTML/CSS/JS)**
- `index.html` - Redirect to dashboard
- `dashboard_with_api.html` - Main dashboard (155.5 KB)
- `login.html` - Login page (14.8 KB)
- `help.html` - Help/docs (33.3 KB)
- `inbox.html` - Messages (33.0 KB)
- `my-favorites.html` - Favorites (12.0 KB)
- `my-notes.html` - Notes (14.8 KB)
- `auth-callback.html` - Auth callback (6.1 KB)
- `supplier-auth-system.html` - Auth system (12.0 KB)
- `supplier-modals.html` - Modals (34.4 KB)
- `dashboard_local_example.html` - Example (24.2 KB)
- `test-setup.js` - Test setup (6.2 KB)
- `favicon.svg` - Icon (505 B)

**Supporting Folders**
- `backend/` - Backend server implementation
- `data-server/` - Data generation server
- `frontend/` - Frontend assets
- `documents/` - ALL DOCUMENTATION (organized!)

---

## Documentation Files (47 + 1 subfolder)

All documentation files have been moved to `documents/` folder for organization.

### Quick Reference
- `documents/README.md` - Documentation index
- `documents/RENDER_FIX_NOW.txt` - **START HERE IF BUILD FAILS**
- `documents/GETTING_STARTED.md` - **START HERE FOR SETUP**
- `documents/READY_TO_DEPLOY.txt` - Quick checklist
- `documents/PRODUCTION_DEPLOYMENT.md` - Complete guide

### Deployment Guides
- `documents/DEPLOYMENT_SUMMARY.md`
- `documents/FIX_RENDER_BUILD.md`
- `documents/DEPLOY_CHECKLIST.md`
- `documents/DEPLOY_TO_RENDER.md`
- `documents/DEPLOY_NOW.txt`
- `documents/DEPLOY_TODAY.txt`
- `documents/CREATE_NEW_RENDER_SERVICE.txt`
- `documents/PUSH_TO_RENDER.md`

### Architecture & Reference
- `documents/ARCHITECTURE.md`
- `documents/INDEX.md`
- `documents/DEPLOYMENT_READY.md`
- `documents/README.md` (original)

### Setup & Configuration
- `documents/SETUP_SERVERS.md`
- `documents/THE_4_COMMANDS.txt`
- `documents/SIMPLE_4_STEPS.txt`
- `documents/QUICKSTART.md`
- `documents/QUICK_START_LIVE.md`
- `documents/INSTALL_NODEJS_NOW.md`
- `documents/RUN_LIVE_DASHBOARD.md`

### Troubleshooting
- `documents/RENDER_NOT_DEPLOYING.txt`
- `documents/SERVER_CONNECTION_DIAGNOSTIC.md`
- `documents/LOCALHOST_CONNECTION_FIX.md`
- `documents/WHY_NO_SERVER_CONNECTION.md`
- `documents/CONNECTING_STATUS_FIXED.md`
- `documents/WHY_NO_CHANGES.txt`

### Reference & Legacy
- `documents/ALTERNATIVE_SOLUTION_PYTHON.md`
- `documents/ANSWER_SERVER_CONNECTION.md`
- `documents/CREATED.md`
- `documents/FIXED_DASHBOARD_READY.md`
- `documents/GO_LIVE_NOW.md`
- `documents/FINAL_VERIFICATION.txt`
- `documents/COPY_PASTE_COMMANDS.txt`
- `documents/COMMIT_GUIDE.txt`
- `documents/CHATBOT_*.txt` (3 files)
- `documents/PYTHON_QUICK_START.md`
- `documents/RUN_PYTHON_SERVERS.md`
- `documents/LOCAL_EXAMPLE_README.md`
- `documents/START_HERE.txt`
- `documents/START_HERE.md`

### Legacy Python
- `documents/legacy_python/backend_server.py` - Legacy Python backend
- `documents/legacy_python/data_server.py` - Legacy Python data server

---

## Key Files

### CRITICAL FILES (Do Not Delete!)

1. **runtime.txt** (14 bytes)
   - Tells Render to use Node.js 18.19.0
   - **MUST be in root directory**
   - **CANNOT be moved**

2. **server.js** (14.4 KB)
   - Main application server
   - Serves frontend + API + WebSocket
   - Entry point for the application

3. **package.json** (953 bytes)
   - Node.js dependencies
   - Build and start scripts
   - Project metadata

4. **render.yaml** (669 bytes)
   - Render deployment configuration
   - Specifies build and start commands

### Configuration Files

- `.env` - Production environment variables
- `.env.example` - Template for .env
- `.gitignore` - Git ignore rules
- `.renderignore` - Render ignore rules

---

## File Sizes

**Root Directory**: 365.5 KB (22 files)
- HTML files: ~330 KB
- Server/Config: ~20 KB

**Documents Folder**: 331.8 KB (47 files + legacy_python/)
- Markdown/Text: ~330 KB
- Python files: ~7 KB

**Total**: ~700 KB

---

## Development vs Production

### Local Development
```bash
npm install        # Install dependencies
npm run dev        # Run with auto-reload
npm start          # Run normally
```

### Production (Render)
```
render.yaml specifies:
- Build: npm install
- Start: node server.js
- Node: 18.19.0
```

---

## Important Notes

1. **runtime.txt is CRITICAL**
   - Must stay in root directory
   - Cannot be moved to documents/
   - Tells Render to use Node.js

2. **All documentation is now organized**
   - In `documents/` folder
   - Keeps root directory clean
   - Easy to find guides

3. **Legacy Python files are archived**
   - Moved to `documents/legacy_python/`
   - No longer used
   - Kept for reference only

4. **Core project is clean**
   - Only essential files in root
   - Ready for production
   - Minimal dependencies

---

## Quick Links

- **Start deployment?** → `documents/RENDER_FIX_NOW.txt`
- **Need help?** → `documents/GETTING_STARTED.md`
- **Full details?** → `documents/PRODUCTION_DEPLOYMENT.md`
- **Build failing?** → `documents/FIX_RENDER_BUILD.md`
- **Connection issues?** → `documents/SERVER_CONNECTION_DIAGNOSTIC.md`

---

**Last Updated**: January 6, 2026  
**Project Status**: Production Ready  
**Runtime**: Node.js 18.19.0  
**Deployment**: Render  
