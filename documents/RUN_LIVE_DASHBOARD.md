# 🚀 RUN THE LIVE DASHBOARD WITH API SERVERS

**Goal:** Get the actual dashboard_with_api.html working with live backend servers  
**Status:** Code has been updated ✅  
**Time Required:** 10 minutes to get running  

---

## ✅ What's Been Fixed

I've updated the `dashboard_with_api.html` file to:

✅ **Initialize `allSuppliers` array properly**
✅ **Connect to Backend API at `http://localhost:3000`**  
✅ **Automatically fetch supplier data on page load**  
✅ **Display error messages if servers aren't running**  
✅ **Show connection status in toolbar**  

---

## 📋 Prerequisites

- ✅ Node.js installed
- ✅ npm installed
- ✅ 3 available terminal windows
- ✅ Ports 3000, 3001, 8000 available

---

## 🎯 Quick Start (10 minutes)

### **Step 1: Install Dependencies**

#### Data Server dependencies:
```bash
cd "C:\Users\n0l08i7\OneDrive - Walmart Inc\Code Puppy\Supplier\data-server"
npm install
```

#### Backend API dependencies:
```bash
cd "C:\Users\n0l08i7\OneDrive - Walmart Inc\Code Puppy\Supplier\backend"
npm install
```

✅ You only need to do this once!

---

### **Step 2: Start Data Server (Terminal 1)**

```bash
cd "C:\Users\n0l08i7\OneDrive - Walmart Inc\Code Puppy\Supplier\data-server"
node server.js
```

**You should see:**
```
🚀 Data Server running on http://localhost:3001
📊 Try: http://localhost:3001/api/suppliers
🔌 WebSocket available at ws://localhost:3001
```

✅ **Leave this running!**

---

### **Step 3: Start Backend API (Terminal 2)**

```bash
cd "C:\Users\n0l08i7\OneDrive - Walmart Inc\Code Puppy\Supplier\backend"
node server.js
```

**You should see:**
```
🚀 Backend API Server running on http://localhost:3000
📡 Connected to Data Server at http://localhost:3001
```

✅ **Leave this running!**

---

### **Step 4: Start Frontend Server (Terminal 3)**

```bash
cd "C:\Users\n0l08i7\OneDrive - Walmart Inc\Code Puppy\Supplier"
python -m http.server 8000
```

**You should see:**
```
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
```

✅ **Leave this running!**

---

### **Step 5: Open Dashboard in Browser**

```
http://localhost:8000/dashboard_with_api.html
```

**What you'll see:**
- ✅ Page loads
- ✅ Toolbar shows "⏳ Loading..."
- ✅ Suppliers start appearing
- ✅ Filters populate automatically
- ✅ Toolbar shows "☁️ API Connected"

---

## 🎮 Test It Works

### **Test 1: Page Loads with Data**
- ✅ Dashboard displays supplier cards
- ✅ Filter sidebar populates
- ✅ Status shows "☁️ API Connected"

### **Test 2: Search Works**
1. Type "Steel" in search box
2. Results should filter
3. Count should decrease

### **Test 3: Filters Work**
1. Check a category filter
2. Suppliers should filter instantly
3. Count updates

### **Test 4: Pagination Works**
1. If more than 12 suppliers, pagination appears
2. Click page numbers
3. Content changes

---

## 🔍 Verify Servers Are Running

### **Check Data Server (Port 3001):**
```
http://localhost:3001/health
```
Should show:
```json
{"status": "ok", "service": "data-server", "port": 3001}
```

### **Check Backend Server (Port 3000):**
```
http://localhost:3000/health
```
Should show:
```json
{"status": "ok", "service": "backend", "port": 3000}
```

### **Check API Endpoint (Port 3000):**
```
http://localhost:3000/api/suppliers
```
Should return JSON with suppliers array

---

## 🛑 Troubleshooting

### **Issue: "Cannot Connect to Server" Error**

**Cause:** Backend server not running on port 3000

**Fix:**
1. Check Terminal 2 (backend) is running
2. Verify it says "running on http://localhost:3000"
3. Refresh browser (Ctrl+R)
4. Check browser console (F12) for error details

---

### **Issue: "API Error - Check server"**

**Cause:** One of the servers isn't responding

**Fix:**
1. Check all 3 terminals show their startup messages
2. Verify no "Error" messages in terminals
3. Try accessing health endpoints above
4. Restart any server that's having issues

---

