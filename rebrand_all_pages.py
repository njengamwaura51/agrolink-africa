#!/usr/bin/env python3
"""
Comprehensive site-wide rebranding for Agrolink Africa.
Updates:
- about-us/index.html
- our-services/index.html
- our-workers/index.html
- contacts/index.html
- services/*/index.html
- cmsms_profile/*/index.html
- Global footer, header, and metadata across all HTML files
"""

import os
import re

BASE_DIR = '/home/pirate101/Downloads/agri/agribusiness.cmsmasters.studio/main'

def update_global_elements(html, rel_path):
    # Fix logo link
    html = re.sub(r'href="https://agribusiness\.cmsmasters\.studio/main/?\"', 'href="../index.html"' if '/' in rel_path else 'href="index.html"', html)
    html = html.replace('alt="Main" title="Main"', 'alt="Agrolink Africa" title="Agrolink Africa"')
    html = html.replace('alt="Main"', 'alt="Agrolink Africa"')
    html = html.replace('title="Main"', 'title="Agrolink Africa"')

    # Fix footer addresses and contacts
    html = html.replace('511 SW 10th Ave 1206, Portland, OR, United States', 'Westlands AgTech Hub, Waiyaki Way, Nairobi, Kenya')
    html = html.replace('123 Madison Avenue, Suite 500,', 'Pilot Regional Hubs: Kiambu • Nakuru • Meru, Kenya')
    html = html.replace('1-800-123-1234', '+254 700 892 411 / +254 20 491 3000')

    # Fix Cloudflare email protection
    html = re.sub(
        r'<a href="[^"]*email-protection[^"]*">\[email&#160;protected\]</a>',
        '<a href="mailto:info@agrolink.africa">info@agrolink.africa</a>',
        html
    )
    html = html.replace('[email&#160;protected]', 'info@agrolink.africa')

    # Footer Copyright
    html = html.replace('This is a sample website', 'Agrolink Africa – AI-Powered Agricultural Ecosystem')
    html = html.replace('cmsmasters', 'Agrolink Africa')
    html = re.sub(
        r'©\s*2026\s*-\s*All Rights Reserved',
        '© 2026 Agrolink Africa. All Rights Reserved. Transforming Agriculture from Reactive to Predictive.',
        html
    )

    # Header CTA
    html = html.replace('>Get a Quote<', '>Join MVP Pilot<')
    return html

