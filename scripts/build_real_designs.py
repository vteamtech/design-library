#!/usr/bin/env python3
"""Build 80 real-world design editions (16 brands × 5 sections)."""
import json, time, subprocess

PROFILES = json.load(open('/tmp/real_design_profiles.json'))
SID = open('/tmp/mcp_sid.txt').read().strip()
API = 'https://willinstructions-new.affinitydns.uk/wp-json/mcp/elementor-mcp-server'
RESULTS = []

def mcp_call(tool, args):
    payload = json.dumps({"jsonrpc": "2.0", "id": 1, "method": "tools/call",
        "params": {"name": tool, "arguments": args}})
    r = subprocess.run(['curl', '-s', '-X', 'POST', API,
        '-H', 'Content-Type: application/json',
        '-H', f'Mcp-Session-Id: {SID}',
        '-d', payload], capture_output=True, text=True, timeout=30)
    data = json.loads(r.stdout)
    content = data.get('result', {}).get('content', [])
    if content:
        return json.loads(content[0]['text'])
    return None

def build_and_save(title, structure):
    r = mcp_call('elementor-mcp-build-page', {"title": title, "structure": structure})
    if not r: return None
    pid = r.get('post_id')
    mcp_call('elementor-mcp-update-page-settings', {"post_id": pid, "settings": {"post_status": "publish"}})
    time.sleep(0.15)
    t = mcp_call('elementor-mcp-save-as-template', {"post_id": pid, "title": title.replace("Library: ", "")})
    tid = t.get('template_id') if t else None
    return {"page_id": pid, "template_id": tid}

def pad(t, r, b, l): return {"unit": "px", "top": str(t), "right": str(r), "bottom": str(b), "left": str(l)}
def rad(v): return {"unit": "px", "top": str(v), "right": str(v), "bottom": str(v), "left": str(v)}
def bw(t, r, b, l): return {"unit": "px", "top": str(t), "right": str(r), "bottom": str(b), "left": str(l)}
def px(v): return {"unit": "px", "size": str(v)}

def s(text, color, size=18, weight='400', family='inherit', transform='none', spacing=0, align='left', lh=1.6, extra=''):
    return f"<p style='color:{color};font-size:{size}px;font-weight:{weight};font-family:{family},sans-serif,serif;text-transform:{transform};letter-spacing:{spacing}px;text-align:{align};line-height:{lh};{extra}'>{text}</p>"

def make_hero(p):
    accent_line = ''
    if p.get('border_width_top', 0) > 0:
        accent_line = {"type": "widget", "widget_type": "html", "settings": {
            "html": f"<div style='width:60px;height:{p['border_width_top']}px;background:{p['accent']};margin:0 auto;'></div>"}}
    children = []
    if accent_line: children.append(accent_line)
    children += [
        {"type": "widget", "widget_type": "html", "settings": {
            "html": s("Design That Makes<br>a Statement", p['text'], p['heading_size_h1'], p['heading_weight'], p['heading_font'], p['heading_transform'], p['letter_spacing'], 'center', 1.1)}},
        {"type": "widget", "widget_type": "html", "settings": {
            "html": s("Every great brand deserves a digital presence that reflects its unique character. We craft experiences that resonate.", p['text_light'], 18, '400', p['body_font'], 'none', 0, 'center', 1.7, 'max-width:600px;margin:0 auto;')}},
        {"type": "container", "settings": {"flex_direction": "row", "gap": px(16), "align_items": "center"},
         "children": [
            {"type": "widget", "widget_type": "html", "settings": {
                "html": f"<a href='/contact' style='display:inline-block;padding:{p['btn_padding']}px 36px;background:{p['accent']};color:{p['bg']};text-decoration:none;font-weight:700;font-family:{p['heading_font']},sans-serif;text-transform:{p['heading_transform']};letter-spacing:{p['letter_spacing']}px;border-radius:{p['btn_radius']}px;font-size:15px;'>Get Started</a>"}},
            {"type": "widget", "widget_type": "html", "settings": {
                "html": f"<a href='/about' style='display:inline-block;padding:{p['btn_padding']}px 36px;background:transparent;color:{p['text']};text-decoration:none;font-weight:600;border:2px solid {p['text']};border-radius:{p['btn_radius']}px;font-size:15px;'>Learn More</a>"}}]}
    ]
    return [{"type": "container", "settings": {
        "flex_direction": "column", "content_width": "full",
        "padding": pad(p['section_padding'], 40, p['section_padding'], 40),
        "background_background": "classic", "background_color": p['bg'],
        "align_items": "center", "gap": px(24)},
        "children": children}]

