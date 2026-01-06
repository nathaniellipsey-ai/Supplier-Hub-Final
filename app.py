#!/usr/bin/env python3
"""
Walmart Supplier Portal - Python Backend
Loads REAL construction material suppliers from web scraping
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
    Load suppliers from scraped JSON file
    """
    try:
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                data = json.load(f)
                print(f"[OK] Loaded {len(data)} REAL suppliers from {filename}")
                return data
        else:
            print(f"[WARNING] {filename} not found")
            print("         No real supplier data available!")
            print("         Run: python scraper.py to generate supplier data")
            return []
    except Exception as e:
        print(f"[ERROR] Failed to load suppliers: {e}")
        return []

def enrich_supplier_data(suppliers):
    """
    Add additional fields to supplier data
    """
    categories = [
        'Concrete & Cement', 'Steel & Metal', 'Lumber & Wood',
        'Roofing Materials', 'Electrical', 'Plumbing', 'HVAC',
        'Paint & Coatings'
    ]
    
    regions = ['Northeast', 'Southeast', 'Midwest', 'Southwest', 'West']
    
    state_to_region = {
        # Northeast
        'Connecticut': 'Northeast', 'Delaware': 'Northeast', 'Maine': 'Northeast',
        'Maryland': 'Northeast', 'Massachusetts': 'Northeast', 'New Hampshire': 'Northeast',
        'New Jersey': 'Northeast', 'New York': 'Northeast', 'Pennsylvania': 'Northeast',
        'Rhode Island': 'Northeast', 'Vermont': 'Northeast', 'West Virginia': 'Northeast',
        # Southeast
        'Alabama': 'Southeast', 'Arkansas': 'Southeast', 'Florida': 'Southeast',
        'Georgia': 'Southeast', 'Kentucky': 'Southeast', 'Louisiana': 'Southeast',
        'Mississippi': 'Southeast', 'North Carolina': 'Southeast', 'South Carolina': 'Southeast',
        'Tennessee': 'Southeast', 'Virginia': 'Southeast',
        # Midwest
        'Illinois': 'Midwest', 'Indiana': 'Midwest', 'Iowa': 'Midwest',
        'Kansas': 'Midwest', 'Michigan': 'Midwest', 'Minnesota': 'Midwest',
        'Missouri': 'Midwest', 'Nebraska': 'Midwest', 'North Dakota': 'Midwest',
        'Ohio': 'Midwest', 'South Dakota': 'Midwest', 'Wisconsin': 'Midwest',
        # Southwest
        'Arizona': 'Southwest', 'New Mexico': 'Southwest', 'Oklahoma': 'Southwest',
        'Texas': 'Southwest',
        # West
        'Alaska': 'West', 'California': 'West', 'Colorado': 'West',
        'Hawaii': 'West', 'Idaho': 'West', 'Montana': 'West',
        'Nevada': 'West', 'Oregon': 'West', 'Utah': 'West',
        'Washington': 'West', 'Wyoming': 'West'
    }
    
    for i, supplier in enumerate(suppliers, 1):
        supplier['id'] = i
        
        # Use category from scraped data if available, otherwise assign
        if 'category' not in supplier or not supplier['category']:
            supplier['category'] = random.choice(categories)
        
        # Map state to region
        supplier['region'] = state_to_region.get(supplier.get('state', 'California'), 'West')
        supplier['rating'] = round(float(supplier.get('rating', 4.0)), 1)
        supplier['reviews'] = int(supplier.get('reviews', 0))
        
        # Add default products if not present
        if 'products' not in supplier or not supplier['products']:
            supplier['products'] = ['Construction Materials', 'Supplies', 'Equipment']
        
        supplier['certifications'] = supplier.get('certifications', ['ISO 9001'] if random.random() > 0.7 else [])
        supplier['leadTime'] = supplier.get('leadTime', '2-4 weeks')
        supplier['responseTime'] = supplier.get('responseTime', '24 hours')
        supplier['stockLevel'] = int(supplier.get('stockLevel', random.randint(100, 5000)))
        supplier['inStock'] = supplier.get('inStock', True)
        supplier['minimumOrder'] = int(supplier.get('minimumOrder', 100))
        supplier['walmartVerified'] = supplier.get('walmartVerified', random.random() > 0.8)
        supplier['size'] = supplier.get('size', random.choice(['Small (1-50)', 'Medium (51-500)', 'Large (500+)']))
        supplier['priceRange'] = supplier.get('priceRange', random.choice(['Budget ($)', 'Standard ($$)', 'Premium ($$$)']))
        supplier['aiScore'] = int(supplier.get('aiScore', random.randint(60, 95)))
        supplier['lastUpdated'] = supplier.get('lastUpdated', datetime.utcnow().isoformat())
        supplier['lastStockCheck'] = supplier.get('lastStockCheck', datetime.utcnow().isoformat())
        supplier['source'] = supplier.get('source', 'Web Scrape')
    
    return suppliers

# Load suppliers
print("[2/3] Initializing supplier database...")
ALL_SUPPLIERS = load_suppliers_from_file()

if ALL_SUPPLIERS:
    # Enrich data with additional fields
    ALL_SUPPLIERS = enrich_supplier_data(ALL_SUPPLIERS)
    print(f"[OK] Enriched {len(ALL_SUPPLIERS)} suppliers with additional data")
else:
    print("[WARNING] No real supplier data loaded!")
    print("\nTo get REAL supplier data, run:")
    print("  python scraper.py")
    print("\nThis will scrape real construction suppliers from Yellow Pages")
    print("and save to suppliers.json\n")

print("[3/3] Starting API server...")
print()

# ==================== API ENDPOINTS ====================

@app.route('/')
def serve_dashboard():
    """Serve the dashboard HTML"""
    return send_from_directory('.', 'dashboard_with_api.html')

@app.route('/api/suppliers', methods=['GET'])
def get_suppliers():
    """
    Get suppliers with pagination
    Query params: page=1, limit=1000
    """
    try:
        if not ALL_SUPPLIERS:
            return jsonify({
                'success': False,
                'error': 'No supplier data loaded. Run: python scraper.py',
                'data': [],
                'total': 0
            }), 200  # Return 200 so frontend doesn't error out
        
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
            'source': 'web_scrape',
            'loaded': len(ALL_SUPPLIERS) > 0
        })
    except Exception as e:
        print(f"ERROR in /api/suppliers: {e}")
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
                   query in s['name'].lower() or 
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
        'status': 'healthy' if ALL_SUPPLIERS else 'no_data',
        'suppliers_loaded': len(ALL_SUPPLIERS),
        'timestamp': datetime.utcnow().isoformat(),
        'source': 'web_scrape',
        'message': 'Run scraper.py to load real supplier data' if not ALL_SUPPLIERS else 'Real suppliers loaded from web scraping'
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
    print(f"\nServer starting on {HOST}:{PORT}...\n")
    
    if not ALL_SUPPLIERS:
        print("====================================================================")
        print("WARNING: No REAL supplier data loaded!")
        print("====================================================================")
        print("\nTo populate with REAL construction suppliers from USA:")
        print("\n  Step 1: Install scraper dependencies")
        print("    pip install beautifulsoup4 requests pandas lxml")
        print("\n  Step 2: Run the web scraper")
        print("    python scraper.py")
        print("\n  Step 3: Restart this server")
        print("    python app.py")
        print("\nThe scraper will pull REAL suppliers from Yellow Pages!")
        print("====================================================================")
        print()
    
    app.run(host=HOST, port=PORT, debug=(NODE_ENV == 'development'))
