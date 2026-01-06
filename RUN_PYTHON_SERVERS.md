# 🚀 RUN DASHBOARD WITH PYTHON SERVERS (No Node.js Needed!)

**Status:** ✅ All Python servers created and dependencies installed!  
**Python Version:** 3.13.5  
**Dependencies:** Flask, Flask-CORS, Requests installed via Walmart PyPI  

---

## ⚡ Quick Start (2 minutes)

### **Terminal 1 - Data Server (Port 3001):**

```bash
cd "C:\Users\n0l08i7\OneDrive - Walmart Inc\Code Puppy\Supplier"
python data_server.py
```

**Expected output:**
```
🚀 Data Server running on http://localhost:3001
📊 Try: http://localhost:3001/api/suppliers
🔌 Endpoints available at http://localhost:3001/
```

✅ **Leave this running!**

---

### **Terminal 2 - Backend API (Port 3000):**

```bash
cd "C:\Users\n0l08i7\OneDrive - Walmart Inc\Code Puppy\Supplier"
python backend_server.py
```

**Expected output:**
```
🚀 Backend API Server running on http://localhost:3000
📡 Connected to Data Server at http://localhost:3001
📚 Try: curl -H 'X-User-ID: user1' http://localhost:3000/api/user/profile
```

✅ **Leave this running!**

---

### **Terminal 3 - Frontend (Port 8000):**

```bash
cd "C:\Users\n0l08i7\OneDrive - Walmart Inc\Code Puppy\Supplier"
python -m http.server 8000
```

**Expected output:**
```
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
```

✅ **Leave this running!**

---

### **Browser - Open Dashboard:**

```
http://localhost:8000/dashboard_with_api.html
```

✅ **Your dashboard is live!**

---

## ✨ What You'll See

✅ Page loads instantly  
✅ 150 suppliers displayed  
✅ Toolbar shows "☁️ API Connected"  
✅ Filters work  
✅ Search works  
✅ Pagination works  
✅ No errors in console  

---

## 🔍 Verify Everything Works

### **Check Data Server:**
```
http://localhost:3001/health
```

Should return:
```json
{"status": "ok", "service": "data-server", "port": 3001}
```

### **Check Backend API:**
```
http://localhost:3000/health
```

Should return:
```json
{"status": "ok", "service": "backend-api", "port": 3000, "dataServer": "connected"}
```

### **Get Suppliers:**
```
http://localhost:3000/api/suppliers
```

Should return JSON with 150 suppliers

### **Get Dashboard:**
```
http://localhost:8000/dashboard_with_api.html
```

Should display the supplier dashboard with data

---

## 🛑 Troubleshooting

### **"ModuleNotFoundError: No module named 'flask'"**

Run this in the same terminal:
```bash
set HTTP_PROXY=http://sysproxy.wal-mart.com:8080
set HTTPS_PROXY=http://sysproxy.wal-mart.com:8080
uv pip install --index-url https://pypi.ci.artifacts.walmart.com/artifactory/api/pypi/external-pypi/simple --allow-insecure-host pypi.ci.artifacts.walmart.com flask flask-cors requests
```

Then try running the server again.

### **"Address already in use" Error**

A port is already occupied. Find and kill the process:
```bash
netstat -ano | findstr :3000
netstat -ano | findstr :3001
netstat -ano | findstr :8000

# Kill the process (replace PID):
taskkill /PID <PID> /F
```

### **Connection Refused**

Make sure all 3 servers are running in separate terminals:
1. Terminal 1: `python data_server.py`
2. Terminal 2: `python backend_server.py`
3. Terminal 3: `python -m http.server 8000`

### **Dashboard Shows "API Error"**

Check:
1. Is Terminal 2 (backend) running?
2. Check browser console (F12) for error messages
3. Verify `http://localhost:3000/health` returns data
4. Check firewall isn't blocking ports

---

## 📊 Architecture

```
Browser (http://localhost:8000)
        ↓
   dashboard_with_api.html
        ↓
Fetch: http://localhost:3000/api/suppliers
        ↓
Backend API (data_server.py - port 3000)
        ↓
Fetch: http://localhost:3001/api/suppliers
        ↓
Data Server (backend_server.py - port 3001)
        ↓
Returns 150 suppliers (JSON)
        ↓
Backend passes to frontend
        ↓
Dashboard displays ✅
```

---

## 💡 Why This Works

Instead of Node.js servers (which couldn't be installed), we're using:

- **Flask** (Python web framework) = Express replacement
- **Flask-CORS** (Cross-origin support) = CORS middleware
- **Requests** (HTTP library) = Fetch replacement

They do exactly the same thing:
- ✅ Listen on ports 3000 & 3001
- ✅ Serve REST API endpoints
- ✅ Return JSON data
- ✅ Support CORS
- ✅ Handle requests & responses

---

## ⏱️ Daily Usage

Every time you want to use the dashboard:

**Terminal 1:**
```bash
cd "C:\Users\n0l08i7\OneDrive - Walmart Inc\Code Puppy\Supplier"
python data_server.py
```

**Terminal 2:**
```bash
cd "C:\Users\n0l08i7\OneDrive - Walmart Inc\Code Puppy\Supplier"
python backend_server.py
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

## ✅ Success Checklist

- [ ] All 3 terminals running servers
- [ ] Data Server shows "running on http://localhost:3001"
- [ ] Backend shows "running on http://localhost:3000"
- [ ] Frontend shows "Serving HTTP on 0.0.0.0 port 8000"
- [ ] Dashboard loads at http://localhost:8000/dashboard_with_api.html
- [ ] Toolbar shows "☁️ API Connected"
- [ ] Suppliers display on page
- [ ] Filters work
- [ ] Search works
- [ ] No red errors in browser console (F12)

---

## 🎉 Done!

Your dashboard is now running with Python servers!

**No Node.js installation needed!** 🚀