# 🔧 FIX: "localhost refused to connect"

## 🎯 Root Cause Identified

❌ **Node.js is NOT installed on your system!**

This is why the servers won't start and localhost refuses to connect.

---

## ✅ System Status

```
✅ Python 3.13.5 - INSTALLED
❌ Node.js - NOT INSTALLED (this is the problem!)
❌ npm - NOT INSTALLED (requires Node.js)
```

---

## 🚀 Solution: Install Node.js

### **Option 1: Download from nodejs.org (Recommended)**

1. Go to: https://nodejs.org/
2. Download **LTS version** (currently v20.x or v22.x)
3. Run the installer
4. Follow default installation steps
5. **Restart your computer** (important!)
6. Verify installation:
   ```bash
   node --version
   npm --version
   ```

---

### **Option 2: Use Winget (Windows Package Manager)**

```bash
winget install OpenJS.NodeJS
```

Then restart your computer and verify:
```bash
node --version
npm --version
```

---

### **Option 3: Use Chocolatey**

```bash
choco install nodejs
```

Then restart and verify:
```bash
node --version
npm --version
```

---

## ✅ After Installing Node.js

### **Step 1: Install Backend Dependencies**

```bash
cd "C:\Users\n0l08i7\OneDrive - Walmart Inc\Code Puppy\Supplier\data-server"
npm install

cd "C:\Users\n0l08i7\OneDrive - Walmart Inc\Code Puppy\Supplier\backend"
npm install
```

---

### **Step 2: Start the Servers**

**Terminal 1 (Data Server):**
```bash
cd "C:\Users\n0l08i7\OneDrive - Walmart Inc\Code Puppy\Supplier\data-server"
node server.js
```

**Terminal 2 (Backend API):**
```bash
cd "C:\Users\n0l08i7\OneDrive - Walmart Inc\Code Puppy\Supplier\backend"
node server.js
```

**Terminal 3 (Frontend):**
```bash
cd "C:\Users\n0l08i7\OneDrive - Walmart Inc\Code Puppy\Supplier"
python -m http.server 8000
```

---

### **Step 3: Open Dashboard**

```
http://localhost:8000/dashboard_with_api.html
```

✅ **Should work now!**

---

## 🛡️ Firewall Check

If still getting "refused to connect" after installing Node.js:

1. Check Windows Firewall:
   - Settings → Privacy & Security → Windows Firewall
   - Allow Python and Node.js through firewall

2. Or temporarily disable firewall to test:
   - Settings → Update & Security → Windows Security
   - Firewall & network protection → Disable (temporarily)

---

## 🎯 Quick Verification After Install

```bash
# Check versions
node --version   # Should show v20.x.x or higher
npm --version    # Should show 10.x.x or higher

# Check npm works
npm list -g npm

# Test running a simple server
python -m http.server 9000
# Should show: Serving HTTP on 0.0.0.0 port 9000
```

---

## ⏱️ Timeline

```
Download Node.js (5 min)
        ↓
Install Node.js (2 min)
        ↓
Restart computer (1 min)
        ↓
npm install in both folders (2 min)
        ↓
Start 3 servers (1 min)
        ↓
Dashboard works! ✅ (total: ~11 minutes)
```

---

## 📝 Why Node.js is Required

Your system has 2 backend servers written in Node.js:

1. **Data Server** (data-server/server.js)
   - Generates 150 suppliers
   - Serves via REST API
   - Requires Node.js to run

2. **Backend API** (backend/server.js)  
   - Proxies to data server
   - Manages user data
   - Requires Node.js to run

Without Node.js, these can't start, so localhost refuses to connect.

---

## ✅ After Node.js Installation

You'll be able to:

✅ Run the backend servers  
✅ Connect to localhost:3000 and :3001  
✅ Frontend fetches data from backend  
✅ Dashboard displays 150 suppliers  
✅ All filters and search work  

---

## 🎯 Next Steps

1. **Install Node.js** (use option 1 or 2 above)
2. **Restart computer**
3. **Verify installation:**
   ```bash
   node --version
   npm --version
   ```
4. **Follow RUN_LIVE_DASHBOARD.md** to start servers
5. **Open dashboard** in browser
6. **Done!** ✨

---

## 🆘 Still Not Working?

After installing Node.js:

1. **Restart your computer** (critical!)
2. **Open a NEW terminal** (not the old one)
3. **Try running a server again**
4. **Check for error messages**
5. **Share the error message** if still stuck

---

**Node.js is the missing piece!** Install it and everything will work. 🚀