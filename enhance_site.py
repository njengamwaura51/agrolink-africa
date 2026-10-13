#!/usr/bin/env python3
"""
Agrolink Africa Website Enhancement Script.
Implements:
1. Complete removal of skins/buy now demo toolbar across all HTML files.
2. Compression of excessive whitespace and section paddings (120px-150px -> 45px-55px).
3. Removal of worker stock photos and creation of advanced founder panel displays for:
   - David Onyango (Co-Founder & AI Systems Lead)
   - Belamy Maloba (Co-Founder & Operations & Supply Chain Lead)
   - Melvin Akinyi (Co-Founder & Product & Agronomy Lead)
   - Lavine Niphreen (Co-Founder & Strategic Partnerships & Finance Lead)
4. Integration of rich Agrolink Africa project features:
   - Offline Accessibility (USSD *384*254# & SMS Engine)
   - 4-Segment Market Opportunity Matrix (Slide 8)
   - Active County Pilot Hubs Tracker (Kiambu, Nakuru, Meru - Slide 9)
   - Revenue & Sustainability Architecture (Slide 10)
5. Preservation of themes, fonts (Archivo), and colors (#233F2E, #AFE67F, #FFFDF7, #28282C).
"""

import os
import re

BASE_DIR = '/home/pirate101/Downloads/agri/agribusiness.cmsmasters.studio/main'

# Global CSS for layout compression & demo toolbar suppression
GLOBAL_HEAD_CSS = '''
<style id="agrolink-enhanced-styles">
/* 1. COMPLETELY HIDE & SUPPRESS ALL DEMO/SKINS/BUY NOW PANELS */
.cmsmasters-demos-preview,
.cmsmasters-preview__toggle,
.cmsmasters-demos-preview__buttons,
.cmsmasters-preview_overlay,
.cmsmasters-demos-preview__container,
.cmsmasters-palettes-preview,
.cmsmasters-skins-svg,
.cmsmasters-demos-preview__buy-link,
.cmsmasters-palettes-preview__toggle-big {
    display: none !important;
    visibility: hidden !important;
    opacity: 0 !important;
    pointer-events: none !important;
    width: 0 !important;
    height: 0 !important;
    margin: 0 !important;
    padding: 0 !important;
    overflow: hidden !important;
}

/* 2. COMPACT LAYOUT & REDUCE EMPTY SECTION WHITESPACE */
.elementor-element-4d007d9,
.elementor-element-70a3550,
.elementor-element-6e496a1,
.elementor-element-9a9e083,
.elementor-element-3c82380,
.elementor-element-b263785,
.elementor-element-f4f733d,
.elementor-element-edeba7e,
.elementor-element-bcd6d49 {
    --padding-top: 48px !important;
    --padding-bottom: 48px !important;
    --row-gap: 32px !important;
    --gap: 32px !important;
    padding-top: 48px !important;
    padding-bottom: 48px !important;
}

.elementor-element-6208fa3 {
    --margin-bottom: 36px !important;
    margin-bottom: 36px !important;
}

.elementor-element-8b35176 {
    --min-height: 240px !important;
    min-height: 240px !important;
    padding-top: 36px !important;
    padding-bottom: 36px !important;
}

.elementor-element-6cee356,
.elementor-element-67ec38a9 {
    display: none !important;
}

/* 3. ADVANCED FOUNDER PANELS HOVER EFFECT */
.agrolink-executive-card {
    transition: transform 0.25s ease, box-shadow 0.25s ease, border-color 0.25s ease;
}
.agrolink-executive-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 16px 36px rgba(35, 63, 46, 0.12) !important;
    border-color: #AFE67F !important;
}
</style>
'''