def rebrand_about_us():
    path = os.path.join(BASE_DIR, 'about-us/index.html')
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()

    html = update_global_elements(html, 'about-us/index.html')
    html = re.sub(r'<title>.*?</title>', '<title>About Us – Agrolink Africa</title>', html, count=1)

    html = html.replace('Why We are the Best?', 'Transforming African Agriculture from Reactive to Predictive')
    html = html.replace('>About Us<', '>THE AGROLINK STORY<')

    story = (
        'Africa grows enough food. Yet millions still go hungry. 30–50% of harvest is lost before reaching the market. '
        'The problem isn\'t production—it\'s connection. Farmers lack market intelligence, supply chains are disconnected, '
        'and climate risks go undetected. Agriculture needs an intelligent ecosystem—not isolated solutions.<br><br>'
        'Introducing Agrolink Africa: an AI-powered platform that connects the entire agricultural ecosystem and predicts decisions '
        'before they happen. We are building a platform where AI collects data, predicts demand and risks, and sends smart recommendations '
        'to farmers while connecting them directly to buyers and transport systems.<br><br>'
        'Our implementation strategy rolls out across 3 phases: Months 1–6 MVP launch in Kiambu, Nakuru, and Meru; Months 7–18 National Kenya expansion '
        'with AgroMarket and AgriFinance; Years 2–3 Regional East African expansion. By Year Three, we aim to onboard 300,000 farmers, '
        'increase farmer net income by 30%, reduce post-harvest waste by 40%, and train 50,000 farmers in digital climate-smart practices.'
    )

    html = re.sub(
        r'<p>From precision agriculture and climate-smart practices.*?</p>',
        f'<p>{story}</p>',
        html,
        flags=re.DOTALL
    )

    # Team section in about-us
    html = html.replace('Meet the Professional Farmers', 'The Founding Team: Agrolink Africa')
    html = html.replace('Conrad Velez', 'David Onyango')
    html = html.replace('Innovation &amp; Tech Advisor', 'Co-Founder &amp; AI Systems Lead')
    html = html.replace('Thomas Lynch', 'Belamy Maloba')
    html = html.replace('Farm Operations Director', 'Co-Founder &amp; Operations &amp; Supply Chain Lead')
    html = html.replace('Karen Thomas', 'Melvin Akinyi')
    html = html.replace('Head Agronomist', 'Co-Founder &amp; Product &amp; Agronomy Lead')
    html = html.replace('Miguel Torres', 'Lavine Niphreen')
    html = html.replace('Sustainability Lead', 'Co-Founder &amp; Strategic Partnerships &amp; Finance Lead')

    # Testimonials in about-us
    html = html.replace(
        'We collaborated with Agribusiness to improve crop yields using precision agriculture in rural communities. Their data-driven approach and commitment to sustainable growth made all the difference.',
        'Working with Agrolink Africa has transformed our cooperative in Kiambu. Demand Prediction AI guided us on what crops to plant, and their Smart Distribution module matched our harvest directly with bulk supermarket buyers at 35% higher profits!'
    )
    html = html.replace(
        'Working alongside Agribusiness., we launched an agroforestry program that revitalized degraded lands in two regions. Their insight into regenerative methods and soil biology made the project a success. Highly recommended.',
        'As a commercial grain grower in Nakuru, post-harvest losses used to wipe out a third of our margins. Agrolink’s logistics timing and early disease alerts saved over 200 acres this season.'
    )
    html = html.replace(
        'Our partnership with Agribusiness enabled the deployment of climate-resilient seed varieties in drought-prone areas. The technical team helped us pilot and scale the initiative, and the results exceeded our expectations.',
        'As a fresh produce distributor in Nairobi, finding reliable, quality farm supply on schedule was a daily nightmare. Agrolink connects us to vetted farm clusters ready to harvest today with transparent quality grading.'
    )
    html = html.replace(
        'Together with Agribusiness, we implemented a farm-to-market strategy that reduced post-harvest loss by 40%. Their logistics expertise and farmer training were critical to the project’s success.',
        'Our agricultural development NGO in Meru partnered with Agrolink to train 5,000 farmers. Their SMS/USSD offline feature ensured even farmers with basic feature phones benefited from predictive weather and market alerts.'
    )

    html = html.replace('Ready to Experience the Best of Farming?', 'Ready to Transform African Agriculture?')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print("about-us/index.html updated successfully.")

def rebrand_our_services():
    path = os.path.join(BASE_DIR, 'our-services/index.html')
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()

    html = update_global_elements(html, 'our-services/index.html')
    html = re.sub(r'<title>.*?</title>', '<title>Ecosystem & Services – Agrolink Africa</title>', html, count=1)

    html = html.replace('>Our Services<', '>THE AGROLINK ECOSYSTEM<')
    html = html.replace('Find the Right Solution for You', 'Intelligent Agricultural Ecosystem Pillars')

    # Update the 6 services in our-services
    html = html.replace('Soil Health &#038; Management', 'Early Warning System (Weather &amp; Disease Risk)')
    html = html.replace('Soil Health &amp; Management', 'Early Warning System (Weather &amp; Disease Risk)')

    html = html.replace('Advanced Irrigation Systems', 'Post-Harvest Optimization &amp; Logistics')

    html = html.replace('Precision Agriculture', 'Demand Prediction AI')

    html = html.replace('Crop Rotation Planning', 'AgriFinance &amp; Digital Payments')

    html = html.replace('Seed Supply &#038; Distribution', 'AgroMarket &amp; Certified Input Supply')
    html = html.replace('Seed Supply &amp; Distribution', 'AgroMarket &amp; Certified Input Supply')

    html = html.replace('Quality Control &#038; Grading', 'Smart Distribution Matching')
    html = html.replace('Quality Control &amp; Grading', 'Smart Distribution Matching')

    html = html.replace(
        'Half the Cost, Double the Growth – 50% Off Now!',
        'Join the Agrolink MVP Pilot in Kiambu, Nakuru, and Meru!'
    )

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print("our-services/index.html updated successfully.")

