#!/usr/bin/env python3
"""
🚀 Walmart Supplier Portal - Python Backend
Combined unified server for all endpoints
Runs on Render, Heroku, or any Python hosting
"""

from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import os
import json
from datetime import datetime
import random

app = Flask(__name__, static_folder='.', static_url_path='')
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Configuration
PORT = int(os.environ.get('PORT', 3000))
HOST = os.environ.get('HOST', '0.0.0.0')
NODE_ENV = os.environ.get('NODE_ENV', 'development')

# ==================== DATA GENERATION ====================

class SeededRandom:
    """Seeded random number generator for consistent data"""
    def __init__(self, seed):
        self.seed = seed
        self.random = random.Random(seed)
    
    def next(self):
        return self.random.random()

def generate_supplier_data(count=150):
    """Generate supplier data with seeded randomness"""
    rng = SeededRandom(1962)  # Walmart's founding year
    
    categories = [
        'Construction Materials', 'Electronics', 'Textiles',
        'Food & Beverage', 'Packaging', 'Hardware',
        'Furniture', 'Home & Garden'
    ]
    
    suppliers_list = [
        {'name': 'TechCorp Industries', 'city': 'San Francisco', 'state': 'CA'},
        {'name': 'Global Materials Ltd', 'city': 'Dallas', 'state': 'TX'},
        {'name': 'Premium Textiles Inc', 'city': 'Charlotte', 'state': 'NC'},
        {'name': 'Apex Manufacturing', 'city': 'Chicago', 'state': 'IL'},
        {'name': 'Summit Supply Chain', 'city': 'Denver', 'state': 'CO'},
        {'name': 'EliteGoods Distributors', 'city': 'Houston', 'state': 'TX'},
        {'name': 'Quantum Logistics', 'city': 'Atlanta', 'state': 'GA'},
        {'name': 'ValueMax Enterprises', 'city': 'Phoenix', 'state': 'AZ'},
        {'name': 'Pinnacle Products', 'city': 'Miami', 'state': 'FL'},
        {'name': 'Zenith Trading', 'city': 'Seattle', 'state': 'WA'},
        {'name': 'ProSource Distribution', 'city': 'Boston', 'state': 'MA'},
        {'name': 'Nexus Components', 'city': 'Austin', 'state': 'TX'},
        {'name': 'Stellar Manufacturing', 'city': 'Portland', 'state': 'OR'},
        {'name': 'Titan Industrial Group', 'city': 'Cleveland', 'state': 'OH'},
        {'name': 'Horizon Supplies', 'city': 'Minneapolis', 'state': 'MN'}
    ]
    
    products = [
        'Steel Beams', 'Concrete Mix', 'Lumber & Wood', 'Industrial Fasteners',
        'Electrical Components', 'HVAC Systems', 'Safety Equipment', 'Tools & Hardware',
        'Packaging Materials', 'Raw Textiles', 'Electronic Modules', 'Chemical Compounds',
        'Industrial Oils', 'Sensors & Controls', 'Custom Components'
    ]
    
    certifications = ['ISO 9001', 'ISO 14001', 'OSHA Certified']
    
    suppliers_data = []
    
    for i in range(1, count + 1):
        supplier = suppliers_list[int(rng.next() * len(suppliers_list))]
        category = categories[int(rng.next() * len(categories))]
        
        # Generate products for this supplier
        product_count = int(rng.next() * 5) + 1
        selected_products = [
            products[int(rng.next() * len(products))] for _ in range(product_count)
        ]
        
        # Generate certifications
        num_certs = int(rng.next() * 3) + 1
        selected_certs = [
            certifications[int(rng.next() * len(certifications))] for _ in range(num_certs)
        ]
        
        suppliers_data.append({
            'id': f'SUP-{str(i).zfill(4)}',
            'name': supplier['name'],
            'category': category,
            'location': f"{supplier['city']}, {supplier['state']}",
            'city': supplier['city'],
            'state': supplier['state'],
            'rating': round(rng.next() * 1.5 + 3.5, 2),
            'reviews': int(rng.next() * 1000) + 50,
            'description': f'Leading provider of {category.lower()} with proven expertise',
            'products': selected_products,
            'inStock': rng.next() > 0.2,
            'stockLevel': int(rng.next() * 10000),
            'minimumOrder': int(rng.next() * 100) + 10,
            'leadTime': f"{int(rng.next() * 14) + 1}-{int(rng.next() * 7) + 8} days",
            'certifications': selected_certs,
            'responseTime': f"{int(rng.next() * 12) + 1} hours",
            'contractTerms': f"{int(rng.next() * 24) + 12} months",
            'verified': rng.next() > 0.1,
            'lastUpdated': datetime.now().isoformat(),
            'walmartVerified': rng.next() > 0.3
        })
    
    return suppliers_data