def make_features(p):
    items = [("01","Strategy","Research-driven insights that guide every decision."),("02","Design","Beautiful interfaces crafted with attention to detail."),("03","Build","Robust solutions built on proven technology."),("04","Support","Ongoing partnership for lasting success.")]
    cards = []
    for num, title, desc in items:
        td = title.upper() if p['heading_transform']=='uppercase' else title
        cs = {"flex_direction": "column", "width": {"unit": "%", "size": 25},
            "padding": pad(p['card_padding'], 20, p['card_padding'], 20),
            "background_background": "classic", "background_color": p['bg'], "gap": px(12)}
        if p['border_style'] != 'none':
            cs["border_border"] = p['border_style']
            cs["border_width"] = bw(p['border_width_top'], 1, 1, 1)
            cs["border_color"] = p['border_color']
            cs["border_radius"] = rad(int(p['border_radius']))
        cards.append({"type": "container", "settings": cs, "children": [
            {"type": "widget", "widget_type": "html", "settings": {"html": s(num, p['accent'], 32, p['heading_weight'], p['heading_font'])}},
            {"type": "widget", "widget_type": "html", "settings": {"html": s(td, p['text'], 16, '700', p['heading_font'], p['heading_transform'])}},
            {"type": "widget", "widget_type": "html", "settings": {"html": s(desc, p['text_light'], 14, '400', p['body_font'])}}
        ]})
    return [{"type": "container", "settings": {
        "flex_direction": "column", "content_width": "full",
        "padding": pad(60, 40, 60, 40),
        "background_background": "classic", "background_color": p['bg_alt'],
        "align_items": "center", "gap": px(40)},
        "children": [
            {"type": "widget", "widget_type": "html", "settings": {"html": s("WHAT WE DO", p['text'], p['heading_size_h2'], p['heading_weight'], p['heading_font'], p['heading_transform'], p['letter_spacing'], 'center')}},
            {"type": "container", "settings": {"flex_direction": "row", "content_width": "full", "gap": px(16), "flex_wrap": "wrap"}, "children": cards}
    ]}]

def make_cta(p):
    return [{"type": "container", "settings": {
        "flex_direction": "column", "content_width": "boxed",
        "padding": pad(70, 40, 70, 40),
        "background_background": "classic", "background_color": p['dark_bg'],
        "align_items": "center", "gap": px(24)},
        "children": [
            {"type": "widget", "widget_type": "html", "settings": {"html": s("Ready to Get Started?", p['dark_text'], 40, p['heading_weight'], p['heading_font'], p['heading_transform'], p['letter_spacing'], 'center', 1.2)}},
            {"type": "widget", "widget_type": "html", "settings": {"html": s("Take the first step. We'll handle the rest with care and precision.", p['text_light'], 16, '400', p['body_font'], 'none', 0, 'center', 1.6, 'max-width:500px;')}},
            {"type": "widget", "widget_type": "html", "settings": {"html": f"<div style='text-align:center;'><a href='/contact' style='display:inline-block;padding:{p['btn_padding']}px 40px;background:{p['accent']};color:{p['dark_bg']};text-decoration:none;font-weight:700;font-family:{p['heading_font']},sans-serif;border-radius:{p['btn_radius']}px;font-size:15px;'>Contact Us Today</a></div>"}}
    ]}]

