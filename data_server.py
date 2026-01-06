#!/usr/bin/env python3
"""
Data Server - Provides supplier data via REST API
Port: 3001
"""

from flask import Flask, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

# Generate 150 sample suppliers
suppliers = []
for i in range(1, 151):
    suppliers.append({
        "id": i,
        "name": f"Supplier {i}",
        "category": ["Construction Materials", "Electronics", "Textiles", "Food & Beverage", "Packaging"][i % 5],
        "location": ["San Francisco, CA", "Dallas, TX", "Charlotte, NC", "Chicago, IL", "Denver, CO"][i % 5],
        "rating": round(3.0 + (i % 20) / 10, 1),
        "reviews": 50 + (i * 3) % 500,
        "walmartVerified": i % 3 != 0,
        "products": [f"Product {i}-1", f"Product {i}-2", f"Product {i}-3"],
        "price": f"${100 * (i % 10)}",
        "leadTime": f"{5 + (i % 20)} days",
        "city": ["San Francisco", "Dallas", "Charlotte", "Chicago", "Denver"][i % 5],
        "state": ["CA", "TX", "NC", "IL", "CO"][i % 5]
    })

@app.route('/api/suppliers', methods=['GET'])
def get_suppliers():
    """Get all suppliers"""
    return jsonify({
        "success": True,
        "data": suppliers,
        "count": len(suppliers),
        "timestamp": "2025-12-12T13:51:21.212265"
    })

@app.route('/api/suppliers/<int:supplier_id>', methods=['GET'])
def get_supplier(supplier_id):
    """Get specific supplier"""
    supplier = next((s for s in suppliers if s['id'] == supplier_id), None)
    if supplier:
        return jsonify({"success": True, "data": supplier})
    return jsonify({"success": False, "error": "Supplier not found"}), 404

@app.route('/api/stats', methods=['GET'])
def get_stats():
    """Get statistics"""
    return jsonify({
        "success": True,
        "data": {
            "totalSuppliers": len(suppliers),
            "averageRating": round(sum(s['rating'] for s in suppliers) / len(suppliers), 2),
            "verifiedCount": sum(1 for s in suppliers if s['walmartVerified']),
            "categories": len(set(s['category'] for s in suppliers))
        }
    })

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({"status": "ok", "service": "data-server", "port": 3001})

@app.route('/', methods=['GET'])
def index():
    """Root endpoint"""
    return jsonify({
        "service": "Data Server",
        "port": 3001,
        "endpoints": {
            "/api/suppliers": "Get all suppliers",
            "/api/suppliers/<id>": "Get specific supplier",
            "/api/stats": "Get statistics",
            "/health": "Health check"
        }
    })

if __name__ == '__main__':
    print("🚀 Data Server running on http://localhost:3001")
    print("📊 Try: http://localhost:3001/api/suppliers")
    print("🔌 Endpoints available at http://localhost:3001/")
    try:
        app.run(host='0.0.0.0', port=3001, debug=False, use_reloader=False)
    except Exception as e:
        print(f"❌ Error starting server: {e}")