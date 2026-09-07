import re

projects = [
    {
        "title": "Havano All-In-One",
        "desc": "The grand master piece suite of interconnected modules, serving as the ultimate backbone for enterprise operations and seamless API extensions.",
        "tags": ["Odoo", "Enterprise", "Architecture"],
        "image": "resources/Login Customizer Havano All In One.png"
    },
    {
        "title": "Havano Odoo API",
        "desc": "Native Odoo session-based REST API for seamless POS synchronization. Features intelligent SKU matching, idempotent sales processing, and real-time stock queries.",
        "tags": ["Odoo", "REST API", "Python"],
        "image": "resources/api_icon.png"
    },
    {
        "title": "Odoo to Frappe/ERPNext Sync",
        "desc": "Bi-directional data synchronization bridge connecting Odoo instances with Frappe/ERPNext systems for distributed operations.",
        "tags": ["Odoo", "Frappe", "ERPNext", "Sync"],
        "image": "resources/api_icon.png"
    },
    {
        "title": "Custom Profit and Loss",
        "desc": "Advanced financial reporting module delivering highly customizable Profit and Loss statements tailored to specific accounting practices.",
        "tags": ["Odoo", "Accounting", "Reporting"],
        "image": "resources/profit and loss.png"
    },
    {
        "title": "Dynamic Balance Sheet Report",
        "desc": "Custom Balance Sheet reporting module, designed to complement Profit and Loss insights with real-time assets, liabilities, and equity analysis.",
        "tags": ["Odoo", "Accounting", "Reporting"],
        "image": "resources/balance sheet.png"
    },
    {
        "title": "Trucking",
        "desc": "Comprehensive logistics and trucking management module for Odoo. Handles vehicle routing, driver assignments, and maintenance schedules.",
        "tags": ["Odoo", "Logistics", "Python"],
        "image": "resources/Trucking App.png"
    },
    {
        "title": "Job Card Management",
        "desc": "Custom workflow for managing job cards, technician assignments, time tracking, and material consumption within Odoo.",
        "tags": ["Odoo", "Workflow", "Python"],
        "image": "resources/job card management app.png"
    },
    {
        "title": "Desktop POS ERP",
        "desc": "Custom desktop Point of Sale application tightly integrated with Odoo ERP for robust offline/online sales handling.",
        "tags": ["Odoo", "POS", "Desktop"],
        "image": "resources/desktop pos.png"
    },
    {
        "title": "Activities Management",
        "desc": "Advanced CRM activities module enhancing user task tracking, automated follow-ups, and calendar integration.",
        "tags": ["Odoo", "CRM", "Python"],
        "image": "resources/activities managemnt.png"
    },
    {
        "title": "Odoo Sage API",
        "desc": "Bi-directional synchronization between Odoo and Sage Pastel Evolution SDK via C# API covering sales, users, quotes, invoices, and cashbook.",
        "tags": ["Odoo", "Sage API", "C#"],
        "image": "resources/sage odoo sync.png"
    },
    {
        "title": "Requisition App",
        "desc": "Internal procurement and requisition management app enforcing approval workflows and budget limits.",
        "tags": ["Odoo", "Procurement"],
        "image": "resources/requation app.png"
    },
    {
        "title": "Cashbook App",
        "desc": "Simplified financial tracking application for rapid cashbook entries, reconciliations, and reporting.",
        "tags": ["Odoo", "Accounting"],
        "image": "resources/cash book.png"
    },
    {
        "title": "Custom Invoice Templates",
        "desc": "Bespoke print formats and PDF designs for professional Odoo invoicing tailored to client brand guidelines.",
        "tags": ["Odoo", "QWeb", "XML/CSS"],
        "image": "resources/Custom Print Format 1.png"
    },
    {
        "title": "Windows Odoo 19 Deployment Engine",
        "desc": "Automated deployment engine for Odoo 19 on Windows. Configures the database, handles instance management, and streamlines the complete setup process.",
        "tags": ["Odoo 19", "Windows", "Deployment"],
        "image": "resources/windows odoo 19 deployment engine and instance management.png"
    },
    {
        "title": "Management CRM App",
        "desc": "Tailor-made lead and CRM management system built specifically to meet a client's unique sales processes.",
        "tags": ["Odoo", "CRM"],
        "image": "resources/crm_icon.png"
    },
    {
        "title": "Zim Localisation Payroll",
        "desc": "Comprehensive Zimbabwe payroll module with predefined ZIMRA rules, complex salary structures, and multi-currency support.",
        "tags": ["Odoo", "Payroll", "Localisation"],
        "image": "resources/hr_icon.png"
    },
    {
        "title": "White Label App",
        "desc": "Module to completely remove 'Powered by Odoo' branding from the website and backend for enterprise clients.",
        "tags": ["Odoo", "Branding"],
        "image": "resources/white label app.png"
    },
    {
        "title": "Multi UoM Addon",
        "desc": "Advanced Unit of Measure customization to handle complex product conversions in sales and inventory.",
        "tags": ["Odoo", "Inventory"],
        "image": "resources/stock_icon.png"
    },
    {
        "title": "Offline/Online Sync API",
        "desc": "API architecture designed to sync sales and purchases from an offline desktop machine to a cloud-hosted Odoo server.",
        "tags": ["Odoo", "Sync API"],
        "image": "resources/api_icon.png"
    },
    {
        "title": "Scrap Analytic Automation",
        "desc": "Automated workflow for managing and analyzing inventory scrap, tightly integrated with accounting analytics.",
        "tags": ["Odoo", "Inventory", "Analytics"],
        "image": "resources/stock_icon.png"
    },
    {
        "title": "Disallow Duplicates Module",
        "desc": "Custom validation addon that strictly prevents the creation of duplicate products, customers, and suppliers.",
        "tags": ["Odoo", "Data Integrity"],
        "image": "resources/disallow duplicate modules.png"
    },
    {
        "title": "HR Performance App",
        "desc": "Custom HR appraisal and 360-degree feedback module for Odoo, managing KPIs, goals, and periodic reviews.",
        "tags": ["Odoo", "HR"],
        "image": "resources/hr_icon.png"
    },
    {
        "title": "WhatsApp API Integration",
        "desc": "Seamlessly send notifications, invoices, and quotes directly to clients via WhatsApp directly from Odoo records.",
        "tags": ["Odoo", "WhatsApp API", "Python"],
        "image": "resources/whatsapp_icon.svg"
    },
    {
        "title": "Fleet Analytics Dashboard",
        "desc": "Advanced reporting and telemetry data integration for the Odoo Fleet module, offering real-time cost and usage metrics.",
        "tags": ["Odoo", "Fleet", "Analytics"],
        "image": "resources/fleet_icon.png"
    },
    {
        "title": "Helpdesk SLA Automation",
        "desc": "Custom module to automatically assign, escalate, and alert on helpdesk tickets based on complex SLA rules.",
        "tags": ["Odoo", "Helpdesk", "Automation"],
        "image": "resources/odoo_logo.png"
    },
    {
        "title": "Sales Target Automation",
        "desc": "Dynamic sales target tracking module with automated commission calculations and real-time dashboard visualizations.",
        "tags": ["Odoo", "Sales"],
        "image": "resources/sales_icon.png"
    },
    {
        "title": "Accounting Budget Management App",
        "desc": "Comprehensive budget management application for Odoo accounting to track and manage financial forecasts and expenditure.",
        "tags": ["Odoo", "Accounting", "Budgeting"],
        "image": "resources/odoo_logo.png"
    },
    {
        "title": "Statement of Financial Position",
        "desc": "Advanced financial reporting module delivering accurate and real-time Statement of Financial Position insights.",
        "tags": ["Odoo", "Accounting", "Reporting"],
        "image": "resources/odoo_logo.png"
    },
    {
        "title": "Insurance Profit and Loss",
        "desc": "Custom Profit and Loss reporting module tailored specifically for the insurance industry's unique financial metrics.",
        "tags": ["Odoo", "Accounting", "Insurance"],
        "image": "resources/profit and loss.png"
    },
    {
        "title": "Statement of Income",
        "desc": "Detailed Statement of Income module providing comprehensive revenue and expense tracking for deep financial analysis.",
        "tags": ["Odoo", "Accounting", "Reporting"],
        "image": "resources/odoo_logo.png"
    }
]

