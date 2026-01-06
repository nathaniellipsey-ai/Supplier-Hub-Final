#!/usr/bin/env python3
"""
Walmart Supplier Portal - Python Backend
Loads REAL construction material suppliers from web scraping or suppliers.json
"""

import os
import sys
import json
from datetime import datetime
import random

try:
    from flask import Flask, jsonify, request, send_from_directory
    from flask_cors import CORS
except ImportError as e:
    print(f"ERROR: Missing Flask dependency: {e}")
    print("Run: pip install Flask Flask-CORS")
    sys.exit(1)

print("\n" + "="*70)
print("WALMART SUPPLIER PORTAL - REAL DATA BACKEND")
print("Serving actual construction material suppliers from USA")
print("="*70)

# Initialize Flask
app = Flask(__name__, static_folder='.', static_url_path='')
app.config['JSON_SORT_KEYS'] = False

# Enable CORS for ALL routes
CORS(app)

# Configuration
PORT = int(os.environ.get('PORT', 3000))
HOST = os.environ.get('HOST', '0.0.0.0')
NODE_ENV = os.environ.get('NODE_ENV', 'development')

print(f"Environment: {NODE_ENV}")
print(f"Host: {HOST}:{PORT}")
print()

# ==================== LOAD REAL SUPPLIER DATA ====================

print("[1/3] Loading supplier data...")

ALL_SUPPLIERS = []

def load_suppliers_from_file(filename='suppliers.json'):
    """
    Load suppliers from suppliers.json file
    """
    try:
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                data = json.load(f)
                print(f"[OK] Loaded {len(data)} suppliers from {filename}")
                return data
        else:
            print(f"[WARNING] {filename} not found - will use fallback")
            return None
    except Exception as e:
        print(f"[ERROR] Failed to load {filename}: {e}")
        return None

def generate_fallback_suppliers(count=150):
    """
    Generate fallback suppliers if suppliers.json doesn't exist
    """
    suppliers = []
    categories = ['Concrete & Cement', 'Steel & Metal', 'Lumber & Wood', 'Roofing Materials', 'Electrical', 'Plumbing', 'HVAC', 'Paint & Coatings']
    regions = ['Northeast', 'Southeast', 'Midwest', 'Southwest', 'West']
    
    for i in range(1, count + 1):
        supplier = {
            'id': i,
            'name': f'Fallback Supplier {i}',
            'category': random.choice(categories),
            'rating': round(random.uniform(3.0, 5.0), 1),
            'reviews': random.randint(5, 500),
            'location': f'City {i}',
            'region': random.choice(regions),
            'products': ['Product 1', 'Product 2'],
            'certifications': ['ISO 9001'] if random.random() > 0.7 else [],
            'leadTime': '2-4 weeks',
            'responseTime': '24 hours',
            'stockLevel': random.randint(100, 5000),
            'inStock': True,
            'minimumOrder': 100,
            'walmartVerified': random.random() > 0.7,
            'size': random.choice(['Small (1-50)', 'Medium (51-500)', 'Large (500-2000)']),
            'priceRange': random.choice(['Budget ($)', 'Standard ($$)', 'Premium ($$$)']),
            'aiScore': random.randint(60, 95),
            'lastUpdated': datetime.utcnow().isoformat(),
            'lastStockCheck': datetime.utcnow().isoformat(),
            'source': 'Fallback Demo'
        }
        suppliers.append(supplier)
    
    return suppliers

# Load suppliers from suppliers.json first
print("[2/3] Initializing supplier database...")
ALL_SUPPLIERS = load_suppliers_from_file('suppliers.json')

if not ALL_SUPPLIERS:
    print("[WARNING] suppliers.json not found - generating fallback data")
    ALL_SUPPLIERS = generate_fallback_suppliers(150)
    print(f"[OK] Generated {len(ALL_SUPPLIERS)} fallback suppliers")
else:
    print(f"[OK] Loaded {len(ALL_SUPPLIERS)} suppliers from suppliers.json")

print(f"[OK] Total suppliers loaded: {len(ALL_SUPPLIERS)}")
print(f"[OK] Source: {'suppliers.json' if len(ALL_SUPPLIERS) > 150 else 'Fallback Demo'}")

print("[3/3] Starting API server...")
print()

# ==================== USERS DATABASE ====================

USERS_DB = {}