### **Issue: "Address already in use" Error**

**Cause:** Port is already occupied

**Fix - Find what's using the port:**
```bash
netstat -ano | findstr :3000
```

**Then kill it:**
```bash
# Replace PID with the number from above
taskkill /PID <PID> /F
```

**Or use different ports:**
```bash
BACKEND_PORT=3010 node server.js
DATA_SERVER_PORT=3011 node server.js
```

---

### **Issue: "Cannot find module 'express'"**

**Cause:** Dependencies not installed

**Fix:**
```bash
# For data server
cd data-server
npm install

# For backend
cd backend
npm install
```

---

### **Issue: Nothing appears on page**

**Check:**
1. Are all 3 servers running? (Check terminals)
2. Open browser console (F12)
3. Look for red error messages
4. Check if data is being loaded:
   - Click F12 → Network tab
   - Look for request to `http://localhost:3000/api/suppliers`
   - Should return JSON data

---

## 📊 What's Happening

```
1. You open http://localhost:8000/dashboard_with_api.html
   ↓
2. Browser downloads HTML/CSS/JavaScript
   ↓
3. JavaScript runs and calls initializeDashboard()
   ↓
4. initializeDashboard() calls loadSuppliersFromAPI()
   ↓
5. Fetch request sent to http://localhost:3000/api/suppliers
   ↓
6. Backend API (port 3000) receives request
   ↓
7. Backend proxies to Data Server (port 3001)
   ↓
8. Data Server returns 150 suppliers
   ↓
9. Backend returns suppliers to frontend
   ↓
10. Dashboard displays suppliers ✅
    Status shows "☁️ API Connected"
```

---

## 🎯 Connection Flow

```
Browser at http://localhost:8000
        ↓
   dashboard_with_api.html
        ↓
Fetch: http://localhost:3000/api/suppliers
        ↓
Backend API (port 3000)
        ↓
Fetch: http://localhost:3001/api/suppliers
        ↓
Data Server (port 3001)
        ↓
Return 150 suppliers (JSON)
        ↓
Backend returns JSON to frontend
        ↓
Dashboard displays suppliers
```

---

## 💡 Daily Usage

### **Every time you want to use the dashboard:**

**Terminal 1:**
```bash
cd "C:\Users\n0l08i7\OneDrive - Walmart Inc\Code Puppy\Supplier\data-server"
node server.js
```

**Terminal 2:**
```bash
cd "C:\Users\n0l08i7\OneDrive - Walmart Inc\Code Puppy\Supplier\backend"
node server.js
```

**Terminal 3:**
```bash
cd "C:\Users\n0l08i7\OneDrive - Walmart Inc\Code Puppy\Supplier"
python -m http.server 8000
```

**Browser:**
```
http://localhost:8000/dashboard_with_api.html
```

---

## 🔧 Configuration

### **Change API URL** (if needed)

Edit `dashboard_with_api.html` line with:
```javascript
const API_URL = 'http://localhost:3000'; // Change this
```

### **Change Port Numbers**

```bash
# Data Server - default 3001
DATA_SERVER_PORT=3011 node data-server/server.js

# Backend - default 3000
BACKEND_PORT=3010 node backend/server.js

# Frontend - default 8000
python -m http.server 9000

# Then open: http://localhost:9000/dashboard_with_api.html
```

---

## ✅ Verification Checklist

- [ ] Data Server running on port 3001
- [ ] Backend API running on port 3000
- [ ] Frontend server running on port 8000
- [ ] Dashboard opens at http://localhost:8000/dashboard_with_api.html
- [ ] Page shows suppliers
- [ ] Toolbar shows "☁️ API Connected"
- [ ] Filters work
- [ ] Search works
- [ ] Pagination works

---

## 🎉 Success!

When everything is working:

✅ Dashboard loads instantly  
✅ Shows 150+ suppliers from API  
✅ All filters and search work  
✅ Real-time data updates  
✅ Production-ready setup  

---

## 📝 Notes

- Don't open the file directly with `file://` protocol
- Must serve via HTTP (`http://localhost:8000`)
- All 3 servers must be running for full functionality
- Close any server with `Ctrl + C`
- Refresh browser if you make changes
- Check browser console (F12) for detailed error messages

---

## 🚀 You're All Set!

The dashboard is now configured to work with live API servers. Follow the steps above to get it running!

**Questions?** Check the error messages in browser console (F12 → Console tab) or terminal output.