def make_testimonial(p):
    return [{"type": "container", "settings": {
        "flex_direction": "column", "content_width": "boxed",
        "padding": pad(70, 40, 70, 40),
        "background_background": "classic", "background_color": p['bg'],
        "align_items": "center", "gap": px(16)},
        "children": [
            {"type": "widget", "widget_type": "html", "settings": {"html": s("\u201c", p['accent'], 100, '400', p['heading_font'], 'none', 0, 'center', 1, 'margin:0;line-height:0.5;')}},
            {"type": "widget", "widget_type": "html", "settings": {"html": s("Working with this team was transformative. They understood our vision perfectly and delivered beyond our expectations.", p['text'], 22, '400', p['body_font'], 'none', 0, 'center', 1.7, 'max-width:700px;')}},
            {"type": "widget", "widget_type": "html", "settings": {"html": f"<div style='width:40px;height:2px;background:{p['accent']};margin:10px auto;'></div>"}},
            {"type": "widget", "widget_type": "html", "settings": {"html": s("ALEXANDRA REID, FOUNDER & CEO", p['accent'], 13, '600', p['body_font'], 'none', p['letter_spacing'], 'center')}}
    ]}]

def make_footer(p):
    col_data = [("COMPANY","Building exceptional digital experiences since 2024."),("NAVIGATION","Home<br>About<br>Services<br>Contact"),("SERVICES","Strategy<br>Design<br>Build<br>Support"),("CONTACT","hello@company.com<br>+44 20 1234 5678")]
    cols = []
    for title, content in col_data:
        cols.append({"type": "container", "settings": {"flex_direction": "column", "width": {"unit": "%", "size": 25}, "gap": px(12)},
            "children": [
                {"type": "widget", "widget_type": "html", "settings": {"html": s(title, p['accent'], 12, '700', p['heading_font'], 'uppercase', p['letter_spacing'])}},
                {"type": "widget", "widget_type": "html", "settings": {"html": s(content, p['text_light'], 13, '400', p['body_font'])}}
            ]})
    return [{"type": "container", "settings": {"flex_direction": "row", "content_width": "full", "padding": pad(50, 40, 30, 40), "background_background": "classic", "background_color": p['dark_bg'], "gap": px(0), "flex_wrap": "wrap"}, "children": cols},
            {"type": "widget", "widget_type": "html", "settings": {"html": f"<div style='height:1px;background:{p['accent']}33;margin:0 40px;'></div>"}},
            {"type": "widget", "widget_type": "html", "settings": {"html": s("\u00a9 2024 Company. All rights reserved.", p['text_light'], 11, '400', p['body_font'], 'none', 0, 'center', 1.6, 'padding:15px 40px 25px;')}}]

generators = {'hero': make_hero, 'features': make_features, 'cta': make_cta, 'testimonial': make_testimonial, 'footer': make_footer}
phil_order = list(PROFILES.keys())
sections = ['hero', 'features', 'cta', 'testimonial', 'footer']

for phil in phil_order:
    p = PROFILES[phil]
    print(f"\n{'='*50}")
    print(f"Building: {p['label']} ({phil})")
    print(f"{'='*50}")
    for sec in sections:
        title = f"Library: {phil}-{sec}"
        struct = generators[sec](p)
        r = build_and_save(title, struct)
        if r:
            RESULTS.append({"philosophy": phil, "section": sec, "label": p['label'], "page_id": r['page_id'], "template_id": r['template_id']})
            print(f"  ✅ {sec:12s} → page {r['page_id']}, template {r['template_id']}")
        else:
            print(f"  ❌ {sec:12s} → FAILED")
        time.sleep(0.3)

print(f"\nBUILT: {len(RESULTS)}/80")
with open('/tmp/real_design_results.json', 'w') as f:
    json.dump(RESULTS, f, indent=2)

print("\nBrand            | Hero  | Feat  | CTA   | Test  | Footer")
print("-" * 70)
for phil in phil_order:
    p = PROFILES[phil]
    row = f"{p['label']:17s}|"
    for sec in sections:
        m = [r for r in RESULTS if r['philosophy'] == phil and r['section'] == sec]
        row += f" {m[0]['page_id']:5d} |" if m else " FAIL  |"
    print(row)