# Generate suppliers on startup
SUPPLIERS_CACHE = generate_supplier_data(150)
LAST_UPDATE_TIME = datetime.now().isoformat()

print(f"✅ Generated {len(SUPPLIERS_CACHE)} suppliers")

# ==================== FRONTEND ROUTES ====================

@app.route('/', methods=['GET'])
def serve_dashboard():
    """Serve the main dashboard"""
    return send_from_directory('.', 'dashboard_with_api.html')

@app.route('/<path:filename>', methods=['GET'])
def serve_static(filename):
    """Serve static files (HTML, CSS, JS)"""
    try:
        return send_from_directory('.', filename)
    except:
        return jsonify({'error': 'File not found'}), 404

# ==================== DATA API ENDPOINTS ====================

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'ok',
        'service': 'walmart-supplier-portal',
        'environment': NODE_ENV,
        'port': PORT,
        'uptime': 'running',
        'suppliers': len(SUPPLIERS_CACHE)
    })

@app.route('/api/suppliers', methods=['GET'])
def get_suppliers():
    """Get all suppliers with optional pagination"""
    skip = request.args.get('skip', 0, type=int)
    limit = request.args.get('limit', 150, type=int)
    
    paginated = SUPPLIERS_CACHE[skip:skip + limit]
    
    return jsonify({
        'success': True,
        'data': paginated,
        'count': len(paginated),
        'total': len(SUPPLIERS_CACHE),
        'timestamp': LAST_UPDATE_TIME
    })

@app.route('/api/suppliers/<supplier_id>', methods=['GET'])
def get_supplier(supplier_id):
    """Get a specific supplier"""
    supplier = next((s for s in SUPPLIERS_CACHE if s['id'] == supplier_id), None)
    if not supplier:
        return jsonify({'success': False, 'error': 'Supplier not found'}), 404
    return jsonify({'success': True, 'data': supplier})

@app.route('/api/suppliers/search', methods=['POST'])
def search_suppliers():
    """Search suppliers by query and filters"""
    data = request.get_json() or {}
    query = data.get('query', '').lower()
    filters = data.get('filters', {})
    
    results = SUPPLIERS_CACHE
    
    if query:
        results = [s for s in results if 
                   query in s['name'].lower() or 
                   query in s['category'].lower() or
                   query in s['location'].lower()]
    
    if filters.get('category'):
        results = [s for s in results if s['category'] == filters['category']]
    
    if filters.get('inStock') is not None:
        results = [s for s in results if s['inStock'] == filters['inStock']]
    
    return jsonify({
        'success': True,
        'data': results,
        'count': len(results)
    })

@app.route('/api/suppliers/category/<category>', methods=['GET'])
def get_by_category(category):
    """Get suppliers by category"""
    filtered = [s for s in SUPPLIERS_CACHE if s['category'].lower() == category.lower()]
    return jsonify({
        'success': True,
        'data': filtered,
        'count': len(filtered)
    })