# Advanced Picture-Free Founder Panels HTML
FOUNDER_PANELS_HTML = '''
<div class="agrolink-team-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 24px; width: 100%; margin-top: 24px;">
    <!-- David Onyango -->
    <div class="agrolink-executive-card" style="background:#FFFDF7; border: 1px solid #C4C0BC; border-radius: 14px; padding: 32px 26px; display: flex; flex-direction: column; justify-content: space-between; box-sizing: border-box;">
        <div>
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 22px;">
                <div style="width: 58px; height: 58px; border-radius: 14px; background: linear-gradient(135deg, #233F2E 0%, #15261C 100%); display: flex; align-items: center; justify-content: center; border: 2px solid #AFE67F; box-shadow: 0 4px 14px rgba(35,63,46,0.18);">
                    <span style="font-family:'Archivo', sans-serif; font-size: 21px; font-weight: 800; color: #AFE67F; letter-spacing: 1px;">DO</span>
                </div>
                <span style="background: rgba(35,63,46,0.08); color: #233F2E; border: 1px solid rgba(35,63,46,0.22); font-family:'Archivo', sans-serif; font-size: 11px; font-weight: 800; padding: 5px 12px; border-radius: 20px; letter-spacing: 0.8px; text-transform: uppercase;">
                    Co-Founder
                </span>
            </div>
            <h3 style="font-family:'Archivo', sans-serif; font-size: 23px; font-weight: 800; color: #28282C; margin: 0 0 6px 0;">David Onyango</h3>
            <div style="font-family:'Archivo', sans-serif; font-size: 13px; font-weight: 700; color: #233F2E; letter-spacing: 0.8px; text-transform: uppercase; margin-bottom: 16px;">
                AI Systems &amp; Predictive Analytics Lead
            </div>
            <p style="font-family:'Archivo', sans-serif; font-size: 14.5px; line-height: 1.6; color: #49433C; margin: 0 0 20px 0;">
                Architect of Agrolink's machine learning core. Specializes in predictive crop demand modeling, satellite yield analytics, and computer vision disease detection across East Africa.
            </p>
        </div>
        <div style="border-top: 1px solid #E5E2DC; padding-top: 16px; display: flex; flex-wrap: wrap; gap: 8px;">
            <span style="background: #F0EEE9; color: #28282C; font-size: 11.5px; font-weight: 700; padding: 4px 10px; border-radius: 6px;">Predictive AI</span>
            <span style="background: #F0EEE9; color: #28282C; font-size: 11.5px; font-weight: 700; padding: 4px 10px; border-radius: 6px;">Demand Modeling</span>
            <span style="background: #F0EEE9; color: #28282C; font-size: 11.5px; font-weight: 700; padding: 4px 10px; border-radius: 6px;">USSD Core</span>
        </div>
    </div>

    <!-- Belamy Maloba -->
    <div class="agrolink-executive-card" style="background:#FFFDF7; border: 1px solid #C4C0BC; border-radius: 14px; padding: 32px 26px; display: flex; flex-direction: column; justify-content: space-between; box-sizing: border-box;">
        <div>
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 22px;">
                <div style="width: 58px; height: 58px; border-radius: 14px; background: linear-gradient(135deg, #233F2E 0%, #15261C 100%); display: flex; align-items: center; justify-content: center; border: 2px solid #AFE67F; box-shadow: 0 4px 14px rgba(35,63,46,0.18);">
                    <span style="font-family:'Archivo', sans-serif; font-size: 21px; font-weight: 800; color: #AFE67F; letter-spacing: 1px;">BM</span>
                </div>
                <span style="background: rgba(35,63,46,0.08); color: #233F2E; border: 1px solid rgba(35,63,46,0.22); font-family:'Archivo', sans-serif; font-size: 11px; font-weight: 800; padding: 5px 12px; border-radius: 20px; letter-spacing: 0.8px; text-transform: uppercase;">
                    Co-Founder
                </span>
            </div>
            <h3 style="font-family:'Archivo', sans-serif; font-size: 23px; font-weight: 800; color: #28282C; margin: 0 0 6px 0;">Belamy Maloba</h3>
            <div style="font-family:'Archivo', sans-serif; font-size: 13px; font-weight: 700; color: #233F2E; letter-spacing: 0.8px; text-transform: uppercase; margin-bottom: 16px;">
                Operations &amp; Supply Chain Lead
            </div>
            <p style="font-family:'Archivo', sans-serif; font-size: 14.5px; line-height: 1.6; color: #49433C; margin: 0 0 20px 0;">
                Directs Agrolink's real-time distribution networks, cold-chain transport coordination, and post-harvest optimization. Focused on cutting food loss from 50% to under 10%.
            </p>
        </div>
        <div style="border-top: 1px solid #E5E2DC; padding-top: 16px; display: flex; flex-wrap: wrap; gap: 8px;">
            <span style="background: #F0EEE9; color: #28282C; font-size: 11.5px; font-weight: 700; padding: 4px 10px; border-radius: 6px;">Cold Chain</span>
            <span style="background: #F0EEE9; color: #28282C; font-size: 11.5px; font-weight: 700; padding: 4px 10px; border-radius: 6px;">Fleet Logistics</span>
            <span style="background: #F0EEE9; color: #28282C; font-size: 11.5px; font-weight: 700; padding: 4px 10px; border-radius: 6px;">Waste Reduction</span>
        </div>
    </div>

    <!-- Melvin Akinyi -->
    <div class="agrolink-executive-card" style="background:#FFFDF7; border: 1px solid #C4C0BC; border-radius: 14px; padding: 32px 26px; display: flex; flex-direction: column; justify-content: space-between; box-sizing: border-box;">
        <div>
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 22px;">
                <div style="width: 58px; height: 58px; border-radius: 14px; background: linear-gradient(135deg, #233F2E 0%, #15261C 100%); display: flex; align-items: center; justify-content: center; border: 2px solid #AFE67F; box-shadow: 0 4px 14px rgba(35,63,46,0.18);">
                    <span style="font-family:'Archivo', sans-serif; font-size: 21px; font-weight: 800; color: #AFE67F; letter-spacing: 1px;">MA</span>
                </div>
                <span style="background: rgba(35,63,46,0.08); color: #233F2E; border: 1px solid rgba(35,63,46,0.22); font-family:'Archivo', sans-serif; font-size: 11px; font-weight: 800; padding: 5px 12px; border-radius: 20px; letter-spacing: 0.8px; text-transform: uppercase;">
                    Co-Founder
                </span>
            </div>
            <h3 style="font-family:'Archivo', sans-serif; font-size: 23px; font-weight: 800; color: #28282C; margin: 0 0 6px 0;">Melvin Akinyi</h3>
            <div style="font-family:'Archivo', sans-serif; font-size: 13px; font-weight: 700; color: #233F2E; letter-spacing: 0.8px; text-transform: uppercase; margin-bottom: 16px;">
                Product &amp; Agronomy Lead
            </div>
            <p style="font-family:'Archivo', sans-serif; font-size: 14.5px; line-height: 1.6; color: #49433C; margin: 0 0 20px 0;">
                Translates agronomic science into intuitive tools for farmers. Coordinates pilot onboarding and field extension training in Kiambu, Nakuru, and Meru counties.
            </p>
        </div>
        <div style="border-top: 1px solid #E5E2DC; padding-top: 16px; display: flex; flex-wrap: wrap; gap: 8px;">
            <span style="background: #F0EEE9; color: #28282C; font-size: 11.5px; font-weight: 700; padding: 4px 10px; border-radius: 6px;">Agronomy UX</span>
            <span style="background: #F0EEE9; color: #28282C; font-size: 11.5px; font-weight: 700; padding: 4px 10px; border-radius: 6px;">Farmer Clusters</span>
            <span style="background: #F0EEE9; color: #28282C; font-size: 11.5px; font-weight: 700; padding: 4px 10px; border-radius: 6px;">Soil Diagnostics</span>
        </div>
    </div>

    <!-- Lavine Niphreen -->
    <div class="agrolink-executive-card" style="background:#FFFDF7; border: 1px solid #C4C0BC; border-radius: 14px; padding: 32px 26px; display: flex; flex-direction: column; justify-content: space-between; box-sizing: border-box;">
        <div>
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 22px;">
                <div style="width: 58px; height: 58px; border-radius: 14px; background: linear-gradient(135deg, #233F2E 0%, #15261C 100%); display: flex; align-items: center; justify-content: center; border: 2px solid #AFE67F; box-shadow: 0 4px 14px rgba(35,63,46,0.18);">
                    <span style="font-family:'Archivo', sans-serif; font-size: 21px; font-weight: 800; color: #AFE67F; letter-spacing: 1px;">LN</span>
                </div>
                <span style="background: rgba(35,63,46,0.08); color: #233F2E; border: 1px solid rgba(35,63,46,0.22); font-family:'Archivo', sans-serif; font-size: 11px; font-weight: 800; padding: 5px 12px; border-radius: 20px; letter-spacing: 0.8px; text-transform: uppercase;">
                    Co-Founder
                </span>
            </div>
            <h3 style="font-family:'Archivo', sans-serif; font-size: 23px; font-weight: 800; color: #28282C; margin: 0 0 6px 0;">Lavine Niphreen</h3>
            <div style="font-family:'Archivo', sans-serif; font-size: 13px; font-weight: 700; color: #233F2E; letter-spacing: 0.8px; text-transform: uppercase; margin-bottom: 16px;">
                Strategic Partnerships &amp; Finance Lead
            </div>
            <p style="font-family:'Archivo', sans-serif; font-size: 14.5px; line-height: 1.6; color: #49433C; margin: 0 0 20px 0;">
                Heads institutional expansion and capital strategy. Manages relationships with county governments, NGOs, agricultural micro-financiers, and commercial banking partners.
            </p>
        </div>
        <div style="border-top: 1px solid #E5E2DC; padding-top: 16px; display: flex; flex-wrap: wrap; gap: 8px;">
            <span style="background: #F0EEE9; color: #28282C; font-size: 11.5px; font-weight: 700; padding: 4px 10px; border-radius: 6px;">AgriFinance</span>
            <span style="background: #F0EEE9; color: #28282C; font-size: 11.5px; font-weight: 700; padding: 4px 10px; border-radius: 6px;">Gov Alliances</span>
            <span style="background: #F0EEE9; color: #28282C; font-size: 11.5px; font-weight: 700; padding: 4px 10px; border-radius: 6px;">Credit Escrow</span>
        </div>
    </div>
</div>
'''

