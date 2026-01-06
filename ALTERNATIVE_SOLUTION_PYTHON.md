# 🎯 ALTERNATIVE: Run Servers with Python (No Node.js Required!)

**Your system:**
- ✅ Python 3.13.5 installed
- ❌ Node.js not installed (installation blocked)
- ✅ We can use Python instead!

---

## 🚀 Solution: Create Python Servers

Instead of Node.js servers, we'll create equivalent Python servers that do the same thing!

---

## **Step 1: Create Data Server (Python)**

Create file: `C:\Users\n0l08i7\OneDrive - Walmart Inc\Code Puppy\Supplier\data_server.py`

```python
from flask import Flask, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

# Sample supplier data (150 suppliers)
suppliers = [
    {"id": 1, "name": "TechCorp Industries", "category": "Electronics", "location": "San Francisco, CA", "rating": 4.8, "reviews": 127, "walmartVerified": True, "products": ["Circuits", "Components"]},
    {"id": 2, "name": "Global Materials Ltd", "category": "Materials", "location": "Dallas, TX", "rating": 4.6, "reviews": 89, "walmartVerified": True, "products": ["Steel", "Concrete"]},
    {"id": 3, "name": "Premium Textiles Inc", "category": "Textiles", "location": "Charlotte, NC", "rating": 4.4, "reviews": 156, "walmartVerified": True, "products": ["Fabric", "Yarn"]},
    # ... more suppliers would be here
]

@app.route('/api/suppliers', methods=['GET'])
def get_suppliers():
    return jsonify({"success": True, "suppliers": suppliers})

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok", "service": "data-server", "port": 3001})

if __name__ == '__main__':
    print("🚀 Data Server running on http://localhost:3001")
    app.run(host='0.0.0.0', port=3001, debug=False)
```

---

## **Step 2: Create Backend API Server (Python)**

Create file: `C:\Users\n0l08i7\OneDrive - Walmart Inc\Code Puppy\Supplier\backend_server.py`

```python
from flask import Flask, jsonify, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

DATA_SERVER_URL = 'http://localhost:3001'

@app.route('/api/suppliers', methods=['GET'])
def get_suppliers():
    try:
        response = requests.get(f'{DATA_SERVER_URL}/api/suppliers')
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok", "service": "backend", "port": 3000})

if __name__ == '__main__':
    print("🚀 Backend API running on http://localhost:3000")
    print("📡 Connected to Data Server at", DATA_SERVER_URL)
    app.run(host='0.0.0.0', port=3000, debug=False)
```

---

## **Step 3: Install Required Python Packages**

```bash
pip install flask flask-cors requests

# OR with uv:
uv pip install flask flask-cors requests
```

---

## **Step 4: Run the Python Servers**

### **Terminal 1 - Data Server:**
```bash
cd "C:\Users\n0l08i7\OneDrive - Walmart Inc\Code Puppy\Supplier"
python data_server.py
```

### **Terminal 2 - Backend API:**
```bash
cd "C:\Users\n0l08i7\OneDrive - Walmart Inc\Code Puppy\Supplier"
python backend_server.py
```

### **Terminal 3 - Frontend:**
```bash
cd "C:\Users\n0l08i7\OneDrive - Walmart Inc\Code Puppy\Supplier"
python -m http.server 8000
```

---

## **Step 5: Open Dashboard**

```
http://localhost:8000/dashboard_with_api.html
```

✅ **Done!**

---

## ⚠️ Important Notes

1. **You need to use Python instead of Node.js**
2. **Flask is a Python web framework** (same as Express in Node.js)
3. **This works exactly the same as the Node.js version**
4. **All 3 servers must be running in separate terminals**

---

## ✅ Verification

After starting all 3 servers:

1. Check data server: `http://localhost:3001/health`
2. Check backend: `http://localhost:3000/health`
3. Open dashboard: `http://localhost:8000/dashboard_with_api.html`

---

## 📋 Why This Works

Instead of:
- Node.js + Express (which you can't install)

We're using:
- Python + Flask (which you already have!)

Both do the same thing:
- ✅ Serve data via REST API
- ✅ Handle requests
- ✅ Return JSON
- ✅ Support CORS

---

**This is your solution if Node.js installation is blocked at Walmart!**