@app.route('/api/stats', methods=['GET'])
def get_stats():
    """Get supplier statistics"""
    stats = {
        'totalSuppliers': len(SUPPLIERS_CACHE),
        'inStock': sum(1 for s in SUPPLIERS_CACHE if s['inStock']),
        'verified': sum(1 for s in SUPPLIERS_CACHE if s['verified']),
        'averageRating': round(
            sum(s['rating'] for s in SUPPLIERS_CACHE) / len(SUPPLIERS_CACHE), 2
        ),
        'categories': len(set(s['category'] for s in SUPPLIERS_CACHE)),
        'lastUpdated': LAST_UPDATE_TIME
    }
    return jsonify({'success': True, 'data': stats})

@app.route('/api/dashboard/suppliers', methods=['GET'])
def get_dashboard_suppliers():
    """Get suppliers for dashboard (with pagination)"""
    skip = request.args.get('skip', 0, type=int)
    limit = request.args.get('limit', 20, type=int)
    
    paginated = SUPPLIERS_CACHE[skip:skip + limit]
    return jsonify({
        'success': True,
        'data': paginated,
        'count': len(paginated),
        'total': len(SUPPLIERS_CACHE)
    })

@app.route('/api/dashboard/stats', methods=['GET'])
def get_dashboard_stats():
    """Get dashboard statistics"""
    stats = {
        'totalSuppliers': len(SUPPLIERS_CACHE),
        'inStock': sum(1 for s in SUPPLIERS_CACHE if s['inStock']),
        'verified': sum(1 for s in SUPPLIERS_CACHE if s['verified']),
        'averageRating': round(
            sum(s['rating'] for s in SUPPLIERS_CACHE) / len(SUPPLIERS_CACHE), 2
        )
    }
    return jsonify({'success': True, 'data': stats})

# ==================== USER ENDPOINTS ====================

@app.route('/api/user/profile', methods=['GET'])
def get_user_profile():
    """Get user profile"""
    user_id = request.headers.get('X-User-ID', 'anonymous')
    return jsonify({
        'success': True,
        'user': {
            'id': user_id,
            'name': 'Walmart Procurement Officer',
            'email': f'{user_id}@walmart.com',
            'role': 'procurement_officer',
            'department': 'Supplier Relations'
        }
    })

@app.route('/api/user/favorites', methods=['GET'])
def get_favorites():
    """Get user favorites"""
    return jsonify({'success': True, 'favorites': []})

@app.route('/api/user/notes', methods=['GET'])
def get_notes():
    """Get user notes"""
    return jsonify({'success': True, 'notes': {}})

@app.route('/api/user/inbox', methods=['GET'])
def get_inbox():
    """Get user inbox"""
    return jsonify({'success': True, 'inbox': []})

# ==================== ERROR HANDLERS ====================

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({'error': 'Endpoint not found', 'status': 404}), 404

@app.errorhandler(500)
def server_error(error):
    """Handle 500 errors"""
    return jsonify({'error': 'Internal server error', 'status': 500}), 500

# ==================== STARTUP ====================

if __name__ == '__main__':
    print(f"\n{'='*60}")
    print("🚀 Walmart Supplier Portal - Python Backend")
    print(f"{'='*60}")
    print(f"Environment: {NODE_ENV}")
    print(f"Host: {HOST}")
    print(f"Port: {PORT}")
    print(f"Suppliers: {len(SUPPLIERS_CACHE)}")
    print(f"URL: http://{HOST}:{PORT}")
    print(f"\n📊 Endpoints:")
    print(f"  GET  /                    - Dashboard")
    print(f"  GET  /health              - Health check")
    print(f"  GET  /api/suppliers       - All suppliers")
    print(f"  GET  /api/stats           - Statistics")
    print(f"  POST /api/suppliers/search - Search suppliers")
    print(f"  GET  /api/user/profile    - User profile")
    print(f"\n{'='*60}\n")
    
    try:
        app.run(host=HOST, port=PORT, debug=(NODE_ENV == 'development'))
    except Exception as e:
        print(f"❌ Error starting server: {e}")
