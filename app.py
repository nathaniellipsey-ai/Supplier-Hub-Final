#!/usr/bin/env python3
"""
Walmart Supplier Portal - Python Backend
Dynamically generates 1000+ realistic suppliers
No database needed - pure in-memory generation
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
print("WALMART SUPPLIER PORTAL - DYNAMIC SUPPLIER GENERATOR")
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

# ==================== SUPPLIER GENERATION ====================

print("[1/3] Setting up supplier data...")

# Company name parts
COMPANY_PREFIXES = [
    'ABC', 'XYZ', 'Global', 'Premier', 'Eastern', 'Western', 'Central',
    'National', 'Regional', 'Local', 'Quality', 'Elite', 'Superior',
    'Advanced', 'Professional', 'Strategic', 'Optimal', 'Reliable',
    'American', 'Universal', 'Dynamic', 'Integrated', 'Progressive'
]

COMPANY_SUFFIXES = [
    'Industries', 'Corp', 'Supplies', 'Builders', 'Materials', 'Trading',
    'Supply Co', 'Vendors', 'Distributors', 'Suppliers', 'Products',
    'Manufacturing', 'Solutions', 'Systems', 'Group', 'Enterprises',
    'Ltd', 'LLC', 'Inc', 'Company', 'Associates'
]

CATEGORIES = [
    'Concrete & Cement', 'Steel & Metal', 'Lumber & Wood', 'Roofing Materials',
    'Insulation', 'Drywall & Gypsum', 'Electrical', 'Plumbing', 'HVAC',
    'Flooring', 'Windows & Doors', 'Paint & Coatings', 'Fasteners & Hardware',
    'Tools & Equipment', 'Safety Equipment', 'Landscaping', 'Masonry',
    'Temporary Construction', 'Personal Protective Equipment', 'Material Handling',
    'Scaffolding & Ladders', 'Lighting Fixtures', 'Plumbing Fixtures',
    'Appliances', 'Cabinets & Storage', 'Hardware & Tools', 'Outdoor Equipment'
]

LOCATIONS = [
    'New York', 'Los Angeles', 'Chicago', 'Dallas', 'Houston', 'Phoenix',
    'Atlanta', 'Miami', 'Seattle', 'Denver', 'Boston', 'San Francisco',
    'Detroit', 'Minneapolis', 'Nashville', 'Austin', 'Memphis', 'Portland',
    'Las Vegas', 'Washington DC', 'Philadelphia', 'Orlando', 'Charlotte',
    'San Diego', 'Tampa', 'Montreal', 'Toronto', 'Vancouver', 'Mexico City',
    'Salt Lake City', 'Kansas City', 'Milwaukee', 'Albuquerque', 'Indianapolis'
]

REGIONS = ['Northeast', 'Southeast', 'Midwest', 'Southwest', 'West', 'National']

PRODUCTS_BY_CATEGORY = {
    'Concrete & Cement': ['Ready-Mix Concrete', 'Portland Cement', 'Concrete Blocks', 'Concrete Admixtures', 'Concrete Sealers'],
    'Steel & Metal': ['Structural Steel', 'Rebar', 'Steel Beams', 'Metal Studs', 'Steel Plate'],
    'Lumber & Wood': ['Dimensional Lumber', 'Plywood', 'OSB Panels', 'Engineered Wood', 'Laminated Veneer Lumber'],
    'Roofing Materials': ['Asphalt Shingles', 'Metal Roofing', 'TPO Membrane', 'Slate Tiles', 'Wood Shakes'],
    'Insulation': ['Fiberglass Batts', 'Spray Foam', 'Rigid Foam Board', 'Cellulose', 'Mineral Wool'],
    'Drywall & Gypsum': ['Standard Drywall', 'Fire-Rated Drywall', 'Ceiling Tiles', 'Moisture-Resistant Drywall'],
    'Electrical': ['Wire & Cable', 'Conduit', 'LED Fixtures', 'Switches & Outlets', 'Circuit Breakers'],
    'Plumbing': ['PVC Pipe', 'Copper Pipe', 'Valves & Fittings', 'Water Heaters', 'Pumps'],
    'HVAC': ['Air Handling Units', 'Ductwork', 'Thermostats', 'Air Filters', 'Refrigerant'],
    'Flooring': ['Vinyl Flooring', 'Ceramic Tile', 'Hardwood', 'Laminate', 'Carpet'],
    'Windows & Doors': ['Vinyl Windows', 'Steel Doors', 'Fiberglass Doors', 'Garage Doors', 'Skylights'],
    'Paint & Coatings': ['Interior Paint', 'Exterior Paint', 'Primers', 'Epoxy Coatings', 'Stains'],
    'Fasteners & Hardware': ['Screws', 'Nails', 'Bolts & Anchors', 'Brackets', 'Hinges'],
    'Tools & Equipment': ['Power Tools', 'Hand Tools', 'Generators', 'Air Compressors', 'Ladders'],
    'Safety Equipment': ['Hard Hats', 'Safety Glasses', 'Work Gloves', 'Steel Toe Boots', 'Reflective Vests'],
    'Landscaping': ['Mulch', 'Topsoil', 'Gravel', 'Landscape Fabric', 'Plants'],
    'Masonry': ['Brick', 'Concrete Block', 'Mortar', 'Stone Veneer', 'Flagstone'],
    'Temporary Construction': ['Temporary Walls', 'Construction Fencing', 'Dust Barriers', 'Temporary Flooring'],
    'Personal Protective Equipment': ['Respirators', 'Dust Masks', 'Gloves', 'Safety Vests', 'Eye Protection'],
    'Material Handling': ['Pallet Racks', 'Conveyor Systems', 'Hoists', 'Dock Levelers', 'Forklifts'],
    'Scaffolding & Ladders': ['Frame Scaffolding', 'Extension Ladders', 'Step Ladders', 'Mobile Scaffolding'],
    'Lighting Fixtures': ['LED Downlights', 'Pendant Lights', 'Track Lighting', 'Wall Sconces', 'Chandeliers'],
    'Plumbing Fixtures': ['Toilets', 'Sinks', 'Faucets', 'Shower Heads', 'Bathtubs'],
    'Appliances': ['Refrigerators', 'Ovens', 'Dishwashers', 'Washers', 'Dryers'],
    'Cabinets & Storage': ['Kitchen Cabinets', 'Bathroom Vanities', 'Storage Shelves', 'Wall Cabinets'],
    'Hardware & Tools': ['Screwdrivers', 'Wrenches', 'Saws', 'Drills', 'Hammers'],
    'Outdoor Equipment': ['Mowers', 'Trimmers', 'Pressure Washers', 'Chainsaws']
}

CERTIFICATIONS = [
    'ISO 9001', 'LEED', 'MBE', 'WBE', 'OSHA Certified', 'Energy Star Partner',
    'ISO 14001', 'UL Certified', 'CSA Certified', 'RoHS Compliant'
]

LEAD_TIMES = ['2-4 weeks', '1-2 weeks', '4-6 weeks', '1-2 months', '2-3 months', '3-5 days', '1 week']
RESPONSE_TIMES = ['24 hours', '48 hours', '2 business days', '3 business days', '1 week']
SIZES = ['Small (1-50)', 'Medium (51-500)', 'Large (500-2000)', 'Enterprise (2000+)']
PRICE_RANGES = ['Budget ($)', 'Standard ($$)', 'Premium ($$$)', 'Enterprise ($$$$)']

def generate_suppliers(count=1000):
    """
    Generate realistic supplier data
    Returns list of supplier dictionaries
    """
    suppliers = []
    used_names = set()
    
    for i in range(1, count + 1):
        # Generate unique company name
        while True:
            company_name = f"{random.choice(COMPANY_PREFIXES)} {random.choice(COMPANY_SUFFIXES)} #{i}"
            if company_name not in used_names:
                used_names.add(company_name)
                break
        
        category = random.choice(CATEGORIES)
        
        # Get products for this category
        products = PRODUCTS_BY_CATEGORY.get(category, ['Product A', 'Product B'])
        selected_products = random.sample(products, min(random.randint(2, 4), len(products)))
        
        # Random certifications
        has_certs = random.random() > 0.6
        certs = random.sample(CERTIFICATIONS, random.randint(1, 3)) if has_certs else []
        
        supplier = {
            'id': i,
            'name': company_name,
            'category': category,
            'rating': round(random.uniform(3.0, 5.0), 1),
            'reviews': random.randint(5, 500),
            'location': random.choice(LOCATIONS),
            'region': random.choice(REGIONS),
            'products': selected_products,
            'certifications': certs,
            'leadTime': random.choice(LEAD_TIMES),
            'responseTime': random.choice(RESPONSE_TIMES),
            'stockLevel': random.randint(100, 5000),
            'inStock': random.random() > 0.05,  # 95% in stock
            'minimumOrder': random.choice([50, 100, 250, 500, 1000]),
            'walmartVerified': random.random() > 0.7,  # 30% verified
            'size': random.choice(SIZES),
            'priceRange': random.choice(PRICE_RANGES),
            'aiScore': random.randint(60, 95),
            'lastUpdated': datetime.utcnow().isoformat(),
            'lastStockCheck': datetime.utcnow().isoformat(),
        }
        suppliers.append(supplier)
    
    return suppliers

# Generate suppliers once at startup
print("[2/3] Generating 1000 suppliers...")
ALL_SUPPLIERS = generate_suppliers(1000)
print(f"      Generated {len(ALL_SUPPLIERS)} suppliers")

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
            'source': 'generated'
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
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
                'results': ALL_SUPPLIERS[:50]  # Return first 50 if no query
            })
        
        results = [s for s in ALL_SUPPLIERS if 
                   query in s['name'].lower() or 
                   query in s['category'].lower() or 
                   query in s['location'].lower() or
                   any(query in p.lower() for p in s['products'])]
        
        return jsonify({
            'success': True,
            'results': results[:100]  # Max 100 results
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
        
        # Filter by category
        if 'category' in filters and filters['category']:
            results = [s for s in results if s['category'] == filters['category']]
        
        # Filter by region
        if 'region' in filters and filters['region']:
            results = [s for s in results if s['region'] == filters['region']]
        
        # Filter by rating
        if 'minRating' in filters:
            min_rating = filters['minRating']
            results = [s for s in results if s['rating'] >= min_rating]
        
        # Filter by verified
        if 'walmartVerified' in filters and filters['walmartVerified']:
            results = [s for s in results if s['walmartVerified']]
        
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
        'suppliers_generated': len(ALL_SUPPLIERS),
        'timestamp': datetime.utcnow().isoformat(),
        'source': 'dynamic_generation'
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
    
    app.run(host=HOST, port=PORT, debug=(NODE_ENV == 'development'))
