# 🚀 Setup & Run Supplier Dashboard Servers

**Goal:** Get the full supplier dashboard working with real servers  
**Time Required:** 10-15 minutes  
**Difficulty:** Easy  

---

## 📋 Prerequisites

- ✅ Node.js installed (`node --version`)
- ✅ npm installed (`npm --version`)
- ✅ Windows (you're using Windows)

---

## 🎯 What You'll Get

After setup:
- ✅ Data Server running on port 3001
- ✅ Backend API running on port 3000
- ✅ Frontend accessible at http://localhost:8000
- ✅ Full supplier dashboard with real data
- ✅ User authentication working
- ✅ Favorites, notes, inbox features

---

## 📦 Step 1: Install Dependencies

### **For Data Server**
```bash
cd "C:\Users\n0l08i7\OneDrive - Walmart Inc\Code Puppy\Supplier\data-server"
npm install
```

**Output should show:**
```
added XX packages
```

### **For Backend Server**
```bash
cd "C:\Users\n0l08i7\OneDrive - Walmart Inc\Code Puppy\Supplier\backend"
npm install
```

**Output should show:**
```
added XX packages
```

---

## 🖥️ Step 2: Start Data Server (Terminal 1)

**Open a new terminal and run:**

```bash
cd "C:\Users\n0l08i7\OneDrive - Walmart Inc\Code Puppy\Supplier\data-server"
node server.js
```

**Expected output:**
```
🚀 Data Server running on http://localhost:3001
📊 Try: http://localhost:3001/api/suppliers
🔌 WebSocket available at ws://localhost:3001
```

✅ **Leave this terminal running!**

---

## 🔧 Step 3: Start Backend Server (Terminal 2)

**Open another terminal and run:**

```bash
cd "C:\Users\n0l08i7\OneDrive - Walmart Inc\Code Puppy\Supplier\backend"
node server.js
```

**Expected output:**
```
🚀 Backend API Server running on http://localhost:3000
📡 Connected to Data Server at http://localhost:3001
```

✅ **Leave this terminal running!**

---

## 🌐 Step 4: Start Frontend Server (Terminal 3)

**Open a third terminal and run:**

### **Option A: Using Python (Recommended)**
```bash
cd "C:\Users\n0l08i7\OneDrive - Walmart Inc\Code Puppy\Supplier"
python -m http.server 8000
```

**Expected output:**
```
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
```

### **Option B: Using Node.js**
```bash
cd "C:\Users\n0l08i7\OneDrive - Walmart Inc\Code Puppy\Supplier"
npm install -g http-server
http-server -p 8000
```

✅ **Leave this terminal running!**

---

## 🌍 Step 5: Open Dashboard in Browser

**Open your browser and go to:**
```
http://localhost:8000/dashboard_with_api.html
```

**What you should see:**
- ✅ Supplier dashboard loads
- ✅ Supplier data populates
- ✅ Status shows "☁️ Cloud Mode" or "💾 Local Mode"
- ✅ Search and filters work
- ✅ Pagination works

---

## ✅ Verify Everything Works

### **Check Data Server**
```
http://localhost:3001/health
```
Should show:
```json
{"status": "ok", "service": "data-server", "port": 3001}
```

### **Check Backend Server**
```
http://localhost:3000/health
```
Should show:
```json
{"status": "ok", "service": "backend", "port": 3000}
```

### **Get Suppliers**
```
http://localhost:3001/api/suppliers
```
Should show JSON data with suppliers

### **Dashboard**
```
http://localhost:8000/dashboard_with_api.html
```
Should load fully with data

---

## 🎮 Test Features

### **Search**
- Type a supplier name in search box
- Should filter results

### **Filter**
- Select categories
- Filter by rating
- Check "Verified Only"
- Should filter suppliers

### **Pagination**
- Click page numbers
- Should navigate pages

### **User Features** (if implemented)
- Add favorites
- Add notes
- View inbox

---

## 🛑 Troubleshooting

### **Issue: "Cannot GET /dashboard_with_api.html"**

**Solution:** Make sure you're in the correct directory
```bash
cd "C:\Users\n0l08i7\OneDrive - Walmart Inc\Code Puppy\Supplier"
python -m http.server 8000
```

### **Issue: "Error: listen EADDRINUSE"**

Port is already in use. Kill the process:
```bash
# Find what's using port 3000
netstat -ano | findstr :3000

# Kill the process (replace PID with the number shown)
taskkill /PID <PID> /F

# Or use different ports:
BACKEND_PORT=3010 node backend/server.js
DATA_SERVER_PORT=3011 node data-server/server.js
```

### **Issue: "Cannot find module 'express'"**

**Solution:** Install dependencies
```bash
cd "C:\Users\n0l08i7\OneDrive - Walmart Inc\Code Puppy\Supplier\backend"
npm install
```

### **Issue: "npm: command not found"**

**Solution:** Node.js not installed. Download from nodejs.org

### **Issue: Dashboard loads but no data shown**

**Check:**
1. Is data server running? (Check terminal 1)
2. Is backend server running? (Check terminal 2)
3. Is frontend server running? (Check terminal 3)
4. Are ports correct? (3000, 3001, 8000)
5. Open browser console (F12) and check for errors

---

## 🔄 Daily Usage

### **To Start Everything:**

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

### **To Stop Everything:**
- Press `Ctrl + C` in each terminal
- Close browser

---

## 💡 Quick Reference

| Service | Command | Port | Status |
|---------|---------|------|--------|
| **Data Server** | `cd data-server && node server.js` | 3001 | Terminal 1 |
| **Backend** | `cd backend && node server.js` | 3000 | Terminal 2 |
| **Frontend** | `cd supplier && python -m http.server 8000` | 8000 | Terminal 3 |
| **Dashboard** | `http://localhost:8000/dashboard_with_api.html` | 8000 | Browser |

---

## 📊 Architecture

```
Browser (localhost:8000)
     ↓
 dashboard_with_api.html
     ↓
Backend API (localhost:3000)
     ↓
Data Server (localhost:3001)
     ↓
Supplier Data (150 items)
```

---

## 🎯 Environment Variables (Optional)

You can customize ports:

```bash
# Data server on port 3011
DATA_SERVER_PORT=3011 node server.js

# Backend on port 3010
BACKEND_PORT=3010 node server.js

# Backend pointing to different data server
DATA_SERVER_URL=http://localhost:3011 node server.js
```

---

## ✨ Done!

Your supplier dashboard system is now running with:
- ✅ Real supplier data
- ✅ REST API
- ✅ User features
- ✅ Full functionality

**Enjoy your fully functional Supplier Dashboard!** 🚀