def rebrand_our_workers():
    path = os.path.join(BASE_DIR, 'our-workers/index.html')
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()

    html = update_global_elements(html, 'our-workers/index.html')
    html = re.sub(r'<title>.*?</title>', '<title>Our Leadership & Team – Agrolink Africa</title>', html, count=1)

    html = html.replace('>Our Workers<', '>THE AGROLINK AFRICA TEAM<')

    # Update members
    html = html.replace('Conrad Velez', 'David Onyango')
    html = html.replace('Innovation &amp; Tech Advisor', 'Co-Founder &amp; AI Systems Lead')

    html = html.replace('Thomas Lynch', 'Belamy Maloba')
    html = html.replace('Farm Operations Director', 'Co-Founder &amp; Operations &amp; Supply Chain Lead')

    html = html.replace('Karen Thomas', 'Melvin Akinyi')
    html = html.replace('Head Agronomist', 'Co-Founder &amp; Product &amp; Agronomy Lead')

    html = html.replace('Miguel Torres', 'Lavine Niphreen')
    html = html.replace('Sustainability Lead', 'Co-Founder &amp; Strategic Partnerships &amp; Finance Lead')

    html = html.replace('Aisha Daniels', 'Dr. Aisha Daniels')
    html = html.replace('Anya Steele', 'Anya Steele')

    html = html.replace('Ask a Question', 'Partner With Our Team')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print("our-workers/index.html updated successfully.")

def rebrand_contacts():
    path = os.path.join(BASE_DIR, 'contacts/index.html')
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()

    html = update_global_elements(html, 'contacts/index.html')
    html = re.sub(r'<title>.*?</title>', '<title>Contact Us – Agrolink Africa</title>', html, count=1)

    html = html.replace(
        'We blend innovation with proven agronomic knowledge to help your agribusiness thrive in a rapidly evolving landscape.',
        'Connect with the Agrolink Africa team to join our farmer onboarding pilot, partner as a bulk buyer or logistics provider, or deploy institutional programs.'
    )

    html = html.replace('Monday – Sunday,9am – 7pm EST', 'Monday – Saturday, 8am – 6pm EAT')
    html = html.replace('All Locations', 'Headquarters & Regional Pilot Hubs')
    html = html.replace('Ask a Question', 'Join the Agrolink Ecosystem')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print("contacts/index.html updated successfully.")

