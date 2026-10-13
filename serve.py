#!/usr/bin/env python3
"""
High-performance Threading HTTP Server & Unified API Engine for Agrolink Africa.
Serves:
  - Corporate Marketing Website from /agribusiness.cmsmasters.studio/main/
  - Integrated AI Platform Cockpit from /platform/
  - Built-in Mock API Engine for offline simulation (/api/*)
"""

import http.server
import json
import os
import sys
import urllib.parse

PORT = 8080
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class AgrolinkHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_GET(self):
        clean_path = self.path.split('?')[0].split('#')[0]
        
        # Root redirects to corporate website
        if clean_path in ('', '/', '/index.html'):
            self.send_response(302)
            self.send_header('Location', '/agribusiness.cmsmasters.studio/main/index.html')
            self.end_headers()
            return

        # /platform redirect to trailing slash
        if clean_path == '/platform':
            self.send_response(301)
            self.send_header('Location', '/platform/')
            self.end_headers()
            return

        # Health check
        if clean_path == '/api/health':
            self.send_json({
                "status": "healthy",
                "service": "Agrolink Africa Unified API & Analytics Engine",
                "version": "2.4.0"
            })
            return

        return super().do_GET()

    def do_POST(self):
        clean_path = self.path.split('?')[0].split('#')[0]
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length) if content_length > 0 else b'{}'
        
        try:
            body = json.loads(post_data.decode('utf-8'))
        except Exception:
            body = {}

        # 1. Demand Prediction API
        if clean_path == '/api/demand-prediction':
            crop = body.get('crop', 'French Beans (Export Grade)')
            county = body.get('county', 'Nakuru (Rift Valley)')
            acreage = float(body.get('acreage', 5) or 5)

            # Heuristic pricing
            prices = {
                'french beans': 118,
                'beans': 118,
                'avocado': 160,
                'potato': 62,
                'maize': 46,
                'tomato': 85
            }
            crop_lower = crop.lower()
            base_price = 110
            for k, v in prices.items():
                if k in crop_lower:
                    base_price = v
                    break

            gross_rev = int(acreage * 3800 * base_price)
            
            self.send_json({
                "success": True,
                "data": {
                    "demandScore": 92,
                    "projectedPricePerKg": base_price,
                    "priceConfidenceRange": f"KES {base_price - 12} - {base_price + 15} / kg",
                    "expectedGrossRevenueKES": gross_rev,
                    "optimalPlantingDate": "October 20 – November 10",
                    "projectedHarvestWindow": "December 22 – January 18",
                    "marketDemandLevel": "HIGH_DEMAND",
                    "spoilageRiskRating": "MODERATE",
                    "keyBuyers": ["Vegpro Kenya Ltd", "AAA Growers", "Twiga Fresh Supply Hub"],
                    "strategicAdvisory": f"Favorable regional price index detected for {crop} in {county}. Contract off-take commitments are high; schedule cold-chain logistics 48h before harvest.",
                    "climateVolatilityRisk": "Low to moderate precipitation variability; ensure drip irrigation backup.",
                    "intercroppingSynergy": "Companion border legumes or marigolds to reduce pest pressure."
                }
            })
            return

        # 2. Weather Analysis API
        if clean_path == '/api/weather-analysis':
            county = body.get('county', 'Nakuru (Rift Valley)')
            is_highland = any(h in county.lower() for h in ['meru', 'nyandarua', 'kiambu'])
            
            self.send_json({
                "success": True,
                "data": {
                    "locationName": county,
                    "latitude": -0.3031 if not is_highland else 0.0463,
                    "longitude": 36.0800 if not is_highland else 37.6559,
                    "temperatureC": 19.4 if is_highland else 22.8,
                    "humidityPercent": 74 if is_highland else 62,
                    "precipitationForecastMm": 3.8 if is_highland else 0.5,
                    "weatherCondition": "Mild & Clear" if not is_highland else "Partly Cloudy & Humid",
                    "frostRisk": "NONE",
                    "blightRiskScore": 55 if is_highland else 28,
                    "windSpeedKmH": 10.5,
                    "soilMoistureIndex": "OPTIMAL",
                    "agronomicAdvisory": "Optimal agronomic conditions for field work, fertilization, and solar fleet transport.",
                    "isGpsDetected": False
                }
            })
            return

        # 3. Crop Diagnosis API
        if clean_path == '/api/crop-diagnosis':
            crop = body.get('cropType', 'Horticulture')
            self.send_json({
                "success": True,
                "data": {
                    "condition": "Mild Foliar Nitrogen Deficiency or Early Blight",
                    "confidenceScore": 89,
                    "primarySymptoms": "Localized chlorosis on lower leaves with minor necrotic margins.",
                    "recommendedRemedies": [
                        "Foliar calcium-ammonium-nitrate (CAN) spray within 48 hours",
                        "Maintain root-zone drip fertigation to avoid waterlogging",
                        "Scout underside of leaves for early fungal spore activity"
                    ],
                    "urgencyLevel": "MODERATE",
                    "estimatedRecoveryDays": 10
                }
            })
            return

        # 4. USSD Simulation API
        if clean_path == '/api/ussd-simulate':
            user_text = str(body.get('userText', '1')).strip()
            session_stage = body.get('sessionStage', 'MAIN_MENU')

            if user_text == '1':
                screen = "AGROLINK SOKO (KES/kg):\nPotatoes: 60\nFrench Beans: 118\nAvocados: 155\nMaize: 46\n0. Back"
            elif user_text == '2':
                screen = "Sajili Mavuno:\nIngiza: [Zao] [Gunia] [Tarehe]\nMfano: Mahindi 40 15/11\n0. Back"
            elif user_text == '3':
                screen = "Hali ya Hewa & Wadudu:\nNakuru: Mvua kidogo wiki hii. Maji asubuhi kabla ya saa 3.\n0. Back"
            elif user_text == '4':
                screen = "AgriWallet M-Pesa:\nSalio: KES 48,250\nMalipo yanayosubiriwa: KES 112,000\n0. Back"
            else:
                screen = "AGROLINK SMART MENU (*384*254#)\n1. Bei za Soko\n2. Sajili Mavuno\n3. Onyo la Hali ya Hewa\n4. M-Pesa Wallet"

            self.send_json({
                "success": True,
                "data": {
                    "screenText": screen,
                    "nextStage": "SUB_MENU" if user_text in ('1','2','3','4') else "MAIN_MENU",
                    "isTerminal": False
                }
            })
            return

        # 5. Gemini Agronomy Chatbot API
        if clean_path == '/api/gemini/chat':
            lang = body.get('language', 'en')
            role = body.get('userRole', 'farmer')
            location = body.get('location', 'Nakuru')
            messages = body.get('messages', [])
            last_msg = messages[-1].get('content', '') if messages else ''
            
            if lang == 'sw':
                reply = (
                    f"Habari! Karibu Agrolink Africa, eneo la {location}. "
                    f"Kuhusu swali lako, hali ya hewa ya sasa inafaa kwa kilimo cha kisasa. "
                    f"Unyevu wa udongo uko katika kiwango bora (62%), na bei ya soko kwa mazao ya bustani imeongezeka hadi KES 118 kwa kilo. "
                    f"Tunapendekeza uthibitishe makadirio ya uvunaji saa 48 mapema ili magari yenye jokofu yakufikie shambani kwa wakati. "
                    f"Je, unahitaji ushauri zaidi kuhusu mbolea, viuatilifu au uunganishaji wa soko la moja kwa moja?"
                )
            else:
                reply = (
                    f"Hello from Agrolink Africa ({location} Cluster)! "
                    f"Regarding your query: current regional soil moisture is optimal at 62%, with daytime temperatures averaging 22°C. "
                    f"Market wholesale demand is currently strong at KES 118/kg for grade-A produce, with verified off-takers actively bidding. "
                    f"We recommend scheduling refrigerated collection 48 hours prior to harvest to minimize field heat spoilage. "
                    f"How can our agronomic AI assist your operations today?"
                )

            self.send_json({
                "success": True,
                "reply": reply,
                "role": role,
                "language": lang
            })
            return

        # Unknown POST
        self.send_response(404)
        self.end_headers()

    def send_json(self, data, status_code=200):
        response_bytes = json.dumps(data).encode('utf-8')
        self.send_response(status_code)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(response_bytes)))
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(response_bytes)

    def guess_type(self, path):
        ctype = super().guess_type(path)
        if path.endswith('.webp'):
            return 'image/webp'
        elif path.endswith('.svg'):
            return 'image/svg+xml'
        elif path.endswith('.woff2'):
            return 'font/woff2'
        elif path.endswith('.woff'):
            return 'font/woff'
        elif path.endswith('.ttf'):
            return 'font/ttf'
        elif path.endswith('.js') or path.endswith('.mjs'):
            return 'application/javascript'
        elif path.endswith('.css'):
            return 'text/css'
        return ctype

def run_server():
    os.chdir(DIRECTORY)
    server_address = ('0.0.0.0', PORT)
    httpd = http.server.ThreadingHTTPServer(server_address, AgrolinkHTTPRequestHandler)
    print("=" * 65)
    print("  AGROLINK AFRICA UNIFIED ENTERPRISE SERVER")
    print("=" * 65)
    print(f"  Corporate Website:   http://localhost:{PORT}/")
    print(f"  AI Platform Cockpit: http://localhost:{PORT}/platform/")
    print(f"  API Health Check:    http://localhost:{PORT}/api/health")
    print("=" * 65)
    sys.stdout.flush()
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server...")

if __name__ == '__main__':
    run_server()