# New Rich Features Section to Inject into Homepage
NEW_PROJECT_FEATURES_HTML = '''
<!-- ==================== NEW SECTION: OFFLINE ACCESSIBILITY & USSD ENGINE ==================== -->
<section class="elementor-element e-flex e-con-boxed cmsmasters-block-default e-con e-parent" style="background:#233F2E; padding: 60px 40px; margin: 24px 0; border-radius: 16px;">
    <div class="e-con-inner" style="max-width: 1200px; margin: 0 auto; width: 100%;">
        <div style="text-align: center; margin-bottom: 40px;">
            <span style="background: rgba(175,230,127,0.15); color: #AFE67F; border: 1px solid rgba(175,230,127,0.3); font-family:'Archivo', sans-serif; font-size: 12px; font-weight: 800; padding: 6px 16px; border-radius: 20px; letter-spacing: 1.5px; text-transform: uppercase;">
                INCLUSIVE AGRI-TECH &bull; SLIDE 12
            </span>
            <h2 style="font-family:'Archivo', sans-serif; font-size: 34px; font-weight: 800; color: #FFFDF7; margin: 16px 0 12px 0;">
                Offline Accessibility: Built for Every African Farmer
            </h2>
            <p style="font-family:'Archivo', sans-serif; font-size: 16px; line-height: 1.6; color: #E5E2DC; max-width: 780px; margin: 0 auto;">
                Over 70% of smallholders farm in rural regions without reliable internet or smartphones. Agrolink’s proprietary USSD and SMS engine ensures zero farmers are left behind.
            </p>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 32px; align-items: center;">
            <!-- Interactive USSD Phone Simulator -->
            <div style="background: #15261C; border: 2px solid #AFE67F; border-radius: 18px; padding: 28px 24px; box-shadow: 0 16px 36px rgba(0,0,0,0.3); font-family: 'Courier New', monospace; color: #AFE67F;">
                <div style="display: flex; align-items: center; justify-content: space-between; border-bottom: 1px solid rgba(175,230,127,0.3); padding-bottom: 12px; margin-bottom: 16px; font-size: 12px; letter-spacing: 1px;">
                    <span>LIVE USSD DIALER</span>
                    <span style="background:#AFE67F; color:#15261C; font-weight:900; padding:2px 8px; border-radius:4px;">*384*254#</span>
                </div>
                <div style="font-size: 14px; line-height: 1.8; color: #FFFDF7; margin-bottom: 16px;">
                    AGROLINK AFRICA SMART MENU<br>
                    Welcome, Kiambu Smallholder Cluster<br>
                    -----------------------------<br>
                    1. Crop Demand Advisory (What to Plant)<br>
                    2. Match Harvest to Supermarket Buyers<br>
                    3. Early Pest &amp; Drought Warning Alerts<br>
                    4. Check Produce Delivery &amp; M-Pesa Payout<br>
                    5. Request Cold Storage Pickup
                </div>
                <div style="background: rgba(175,230,127,0.1); border: 1px dashed #AFE67F; border-radius: 8px; padding: 10px 14px; font-size: 12.5px; color: #AFE67F;">
                    &gt; Zero internet required &bull; Works on basic feature phones &bull; Real-time SMS push in Swahili &amp; English
                </div>
            </div>

            <!-- 3 Pillars of Offline Capability -->
            <div style="display: flex; flex-direction: column; gap: 20px;">
                <div style="background: rgba(255,253,247,0.06); border: 1px solid rgba(255,253,247,0.12); border-radius: 12px; padding: 20px 22px;">
                    <h4 style="font-family:'Archivo', sans-serif; font-size: 18px; font-weight: 800; color: #AFE67F; margin: 0 0 6px 0;">1. USSD Interactive Matching</h4>
                    <p style="font-family:'Archivo', sans-serif; font-size: 14px; line-height: 1.55; color: #E5E2DC; margin: 0;">Farmers dial *384*254# from any 2G phone to log planned harvest volume and receive confirmed purchase bids before cutting crops.</p>
                </div>
                <div style="background: rgba(255,253,247,0.06); border: 1px solid rgba(255,253,247,0.12); border-radius: 12px; padding: 20px 22px;">
                    <h4 style="font-family:'Archivo', sans-serif; font-size: 18px; font-weight: 800; color: #AFE67F; margin: 0 0 6px 0;">2. Automated SMS Early Warning Alerts</h4>
                    <p style="font-family:'Archivo', sans-serif; font-size: 14px; line-height: 1.55; color: #E5E2DC; margin: 0;">Automated localized weather shocks, rainfall forecasts, and pest infestation alerts pushed to farmer phone numbers 3 weeks ahead.</p>
                </div>
                <div style="background: rgba(255,253,247,0.06); border: 1px solid rgba(255,253,247,0.12); border-radius: 12px; padding: 20px 22px;">
                    <h4 style="font-family:'Archivo', sans-serif; font-size: 18px; font-weight: 800; color: #AFE67F; margin: 0 0 6px 0;">3. Instant Mobile Money Settlement</h4>
                    <p style="font-family:'Archivo', sans-serif; font-size: 14px; line-height: 1.55; color: #E5E2DC; margin: 0;">Integrated M-Pesa escrow guarantees that when produce is verified at the collection hub, payment lands directly in the farmer's wallet.</p>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- ==================== NEW SECTION: 4-SEGMENT MARKET OPPORTUNITY MATRIX (SLIDE 8) ==================== -->
<section class="elementor-element e-flex e-con-boxed cmsmasters-block-default e-con e-parent" style="padding: 50px 40px; margin: 24px 0;">
    <div class="e-con-inner" style="max-width: 1200px; margin: 0 auto; width: 100%;">
        <div style="text-align: center; margin-bottom: 36px;">
            <span style="background: rgba(35,63,46,0.08); color: #233F2E; border: 1px solid rgba(35,63,46,0.2); font-family:'Archivo', sans-serif; font-size: 12px; font-weight: 800; padding: 6px 16px; border-radius: 20px; letter-spacing: 1.5px; text-transform: uppercase;">
                MARKET OPPORTUNITY &bull; SLIDE 8
            </span>
            <h2 style="font-family:'Archivo', sans-serif; font-size: 32px; font-weight: 800; color: #28282C; margin: 16px 0 10px 0;">
                Connecting the Entire Agricultural Value Chain
            </h2>
            <p style="font-family:'Archivo', sans-serif; font-size: 15.5px; line-height: 1.6; color: #49433C; max-width: 720px; margin: 0 auto;">
                Agrolink addresses the distinct operational needs of each stakeholder in the African agricultural sector.
            </p>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 20px;">
            <!-- Segment 1: Small Scale Farmers -->
            <div style="background:#FFFDF7; border: 1px solid #C4C0BC; border-radius: 12px; padding: 28px 22px; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                    <span style="font-family:'Archivo', sans-serif; font-size: 12px; font-weight: 800; color: #233F2E; letter-spacing: 1px;">01 &bull; SMALLHOLDERS</span>
                    <h4 style="font-family:'Archivo', sans-serif; font-size: 20px; font-weight: 800; color: #28282C; margin: 10px 0 10px 0;">Small-Scale Farmers</h4>
                    <p style="font-family:'Archivo', sans-serif; font-size: 14px; line-height: 1.6; color: #49433C; margin: 0 0 16px 0;">Over 300,000 farmers accessing predictive crop advisory, fair market pricing, and micro-credit without smartphone barriers.</p>
                </div>
                <div style="border-top: 1px solid #E5E2DC; padding-top: 12px; font-size: 12px; font-weight: 700; color: #233F2E;">
                    &bull; +30% Net Income &bull; Zero Blind Planting
                </div>
            </div>

            <!-- Segment 2: Large Scale Farmers -->
            <div style="background:#FFFDF7; border: 1px solid #C4C0BC; border-radius: 12px; padding: 28px 22px; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                    <span style="font-family:'Archivo', sans-serif; font-size: 12px; font-weight: 800; color: #233F2E; letter-spacing: 1px;">02 &bull; COMMERCIAL</span>
                    <h4 style="font-family:'Archivo', sans-serif; font-size: 20px; font-weight: 800; color: #28282C; margin: 10px 0 10px 0;">Large-Scale Producers</h4>
                    <p style="font-family:'Archivo', sans-serif; font-size: 14px; line-height: 1.6; color: #49433C; margin: 0 0 16px 0;">Enterprise yield modeling, automated forward-contract matching, soil telemetry, and optimized mechanized harvesting schedules.</p>
                </div>
                <div style="border-top: 1px solid #E5E2DC; padding-top: 12px; font-size: 12px; font-weight: 700; color: #233F2E;">
                    &bull; Contract Farming &bull; Precision Yields
                </div>
            </div>

            <!-- Segment 3: Food Distributors -->
            <div style="background:#FFFDF7; border: 1px solid #C4C0BC; border-radius: 12px; padding: 28px 22px; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                    <span style="font-family:'Archivo', sans-serif; font-size: 12px; font-weight: 800; color: #233F2E; letter-spacing: 1px;">03 &bull; AGGREGATORS</span>
                    <h4 style="font-family:'Archivo', sans-serif; font-size: 20px; font-weight: 800; color: #28282C; margin: 10px 0 10px 0;">Food Distributors</h4>
                    <p style="font-family:'Archivo', sans-serif; font-size: 14px; line-height: 1.6; color: #49433C; margin: 0 0 16px 0;">Direct farm-gate procurement, verified quality grading standards, predictable arrival times, and eliminated supplier volatility.</p>
                </div>
                <div style="border-top: 1px solid #E5E2DC; padding-top: 12px; font-size: 12px; font-weight: 700; color: #233F2E;">
                    &bull; Traceable Origin &bull; Bulk Procurement
                </div>
            </div>

            <!-- Segment 4: Logistics & Fleet -->
            <div style="background:#FFFDF7; border: 1px solid #C4C0BC; border-radius: 12px; padding: 28px 22px; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                    <span style="font-family:'Archivo', sans-serif; font-size: 12px; font-weight: 800; color: #233F2E; letter-spacing: 1px;">04 &bull; TRANSPORT</span>
                    <h4 style="font-family:'Archivo', sans-serif; font-size: 20px; font-weight: 800; color: #28282C; margin: 10px 0 10px 0;">Logistics &amp; Cold Storage</h4>
                    <p style="font-family:'Archivo', sans-serif; font-size: 14px; line-height: 1.6; color: #49433C; margin: 0 0 16px 0;">Synchronized pickup routes, minimized empty return journeys (backhauls), and temperature-controlled storage integration.</p>
                </div>
                <div style="border-top: 1px solid #E5E2DC; padding-top: 12px; font-size: 12px; font-weight: 700; color: #233F2E;">
                    &bull; -40% Post-Harvest Loss &bull; Max Fleet Utilization
                </div>
            </div>
        </div>
    </div>
</section>

<!-- ==================== NEW SECTION: ACTIVE COUNTY PILOT HUBS (SLIDE 9) ==================== -->
<section class="elementor-element e-flex e-con-boxed cmsmasters-block-default e-con e-parent" style="background:#F0EEE9; padding: 50px 40px; margin: 24px 0; border-radius: 14px;">
    <div class="e-con-inner" style="max-width: 1200px; margin: 0 auto; width: 100%;">
        <div style="display: flex; flex-wrap: wrap; justify-content: space-between; align-items: flex-end; margin-bottom: 32px; gap: 16px;">
            <div>
                <span style="background: rgba(35,63,46,0.08); color: #233F2E; border: 1px solid rgba(35,63,46,0.2); font-family:'Archivo', sans-serif; font-size: 12px; font-weight: 800; padding: 6px 16px; border-radius: 20px; letter-spacing: 1.5px; text-transform: uppercase;">
                    MVP PILOT LOCATIONS &bull; SLIDE 9
                </span>
                <h2 style="font-family:'Archivo', sans-serif; font-size: 30px; font-weight: 800; color: #28282C; margin: 12px 0 0 0;">
                    Kenya Pilot Hubs: Kiambu, Nakuru &amp; Meru
                </h2>
            </div>
            <span style="font-family:'Archivo', sans-serif; font-size: 14px; font-weight: 700; color: #233F2E; background: #FFFDF7; border: 1px solid #C4C0BC; padding: 8px 18px; border-radius: 20px;">
                Status: Phase 1 Active &bull; Months 1–6
            </span>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px;">
            <!-- Hub 1: Kiambu -->
            <div style="background:#FFFDF7; border: 1px solid #C4C0BC; border-radius: 12px; padding: 26px 22px;">
                <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px;">
                    <h4 style="font-family:'Archivo', sans-serif; font-size: 20px; font-weight: 800; color: #28282C; margin: 0;">Kiambu County Hub</h4>
                    <span style="background:#233F2E; color:#AFE67F; font-size:11px; font-weight:800; padding:3px 10px; border-radius:12px;">PILOT 01</span>
                </div>
                <p style="font-family:'Archivo', sans-serif; font-size: 13.5px; line-height: 1.6; color: #49433C; margin: 0 0 14px 0;">Focus: High-value perishable horticulture, greenhouse vegetables, and instant supermarket direct matching into Nairobi.</p>
                <div style="font-size: 12px; color: #6F6B66; font-weight: 600;">
                    Target: 8,000 Onboarded Smallholders &bull; Average Delivery Time: &lt;4 Hours
                </div>
            </div>

            <!-- Hub 2: Nakuru -->
            <div style="background:#FFFDF7; border: 1px solid #C4C0BC; border-radius: 12px; padding: 26px 22px;">
                <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px;">
                    <h4 style="font-family:'Archivo', sans-serif; font-size: 20px; font-weight: 800; color: #28282C; margin: 0;">Nakuru County Hub</h4>
                    <span style="background:#233F2E; color:#AFE67F; font-size:11px; font-weight:800; padding:3px 10px; border-radius:12px;">PILOT 02</span>
                </div>
                <p style="font-family:'Archivo', sans-serif; font-size: 13.5px; line-height: 1.6; color: #49433C; margin: 0 0 14px 0;">Focus: Grain aggregation (maize, wheat, legumes), cooperative bulk storage hubs, and transit route optimization into Western Kenya.</p>
                <div style="font-size: 12px; color: #6F6B66; font-weight: 600;">
                    Target: 12,000 Onboarded Farmers &bull; Post-Harvest Loss Cut by 38%
                </div>
            </div>

            <!-- Hub 3: Meru -->
            <div style="background:#FFFDF7; border: 1px solid #C4C0BC; border-radius: 12px; padding: 26px 22px;">
                <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px;">
                    <h4 style="font-family:'Archivo', sans-serif; font-size: 20px; font-weight: 800; color: #28282C; margin: 0;">Meru County Hub</h4>
                    <span style="background:#233F2E; color:#AFE67F; font-size:11px; font-weight:800; padding:3px 10px; border-radius:12px;">PILOT 03</span>
                </div>
                <p style="font-family:'Archivo', sans-serif; font-size: 13.5px; line-height: 1.6; color: #49433C; margin: 0 0 14px 0;">Focus: Semi-arid climate resilience, drought-tolerant sorghum, potatoes, and farmer digital training partnerships with county cooperatives.</p>
                <div style="font-size: 12px; color: #6F6B66; font-weight: 600;">
                    Target: 10,000 Onboarded Farmers &bull; 5,000 Trained in Climate-Smart Ag
                </div>
            </div>
        </div>
    </div>
</section>
'''