def rebrand_service_pages():
    services_map = {
        'precision-agriculture': {
            'old_title': 'Precision Agriculture',
            'new_title': 'Demand Prediction AI',
            'badge': 'AI-Powered Crop & Planting Advisory',
            'desc': (
                'Demand Prediction AI advises farmers on what crops to plant based on real-time market demand, '
                'historical price trends, and climatic risk models. Instead of farmers producing blind surpluses that crash local markets, '
                'our AI engine matches future harvest volumes to guaranteed buyer demand, maximizing net farmer profitability.'
            )
        },
        'quality-control-grading': {
            'old_title': 'Quality Control &#038; Grading',
            'new_title': 'Smart Distribution Matching',
            'badge': 'Instant Matchmaking Between Farmers & Buyers',
            'desc': (
                'Smart Distribution Matching connects smallholder and commercial farmers directly to verified food distributors, '
                'supermarket chains, and institutional buyers in real time. By cutting out exploitative middlemen and establishing transparent '
                'quality grading standards, farmers secure fair market prices and buyers receive guaranteed on-time supply.'
            )
        },
        'soil-health-management': {
            'old_title': 'Soil Health &#038; Management',
            'new_title': 'Early Warning System',
            'badge': 'Predictive Climate & Disease Risk Alerts',
            'desc': (
                'Our Early Warning System continuously monitors satellite meteorological data, ground soil sensors, and regional pest movement '
                'to alert farmers on disease outbreaks, pest risks, droughts, and erratic weather patterns. By predicting threats weeks before symptoms appear, '
                'farmers take preemptive action to safeguard crop yields.'
            )
        },
        'advanced-irrigation-systems': {
            'old_title': 'Advanced Irrigation Systems',
            'new_title': 'Post-Harvest Optimization & Logistics',
            'badge': 'Slashing Post-Harvest Loss from 50% to Under 10%',
            'desc': (
                'Across Africa, 30% to 50% of harvests rot in fields or transit before reaching the market. Post-Harvest Optimization '
                'coordinates harvest timing, cold storage allocation, and transport fleet dispatching to move fresh produce quickly from farm gate '
                'to market stalls, preserving freshness and eliminating wasteful post-harvest spoilage.'
            )
        },
        'seed-supply-distribution': {
            'old_title': 'Seed Supply &#038; Distribution',
            'new_title': 'AgroMarket & Input Supply',
            'badge': 'Certified Climate-Resilient Inputs & Seed Marketplace',
            'desc': (
                'AgroMarket connects farmers with certified climate-smart seeds, fertilizers, and eco-friendly crop protection. '
                'Through cooperative bulk purchasing, smallholder clusters receive premium agricultural inputs at reduced costs with verified authenticity.'
            )
        },
        'crop-rotation-planning': {
            'old_title': 'Crop Rotation Planning',
            'new_title': 'AgriFinance & Digital Payments',
            'badge': 'Financial Inclusion, Escrow Security & Micro-Credit',
            'desc': (
                'AgriFinance provides transparent mobile money escrow checkout, instant farmer payouts upon delivery verification, '
                'and data-driven credit scoring. By leveraging AI predictive yield data, financial institutions can de-risk micro-loans '
                'and index-based crop insurance for smallholder farmers across Kenya.'
            )
        }
    }

    for s_slug, data in services_map.items():
        p = os.path.join(BASE_DIR, f'services/{s_slug}/index.html')
        if not os.path.exists(p):
            continue
        with open(p, 'r', encoding='utf-8', errors='ignore') as f:
            html = f.read()

        html = update_global_elements(html, f'services/{s_slug}/index.html')
        html = re.sub(r'<title>.*?</title>', f'<title>{data["new_title"]} – Agrolink Africa</title>', html, count=1)

        html = html.replace(f'>{data["old_title"]}<', f'>{data["new_title"]}<')
        html = html.replace(f'>About {data["old_title"]}<', f'>About {data["new_title"]}<')
        html = html.replace('Precision agriculture uses data and technology to make farming more accurate, efficient, and sustainable.', data['desc'])

        # Update specialists
        html = html.replace('Conrad Velez', 'David Onyango')
        html = html.replace('Karen Thomas', 'Melvin Akinyi')
        html = html.replace('Thomas Lynch', 'Belamy Maloba')
        html = html.replace('Miguel Torres', 'Lavine Niphreen')

        with open(p, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Service page {s_slug} updated.")

def rebrand_profile_pages():
    profiles_map = {
        'conrad-velez': {
            'name': 'David Onyango',
            'role': 'Co-Founder & AI Systems Lead',
            'bio': 'David leads Agrolink Africa’s artificial intelligence architecture, demand prediction models, and computer vision early warning systems. He holds advanced expertise in machine learning and data engineering applied to agricultural ecosystems across East Africa.'
        },
        'thomas-lynch': {
            'name': 'Belamy Maloba',
            'role': 'Co-Founder & Operations & Supply Chain Lead',
            'bio': 'Belamy directs Agrolink Africa’s logistics network, smart distribution matching, transport routing, and post-harvest waste reduction operations. With deep operational expertise in agricultural value chains, he coordinates farm-to-market logistics across Kenya.'
        },
        'karen-thomas': {
            'name': 'Melvin Akinyi',
            'role': 'Co-Founder & Product & Agronomy Lead',
            'bio': 'Melvin oversees farmer-centric product design, agronomy research, and field onboarding. She works closely with farmer cooperatives in Kiambu, Nakuru, and Meru to ensure Agrolink’s mobile, SMS, and USSD tools deliver real value to smallholder farmers.'
        },
        'miguel-torres': {
            'name': 'Lavine Niphreen',
            'role': 'Co-Founder & Strategic Partnerships & Finance Lead',
            'bio': 'Lavine manages institutional relationships with county governments, NGOs, agricultural micro-finance lenders, and commercial agribusinesses. She leads the rollout of the AgriFinance module to expand financial inclusion for smallholder farmers.'
        },
        'aisha-daniels': {
            'name': 'Dr. Aisha Daniels',
            'role': 'Kiambu & Nakuru Agricultural Extension Specialist',
            'bio': 'Dr. Aisha coordinates field extension services and farmer training programs across Kiambu and Nakuru counties, driving adoption of climate-smart farming practices and digital tools.'
        },
        'anya-steele': {
            'name': 'Anya Steele',
            'role': 'Meru Operations & Logistics Coordinator',
            'bio': 'Anya manages regional distribution hubs, cold storage partnerships, and farmer cooperative onboarding in Meru and Eastern Kenya.'
        }
    }

    for p_slug, data in profiles_map.items():
        p = os.path.join(BASE_DIR, f'cmsms_profile/{p_slug}/index.html')
        if not os.path.exists(p):
            continue
        with open(p, 'r', encoding='utf-8', errors='ignore') as f:
            html = f.read()

        html = update_global_elements(html, f'cmsms_profile/{p_slug}/index.html')
        html = re.sub(r'<title>.*?</title>', f'<title>{data["name"]} – Agrolink Africa</title>', html, count=1)

        # Replace name and role
        old_name = {
            'conrad-velez': 'Conrad Velez',
            'thomas-lynch': 'Thomas Lynch',
            'karen-thomas': 'Karen Thomas',
            'miguel-torres': 'Miguel Torres',
            'aisha-daniels': 'Aisha Daniels',
            'anya-steele': 'Anya Steele'
        }[p_slug]

        html = html.replace(f'>{old_name}<', f'>{data["name"]}<')
        html = html.replace(old_name, data["name"])

        # Replace placeholder latin bio
        html = re.sub(
            r'<p>The languages only differ in their grammar.*?</p>',
            f'<p>{data["bio"]}</p>',
            html,
            flags=re.DOTALL
        )
        html = re.sub(
            r'<p>For science, music, sport, etc.*?</p>',
            f'<p>Focus areas: Predictive AI, Sustainable Value Chains, Smallholder Empowerment, Food Security.</p>',
            html,
            flags=re.DOTALL
        )

        with open(p, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Profile page {p_slug} updated.")

def rebrand_all_html_files():
    count = 0
    for root, dirs, files in os.walk(BASE_DIR):
        for f in files:
            if f.endswith('.html'):
                file_path = os.path.join(root, f)
                rel_path = os.path.relpath(file_path, BASE_DIR)
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as fp:
                    content = fp.read()

                updated = update_global_elements(content, rel_path)

                # Replace leftover "Agribusiness" in user-facing text
                updated = updated.replace('Welcome to Agribusiness', 'Welcome to Agrolink Africa')
                updated = re.sub(r'©\s*2026\s*-\s*All Rights Reserved', '© 2026 Agrolink Africa. All Rights Reserved.', updated)

                if updated != content:
                    with open(file_path, 'w', encoding='utf-8') as fp:
                        fp.write(updated)
                    count += 1

    print(f"Global pass completed: {count} HTML files updated with Agrolink Africa branding.")

if __name__ == '__main__':
    rebrand_about_us()
    rebrand_our_services()
    rebrand_our_workers()
    rebrand_contacts()
    rebrand_service_pages()
    rebrand_profile_pages()
    rebrand_all_html_files()
    print("ALL SITE PAGES REBRANDED SUCCESSFULLY!")