html_cards = []
for p in projects:
    tags_html = "".join([f'<span class="project-tag">{t}</span>' for t in p['tags']])
    
    if "image" in p:
        # Check if it's an icon downloaded from Odoo
        if "_icon.png" in p["image"] or "_logo.png" in p["image"] or "whatsapp_icon.svg" in p["image"]:
             image_html = f'<img src="{p["image"]}" alt="{p["title"]}" class="project-image" style="object-fit: contain; padding: 40px; background: rgba(255, 255, 255, 0.05);">'
        else:
             image_html = f'<img src="{p["image"]}" alt="{p["title"]}" class="project-image">'
    else:
        image_html = '<div class="project-image-placeholder">Screenshot Pending</div>'

    card = f"""
      <div class="project-card reveal">
        {image_html}
        <div class="project-info">
          <h3 class="project-title">{p['title']}</h3>
          <p class="project-desc">{p['desc']}</p>
          <div class="project-tags">
            {tags_html}
          </div>
        </div>
      </div>"""
    html_cards.append(card)

projects_html = f"""
  <div class="projects-header reveal">
    <h1>Featured Projects</h1>
    <div class="projects-counter">
      <span class="counter" data-target="{len(projects)}" data-decimals="0">{len(projects)}</span>+
      <span class="projects-counter-label">Custom Modules & Integrations</span>
    </div>
    <p class="section-body" style="margin: 0 auto;">A collection of my custom Odoo ERP modules, API integrations, and desktop architectures.</p>
  </div>
  
  <div class="projects-grid-container">
    <div class="projects-grid">
      {"".join(html_cards)}
    </div>
  </div>
"""

file_path = r'c:\Users\Stark\Desktop\portfolio_site\projects.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace everything from <section class="hero" id="hero"> up to the footer-cta
pattern = r'<div class="projects-header reveal">.*?(?=<!-- ═══ FOOTER CTA ═══ -->)'
content = re.sub(pattern, projects_html, content, flags=re.DOTALL)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated projects.html successfully with", len(projects), "projects and screenshots.")