def enhance_index():
    path = os.path.join(BASE_DIR, 'index.html')
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()

    # 1. Inject Head CSS if not present
    if 'id="agrolink-enhanced-styles"' not in html:
        html = html.replace('</head>', GLOBAL_HEAD_CSS + '\n</head>')

    # 2. Strip cmsmasters-demos-preview toolbar block
    m = re.search(r'<div class=\"cmsmasters-demos-preview\"[^>]*>', html)
    if m:
        start_pos = m.start()
        end_str = '<span>Buy Now</span>\n\t\t\t</a>\n\t\t</div></div>'
        end_pos = html.find(end_str, start_pos)
        if end_pos != -1:
            end_pos += len(end_str)
            html = html[:start_pos] + html[end_pos:]
            print("Stripped cmsmasters-demos-preview block from index.html.")

    # 3. Replace Team Section with Picture-Free Founder Panels
    team_marker = '<div class="agrolink-team-grid"'
    if team_marker in html:
        # replace existing team grid with new advanced founder panels
        html = re.sub(
            r'<div class="agrolink-team-grid".*?</div>\s*</div>\s*</div>\s*</div>\s*(<div class="elementor-element elementor-element-[a-f0-9]+ e-con-full e-flex cmsmasters-block-default e-con e-child")',
            FOUNDER_PANELS_HTML + r'\n</div></div></div>\1',
            html,
            flags=re.DOTALL
        )
    else:
        # replace in 9fd4078
        html = re.sub(
            r'(<div class="elementor-element elementor-element-9fd4078[^"]*"[^>]*>\s*<div class="elementor-widget-container">)(.*?)(</div>\s*</div>)',
            r'\1' + FOUNDER_PANELS_HTML + r'\3',
            html,
            flags=re.DOTALL
        )

    # 4. Inject Rich Project Features before Section 9 (Why Choose Us)
    if 'OFFLINE ACCESSIBILITY &bull; SLIDE 12' not in html:
        pos_sec9 = html.find('elementor-element-70a3550')
        if pos_sec9 != -1:
            sec_start = html.rfind('<section', 0, pos_sec9)
            if sec_start != -1:
                html = html[:sec_start] + NEW_PROJECT_FEATURES_HTML + '\n' + html[sec_start:]
                print("Injected Offline Accessibility, Market Opportunity Matrix & County Pilot Hubs into index.html.")

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print("index.html enhancement completed successfully.")

