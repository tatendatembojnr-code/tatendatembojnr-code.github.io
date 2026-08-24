import re

with open('C:\\Users\\Stark\\Desktop\\portfolio_site\\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Nav Brand
content = content.replace('Luminary<span>Platform</span>', 'TATENDA.<span>DEV</span>')

# Hero
content = content.replace('Workflows that<br><em>think ahead</em>', 'Architecting The Future<br><em>Of Digital ERPs</em>')
content = content.replace('Luminary connects your tools, automates the repetitive, and surfaces insights\n      before you know to ask. Built for teams that refuse to settle.', 'Tatenda is a premium software engineer building powerful ERPs, elegant APIs, and high-impact web architectures.')

# Hero Metrics
content = re.sub(
    r'<div class="metric-value"><span class="counter" data-target="99\.9" data-decimals="1">0\.0</span><span>%</span></div>\s*<div class="metric-label">Uptime SLA</div>',
    '<div class="metric-value"><span class="counter" data-target="5" data-decimals="0">0</span><span>+</span></div>\n        <div class="metric-label">Years Experience</div>',
    content
)

content = re.sub(
    r'<div class="metric-value"><span class="counter" data-target="4200" data-decimals="0">0</span><span>\+</span></div>\s*<div class="metric-label">Teams Active</div>',
    '<div class="metric-value"><span class="counter" data-target="15" data-decimals="0">0</span><span>+</span></div>\n        <div class="metric-label">Enterprise Modules</div>',
    content
)

content = re.sub(
    r'<div class="metric-value"><span class="counter" data-target="12" data-decimals="0">0</span><span>ms</span></div>\s*<div class="metric-label">Avg Latency</div>',
    '<div class="metric-value"><span class="counter" data-target="99" data-decimals="0">0</span><span>%</span></div>\n        <div class="metric-label">Client Satisfaction</div>',
    content
)

# Ticker
old_ticker = '''      <span class="ticker-item">Meridian Labs</span><span class="ticker-dot"></span>
      <span class="ticker-item">Vertex Capital</span><span class="ticker-dot"></span>
      <span class="ticker-item">Arcline Systems</span><span class="ticker-dot"></span>
      <span class="ticker-item">Nova Engineering</span><span class="ticker-dot"></span>
      <span class="ticker-item">Prism Analytics</span><span class="ticker-dot"></span>
      <span class="ticker-item">Helix Health</span><span class="ticker-dot"></span>
      <span class="ticker-item">Stratos AI</span><span class=\"ticker-dot\"></span>
      <span class=\"ticker-item\">Cobalt Finance</span><span class=\"ticker-dot\"></span>'''

new_ticker = '''      <span class="ticker-item">Python</span><span class="ticker-dot"></span>
      <span class="ticker-item">Django</span><span class="ticker-dot"></span>
      <span class="ticker-item">Odoo</span><span class="ticker-dot"></span>
      <span class="ticker-item">PostgreSQL</span><span class="ticker-dot"></span>
      <span class="ticker-item">Linux</span><span class="ticker-dot"></span>
      <span class="ticker-item">JavaScript</span><span class="ticker-dot"></span>
      <span class="ticker-item">AWS</span><span class="ticker-dot"></span>
      <span class="ticker-item">REST APIs</span><span class="ticker-dot"></span>'''
content = content.replace(old_ticker, new_ticker)
content = content.replace('Trusted by forward-thinking teams', 'Empowered by enterprise-grade technologies')

# Features Section -> Projects
content = content.replace('      <div class="section-badge">The Platform</div>\n      <h2 class="section-title">An OS for your<br><em>business logic</em></h2>', '      <div class="section-badge">Projects Showcase</div>\n      <h2 class="section-title">Engineered Perfection<br><em>At Its Finest</em></h2>')

content = content.replace('Visual Builder', 'Zimra Fiscalisation')
content = content.replace('Drag, drop, and connect APIs without writing a single line of integration code. Watch your logic flow visually.', 'Real-time tax integration engine bridging Odoo with Zimbabwe Revenue Authority for automated compliance.')

content = content.replace('Predictive Routing', 'Logistics & Trucking')
content = content.replace('Let Luminary’s engine analyze payload contents and automatically route exceptions to the right human reviewer.', 'Custom modules for fleet management, activities tracking, and job card allocation across vast enterprise operations.')

content = content.replace('Unified Audit', 'Desktop POS Sync')
content = content.replace('Every action, automated or manual, is logged in an immutable, searchable ledger for total compliance.', 'Robust offline-to-online synchronization connecting third-party desktop POS systems with the centralized Odoo database.')

content = content.replace('Dynamic Webhooks', 'Matrix ERP System')
content = content.replace('Trigger external systems based on complex logic gates. If this, and that, but not those—then fire.', 'A comprehensive, ground-up ERP solution built using the Django framework to manage multiple institutional workflows.')

# Pricing -> Services
content = content.replace('id="pricing"', 'id="services"')
content = content.replace('<li><a href="#pricing">Pricing</a></li>', '<li><a href="#services">Services</a></li>')
content = content.replace('href="#pricing" class="nav-cta"', 'href="#contact" class="nav-cta"')
content = content.replace('href="#pricing" class="btn-primary"', 'href="#contact" class="btn-primary"')
content = content.replace('href="#pricing" class="mobile-menu-link"', 'href="#services" class="mobile-menu-link"')
content = content.replace('Pricing Plans', 'Service Offerings')
content = content.replace('Transparent pricing<br><em>for every stage</em>', 'Enterprise Solutions<br><em>For Every Stage</em>')

content = content.replace('Starter', 'Custom Modules')
content = content.replace('$49', '$500+')
content = content.replace('/mo', '')
content = content.replace('For small teams building their first automated workflows.', 'For businesses needing specific Odoo or Django extensions.')

content = content.replace('Professional', 'Full ERP Deployment')
content = content.replace('$199', '$2000+')
content = content.replace('For growing businesses needing advanced logic and higher limits.', 'End-to-end Odoo or Django implementation for enterprise.')

content = content.replace('Enterprise', 'API Integration')
content = content.replace('Custom', '$1000+')
content = content.replace('For large organizations requiring SLA, SSO, and dedicated support.', 'Connecting 3rd-party systems like Zimra, POS, or legacy tools.')

# Testimonials & Integrations
content = content.replace('Customer Stories', 'Client Feedback')
content = content.replace('Loved by operators<br><em>worldwide</em>', 'Proven Enterprise<br><em>Track Record</em>')
content = content.replace('The Ecosystem', 'Tech Stack')
content = content.replace('Plays nice with<br><em>your stack</em>', 'Deep Expertise<br><em>In Modern Tools</em>')
content = content.replace('Luminary natively integrates with over 200 of the tools your team already uses.', 'I build robust systems using industry-standard enterprise technologies.')

# Bottom CTA
content = content.replace('Ready to upgrade<br><em>your workflow?</em>', 'Ready to architect<br><em>your next system?</em>')
content = content.replace('Start Free Trial', 'Contact Me')

with open('C:\\Users\\Stark\\Desktop\\portfolio_site\\index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Index updated!')
