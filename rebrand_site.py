#!/usr/bin/env python3
"""
Comprehensive rebranding script for Agrolink Africa website.
Rebrands the website at /home/pirate101/Downloads/agri to match
the project in /home/pirate101/Downloads/Presentation5.pptx.
Sticks strictly to the site's existing themes, fonts, and styles.
"""

import os
import re
from bs4 import BeautifulSoup

BASE_DIR = '/home/pirate101/Downloads/agri/agribusiness.cmsmasters.studio/main'

def rebrand_homepage():
    path = os.path.join(BASE_DIR, 'index.html')
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()

    # 1. Title & Meta
    html = re.sub(r'<title>.*?</title>', '<title>Agrolink Africa – AI-Powered Agricultural Ecosystem</title>', html, count=1)
    html = html.replace('<title></title>', '')
    html = re.sub(r'<meta property="og:title" content="[^"]*"', '<meta property="og:title" content="Agrolink Africa – AI-Powered Agricultural Ecosystem"', html)
    html = re.sub(r'<meta property="og:site_name" content="[^"]*"', '<meta property="og:site_name" content="Agrolink Africa"', html)
    html = re.sub(r'<meta name="description" content="[^"]*"', '<meta name="description" content="Agrolink Africa transforms agriculture from reactive to predictive—reducing waste, increasing farmer income, and connecting the entire ecosystem with AI."', html)

    # 2. Header & Logo Links
    html = html.replace('href="https://agribusiness.cmsmasters.studio/main"', 'href="index.html"')
    html = html.replace('alt="Main" title="Main"', 'alt="Agrolink Africa" title="Agrolink Africa"')
    html = html.replace('alt="Main"', 'alt="Agrolink Africa"')
    html = html.replace('>Get a Quote<', '>Join MVP Pilot<')

    # 3. Hero Section (7629215)
    # Background styling with presentation hero harvest photo
    if 'agrolink-hero-style' not in html:
        html = re.sub(
            r'(<section class="[^"]*elementor-element-7629215[^"]*"[^>]*>)',
            r'\1\n<style id="agrolink-hero-style">.elementor-element-7629215 { background: linear-gradient(rgba(35, 63, 46, 0.75), rgba(35, 63, 46, 0.88)), url("wp-content/uploads/sites/2/agrolink/image1.webp") center/cover no-repeat !important; }</style>',
            html
        )

    # Hero H1 & H2
    html = html.replace(
        'Innovating Agriculture for a Smarter Tomorrow',
        'Transforming African Agriculture from Reactive to Predictive'
    )
    html = html.replace(
        'Empowering agribusinesses with cutting-edge consulting in precision farming, automation, and sustainable solutions.',
        'Agrolink Africa connects the entire agricultural ecosystem with predictive AI—reducing waste, forecasting risks, and helping feed the future.'
    )

    # Hero Buttons
    html = html.replace('>Explore Solutions<', '>Explore Ecosystem<')
    html = html.replace('>Request a Quote<', '>Join MVP Pilot<')
    html = re.sub(
        r'href="about-us/index\.html"([^>]*>[^<]*<span class="elementor-widget-cmsmasters-button__text">Explore Ecosystem</span>)',
        r'href="#ecosystem"\1',
        html
    )

    # 4. Section 5 (The Core Problem & Our Vision)
    html = html.replace('Welcome to Agribusiness', 'THE PROBLEM & OUR VISION')
    html = html.replace(
        'We’re a forward-thinking agro consulting firm helping agribusinesses grow smarter. From drone mapping to data-driven crop management, we guide you through every step of your agri-innovation journey.',
        'Africa grows enough food. Yet millions still go hungry. 30–50% of harvest is lost before reaching the market. The problem isn’t production—it’s connection. Agriculture needs an intelligent ecosystem—not isolated solutions.'
    )

    # 3 Feature Boxes in Section 5
    html = re.sub(
        r'(<h4 class="elementor-widget-cmsmasters-featured-box__title[^"]*">\s*)Smart Farming Solutions(\s*</h4>)',
        r'\1Market Intelligence Gap\2',
        html
    )
    html = re.sub(
        r'(<h4 class="elementor-widget-cmsmasters-featured-box__title[^"]*">\s*)Precision Agriculture(\s*</h4>)',
        r'\1Disconnected Supply Chains\2',
        html
    )
    html = re.sub(
        r'(<h4 class="elementor-widget-cmsmasters-featured-box__title[^"]*">\s*)Sustainable Growth(\s*</h4>)',
        r'\1Undetected Climate & Disease Risks\2',
        html
    )

    # 5. Section 6 Quote
    html = html.replace(
        'From aerial imaging to data-driven decisions — we bring intelligence to every acre.',
        '“Agriculture needs an intelligent ecosystem—not isolated solutions. Agrolink collects data, predicts demand and risks, and connects farmers to buyers before decisions happen.”'
    )

    # 6. Section 7 (Impact Commitments)
    html = html.replace(
        'Through innovative tools and a deep respect for the land, we strive to:',
        'Target Impact by Year Three: Driving Africa’s Agricultural Transformation'
    )
    html = html.replace(
        'Promote sustainable agriculture that protects soil and ecosystems;',
        'Onboard 300,000 smallholder and commercial farmers onto the platform;'
    )
    html = html.replace(
        'Support large-scale efficiency with smart, scalable solutions;',
        'Deliver a 30% increase in farmer net income through direct market matching;'
    )
    html = html.replace(
        'Deliver measurable ROI through data and precision tools;',
        'Achieve a 40% reduction in post-harvest losses via synchronized logistics;'
    )
    html = html.replace(
        'Empower the next generation of agribusiness leaders.',
        'Train 50,000 farmers in digital, predictive, and climate-smart farming.'
    )
    html = html.replace('Ready to grow with us?', 'Partner With Agrolink Africa')
    html = html.replace('>more about us<', '>About Agrolink Africa<')
    html = html.replace('>Get in Touch<', '>Join the Pilot<')

    # 7. Section 8 (Services & Solutions -> The 6 Ecosystem Pillars)
    if 'id="ecosystem"' not in html:
        html = re.sub(
            r'(<section class="elementor-element elementor-element-6208fa3[^"]*")',
            r'\1 id="ecosystem"',
            html
        )
    html = html.replace('>Services & Solutions<', '>THE AGROLINK ECOSYSTEM<')
    html = html.replace('Smart Farming Starts Here', 'How It Works: Connected End-to-End')
    html = html.replace(
        'Discover our comprehensive range of agriculture solutions designed for performance, sustainability, and scale:',
        'Agrolink unites the entire value chain: AI collects data, predicts demand and risks, and sends smart recommendations to farmers while connecting them directly to buyers and transport systems:'
    )

    # Render static cards in Section 8 (05affc8) so it is 100% visible offline
    static_services_html = '''
    <div class="agrolink-services-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 24px; width: 100%; margin-top: 20px;">
        <!-- Service 1 -->
        <a href="services/precision-agriculture/index.html" style="text-decoration:none; color:inherit; display:block;">
            <div style="background:#FFFDF7; border: 1px solid #C4C0BC; border-radius: 12px; padding: 32px 28px; transition: transform 0.3s, box-shadow 0.3s; height: 100%; box-sizing: border-box;">
                <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 20px;">
                    <span style="font-family:'Archivo', sans-serif; font-size: 13px; font-weight: 700; letter-spacing: 2px; color: #6F6B66; text-transform: uppercase;">01 / PREDICTIVE AI</span>
                    <img src="wp-content/uploads/sites/2/2025/05/service-1.svg" width="48" height="48" alt="Demand Prediction" />
                </div>
                <h4 style="font-family:'Archivo', sans-serif; font-size: 22px; font-weight: 800; color: #28282C; margin: 0 0 12px 0;">Demand Prediction AI</h4>
                <p style="font-family:'Archivo', sans-serif; font-size: 15px; line-height: 1.6; color: #49433C; margin: 0 0 20px 0;">Advises farmers on optimal crop selection and planting schedules based on regional buyer demand, price forecasts, and climatic suitability.</p>
                <span style="font-family:'Archivo', sans-serif; font-size: 14px; font-weight: 700; color: #233F2E; display: inline-flex; align-items: center; gap: 6px;">Explore Feature &rarr;</span>
            </div>
        </a>
        <!-- Service 2 -->
        <a href="services/quality-control-grading/index.html" style="text-decoration:none; color:inherit; display:block;">
            <div style="background:#FFFDF7; border: 1px solid #C4C0BC; border-radius: 12px; padding: 32px 28px; transition: transform 0.3s, box-shadow 0.3s; height: 100%; box-sizing: border-box;">
                <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 20px;">
                    <span style="font-family:'Archivo', sans-serif; font-size: 13px; font-weight: 700; letter-spacing: 2px; color: #6F6B66; text-transform: uppercase;">02 / MARKET MATCH</span>
                    <img src="wp-content/uploads/sites/2/2025/05/service-2.svg" width="48" height="48" alt="Smart Distribution" />
                </div>
                <h4 style="font-family:'Archivo', sans-serif; font-size: 22px; font-weight: 800; color: #28282C; margin: 0 0 12px 0;">Smart Distribution Matching</h4>
                <p style="font-family:'Archivo', sans-serif; font-size: 15px; line-height: 1.6; color: #49433C; margin: 0 0 20px 0;">Instantly links smallholder and commercial farmers directly to verified food distributors and supermarket buyers, eliminating exploitative middlemen.</p>
                <span style="font-family:'Archivo', sans-serif; font-size: 14px; font-weight: 700; color: #233F2E; display: inline-flex; align-items: center; gap: 6px;">Explore Feature &rarr;</span>
            </div>
        </a>
        <!-- Service 3 -->
        <a href="services/soil-health-management/index.html" style="text-decoration:none; color:inherit; display:block;">
            <div style="background:#FFFDF7; border: 1px solid #C4C0BC; border-radius: 12px; padding: 32px 28px; transition: transform 0.3s, box-shadow 0.3s; height: 100%; box-sizing: border-box;">
                <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 20px;">
                    <span style="font-family:'Archivo', sans-serif; font-size: 13px; font-weight: 700; letter-spacing: 2px; color: #6F6B66; text-transform: uppercase;">03 / CLIMATE RESILIENCE</span>
                    <img src="wp-content/uploads/sites/2/2025/05/service-3.svg" width="48" height="48" alt="Early Warning" />
                </div>
                <h4 style="font-family:'Archivo', sans-serif; font-size: 22px; font-weight: 800; color: #28282C; margin: 0 0 12px 0;">Early Warning System</h4>
                <p style="font-family:'Archivo', sans-serif; font-size: 15px; line-height: 1.6; color: #49433C; margin: 0 0 20px 0;">Early AI-powered alerts on disease outbreaks, pest risks, droughts, and erratic weather anomalies, enabling proactive mitigation weeks in advance.</p>
                <span style="font-family:'Archivo', sans-serif; font-size: 14px; font-weight: 700; color: #233F2E; display: inline-flex; align-items: center; gap: 6px;">Explore Feature &rarr;</span>
            </div>
        </a>
        <!-- Service 4 -->
        <a href="services/advanced-irrigation-systems/index.html" style="text-decoration:none; color:inherit; display:block;">
            <div style="background:#FFFDF7; border: 1px solid #C4C0BC; border-radius: 12px; padding: 32px 28px; transition: transform 0.3s, box-shadow 0.3s; height: 100%; box-sizing: border-box;">
                <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 20px;">
                    <span style="font-family:'Archivo', sans-serif; font-size: 13px; font-weight: 700; letter-spacing: 2px; color: #6F6B66; text-transform: uppercase;">04 / LOGISTICS</span>
                    <img src="wp-content/uploads/sites/2/2025/05/service-4.svg" width="48" height="48" alt="Post-Harvest" />
                </div>
                <h4 style="font-family:'Archivo', sans-serif; font-size: 22px; font-weight: 800; color: #28282C; margin: 0 0 12px 0;">Post-Harvest Optimization</h4>
                <p style="font-family:'Archivo', sans-serif; font-size: 15px; line-height: 1.6; color: #49433C; margin: 0 0 20px 0;">Dramatically reduces post-harvest waste through synchronized harvest scheduling, cold-chain storage routing, and optimized transit coordination.</p>
                <span style="font-family:'Archivo', sans-serif; font-size: 14px; font-weight: 700; color: #233F2E; display: inline-flex; align-items: center; gap: 6px;">Explore Feature &rarr;</span>
            </div>
        </a>
        <!-- Service 5 -->
        <a href="services/seed-supply-distribution/index.html" style="text-decoration:none; color:inherit; display:block;">
            <div style="background:#FFFDF7; border: 1px solid #C4C0BC; border-radius: 12px; padding: 32px 28px; transition: transform 0.3s, box-shadow 0.3s; height: 100%; box-sizing: border-box;">
                <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 20px;">
                    <span style="font-family:'Archivo', sans-serif; font-size: 13px; font-weight: 700; letter-spacing: 2px; color: #6F6B66; text-transform: uppercase;">05 / MARKETPLACE</span>
                    <img src="wp-content/uploads/sites/2/2025/05/service-5.svg" width="48" height="48" alt="AgroMarket" />
                </div>
                <h4 style="font-family:'Archivo', sans-serif; font-size: 22px; font-weight: 800; color: #28282C; margin: 0 0 12px 0;">AgroMarket & Input Supply</h4>
                <p style="font-family:'Archivo', sans-serif; font-size: 15px; line-height: 1.6; color: #49433C; margin: 0 0 20px 0;">Direct access to certified climate-resilient seeds, quality agronomic inputs, and verified wholesale purchase contracts across Kenya.</p>
                <span style="font-family:'Archivo', sans-serif; font-size: 14px; font-weight: 700; color: #233F2E; display: inline-flex; align-items: center; gap: 6px;">Explore Feature &rarr;</span>
            </div>
        </a>
        <!-- Service 6 -->
        <a href="services/crop-rotation-planning/index.html" style="text-decoration:none; color:inherit; display:block;">
            <div style="background:#FFFDF7; border: 1px solid #C4C0BC; border-radius: 12px; padding: 32px 28px; transition: transform 0.3s, box-shadow 0.3s; height: 100%; box-sizing: border-box;">
                <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 20px;">
                    <span style="font-family:'Archivo', sans-serif; font-size: 13px; font-weight: 700; letter-spacing: 2px; color: #6F6B66; text-transform: uppercase;">06 / AGRIFINANCE</span>
                    <img src="wp-content/uploads/sites/2/2025/05/service-6.svg" width="48" height="48" alt="Digital Payments" />
                </div>
                <h4 style="font-family:'Archivo', sans-serif; font-size: 22px; font-weight: 800; color: #28282C; margin: 0 0 12px 0;">AgriFinance & Digital Payments</h4>
                <p style="font-family:'Archivo', sans-serif; font-size: 15px; line-height: 1.6; color: #49433C; margin: 0 0 20px 0;">Secure escrow transactions, mobile money payouts, and credit scoring to de-risk micro-finance and insurance for smallholder farmers.</p>
                <span style="font-family:'Archivo', sans-serif; font-size: 14px; font-weight: 700; color: #233F2E; display: inline-flex; align-items: center; gap: 6px;">Explore Feature &rarr;</span>
            </div>
        </a>
    </div>
    '''
    # Replace lazyload preloader in 05affc8 with static services
    html = re.sub(
        r'(<div class="elementor-element elementor-element-05affc8[^"]*"[^>]*>\s*<div class="elementor-widget-container">)(.*?)(</div>\s*</div>\s*</div>\s*</div>\s*<div class="elementor-element elementor-element-ebe7807)',
        r'\1' + static_services_html + r'\3',
        html,
        flags=re.DOTALL
    )

    # 8. Section 9-13 (Competitive Advantage)
    html = html.replace('>Why Choose Us<', '>COMPETITIVE ADVANTAGE<')
    html = html.replace('Leading the Way in Smart, Scalable Farming', 'Why Agrolink Leads the African AgTech Frontier')
    html = html.replace(
        'We blend innovation with proven agronomic knowledge to help your agribusiness thrive in a rapidly evolving landscape.',
        'While traditional approaches offer isolated tools, Agrolink delivers a fully integrated, predictive ecosystem tailored for African farming realities.'
    )

    html = re.sub(
        r'(<h4 class="elementor-widget-cmsmasters-featured-box__title[^"]*">\s*)Innovation-Driven(\s*</h4>)',
        r'\1Predictive AI\2',
        html
    )
    html = html.replace(
        'We use AI, IoT, and machine learning to support smarter decisions in real time.',
        'Our proprietary AI predicts market demand, optimal planting windows, and disease risks before they happen—transforming farming from reactive to predictive.'
    )

    html = re.sub(
        r'(<h4 class="elementor-widget-cmsmasters-featured-box__title[^"]*">\s*)Sustainability First(\s*</h4>)',
        r'\1Real-Time Ecosystem Connection\2',
        html
    )
    html = html.replace(
        'Every solution we offer is designed to protect soil, water, and ecosystems for the long term.',
        'Directly connects farmers, food distributors, bulk buyers, transport fleets, and financial institutions in one seamless, real-time operating loop.'
    )

    html = re.sub(
        r'(<h4 class="elementor-widget-cmsmasters-featured-box__title[^"]*">\s*)Proven Results(\s*</h4>)',
        r'\1End-to-End Optimization\2',
        html
    )
    html = html.replace(
        'Higher yields, lower costs, and improved sustainability — validated on working farms.',
        'Complete value chain optimization from crop selection advice and input supply to post-harvest cold chain storage, freight routing, and instant digital payout.'
    )

    html = re.sub(
        r'(<h4 class="elementor-widget-cmsmasters-featured-box__title[^"]*">\s*)Farm-Tested Expertise(\s*</h4>)',
        r'\1Offline Accessibility\2',
        html
    )
    html = html.replace(
        'Developed by farmers, for farmers — backed by agronomists and tech experts.',
        'Engineered for Africa’s rural infrastructure with full SMS and USSD accessibility—ensuring smallholders in remote communities participate without smartphones.'
    )

    # 9. Section 14 (The Founding Team)
    html = html.replace('>meet our experts<', '>THE FOUNDING TEAM<')
    html = html.replace('Leaders in Modern Agriculture', 'The Minds Behind Agrolink Africa')
    html = html.replace('>Meet the Full Team<', '>Meet the Leadership & Field Team<')

    # Static team grid in 9fd4078
    static_team_html = '''
    <div class="agrolink-team-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 24px; width: 100%; margin-top: 24px;">
        <!-- David Onyango -->
        <div style="background:#FFFDF7; border: 1px solid #C4C0BC; border-radius: 12px; overflow: hidden; text-align: left;">
            <div style="height: 280px; overflow: hidden; background: #233F2E;">
                <img src="wp-content/uploads/sites/2/2025/05/63-profile-1-768x768.webp" style="width: 100%; height: 100%; object-fit: cover;" alt="David Onyango" />
            </div>
            <div style="padding: 24px 20px;">
                <span style="font-family:'Archivo', sans-serif; font-size: 12px; font-weight: 700; color: #233F2E; letter-spacing: 1.5px; text-transform: uppercase;">Co-Founder & AI Systems Lead</span>
                <h4 style="font-family:'Archivo', sans-serif; font-size: 20px; font-weight: 800; color: #28282C; margin: 8px 0 10px 0;">David Onyango</h4>
                <p style="font-family:'Archivo', sans-serif; font-size: 14px; line-height: 1.5; color: #49433C; margin: 0;">Leads Agrolink's machine learning architecture, crop demand forecasting models, and computer vision disease detection engine.</p>
            </div>
        </div>
        <!-- Belamy Maloba -->
        <div style="background:#FFFDF7; border: 1px solid #C4C0BC; border-radius: 12px; overflow: hidden; text-align: left;">
            <div style="height: 280px; overflow: hidden; background: #233F2E;">
                <img src="wp-content/uploads/sites/2/2025/05/63-profile-3-768x768.webp" style="width: 100%; height: 100%; object-fit: cover;" alt="Belamy Maloba" />
            </div>
            <div style="padding: 24px 20px;">
                <span style="font-family:'Archivo', sans-serif; font-size: 12px; font-weight: 700; color: #233F2E; letter-spacing: 1.5px; text-transform: uppercase;">Co-Founder & Operations & Supply Chain</span>
                <h4 style="font-family:'Archivo', sans-serif; font-size: 20px; font-weight: 800; color: #28282C; margin: 8px 0 10px 0;">Belamy Maloba</h4>
                <p style="font-family:'Archivo', sans-serif; font-size: 14px; line-height: 1.5; color: #49433C; margin: 0;">Directs smart distribution networks, cold-chain transport scheduling, and post-harvest reduction logistics across Kenyan counties.</p>
            </div>
        </div>
        <!-- Melvin Akinyi -->
        <div style="background:#FFFDF7; border: 1px solid #C4C0BC; border-radius: 12px; overflow: hidden; text-align: left;">
            <div style="height: 280px; overflow: hidden; background: #233F2E;">
                <img src="wp-content/uploads/sites/2/2025/05/63-profile-2-768x768.webp" style="width: 100%; height: 100%; object-fit: cover;" alt="Melvin Akinyi" />
            </div>
            <div style="padding: 24px 20px;">
                <span style="font-family:'Archivo', sans-serif; font-size: 12px; font-weight: 700; color: #233F2E; letter-spacing: 1.5px; text-transform: uppercase;">Co-Founder & Product & Agronomy</span>
                <h4 style="font-family:'Archivo', sans-serif; font-size: 20px; font-weight: 800; color: #28282C; margin: 8px 0 10px 0;">Melvin Akinyi</h4>
                <p style="font-family:'Archivo', sans-serif; font-size: 14px; line-height: 1.5; color: #49433C; margin: 0;">Heads farmer-centric product design, agronomic research, and pilot field onboarding across Kiambu, Nakuru, and Meru.</p>
            </div>
        </div>
        <!-- Lavine Niphreen -->
        <div style="background:#FFFDF7; border: 1px solid #C4C0BC; border-radius: 12px; overflow: hidden; text-align: left;">
            <div style="height: 280px; overflow: hidden; background: #233F2E;">
                <img src="wp-content/uploads/sites/2/2025/05/63-profile-4-768x768.webp" style="width: 100%; height: 100%; object-fit: cover;" alt="Lavine Niphreen" />
            </div>
            <div style="padding: 24px 20px;">
                <span style="font-family:'Archivo', sans-serif; font-size: 12px; font-weight: 700; color: #233F2E; letter-spacing: 1.5px; text-transform: uppercase;">Co-Founder & Partnerships & Finance</span>
                <h4 style="font-family:'Archivo', sans-serif; font-size: 20px; font-weight: 800; color: #28282C; margin: 8px 0 10px 0;">Lavine Niphreen</h4>
                <p style="font-family:'Archivo', sans-serif; font-size: 14px; line-height: 1.5; color: #49433C; margin: 0;">Leads strategic partnerships with government agencies, NGOs, micro-finance lenders, and commercial agricultural institutions.</p>
            </div>
        </div>
    </div>
    '''
    html = re.sub(
        r'(<div class="elementor-element elementor-element-9fd4078[^"]*"[^>]*>\s*<div class="elementor-widget-container">)(.*?)(</div>\s*</div>)',
        r'\1' + static_team_html + r'\3',
        html,
        flags=re.DOTALL
    )

    # 10. Section 15 (Results / Impact Counters)
    html = html.replace('Results That Speak for Themselves', 'Target Impact: By Year Three')
    html = html.replace('data-to-value="125"', 'data-to-value="300"')
    html = html.replace('>Acres Managed<', '>Farmers Onboarded<')
    html = html.replace(
        'Across precision farming, irrigation, and crop rotation programs.',
        'Empowered smallholder and commercial farmers across Kenya and East Africa.'
    )

    html = html.replace('data-to-value="15"', 'data-to-value="30"')
    html = html.replace('>Years of  Innovation<', '>Farmer Net Income Increase<')
    html = html.replace(
        'Bringing cutting-edge solutions to the fields since 1996.',
        'Average net income growth powered by direct market matching and fair prices.'
    )

    html = html.replace('data-to-value="28"', 'data-to-value="40"')
    html = html.replace('>Average Yield Increase<', '>Reduction in Post-Harvest Losses<')
    html = html.replace(
        'Average yield improvement achieved through precision crop management.',
        'Drastic reduction from the 30–50% baseline loss via synchronized timing & logistics.'
    )

    html = html.replace('data-to-value="20"', 'data-to-value="50"')
    html = html.replace('>Reduction in Input Costs<', '>Farmers Trained in Digital Ag<')
    html = html.replace(
        'Average savings in fertilizers, water, and crop protection products.',
        'Smallholders trained in climate-smart resilience, mobile tools, and predictive farming.'
    )

    # 11. Section 21 (Testimonials)
    html = html.replace('>testimonials<', '>VOICES FROM THE ECOSYSTEM<')
    html = html.replace('>What Our Clients Say<', '>Transforming Agriculture on the Ground<')
    html = html.replace(
        'Working with Agribusiness has completely transformed our operations. Their precision agriculture strategies allowed us to optimize irrigation and fertilizer use, resulting in higher yields and lower input costs. Their hands-on approach and deep expertise make them an invaluable partner.',
        'Working with Agrolink Africa has transformed our farming cooperative in Kiambu. The Demand Prediction AI guided us on what crops to plant, and their Smart Distribution module matched our harvest directly with bulk supermarket buyers at 35% higher profits!'
    )
    html = html.replace(
        'Agribusiness’s technical team helped us pilot and scale our IoT sensor system on actual farms. The feedback was invaluable, and the deployment went seamlessly. They truly understand modern agtech.',
        'As a commercial grain grower in Nakuru, post-harvest losses used to wipe out a third of our margins. Agrolink’s logistics timing and early disease alerts saved over 200 acres this season. A game changer for African farming.'
    )
    html = html.replace(
        'We partnered with Agribusiness for a sustainable farming initiative across three countries. Their insight into regenerative methods and soil biology made the project a success. Highly recommended.',
        'As a fresh produce distributor in Nairobi, finding reliable, quality farm supply on schedule was a daily nightmare. Agrolink connects us to vetted farm clusters ready to harvest today with transparent quality grading.'
    )
    html = html.replace(
        'Together with Agribusiness, we implemented a farm-to-market strategy that reduced post-harvest loss by 40%. Their logistics expertise and farmer training were critical to the project’s success.',
        'Our agricultural development NGO in Meru partnered with Agrolink to train 5,000 farmers. Their SMS/USSD offline feature ensured even elderly farmers with basic feature phones benefited from predictive weather and market alerts.'
    )
    html = html.replace(
        'We collaborated with Agribusiness to improve crop yields. Their data-driven approach and commitment to sustainable growth made all the difference.',
        'The integrated digital payments and yield predictive data allow us to extend micro-credit safely to smallholder farmers who previously had zero credit access. Agrolink is building the future of African agri-finance.'
    )

    # 12. Section 22 (Implementation Strategy / Roadmap)
    html = html.replace('Insights from the Field', 'IMPLEMENTATION STRATEGY & ROADMAP')
    html = html.replace(
        'Stay ahead with articles on precision ag, sustainability trends, new tech, and more.',
        'Our phased execution roadmap: From MVP rollout in Kiambu, Nakuru, and Meru to nationwide Kenya scaling and pan-African expansion.'
    )

    static_roadmap_html = '''
    <div class="agrolink-roadmap-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 24px; width: 100%; margin-top: 24px;">
        <!-- Phase 1 -->
        <div style="background:#FFFDF7; border: 2px solid #AFE67F; border-radius: 12px; padding: 32px 24px; text-align: left;">
            <div style="display:inline-block; background:#233F2E; color:#AFE67F; font-family:'Archivo', sans-serif; font-size:12px; font-weight:800; padding:6px 14px; border-radius:20px; letter-spacing:1px; margin-bottom:16px;">PHASE 1 &bull; MONTHS 1–6</div>
            <h4 style="font-family:'Archivo', sans-serif; font-size:22px; font-weight:800; color:#28282C; margin:0 0 12px 0;">MVP Launch</h4>
            <p style="font-family:'Archivo', sans-serif; font-size:15px; line-height:1.6; color:#49433C; margin:0 0 16px 0;">Develop core platform and AI predictive algorithms. Launch MVP clusters with farmers in <strong>Kiambu, Nakuru, and Meru</strong>. Gather on-ground user feedback and refine models.</p>
            <ul style="font-family:'Archivo', sans-serif; font-size:13px; color:#6F6B66; padding-left:18px; margin:0; line-height:1.7;">
                <li>Pilot farmer onboarding in 3 counties</li>
                <li>Demand Prediction AI calibration</li>
                <li>USSD & SMS integration testing</li>
            </ul>
        </div>
        <!-- Phase 2 -->
        <div style="background:#FFFDF7; border: 1px solid #C4C0BC; border-radius: 12px; padding: 32px 24px; text-align: left;">
            <div style="display:inline-block; background:#AFE67F; color:#233F2E; font-family:'Archivo', sans-serif; font-size:12px; font-weight:800; padding:6px 14px; border-radius:20px; letter-spacing:1px; margin-bottom:16px;">PHASE 2 &bull; MONTHS 7–18</div>
            <h4 style="font-family:'Archivo', sans-serif; font-size:22px; font-weight:800; color:#28282C; margin:0 0 12px 0;">National Expansion</h4>
            <p style="font-family:'Archivo', sans-serif; font-size:15px; line-height:1.6; color:#49433C; margin:0 0 16px 0;">Scale across all agricultural hubs in Kenya. Onboard commercial farmers, institutional buyers, and financial partners. Officially roll out <strong>AgroMarket and AgriFinance</strong> modules.</p>
            <ul style="font-family:'Archivo', sans-serif; font-size:13px; color:#6F6B66; padding-left:18px; margin:0; line-height:1.7;">
                <li>Nationwide buyer-farmer matching</li>
                <li>Digital escrow payments & micro-loans</li>
                <li>Cold-chain fleet partner integration</li>
            </ul>
        </div>
        <!-- Phase 3 -->
        <div style="background:#FFFDF7; border: 1px solid #C4C0BC; border-radius: 12px; padding: 32px 24px; text-align: left;">
            <div style="display:inline-block; background:#F0EEE9; color:#28282C; font-family:'Archivo', sans-serif; font-size:12px; font-weight:800; padding:6px 14px; border-radius:20px; letter-spacing:1px; margin-bottom:16px;">PHASE 3 &bull; YEARS 2–3</div>
            <h4 style="font-family:'Archivo', sans-serif; font-size:22px; font-weight:800; color:#28282C; margin:0 0 12px 0;">Regional Pan-African Expansion</h4>
            <p style="font-family:'Archivo', sans-serif; font-size:15px; line-height:1.6; color:#49433C; margin:0 0 16px 0;">Expand across all 47 Kenyan counties and neighboring African countries. Localize the platform for multiple regional languages and farming systems in partnership with governments and NGOs.</p>
            <ul style="font-family:'Archivo', sans-serif; font-size:13px; color:#6F6B66; padding-left:18px; margin:0; line-height:1.7;">
                <li>Multi-country East African rollout</li>
                <li>Pan-African food security analytics</li>
                <li>Target: 300,000+ onboarded farmers</li>
            </ul>
        </div>
    </div>
    '''
    html = re.sub(
        r'(<div class="elementor-element elementor-element-dc05a40[^"]*"[^>]*>\s*<div class="elementor-widget-container">)(.*?)(</div>\s*</div>)',
        r'\1' + static_roadmap_html + r'\3',
        html,
        flags=re.DOTALL
    )

    # 13. Section 23 (FAQ)
    html = html.replace('Got Questions? We’ve Got Answers', 'Frequently Asked Questions: Agrolink Africa')
    html = html.replace(
        'What is precision agriculture, and how does it help?',
        'What is Agrolink Africa and how does the platform work?'
    )
    html = html.replace(
        'Precision agriculture uses data and technology to make farming more accurate, efficient, and sustainable. By monitoring crop health, soil conditions, and weather in real time, it allows farmers to apply resources like water and fertilizer only where and when needed, saving money and boosting yields.',
        'Agrolink Africa is an AI-powered agricultural ecosystem platform connecting farmers, buyers, transport fleets, and financial institutions. Our AI collects data, predicts demand and risks, and sends smart recommendations to farmers while connecting them directly to buyers and transport systems—shifting agriculture from reactive to predictive.'
    )

    html = html.replace(
        'Can small farms benefit from your services?',
        'Why is connection the problem in Africa rather than food production?'
    )
    html = html.replace(
        'Small farms often face challenges that at first glance may seem difficult to overcome. Limited resources, lack of access to advanced tools, and market pressures can make growth feel out of reach. But here’s the truth: with the right strategies, small farms have unique advantages.',
        'Africa produces vast amounts of agricultural harvest, yet 30% to 50% spoils before reaching markets while millions go hungry. The bottleneck is not production—it is connection. Farmers lack market intelligence, supply chains are fragmented, and climate risks go undetected. Agrolink provides the intelligent ecosystem linking all parties.'
    )

    html = html.replace(
        'What types of automation can you implement?',
        'How does the Demand Prediction AI assist farmers?'
    )
    html = html.replace(
        'There are four types of automation systems: fixed automation, programmable automation, flexible automation and integrated automation.',
        'Instead of farmers guessing what to plant and suffering localized market gluts, our Demand Prediction AI analyzes real-time buyer demand, regional price forecasts, and agronomic conditions to recommend high-yield, high-margin crops with guaranteed buyer appetite.'
    )

    html = html.replace(
        'Is training provided for new systems and technology?',
        'Can smallholder farmers without smartphones use Agrolink?'
    )
    html = html.replace(
        'Here are our five tips on how to train employees on a new system or technology: Trainers need to know the software or system inside and out before teaching others. Highlight how the new tool solves problems and makes their work easier. Use live demos, practice scenarios, and step-by-step guides.',
        'Yes! Offline Accessibility is one of our defining competitive advantages. Agrolink is built with SMS and USSD functionality so smallholder farmers in remote areas with basic feature phones can receive planting advice, weather alerts, and buyer bids without needing internet.'
    )

    html = html.replace(
        'Do you offer on-site consultations or is everything remote?',
        'What is Agrolink’s implementation strategy and revenue model?'
    )
    html = html.replace(
        'We offer all types of consultations.',
        'Our implementation strategy rolls out across 3 phases: Months 1–6 MVP launch in Kiambu, Nakuru, and Meru; Months 7–18 National Kenya expansion with AgroMarket and AgriFinance; Years 2–3 Regional East African expansion. Revenue streams include commercial SaaS subscriptions, marketplace transaction fees, data analytics services, and government/NGO partnerships.'
    )

    # 14. Section 24 (Partners)
    html = html.replace('Trusted by Innovators in Agriculture', 'Supported by Leading Partners Across Agriculture & Innovation')

    # 15. Section 25 (CTA)
    html = html.replace('Ready to Cultivate the Future?', 'Ready to Transform African Agriculture?')
    html = html.replace(
        'Partner with us to unlock the full potential of your agribusiness.',
        'Join Agrolink Africa today to eliminate harvest waste, boost farmer incomes, and secure Africa’s food future.'
    )
    html = html.replace('>Request a Call<', '>Join MVP Pilot<')
    html = html.replace('>get a quote<', '>Partner With Us<')

    # 16. Footer & Contact Details
    html = html.replace('511 SW 10th Ave 1206, Portland, OR, United States', 'Westlands AgTech Hub, Waiyaki Way, Nairobi, Kenya')
    html = html.replace('123 Madison Avenue, Suite 500,', 'Regional Pilot Hubs: Kiambu • Nakuru • Meru, Kenya')
    html = html.replace('1-800-123-1234', '+254 700 892 411 / +254 20 491 3000')

    # Clean Cloudflare email obfuscation
    html = re.sub(
        r'<a href="[^"]*email-protection[^"]*">\[email&#160;protected\]</a>',
        '<a href="mailto:info@agrolink.africa">info@agrolink.africa</a>',
        html
    )
    html = html.replace('[email&#160;protected]', 'info@agrolink.africa')

    # Footer Copyright & Credits
    html = html.replace('This is a sample website', 'Agrolink Africa – AI-Powered Agricultural Ecosystem')
    html = html.replace('cmsmasters', 'Agrolink Africa')
    html = re.sub(
        r'©\s*2026\s*-\s*All Rights Reserved',
        '© 2026 Agrolink Africa. All Rights Reserved. Transforming Agriculture from Reactive to Predictive.',
        html
    )

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Homepage (index.html) rebranded successfully.")

if __name__ == '__main__':
    rebrand_homepage()