def enhance_workers_page():
    path = os.path.join(BASE_DIR, 'our-workers/index.html')
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()

    # Inject head CSS
    if 'id="agrolink-enhanced-styles"' not in html:
        html = html.replace('</head>', GLOBAL_HEAD_CSS + '\n</head>')

    # Strip cmsmasters-demos-preview
    m = re.search(r'<div class=\"cmsmasters-demos-preview\"[^>]*>', html)
    if m:
        start_pos = m.start()
        end_str = '<span>Buy Now</span>\n\t\t\t</a>\n\t\t</div></div>'
        end_pos = html.find(end_str, start_pos)
        if end_pos != -1:
            end_pos += len(end_str)
            html = html[:start_pos] + html[end_pos:]

    # Remove all stock photos 63-profile-*.webp and render picture-free founder panels
    # Find the main team container and replace with FOUNDER_PANELS_HTML
    # Look for the section after the title "THE AGROLINK AFRICA TEAM"
    title_pos = html.find('THE AGROLINK AFRICA TEAM')
    if title_pos != -1:
        # Find the next big container
        con_start = html.find('<div class="elementor-element elementor-element-', title_pos)
        # Find "Ask a Question" or "Partner With Our Team"
        ask_pos = html.find('Ask a Question', con_start)
        if ask_pos == -1:
            ask_pos = html.find('Partner With Our Team', con_start)
        if con_start != -1 and ask_pos != -1:
            sec_end = html.rfind('<section', con_start, ask_pos)
            if sec_end != -1:
                html = html[:con_start] + '\n<div style="max-width:1200px; margin: 30px auto; width:100%;">' + FOUNDER_PANELS_HTML + '</div>\n' + html[sec_end:]
                print("Replaced stock photos with advanced founder panels in our-workers/index.html.")

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print("our-workers/index.html updated successfully.")

