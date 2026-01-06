#!/usr/bin/env python3
"""
🚀 Walmart Supplier Portal - Python Backend with PostgreSQL Database
Connects to internet-based PostgreSQL database
Returns 1000+ real suppliers from database
"""

import os
import sys
import json
from datetime import datetime
import logging

try:
    from flask import Flask, jsonify, request, send_from_directory
    from flask_cors import CORS
    from flask_sqlalchemy import SQLAlchemy
except ImportError as e:
    print(f"ERROR: Missing Flask dependency: {e}")
    print("Run: pip install Flask Flask-CORS Flask-SQLAlchemy psycopg2-binary")
    sys.exit(1)

print("\n" + "="*70)
print("🚀 WALMART SUPPLIER PORTAL - PYTHON + DATABASE BACKEND")
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

# ==================== DATABASE CONFIGURATION ====================

# Get database URL from environment
DATABASE_URL = os.environ.get('DATABASE_URL')

if DATABASE_URL:
    # Use PostgreSQL if available
    print("[1/3] Configuring PostgreSQL database...")
    # Fix psycopg2 deprecation warning
    if DATABASE_URL.startswith('postgres://'):
        DATABASE_URL = DATABASE_URL.replace('postgres://', 'postgresql://', 1)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy(app)
    
    # Define Supplier model
    class Supplier(db.Model):
        __tablename__ = 'suppliers'
        
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(255), nullable=False, unique=True)
        category = db.Column(db.String(100), nullable=False)
        rating = db.Column(db.Float, default=4.0)
        reviews = db.Column(db.Integer, default=0)
        location = db.Column(db.String(100), nullable=False)
        region = db.Column(db.String(50), nullable=False)
        products = db.Column(db.JSON, default=[])
        certifications = db.Column(db.JSON, default=[])
        leadTime = db.Column(db.String(50), default="2-4 weeks")
        responseTime = db.Column(db.String(50), default="24 hours")
        stockLevel = db.Column(db.Integer, default=1000)
        inStock = db.Column(db.Boolean, default=True)
        minimumOrder = db.Column(db.Integer, default=100)
        walmartVerified = db.Column(db.Boolean, default=False)
        size = db.Column(db.String(50), default="Medium (51-500)")
        priceRange = db.Column(db.String(50), default="Standard ($$)")
        aiScore = db.Column(db.Integer, default=75)
        lastUpdated = db.Column(db.DateTime, default=datetime.utcnow)
        lastStockCheck = db.Column(db.DateTime, default=datetime.utcnow)
        
        def to_dict(self):
            return {
                'id': self.id,
                'name': self.name,
                'category': self.category,
                'rating': self.rating,
                'reviews': self.reviews,
                'location': self.location,
                'region': self.region,
                'products': self.products,
                'certifications': self.certifications,
                'leadTime': self.leadTime,
                'responseTime': self.responseTime,
                'stockLevel': self.stockLevel,
                'inStock': self.inStock,
                'minimumOrder': self.minimumOrder,
                'walmartVerified': self.walmartVerified,
                'size': self.size,
                'priceRange': self.priceRange,
                'aiScore': self.aiScore,
                'lastUpdated': self.lastUpdated.isoformat() if self.lastUpdated else None,
                'lastStockCheck': self.lastStockCheck.isoformat() if self.lastStockCheck else None,
            }
    
    # Initialize database
    with app.app_context():
        db.create_all()
        print("✅ Database tables created")
    
    HAS_DATABASE = True
else:
    print("⚠️  No DATABASE_URL provided")
    print("   Set DATABASE_URL environment variable to use PostgreSQL")
    print("   Using demo mode (150 suppliers)")
    HAS_DATABASE = False
    db = None

# ==================== DEMO DATA (fallback) ====================

def generate_demo_suppliers():
    """Generate 150 demo suppliers for testing"""
    suppliers = []
    categories = ['Concrete & Cement', 'Steel & Metal', 'Lumber & Wood', 'Roofing Materials', 'Insulation']
    regions = ['Northeast', 'Southeast', 'Midwest', 'Southwest', 'West']
    
    for i in range(1, 151):
        suppliers.append({
            'id': i,
            'name': f'Supplier {i}',
            'category': categories[i % len(categories)],
            'rating': 3.5 + (i % 20) * 0.1,
            'reviews': 50 + (i % 200),
            'location': f'City {i}',
            'region': regions[i % len(regions)],
            'products': ['Product 1', 'Product 2'],
            'certifications': ['ISO 9001'],
            'leadTime': '2-4 weeks',
            'responseTime': '24 hours',
            'stockLevel': 500 + (i % 1000),
            'inStock': True,
            'minimumOrder': 100,
            'walmartVerified': i % 3 == 0,
            'size': 'Medium (51-500)',
            'priceRange': 'Standard ($$)',
            'aiScore': 70 + (i % 30),
            'lastUpdated': datetime.utcnow().isoformat(),
            'lastStockCheck': datetime.utcnow().isoformat(),
        })
    
    return suppliers