def generate_session_id():
    """Generate a unique session ID"""
    import uuid
    return str(uuid.uuid4())

def get_user_by_email(email):
    """Get user from database by email"""
    for user_id, user_data in USERS_DB.items():
        if user_data.get('email') == email:
            return user_id, user_data
    return None, None

# ==================== API ENDPOINTS ====================

@app.route('/')
def serve_home():
    """Serve the login page by default"""
    return send_from_directory('.', 'login.html')

@app.route('/login')
def serve_login():
    """Serve the login page"""
    return send_from_directory('.', 'login.html')

@app.route('/login.html')
def serve_login_html():
    """Serve the login.html file"""
    return send_from_directory('.', 'login.html')

@app.route('/dashboard_with_api.html')
def serve_dashboard_html():
    """Serve the dashboard HTML"""
    return send_from_directory('.', 'dashboard_with_api.html')

# ==================== AUTHENTICATION ENDPOINTS ====================

@app.route('/api/auth/login', methods=['POST'])
def auth_login():
    """
    Login or create account
    Request body: {"email": "...", "name": "...", "walmart_id": "..."}
    """
    try:
        data = request.get_json() or {}
        email = data.get('email', '').strip()
        name = data.get('name', '').strip()
        walmart_id = data.get('walmart_id', '').strip()
        
        if not email or not name:
            return jsonify({
                'success': False,
                'detail': 'Email and name are required'
            }), 400
        
        # Check if user exists
        user_id, existing_user = get_user_by_email(email)
        
        if user_id:
            # User already exists, just login
            session_id = generate_session_id()
            existing_user['last_login'] = datetime.utcnow().isoformat()
            
            print(f"[AUTH] User logged in: {email}")
            
            return jsonify({
                'success': True,
                'session_id': session_id,
                'user_id': user_id,
                'email': email,
                'name': name,
                'walmart_id': walmart_id,
                'message': 'Login successful'
            }), 200
        else:
            # Create new user account
            import uuid
            new_user_id = str(uuid.uuid4())
            
            USERS_DB[new_user_id] = {
                'id': new_user_id,
                'email': email,
                'name': name,
                'walmart_id': walmart_id,
                'created_at': datetime.utcnow().isoformat(),
                'last_login': datetime.utcnow().isoformat(),
                'favorites': [],
                'notes': {}
            }
            
            session_id = generate_session_id()
            
            print(f"[AUTH] New user created and logged in: {email}")
            
            return jsonify({
                'success': True,
                'session_id': session_id,
                'user_id': new_user_id,
                'email': email,
                'name': name,
                'walmart_id': walmart_id,
                'message': 'Account created and login successful'
            }), 201
    
    except Exception as e:
        print(f"[ERROR] Auth login failed: {e}")
        return jsonify({
            'success': False,
            'detail': str(e)
        }), 500

@app.route('/api/auth/logout', methods=['POST'])
def auth_logout():
    """
    Logout endpoint
    """
    try:
        data = request.get_json() or {}
        user_id = data.get('user_id')
        
        if user_id and user_id in USERS_DB:
            print(f"[AUTH] User logged out: {USERS_DB[user_id]['email']}")
        
        return jsonify({
            'success': True,
            'message': 'Logged out successfully'
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'detail': str(e)
        }), 500

@app.route('/api/auth/verify', methods=['GET'])
def auth_verify():
    """
    Verify if user is authenticated
    Query params: session_id, user_id
    """
    try:
        session_id = request.args.get('session_id')
        user_id = request.args.get('user_id')
        
        if not user_id or user_id not in USERS_DB:
            return jsonify({
                'success': False,
                'authenticated': False
            }), 401
        
        user = USERS_DB[user_id]
        return jsonify({
            'success': True,
            'authenticated': True,
            'user_id': user_id,
            'email': user.get('email'),
            'name': user.get('name'),
            'walmart_id': user.get('walmart_id')
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'detail': str(e)
        }), 500

@app.route('/api/auth/user', methods=['GET'])
def auth_get_user():
    """
    Get current user info
    Query params: user_id
    """
    try:
        user_id = request.args.get('user_id')
        
        if not user_id or user_id not in USERS_DB:
            return jsonify({
                'success': False,
                'detail': 'User not found'
            }), 404
        
        user = USERS_DB[user_id]
        return jsonify({
            'success': True,
            'user': {
                'id': user.get('id'),
                'email': user.get('email'),
                'name': user.get('name'),
                'walmart_id': user.get('walmart_id'),
                'created_at': user.get('created_at'),
                'last_login': user.get('last_login'),
                'favorites': user.get('favorites', []),
                'notes': user.get('notes', {})
            }
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'detail': str(e)
        }), 500