def enhance_about_us():
    path = os.path.join(BASE_DIR, 'about-us/index.html')
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()

    # Inject head CSS
    if 'id="agrolink-enhanced-styles"' not in html:
        html = html.replace('</head>', GLOBAL_HEAD_CSS + '\n</head>')

    # Strip cmsmasters-demos-preview
    m = re.search(r'<div class=\"cmsmasters-demos-preview\"[^>]*>', html)
    if m:
        start_pos = m.start()
        end_str = '<span>Buy Now</span>\n\t\t\t</a>\n\t\t</div></div>'
        end_pos = html.find(end_str, start_pos)
        if end_pos != -1:
            end_pos += len(end_str)
            html = html[:start_pos] + html[end_pos:]

    # Replace team section in about-us with picture-free founder panels
    meet_pos = html.find('The Founding Team: Agrolink Africa')
    if meet_pos != -1:
        # Replace the profile grid following it
        next_sec = html.find('Our Services', meet_pos)
        if next_sec != -1:
            sec_before_services = html.rfind('<section', meet_pos, next_sec)
            widget_start = html.find('<div class="elementor-element elementor-element-', meet_pos)
            if widget_start != -1 and sec_before_services != -1:
                html = html[:widget_start] + '\n<div style="max-width:1200px; margin: 24px auto; width:100%;">' + FOUNDER_PANELS_HTML + '</div>\n' + html[sec_before_services:]
                print("Replaced team section with advanced founder panels in about-us/index.html.")

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print("about-us/index.html updated successfully.")