# ==================== API ENDPOINTS ====================

@app.route('/')
def serve_dashboard():
    """Serve the dashboard HTML"""
    return send_from_directory('.', 'dashboard_with_api.html')

@app.route('/api/suppliers', methods=['GET'])
def get_suppliers():
    """Get all suppliers from database or demo data"""
    try:
        if HAS_DATABASE:
            # Load from PostgreSQL database
            page = request.args.get('page', 1, type=int)
            limit = request.args.get('limit', 1000, type=int)
            skip = (page - 1) * limit
            
            suppliers = Supplier.query.offset(skip).limit(limit).all()
            supplier_count = Supplier.query.count()
            
            return jsonify({
                'success': True,
                'data': [s.to_dict() for s in suppliers],
                'total': supplier_count,
                'page': page,
                'limit': limit,
                'source': 'database'
            })
        else:
            # Use demo data
            suppliers = generate_demo_suppliers()
            return jsonify({
                'success': True,
                'data': suppliers,
                'total': len(suppliers),
                'source': 'demo'
            })
    except Exception as e:
        print(f"ERROR in /api/suppliers: {e}")
        return jsonify({
            'success': False,
            'error': str(e),
            'data': generate_demo_suppliers()  # Fallback
        }), 500

@app.route('/api/suppliers/<int:supplier_id>', methods=['GET'])
def get_supplier(supplier_id):
    """Get a specific supplier"""
    try:
        if HAS_DATABASE:
            supplier = Supplier.query.get(supplier_id)
            if supplier:
                return jsonify({
                    'success': True,
                    'data': supplier.to_dict()
                })
            else:
                return jsonify({
                    'success': False,
                    'error': 'Supplier not found'
                }), 404
        else:
            suppliers = generate_demo_suppliers()
            for s in suppliers:
                if s['id'] == supplier_id:
                    return jsonify({'success': True, 'data': s})
            return jsonify({'success': False, 'error': 'Not found'}), 404
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/suppliers/search', methods=['POST'])
def search_suppliers():
    """Search suppliers by query"""
    try:
        query = request.json.get('q', '').lower()
        
        if HAS_DATABASE:
            suppliers = Supplier.query.filter(
                (Supplier.name.ilike(f'%{query}%')) |
                (Supplier.category.ilike(f'%{query}%')) |
                (Supplier.location.ilike(f'%{query}%'))
            ).limit(100).all()
            
            return jsonify({
                'success': True,
                'results': [s.to_dict() for s in suppliers]
            })
        else:
            suppliers = generate_demo_suppliers()
            results = [s for s in suppliers if query in s['name'].lower() or query in s['category'].lower()]
            return jsonify({'success': True, 'results': results})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    try:
        if HAS_DATABASE:
            # Test database connection
            db.session.execute('SELECT 1')
            db_status = 'connected'
            supplier_count = Supplier.query.count()
        else:
            db_status = 'demo_mode'
            supplier_count = 150
        
        return jsonify({
            'status': 'healthy',
            'database': db_status,
            'suppliers': supplier_count,
            'timestamp': datetime.utcnow().isoformat()
        })
    except Exception as e:
        return jsonify({
            'status': 'unhealthy',
            'error': str(e)
        }), 500

# ==================== ERROR HANDLERS ====================

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({
        'success': False,
        'error': 'Endpoint not found'
    }), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return jsonify({
        'success': False,
        'error': 'Internal server error'
    }), 500

# ==================== MAIN ====================

if __name__ == '__main__':
    print(f"\n📊 API Endpoint:     http://{HOST}:{PORT}/api/suppliers")
    print(f"🏥 Health Check:     http://{HOST}:{PORT}/health")
    print(f"📱 Dashboard:        http://{HOST}:{PORT}/")
    print(f"\n✅ Server starting on {HOST}:{PORT}...\n")
    
    # Start server
    app.run(host=HOST, port=PORT, debug=(NODE_ENV == 'development'))
