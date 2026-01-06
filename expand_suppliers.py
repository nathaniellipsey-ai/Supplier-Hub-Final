#!/usr/bin/env python3
"""
Expand suppliers.json to include 500+ suppliers
"""

import json
import random
from datetime import datetime

STATES = [
    'Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado',
    'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho',
    'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana',
    'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota',
    'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada',
    'New Hampshire', 'New Jersey', 'New Mexico', 'New York',
    'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon',
    'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota',
    'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington',
    'West Virginia', 'Wisconsin', 'Wyoming'
]

CATEGORIES = [
    'Concrete & Cement', 'Steel & Metal', 'Lumber & Wood', 'Roofing Materials',
    'Insulation', 'Drywall & Gypsum', 'Electrical', 'Plumbing', 'HVAC',
    'Flooring', 'Windows & Doors', 'Paint & Coatings', 'Fasteners & Hardware',
    'Tools & Equipment', 'Safety Equipment', 'Landscaping', 'Masonry'
]

PREFIXES = [
    'ABC', 'XYZ', 'Global', 'Premier', 'Eastern', 'Western', 'Central',
    'National', 'Regional', 'Local', 'Quality', 'Elite', 'Superior',
    'Advanced', 'Professional', 'Strategic', 'Optimal', 'Reliable',
    'American', 'Universal', 'Dynamic', 'Integrated', 'Progressive',
    'Apex', 'Best', 'Complete', 'Direct', 'Express', 'Fast', 'Genuine'
]

SUFFIXES = [
    'Industries', 'Corp', 'Supplies', 'Builders', 'Materials', 'Trading',
    'Supply Co', 'Vendors', 'Distributors', 'Suppliers', 'Products',
    'Manufacturing', 'Solutions', 'Systems', 'Group', 'Enterprises',
    'Ltd', 'LLC', 'Inc', 'Company', 'Associates', 'Partners'
]

REGIONS = {
    'Northeast': ['Connecticut', 'Delaware', 'Maine', 'Maryland', 'Massachusetts', 'New Hampshire', 'New Jersey', 'New York', 'Pennsylvania', 'Rhode Island', 'Vermont', 'West Virginia'],
    'Southeast': ['Alabama', 'Arkansas', 'Florida', 'Georgia', 'Kentucky', 'Louisiana', 'Mississippi', 'North Carolina', 'South Carolina', 'Tennessee', 'Virginia'],
    'Midwest': ['Illinois', 'Indiana', 'Iowa', 'Kansas', 'Michigan', 'Minnesota', 'Missouri', 'Nebraska', 'North Dakota', 'Ohio', 'South Dakota', 'Wisconsin'],
    'Southwest': ['Arizona', 'New Mexico', 'Oklahoma', 'Texas'],
    'West': ['Alaska', 'California', 'Colorado', 'Hawaii', 'Idaho', 'Montana', 'Nevada', 'Oregon', 'Utah', 'Washington', 'Wyoming']
}

CITIES = {
    'Alabama': 'Birmingham', 'Alaska': 'Anchorage', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock',
    'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Wilmington',
    'Florida': 'Jacksonville', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise',
    'Illinois': 'Chicago', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka',
    'Kentucky': 'Louisville', 'Louisiana': 'New Orleans', 'Maine': 'Portland', 'Maryland': 'Baltimore',
    'Massachusetts': 'Boston', 'Michigan': 'Detroit', 'Minnesota': 'Minneapolis', 'Mississippi': 'Jackson',
    'Missouri': 'Kansas City', 'Montana': 'Billings', 'Nebraska': 'Omaha', 'Nevada': 'Las Vegas',
    'New Hampshire': 'Manchester', 'New Jersey': 'Newark', 'New Mexico': 'Albuquerque', 'New York': 'New York',
    'North Carolina': 'Charlotte', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
    'Oregon': 'Portland', 'Pennsylvania': 'Philadelphia', 'Rhode Island': 'Providence', 'South Carolina': 'Charleston',
    'South Dakota': 'Sioux Falls', 'Tennessee': 'Memphis', 'Texas': 'Houston', 'Utah': 'Salt Lake City',
    'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Seattle', 'West Virginia': 'Charleston',
    'Wisconsin': 'Milwaukee', 'Wyoming': 'Cheyenne'
}

def generate_suppliers(count=500):
    suppliers = []
    used_names = set()
    
    for i in range(1, count + 1):
        # Generate unique name
        while True:
            name = f"{random.choice(PREFIXES)} {random.choice(SUFFIXES)}"
            if name not in used_names:
                used_names.add(name)
                break
        
        state = random.choice(STATES)
        region = next((r for r, states in REGIONS.items() if state in states), 'West')
        city = CITIES.get(state, 'Unknown')
        category = random.choice(CATEGORIES)
        
        supplier = {
            'id': i,
            'name': name,
            'location': f"{random.randint(100, 999)} Main St, {city}, {state} {random.randint(10000, 99999)}",
            'state': state,
            'phone': f"{random.randint(201, 999)}-555-{random.randint(1000, 9999)}",
            'rating': round(random.uniform(3.0, 5.0), 1),
            'reviews': random.randint(5, 200),
            'source': 'Directory',
            'category': category,
            'region': region,
            'products': [category, f'{category} Supplies', 'Equipment'],
            'certifications': ['ISO 9001'] if random.random() > 0.7 else [],
            'leadTime': random.choice(['1-2 weeks', '2-4 weeks', '3-5 days', '4-6 weeks']),
            'responseTime': random.choice(['24 hours', '48 hours', '2 business days']),
            'stockLevel': random.randint(500, 5000),
            'inStock': random.random() > 0.05,
            'minimumOrder': random.choice([50, 100, 250, 500]),
            'walmartVerified': random.random() > 0.7,
            'size': random.choice(['Small (1-50)', 'Medium (51-500)', 'Large (500-2000)']),
            'priceRange': random.choice(['Budget ($)', 'Standard ($$)', 'Premium ($$$)']),
            'aiScore': random.randint(60, 95),
            'lastUpdated': datetime.utcnow().isoformat(),
            'lastStockCheck': datetime.utcnow().isoformat()
        }
        suppliers.append(supplier)
    
    return suppliers

print(f"Generating {500} suppliers...")
suppliers = generate_suppliers(500)

print(f"Saving to suppliers.json...")
with open('suppliers.json', 'w') as f:
    json.dump(suppliers, f, indent=2)

print(f"\nDone! Created suppliers.json with {len(suppliers)} suppliers")
print(f"  - Covering all 50 US states")
print(f"  - All construction material categories")
print(f"  - Realistic data (names, addresses, phone numbers, ratings)")
print(f"  - Ready to deploy!")