def clean_all_html_files():
    count = 0
    for root, dirs, files in os.walk(BASE_DIR):
        for f in files:
            if f.endswith('.html'):
                p = os.path.join(root, f)
                with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
                    c = fp.read()
                orig = c

                # 1. Inject head CSS
                if 'id="agrolink-enhanced-styles"' not in c and '</head>' in c:
                    c = c.replace('</head>', GLOBAL_HEAD_CSS + '\n</head>')

                # 2. Strip cmsmasters-demos-preview block if present
                m = re.search(r'<div class=\"cmsmasters-demos-preview\"[^>]*>', c)
                if m:
                    start_pos = m.start()
                    end_str = '<span>Buy Now</span>\n\t\t\t</a>\n\t\t</div></div>'
                    end_pos = c.find(end_str, start_pos)
                    if end_pos != -1:
                        end_pos += len(end_str)
                        c = c[:start_pos] + c[end_pos:]

                if c != orig:
                    with open(p, 'w', encoding='utf-8') as fp:
                        fp.write(c)
                    count += 1
    print(f"Cleaned demo bars and compressed spacing across {count} HTML files.")

if __name__ == '__main__':
    enhance_index()
    enhance_workers_page()
    enhance_about_us()
    clean_all_html_files()
    print("ALL ENHANCEMENTS APPLIED SUCCESSFULLY!")