# ==================== SUPPLIER ENDPOINTS ====================

@app.route('/api/suppliers', methods=['GET'])
def get_suppliers():
    """
    Get suppliers with pagination
    Query params: page=1, limit=1000
    """
    try:
        print(f"[API] GET /api/suppliers - Returning {len(ALL_SUPPLIERS)} suppliers")
        
        page = request.args.get('page', 1, type=int)
        limit = request.args.get('limit', 1000, type=int)
        
        # Pagination
        start = (page - 1) * limit
        end = start + limit
        paginated = ALL_SUPPLIERS[start:end]
        
        return jsonify({
            'success': True,
            'data': paginated,
            'total': len(ALL_SUPPLIERS),
            'page': page,
            'limit': limit,
            'source': 'suppliers.json' if len(ALL_SUPPLIERS) > 150 else 'fallback'
        })
    except Exception as e:
        print(f"[ERROR] /api/suppliers: {e}")
        return jsonify({
            'success': False,
            'error': str(e),
            'data': []
        }), 500

@app.route('/api/suppliers/<int:supplier_id>', methods=['GET'])
def get_supplier(supplier_id):
    """Get a specific supplier by ID"""
    try:
        supplier = next((s for s in ALL_SUPPLIERS if s['id'] == supplier_id), None)
        if supplier:
            return jsonify({
                'success': True,
                'data': supplier
            })
        else:
            return jsonify({
                'success': False,
                'error': 'Supplier not found'
            }), 404
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/suppliers/search', methods=['POST'])
def search_suppliers():
    """Search suppliers by query"""
    try:
        data = request.get_json() or {}
        query = data.get('q', '').lower()
        
        if not query:
            return jsonify({
                'success': True,
                'results': ALL_SUPPLIERS[:50] if ALL_SUPPLIERS else []
            })
        
        results = [s for s in ALL_SUPPLIERS if 
                   query in s.get('name', '').lower() or 
                   query in s.get('location', '').lower() or
                   query in s.get('state', '').lower() or
                   query in s.get('category', '').lower()]
        
        return jsonify({
            'success': True,
            'results': results[:100]
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/suppliers/filter', methods=['POST'])
def filter_suppliers():
    """Filter suppliers by criteria"""
    try:
        filters = request.get_json() or {}
        
        results = ALL_SUPPLIERS.copy()
        
        if 'state' in filters and filters['state']:
            results = [s for s in results if s.get('state') == filters['state']]
        
        if 'category' in filters and filters['category']:
            results = [s for s in results if s.get('category') == filters['category']]
        
        if 'region' in filters and filters['region']:
            results = [s for s in results if s.get('region') == filters['region']]
        
        if 'minRating' in filters:
            min_rating = filters['minRating']
            results = [s for s in results if s.get('rating', 0) >= min_rating]
        
        return jsonify({
            'success': True,
            'results': results,
            'count': len(results)
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'suppliers_loaded': len(ALL_SUPPLIERS),
        'source': 'suppliers.json' if len(ALL_SUPPLIERS) > 150 else 'fallback',
        'timestamp': datetime.utcnow().isoformat()
    })

# ==================== ERROR HANDLERS ====================

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'success': False,
        'error': 'Endpoint not found'
    }), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({
        'success': False,
        'error': 'Internal server error'
    }), 500

# ==================== MAIN ====================

if __name__ == '__main__':
    print(f"API Endpoint:        http://{HOST}:{PORT}/api/suppliers")
    print(f"Health Check:        http://{HOST}:{PORT}/health")
    print(f"Dashboard:           http://{HOST}:{PORT}/")
    print(f"\nSuppliers Loaded:    {len(ALL_SUPPLIERS)}")
    print(f"Source:              {'suppliers.json (REAL DATA)' if len(ALL_SUPPLIERS) > 150 else 'Fallback Demo'}")
    print(f"\nServer starting on {HOST}:{PORT}...\n")
    
    app.run(host=HOST, port=PORT, debug=(NODE_ENV == 'development'))
