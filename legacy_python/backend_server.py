#!/usr/bin/env python3
"""
Backend API Server - Proxies requests to Data Server
Port: 3000
"""

from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
import time

app = Flask(__name__)
CORS(app)

DATA_SERVER_URL = 'http://localhost:3001'
MAX_RETRIES = 3
RETRY_DELAY = 0.5

def fetch_from_data_server(endpoint):
    """Fetch data from data server with retries"""
    for attempt in range(MAX_RETRIES):
        try:
            response = requests.get(f'{DATA_SERVER_URL}{endpoint}', timeout=5)
            return response.json()
        except requests.exceptions.ConnectionError:
            if attempt < MAX_RETRIES - 1:
                time.sleep(RETRY_DELAY)
            else:
                return {"error": f"Cannot connect to data server at {DATA_SERVER_URL}"}
        except Exception as e:
            return {"error": str(e)}

@app.route('/api/suppliers', methods=['GET'])
def get_suppliers():
    """Get all suppliers from data server"""
    result = fetch_from_data_server('/api/suppliers')
    if 'error' in result:
        return jsonify({"success": False, **result}), 503
    return jsonify(result)

@app.route('/api/suppliers/<int:supplier_id>', methods=['GET'])
def get_supplier(supplier_id):
    """Get specific supplier"""
    result = fetch_from_data_server(f'/api/suppliers/{supplier_id}')
    if 'error' in result:
        return jsonify({"success": False, **result}), 503
    return jsonify(result)

@app.route('/api/stats', methods=['GET'])
def get_stats():
    """Get statistics from data server"""
    result = fetch_from_data_server('/api/stats')
    if 'error' in result:
        return jsonify({"success": False, **result}), 503
    return jsonify(result)

@app.route('/api/user/profile', methods=['GET'])
def get_user_profile():
    """Get user profile"""
    user_id = request.headers.get('X-User-ID', 'anonymous')
    return jsonify({
        "success": True,
        "user": {
            "id": user_id,
            "name": "Test User",
            "email": f"{user_id}@example.com",
            "role": "procurement_officer"
        }
    })

@app.route('/api/user/favorites', methods=['GET'])
def get_favorites():
    """Get user favorites"""
    return jsonify({"success": True, "favorites": []})

@app.route('/api/user/notes', methods=['GET'])
def get_notes():
    """Get user notes"""
    return jsonify({"success": True, "notes": {}})

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    # Try to check if data server is up
    try:
        data_health = requests.get(f'{DATA_SERVER_URL}/health', timeout=2).json()
        data_status = "connected"
    except:
        data_status = "disconnected"
    
    return jsonify({
        "status": "ok",
        "service": "backend-api",
        "port": 3000,
        "dataServer": data_status
    })

@app.route('/', methods=['GET'])
def index():
    """Root endpoint"""
    return jsonify({
        "service": "Backend API Server",
        "port": 3000,
        "dataServer": DATA_SERVER_URL,
        "endpoints": {
            "/api/suppliers": "Get all suppliers",
            "/api/suppliers/<id>": "Get specific supplier",
            "/api/stats": "Get statistics",
            "/api/user/profile": "Get user profile",
            "/api/user/favorites": "Get user favorites",
            "/api/user/notes": "Get user notes",
            "/health": "Health check"
        }
    })

if __name__ == '__main__':
    print("🚀 Backend API Server running on http://localhost:3000")
    print(f"📡 Connected to Data Server at {DATA_SERVER_URL}")
    print("📚 Try: curl -H 'X-User-ID: user1' http://localhost:3000/api/user/profile")
    try:
        app.run(host='0.0.0.0', port=3000, debug=False, use_reloader=False)
    except Exception as e:
        print(f"❌ Error starting server: {e}")