# 🔴 URGENT FIX: Install Node.js NOW

## ⚠️ Problem

**"localhost refused to connect" because Node.js is NOT installed!**

---

## ✅ Quick Fix (5 minutes)

### **OPTION A: Download & Install**

1. Go to: **https://nodejs.org/**
2. Click: **"Download LTS" (green button)**
3. Run the `.msi` file
4. Click "Next" → "Next" → "Install"
5. **RESTART YOUR COMPUTER** (important!)
6. Done!

---

### **OPTION B: Use Windows Package Manager**

```bash
winget install OpenJS.NodeJS
```

Then restart computer.

---

## 🔍 Verify Installation

```bash
node --version
npm --version
```

Both should show version numbers (no errors).

---

## 🚀 After Installing

1. Open 3 terminals
2. Run servers (see RUN_LIVE_DASHBOARD.md)
3. Open browser to http://localhost:8000/dashboard_with_api.html
4. ✅ Done!

---

**INSTALL NODE.JS FIRST - Everything else depends on it!**