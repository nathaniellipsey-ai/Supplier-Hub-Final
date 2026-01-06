# ⚡ PYTHON QUICK START - 1 MINUTE

## 🎯 Copy & Paste These Commands

### **Terminal 1:**
```bash
cd "C:\Users\n0l08i7\OneDrive - Walmart Inc\Code Puppy\Supplier" && python data_server.py
```

### **Terminal 2:**
```bash
cd "C:\Users\n0l08i7\OneDrive - Walmart Inc\Code Puppy\Supplier" && python backend_server.py
```

### **Terminal 3:**
```bash
cd "C:\Users\n0l08i7\OneDrive - Walmart Inc\Code Puppy\Supplier" && python -m http.server 8000
```

### **Browser:**
```
http://localhost:8000/dashboard_with_api.html
```

✅ **Done! Dashboard is live!**

---

## ✨ What You'll See

✅ 150 suppliers displayed  
✅ Status shows "☁️ API Connected"  
✅ Filters work  
✅ Search works  

---

## 🆘 Not Working?

If you get "ModuleNotFoundError: No module named 'flask'":

```bash
set HTTP_PROXY=http://sysproxy.wal-mart.com:8080 && set HTTPS_PROXY=http://sysproxy.wal-mart.com:8080 && uv pip install --index-url https://pypi.ci.artifacts.walmart.com/artifactory/api/pypi/external-pypi/simple --allow-insecure-host pypi.ci.artifacts.walmart.com flask flask-cors requests
```

Then try again.

---

**That's it! Your dashboard is ready!** 🚀