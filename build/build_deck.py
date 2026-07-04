#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""NikoMom Reimagined — Workshop 1 (Brand Council). Board-level strategic recommendation."""
from brandkit import *
from brandkit import _blank, _set_font, _set_font as _sf

prs = new_deck()
N = 0
def num():
    global N; N += 1; return N

# ============================================================ 1. COVER
s = _blank(prs)
rect(s, 0, 0, 13.34, 7.5, fill=WHITE)
rect(s, 0, 0, 0.28, 7.5, fill=PINK)
rect(s, 0.28, 0, 0.10, 7.5, fill=PURPLE)
# centered logo lockup
lb = rect(s, 5.55, 1.15, 0.95, 0.95, fill=PINK, shape=MSO_SHAPE.ROUNDED_RECTANGLE); lb.adjustments[0]=0.28
tf=lb.text_frame; tf.vertical_anchor=MSO_ANCHOR.MIDDLE
for m in ('left','right','top','bottom'): setattr(tf,f'margin_{m}',0)
p=tf.paragraphs[0]; p.alignment=PP_ALIGN.CENTER; r=p.add_run(); r.text="7N"; _set_font(r,32,WHITE,True,False,TITLE_FONT)
txt(s, 6.6, 1.24, 4.5, 0.9, [[("Panacea Biotec",22,PURPLE,True,False,TITLE_FONT)],
    [("BEST IN GOODNESS",11,CHAR,True,False,BODY_FONT)]], anchor=MSO_ANCHOR.MIDDLE, space_after=2)
txt(s, 0.9, 2.75, 11.5, 0.4, [[("BRAND CREATION WORKSHOP 1  ·  REIMAGINED FROM FIRST PRINCIPLES",13,PINK,True)]], align=PP_ALIGN.CENTER)
txt(s, 0.9, 3.25, 11.5, 1.6, [[("NikoMom",64,PURPLE,True,False,TITLE_FONT)],
    [("Building India's most trusted, globally scalable baby-care system",22,CHAR,False,False,TITLE_FONT)]],
    align=PP_ALIGN.CENTER, space_after=6)
divider(s, x=4.4, y=5.15, w=4.5)
txt(s, 0.9, 5.4, 11.5, 0.9,
    [[("A board-level strategic recommendation by the Global Brand Council",13,CHAR,False,True)],
     [("Challenge everything. Keep only what survives scrutiny.",12,GREY,False,True)]],
    align=PP_ALIGN.CENTER, space_after=3)
txt(s, 0.9, 6.85, 11.5, 0.3, [[("July 2026   ·   Confidential. Circulation Restricted.",9,GREY)]], align=PP_ALIGN.CENTER)

# ============================================================ 2. MANDATE
s = content_slide(prs, num(), "The mandate: do not redesign — reimagine", kicker="Why we are here")
divider(s)
txt(s, 0.5, 1.75, 7.0, 1.4,
    [[("We were not asked to refine packaging. We were asked whether ",13,CHAR),
      ("the current direction is the strongest possible direction",13,PINK,True),
      (" — and to replace it if it is not.",13,CHAR)],
     [("Everything in the existing workshop — positioning, technologies, trust architecture, layouts — is treated as a ",12,CHAR),
      ("hypothesis, not a decision.",12,PURPLE,True)]], space_after=8, line_spacing=1.2)
# assumptions we broke
card(s, 7.7, 1.7, 5.1, 5.0, fill=SOFTPK)
txt(s, 8.0, 1.9, 4.6, 0.4, [[("SIX ASSUMPTIONS WE PUT ON TRIAL",11,PINK,True)]])
assumptions = [
    ("The category needs another “safe” brand", "“Safe” is now table-stakes hygiene, not a difference."),
    ("NikoMom should be a “Baby Care Expert”", "Expertise talks down; parents want to feel capable."),
    ("Trust is the goal", "Trust is the entry ticket. Confidence is the prize."),
    ("Science is the differentiator", "Everyone claims science. Proven outcomes differentiate."),
    ("Four proprietary technologies add value", "They add cost and confusion for a young brand."),
    ("The mother is the hero", "The baby's protected skin is the hero; the parent is the winner."),
]
yy = 2.4
for i,(a,b) in enumerate(assumptions):
    txt(s, 8.05, yy, 4.5, 0.7,
        [[("✕  ",11,PINK,True),(a,11.5,PURPLE,True)],
         [("     "+b,10,CHAR)]], space_after=1, line_spacing=1.02)
    yy += 0.71

# ============================================================ 3. THE COUNCIL
s = content_slide(prs, num(), "The Brand Council in the room", kicker="Twenty-seven points of view")
divider(s)
txt(s, 0.5, 1.7, 12.3, 0.5, [[("Every recommendation in this document was pressure-tested from three angles: ",12,CHAR),
    ("world-class brand craft, category-specific expertise, and the behavioural science of how parents actually buy.",12,PURPLE,True)]], line_spacing=1.15)
cols = [
    ("BRAND & DESIGN CRAFT", PURPLE, ["Pentagram","DesignStudio","Base Design","Jones Knowles Ritchie","Landor","Interbrand","Wolff Olins","Lippincott","IDEO","Apple Industrial Design"]),
    ("CATEGORY & SKIN EXPERTISE", PINK, ["P&G Baby Care","Kimberly-Clark","Unilever Baby Care","Johnson's Baby","Mustela","Sebamed","CeraVe","Dove Baby","Pediatric Dermatologists","Packaging Engineers"]),
    ("COMMERCE & BEHAVIOUR", BLUE, ["Consumer Psychologists","Behavioural Economists","Information Architects","Semiotics Experts","FMCG Growth Strategists","Retail Shelf Experts","Amazon Marketplace Specialists"]),
]
x = 0.5
for head, col, names in cols:
    card(s, x, 2.35, 3.94, 4.35, fill=SOFT)
    rect(s, x, 2.35, 3.94, 0.5, fill=col, shape=MSO_SHAPE.ROUNDED_RECTANGLE).adjustments[0]=0.12
    rect(s, x, 2.6, 3.94, 0.25, fill=col)
    txt(s, x+0.2, 2.42, 3.6, 0.4, [[(head,11,WHITE,True)]], anchor=MSO_ANCHOR.MIDDLE)
    body = [[("•  "+nm,11,CHAR)] for nm in names]
    txt(s, x+0.28, 3.0, 3.5, 3.6, body, space_after=3.5, line_spacing=1.0)
    x += 4.12

# ============================================================ 4. EXECUTIVE SUMMARY
s = content_slide(prs, num(), "The recommendation, up front", kicker="Executive summary")
divider(s)
card(s, 0.5, 1.7, 12.33, 1.55, fill=PURPLE)
txt(s, 0.85, 1.9, 11.7, 1.2,
    [[("Reposition NikoMom from “Baby Care Expert” to ",16,WHITE,False),
      ("India's Baby Skin-Barrier Company",16,WHITE,True),(" — the pharma-backed brand that ",16,WHITE),
      ("protects and builds a baby's skin barrier, and turns anxious parents into confident ones through visible proof.",16,WHITE,True)],
     [("Emotional territory owned: CONFIDENCE, not reassurance.    Signature idea: “Protection, proven.”",12.5,RGBColor(0xE7,0xD8,0xF0),False,True)]],
    space_after=8, line_spacing=1.12)
pts = [
    ("Why this wins","Backed by Panacea Biotec's pharma credibility, it claims a moat that D2C 'natural' brands (Mamaearth) and legacy players (Johnson's) cannot copy.",PINK),
    ("What changes","One master technology (BarrierNest™) replaces four '-Nests'. Outcome & proof lead the pack, not 'safe/toxin-free'. Keep the name — replace what it means.",BLUE),
    ("What it unlocks","A system — skin, bath, wipes, diapers today; first-1000-days healthcare, nutrition, subscriptions and community tomorrow — all under one science spine.",GREEN),
]
x=0.5
for h,b,c in pts:
    card(s, x, 3.5, 3.94, 3.2, fill=SOFT)
    rect(s, x+0.25, 3.75, 0.5, 0.09, fill=c)
    txt(s, x+0.25, 3.95, 3.45, 0.5, [[(h,14,c,True,False,TITLE_FONT)]])
    txt(s, x+0.25, 4.5, 3.45, 2.0, [[(b,11.5,CHAR)]], line_spacing=1.16)
    x+=4.12

# ============================================================ 5. INTEGRATED APPROACH
s = content_slide(prs, num(), "Not a redesign — an integrated brand-management system", kicker="How to read this document")
divider(s)
txt(s, 0.5, 1.68, 12.3, 0.7, [[("This document runs the full five-workshop journey as one cumulative system. A single strategy — ",12,CHAR),
    ("“Protection, proven”",12,PINK,True),
    (" — cascades from category strategy all the way to what a parent reads on a shelf and hears in an ad. Every layer constrains the next.",12,CHAR)]], line_spacing=1.16)
steps=[("1","Understand","Strategy & white space","Baby Skin-Barrier Company",PINK),
       ("2","Define","Product truth & claims","Claims + BarrierNest™",BLUE),
       ("3","Meaning","Voice & payoff lines","Purpose, tone, endlines",VIOLET),
       ("4","Translate","Visual & packaging","Clinical-warmth system",ORANGE),
       ("5","Finalise","Communication system","Channels & governance",GREEN)]
x=0.5; w=2.4
for nu,t,d,pay,c in steps:
    card(s, x, 2.65, w, 2.35, fill=SOFT)
    rect(s, x, 2.65, w, 0.6, fill=c, shape=MSO_SHAPE.ROUNDED_RECTANGLE).adjustments[0]=0.1
    rect(s, x, 2.95, w, 0.3, fill=c)
    txt(s, x+0.18, 2.72, w-0.36, 0.5, [[("WORKSHOP "+nu,10.5,WHITE,True)]], anchor=MSO_ANCHOR.MIDDLE)
    txt(s, x+0.18, 3.4, w-0.36, 0.4, [[(t,15,c,True,False,TITLE_FONT)]])
    txt(s, x+0.18, 3.85, w-0.36, 0.6, [[(d,10.5,CHAR)]], line_spacing=1.05)
    txt(s, x+0.18, 4.5, w-0.36, 0.45, [[("→ "+pay,9.5,PURPLE,True)]], line_spacing=1.0)
    if nu!="5":
        txt(s, x+w-0.06, 3.5, 0.3, 0.4, [[("›",22,LGREY,True)]])
    x+=w+0.09
card(s, 0.5, 5.25, 12.33, 1.35, fill=PURPLE)
txt(s, 0.8, 5.45, 11.8, 1.0, [[("THE THREAD THAT NEVER BREAKS",11,RGBColor(0xEB,0xDD,0xF3),True)]], space_after=4)
txt(s, 0.8, 5.8, 11.8, 0.7, [[("Strategy",13,WHITE,True),("  governs  ",11,RGBColor(0xD9,0xC4,0xE8)),
    ("Claims",13,WHITE,True),("  governs  ",11,RGBColor(0xD9,0xC4,0xE8)),
    ("Meaning & Voice",13,WHITE,True),("  governs  ",11,RGBColor(0xD9,0xC4,0xE8)),
    ("Design",13,WHITE,True),("  governs  ",11,RGBColor(0xD9,0xC4,0xE8)),
    ("Communication.",13,WHITE,True),("   One brand, end to end.",11,RGBColor(0xEB,0xDD,0xF3),False,True)]], line_spacing=1.1)

# ============================================================ WORKSHOP 1 OPENER
workshop_opener(prs, 1, "Strategy & Category White Space",
    "What kind of brand should NikoMom become — and why now?",
    ["Reframe the category from first principles","Ten strategic territories, scored",
     "Ten packaging worlds & the winning feel","Brand elements: keep / modify / replace / delete / invent",
     "Naming & technology architecture","Decision matrix & the final recommendation"],
    num(), accent=PINK)

# ============================================================ SECTION 1
section_slide(prs, "1", "Category White Space", "Redefining the opportunity from unmet human needs — not from what competitors already do.", num(), bg=PURPLE)

# ---- category today
s = content_slide(prs, num(), "The category is drowning in the same word: “safe”", kicker="1 · Category white space")
divider(s)
txt(s, 0.5, 1.7, 12.3, 0.5, [[("Scan any Indian baby-care shelf or Amazon page and the codes collapse into one message. When everyone says the same thing, the word stops selling.",12,CHAR)]], line_spacing=1.15)
players=[("Johnson's Baby","Legacy trust, softness","Talc controversy; dated science",GREY),
    ("Mamaearth / The Moms Co","“Toxin-free”, natural, D2C","Marketing-led; thin real science",GREEN),
    ("Himalaya","Herbal / Ayurvedic heritage","Mass, low premium ceiling",GREEN),
    ("Sebamed","pH 5.5 clinical authority","Cold; low emotional warmth",SKY),
    ("Cetaphil / CeraVe","Dermatologist, barrier science","Adult-first; not baby-owned",BLUE),
    ("Mustela / Chicco","Premium French / Italian","Price; low India relevance",VIOLET)]
x=0.5; y=2.35; w=3.95; h=1.35
for i,(nm,own,gap,c) in enumerate(players):
    col=i%3; row=i//3
    xx=0.5+col*4.12; yy=2.35+row*1.55
    card(s, xx, yy, w, h, fill=SOFT)
    rect(s, xx, yy, 0.09, h, fill=c)
    txt(s, xx+0.25, yy+0.13, w-0.4, 0.4, [[(nm,12.5,PURPLE,True,False,TITLE_FONT)]])
    txt(s, xx+0.25, yy+0.55, w-0.4, 0.4, [[("Owns: ",10,GREY,True),(own,10,CHAR)]], line_spacing=1.0)
    txt(s, xx+0.25, yy+0.9, w-0.4, 0.4, [[("Gap: ",10,PINK,True),(gap,10,CHAR)]], line_spacing=1.0)
txt(s, 0.5, 5.7, 12.3, 0.9, [[("THE PATTERN  ",11,PINK,True),
    ("Natural, gentle, pH-balanced, toxin-free, dermatologically tested. Six brands, one vocabulary. ",12,CHAR),
    ("Nobody owns the baby's skin barrier as a science platform built for Indian conditions.",12,PURPLE,True)]], line_spacing=1.2)

# ---- first principles
s = content_slide(prs, num(), "First-principle challenges", kicker="1 · Category white space")
divider(s)
txt(s, 0.5, 1.7, 12.3, 0.4, [[("We asked the uncomfortable questions before proposing anything.",12,CHAR)]])
qa=[("Does the category need another “safe” brand?","No. Safety is expected. Differentiation must come from proof and outcome."),
    ("Should the hero be the parent, baby, routine or outcome?","The outcome (protected, healthy skin). The parent is the winner, not the subject."),
    ("Is “trust” enough?","Trust gets you considered. Confidence — “I know I'm doing it right” — gets you chosen and repeated."),
    ("Does science create differentiation, or does confidence?","Science is the reason to believe. Confidence is the reason to buy. We sell confidence, proven by science."),
    ("Is “gentle / toxin-free” ownable?","No — legally claimable by all, owned by none. A barrier-science platform is ownable."),
    ("What mental shortcut is the parent searching for?","“Which brand actually understands my baby's skin — not just markets to me?”")]
x=0.5;
for i,(q,a) in enumerate(qa):
    col=i%2; row=i//2
    xx=0.5+col*6.16; yy=2.35+row*1.42
    card(s, xx, yy, 6.0, 1.28, fill=(SOFTPK if col==0 else SOFT))
    txt(s, xx+0.25, yy+0.14, 5.5, 0.55, [[("Q  ",12,PINK,True,False,TITLE_FONT),(q,12,PURPLE,True,False,TITLE_FONT)]], line_spacing=1.02)
    txt(s, xx+0.25, yy+0.72, 5.55, 0.5, [[("→  ",11,PINK,True),(a,10.5,CHAR)]], line_spacing=1.05)

# ---- unmet need
s = content_slide(prs, num(), "The real unmet need: anxiety, not dirt", kicker="1 · Category white space")
divider(s)
txt(s, 0.5, 1.7, 12.3, 0.6, [[("Indian parents — especially first-time, urban, digitally-informed — are not short of “safe products.” They are short of ",12,CHAR),
    ("confidence.",12,PINK,True),
    (" They are anxious, over-Googled, guilt-prone, and unsure whether they are protecting their baby correctly.",12,CHAR)]], line_spacing=1.18)
# journey from anxiety to confidence
card(s, 0.5, 2.7, 5.9, 3.9, fill=SOFT)
txt(s, 0.75, 2.9, 5.4, 0.4, [[("WHAT THE CATEGORY SELLS TODAY",11,GREY,True)]])
old=["“Gentle & safe” — removes a fear","Products, bought one at a time","Reassurance: “don't worry”","The mother's love as the proof","Ingredients lists as evidence"]
txt(s, 0.8, 3.35, 5.4, 3.0, [[("–  "+o,12.5,CHAR)] for o in old], space_after=8, line_spacing=1.05)
card(s, 6.9, 2.7, 5.9, 3.9, fill=SOFTPK)
txt(s, 7.15, 2.9, 5.4, 0.4, [[("WHAT THE PARENT ACTUALLY WANTS",11,PINK,True)]])
new=["“Am I doing this right?” answered","A system that guides the whole routine","Confidence: “you've got this — here's proof”","The baby's visible outcome as the proof","Seeing the result on their own baby"]
txt(s, 7.2, 3.35, 5.4, 3.0, [[("+  "+o,12.5,PURPLE,True)] for o in new], space_after=8, line_spacing=1.05)

# ---- the white space
s = content_slide(prs, num(), "The white space we will own", kicker="1 · Category white space")
divider(s)
card(s, 0.5, 1.7, 12.33, 1.5, fill=PURPLE)
txt(s, 0.85, 1.92, 11.7, 1.1, [[("The Baby Skin-Barrier Company",22,WHITE,True,False,TITLE_FONT)],
    [("The skin barrier is a baby's first line of defence — its first immune system. We are the pharma-backed brand that protects and builds it, and proves it. ",13,RGBColor(0xEB,0xDD,0xF3)),
     ("Protection, proven.",13,WHITE,True)]], space_after=6, line_spacing=1.14)
cols=[("Unmet need it solves","Parental anxiety — the fear of getting it wrong. We convert it into earned confidence.",PINK),
    ("Emotion it owns","Confidence & control, not soft reassurance. Calm competence.",BLUE),
    ("Why it can't be copied","Requires real pharma R&D + India-specific barrier data. D2C 'natural' and legacy brands lack both.",GREEN),
    ("The mental shortcut","“The science company for my baby's skin.” One idea, instantly filed.",ORANGE)]
x=0.5
for h,b,c in cols:
    card(s, x, 3.4, 2.96, 3.25, fill=SOFT)
    rect(s, x+0.22, 3.62, 0.5, 0.08, fill=c)
    txt(s, x+0.22, 3.8, 2.55, 0.7, [[(h,12.5,c,True,False,TITLE_FONT)]], line_spacing=1.0)
    txt(s, x+0.22, 4.5, 2.55, 2.0, [[(b,10.5,CHAR)]], line_spacing=1.14)
    x+=3.09
txt(s, 0.5, 6.72, 12.3, 0.35, [[("Not a leap — a sharpening.  ",10.5,PINK,True),
    ("“Protecting the skin barrier” already sits inside your current brand foundation — buried as one bullet among five. We make it the spine.",10.5,CHAR)]])

# ---- future 2035
s = content_slide(prs, num(), "Baby care in 2035 — and the category NikoMom can create", kicker="1 · Category white space")
divider(s)
txt(s, 0.5, 1.7, 12.3, 0.5, [[("The product is the entry point, not the endgame. The winning brands of 2035 will be ",12,CHAR),
    ("connected preventive-health systems for the first 1000 days,",12,PURPLE,True),(" not shelves of bottles.",12,CHAR)]], line_spacing=1.15)
fut=[("From products → to a system","A connected routine, not disconnected SKUs.",PINK),
    ("From reactive → to preventive","Protect the barrier before rash, dryness, infection.",BLUE),
    ("From generic → to India-specific","Built for Indian climate, water, pollution, skin.",ORANGE),
    ("From selling → to guiding","A daily companion (WhatsApp/app) that coaches parents.",GREEN),
    ("From skin → to wellbeing","Skin, sleep, nutrition, development — one platform.",VIOLET),
    ("From transaction → to subscription","Refills, growth-stage kits, membership, community.",SKY)]
x=0.5
for i,(h,b,c) in enumerate(fut):
    col=i%3; row=i//3
    xx=0.5+col*4.12; yy=2.35+row*2.05
    card(s, xx, yy, 3.95, 1.85, fill=SOFT)
    rect(s, xx, yy, 3.95, 0.09, fill=c)
    txt(s, xx+0.25, yy+0.28, 3.5, 0.7, [[(h,13,PURPLE,True,False,TITLE_FONT)]], line_spacing=1.02)
    txt(s, xx+0.25, yy+1.05, 3.5, 0.7, [[(b,11,CHAR)]], line_spacing=1.12)
    x+=1
txt(s, 0.5, 6.55, 12.3, 0.5, [[("THE CATEGORY TO CREATE   ",11,PINK,True),
    ("“Baby Skin-Barrier Protection” — preventive, science-led, made for India, delivered as a system.",12,PURPLE,True)]])

# ============================================================ SECTION 2
section_slide(prs, "2", "Strategic Territories", "Ten radically different brand worlds. Each solves a human need, owns an emotion, and resists copying.", num(), bg=PINK)

# ---- territories grid
s = content_slide(prs, num(), "Ten territories on the table", kicker="2 · Strategic territories")
divider(s)
terr=[("01","Skin-Barrier Company","The barrier = first defence. Own barrier science.",PINK,True),
    ("02","Protection Intelligence","Invisible, always-on, adaptive protection.",BLUE,True),
    ("03","First 1000 Days System","Own the early-development window end to end.",VIOLET,True),
    ("04","Indian Baby Science","Built for Indian climate, water, pollution, skin.",ORANGE,True),
    ("05","Parent-Confidence Platform","Sell confidence & competence, not products.",GREEN,False),
    ("06","Daily Rituals / Calm","Turn routines into calm, bonding rituals.",SKY,False),
    ("07","Preventive Baby Care","Prevention over treatment; pharma-grade.",PINK,False),
    ("08","Invisible Care","Care that disappears — no fear-marketing.",PURPLE,False),
    ("09","Pediatric-Grade at Home","Hospital-grade standards for the home.",BLUE,False),
    ("10","Baby Skin Intelligence","Data + product that adapts as baby grows.",GREEN,False)]
x=0.5;
for i,(nu,nm,d,c,short) in enumerate(terr):
    col=i%5; row=i//5
    xx=0.5+col*2.45; yy=2.3+row*2.15
    card(s, xx, yy, 2.32, 1.95, fill=(SOFTPK if short else SOFT), line=(c if short else None), radius=0.09)
    txt(s, xx+0.18, yy+0.14, 2.0, 0.4, [[(nu,15,c,True,False,TITLE_FONT)]])
    if short: chip(s, xx+1.15, yy+0.16, 1.0, "SHORTLIST", color=c, h=0.24, size=7)
    txt(s, xx+0.18, yy+0.55, 2.0, 0.7, [[(nm,11.5,PURPLE,True,False,TITLE_FONT)]], line_spacing=0.98)
    txt(s, xx+0.18, yy+1.2, 2.0, 0.7, [[(d,9.5,CHAR)]], line_spacing=1.05)
txt(s, 0.5, 6.65, 12.3, 0.4, [[("Four carried into the decision matrix (highlighted). The rest were rejected early — reasons on the matrix and rejection slides.",10.5,GREY,False,True)]])

# ---- territory deep dive 1 (top 2)
def terr_detail_slide(nn, items):
    s = content_slide(prs, nn, "Territories in depth — the front-runners", kicker="2 · Strategic territories")
    divider(s)
    x=0.5
    for (num_s,name,why,need,emo,moat,scale,c) in items:
        card(s, x, 1.7, 6.0, 4.95, fill=SOFT)
        rect(s, x, 1.7, 6.0, 0.7, fill=c, shape=MSO_SHAPE.ROUNDED_RECTANGLE).adjustments[0]=0.06
        rect(s, x, 2.05, 6.0, 0.35, fill=c)
        txt(s, x+0.25, 1.82, 5.5, 0.5, [[(num_s+"   "+name,15,WHITE,True,False,TITLE_FONT)]], anchor=MSO_ANCHOR.MIDDLE)
        rows=[("Why it exists",why),("Human need",need),("Emotion owned",emo),("Why hard to copy",moat),("How it scales",scale)]
        yy=2.6
        for lbl,val in rows:
            txt(s, x+0.25, yy, 5.5, 0.75,
                [[(lbl.upper(),9.5,c,True)],[ (val,11,CHAR)]], space_after=1, line_spacing=1.05)
            yy+=0.80
        x+=6.33
    return s

terr_detail_slide(num(), [
 ("01","Skin-Barrier Company",
  "The skin barrier is a baby's first immune system; no brand owns it as a platform.",
  "Protect my baby from the outside world — rash, dryness, infection, irritation.",
  "Confidence through protection. Calm competence.",
  "Needs genuine pharma R&D + India barrier data. Natural/legacy brands lack the credibility.",
  "Every SKU is a barrier act: cleanse, protect, repair, seal — skin, bath, diaper, wipes.", PINK),
 ("02","Protection Intelligence",
  "Reframe care as an intelligent, invisible, always-on protection system.",
  "I want protection I don't have to think about — that adapts to my baby.",
  "Control and modern confidence. Tech-grade reassurance.",
  "Fuses science + design + data language few FMCG brands can hold credibly.",
  "Scales from packs to app, sensors, subscriptions, personalised routines.", BLUE),
])

terr_detail_slide(num(), [
 ("03","First 1000 Days System",
  "The 1000-day window (conception–age 2) is the most consequential in human development.",
  "Give my baby the best possible start — across skin, sleep, nutrition, growth.",
  "Purpose and hope. Long-horizon parental love.",
  "Panacea's healthcare + nutrition breadth lets it own a window pure-play cosmetics can't.",
  "Broadest runway: skin → nutrition → healthcare → community → digital tracking.", VIOLET),
 ("04","Indian Baby Science",
  "Global formulas ignore Indian heat, humidity, hard water, pollution and skin tones.",
  "Give me care actually built for my baby's real environment, not a foreign one.",
  "Pride and relevance. “Finally, made for us.”",
  "Deep local R&D + Panacea's Indian scale; imports and D2C can't match the data.",
  "A lens over every product and claim; powerful in India, exportable to similar climates.", ORANGE),
])

# ---- territory rationale
s = content_slide(prs, num(), "Why these four — and how they combine", kicker="2 · Strategic territories")
divider(s)
txt(s, 0.5, 1.7, 12.3, 0.6, [[("The four front-runners are not rivals — they nest. ",12,CHAR),
    ("Skin-Barrier Science",12,PINK,True),(" is the ",12,CHAR),("what",12,PURPLE,True),
    (";  ",12,CHAR),("Protection Intelligence",12,BLUE,True),(" is the ",12,CHAR),("how it feels",12,PURPLE,True),
    (";  ",12,CHAR),("Indian Baby Science",12,ORANGE,True),(" is the ",12,CHAR),("proof of relevance",12,PURPLE,True),
    (";  ",12,CHAR),("First 1000 Days",12,VIOLET,True),(" is the ",12,CHAR),("growth runway.",12,PURPLE,True)]], line_spacing=1.2)
card(s, 0.5, 2.6, 12.33, 1.35, fill=SOFTPK)
txt(s, 0.8, 2.78, 11.8, 1.0, [[("THE SYNTHESIS   ",12,PINK,True),
    ("“The Baby Skin-Barrier Company — protection intelligence, built for India, for the first 1000 days.”",15,PURPLE,True,False,TITLE_FONT)],
    [("A defensible core (barrier science) with a broad runway (the 1000-day system) and a credible moat (Indian data + Panacea pharma).",11.5,CHAR)]], space_after=6, line_spacing=1.12)
rej=[("Parent-Confidence Platform","Right emotion, but it's an outcome of barrier science — folded in, not a separate territory."),
    ("Daily Rituals / Calm","Warm but soft; loses the science moat that only Panacea can own."),
    ("Invisible Care","Elegant, but too quiet for shelf/Amazon shout-through in a value-conscious market."),
    ("Pediatric-Grade at Home","Strong RTB, weak as a whole-brand idea; becomes a proof pillar instead.")]
txt(s, 0.5, 4.15, 12.3, 0.4, [[("CARRIED AS INGREDIENTS, NOT AS THE CORE",11,GREY,True)]])
x=0.5
for i,(h,b) in enumerate(rej):
    col=i%2; row=i//2
    xx=0.5+col*6.16; yy=4.5+row*1.0
    card(s, xx, yy, 6.0, 0.9, fill=SOFT)
    txt(s, xx+0.22, yy+0.12, 5.6, 0.7, [[(h+"  ",11.5,PURPLE,True),("— "+b,10.5,CHAR)]], line_spacing=1.06)

# ============================================================ SECTION 3
section_slide(prs, "3", "Packaging Worlds", "Ten visual worlds. We define what the parent should feel and understand — not labels.", num(), bg=SKY)

# ---- 10 worlds grid
s = content_slide(prs, num(), "Ten packaging worlds — what should the parent feel?", kicker="3 · Packaging worlds")
divider(s)
worlds=[("Clinical Science","Trust via rigour","White, data, proof marks",SKY,False),
    ("Warm Care Authority","Reassured, held","Soft warmth, human touch",ORANGE,False),
    ("Premium Modern Wellness","Aspirational calm","Skincare-grade minimalism",VIOLET,False),
    ("Japanese Minimal","Quiet competence","Reductive, honest, muji-like",CHAR,False),
    ("Scandinavian Soft","Gentle & human","Calm pastels, rounded, airy",GREEN,False),
    ("Protection Intelligence","In control, modern","Structural, tech-grade, Apple-like",BLUE,True),
    ("Editorial / Knowledge","Informed, respected","Magazine, education-led",PURPLE,False),
    ("Pharma-Consumer Hybrid","Credible & accessible","Rx cues + human warmth",PINK,True),
    ("Playful Developmental","Optimistic, guided","Growth-stage colour coding",ORANGE,False),
    ("Luxury Derm-Skincare","Premium, precious","Prestige, restraint, tactile",VIOLET,False)]
x=0.5
for i,(nm,feel,cue,c,pick) in enumerate(worlds):
    col=i%5; row=i//5
    xx=0.5+col*2.45; yy=2.3+row*2.15
    card(s, xx, yy, 2.32, 1.98, fill=(SOFTPK if pick else SOFT), line=(c if pick else None))
    rect(s, xx, yy, 2.32, 0.5, fill=c, shape=MSO_SHAPE.ROUNDED_RECTANGLE).adjustments[0]=0.10
    rect(s, xx, yy+0.25, 2.32, 0.25, fill=c)
    txt(s, xx+0.15, yy+0.06, 2.05, 0.45, [[(nm,10.5,WHITE,True,False,TITLE_FONT)]], anchor=MSO_ANCHOR.MIDDLE, line_spacing=0.95)
    txt(s, xx+0.15, yy+0.6, 2.05, 0.5, [[("Feel: ",9,c,True),(feel,9,CHAR)]], line_spacing=1.02)
    txt(s, xx+0.15, yy+1.15, 2.05, 0.7, [[("Cue: ",9,c,True),(cue,9,CHAR)]], line_spacing=1.02)
    if pick: chip(s, xx+0.5, yy+1.62, 1.3, "FRONT-RUNNER", color=c, h=0.26, size=7)
txt(s, 0.5, 6.7, 12.3, 0.4, [[("The winning direction fuses the two front-runners into ",10.5,GREY),
    ("“Clinical Warmth” — pharma credibility with human calm.",10.5,PURPLE,True)]])

# ---- worlds evaluated
s = content_slide(prs, num(), "Six worlds, six commercial verdicts", kicker="3 · Packaging worlds")
divider(s)
# table-like eval
heads=["WORLD","EMOTION","RETAIL / AMAZON EDGE","SCALE","PREMIUM","VERDICT"]
colx=[0.5,2.7,4.4,8.2,9.2,10.4]
colw=[2.1,1.6,3.7,0.9,1.1,2.35]
rect(s, 0.5, 1.75, 12.33, 0.45, fill=PURPLE)
for h,cx,cw in zip(heads,colx,colw):
    txt(s, cx+0.1, 1.83, cw, 0.35, [[(h,9.5,WHITE,True)]], anchor=MSO_ANCHOR.MIDDLE)
rows=[("Clinical Science","Trust","Screams credibility on thumbnails","High","Mid","Cold alone — needs warmth",SKY),
    ("Warm Care Authority","Comfort","Blends in; low shelf shout","High","Low","Too close to Johnson's",ORANGE),
    ("Premium Wellness","Aspiration","Beautiful but quiet on Amazon","Mid","High","Premium, weak mass reach",VIOLET),
    ("Protection Intelligence","Control","Distinct, structural, ownable","High","High","Strong — modern & unique",BLUE),
    ("Pharma-Consumer Hybrid","Confidence","Reads credible + human at a glance","High","Mid-Hi","Strong — India-right",PINK),
    ("Luxury Derm","Prestige","Premium; too niche for scale","Low","V.High","Halo SKU only",VIOLET)]
y=2.2
for i,(w,e,r,sc,pr,v,c) in enumerate(rows):
    fill = SOFTPK if c in (BLUE,PINK) else (WHITE if i%2==0 else SOFT)
    rect(s, 0.5, y, 12.33, 0.72, fill=fill)
    rect(s, 0.5, y, 0.08, 0.72, fill=c)
    txt(s, colx[0]+0.12, y+0.06, colw[0], 0.6, [[(w,10.5,PURPLE,True)]], anchor=MSO_ANCHOR.MIDDLE, line_spacing=0.98)
    txt(s, colx[1]+0.1, y+0.06, colw[1], 0.6, [[(e,10,CHAR)]], anchor=MSO_ANCHOR.MIDDLE)
    txt(s, colx[2]+0.1, y+0.06, colw[2], 0.6, [[(r,10,CHAR)]], anchor=MSO_ANCHOR.MIDDLE, line_spacing=0.98)
    txt(s, colx[3]+0.1, y+0.06, colw[3], 0.6, [[(sc,10,CHAR)]], anchor=MSO_ANCHOR.MIDDLE)
    txt(s, colx[4]+0.1, y+0.06, colw[4], 0.6, [[(pr,10,CHAR)]], anchor=MSO_ANCHOR.MIDDLE)
    vc = GREEN if "Strong" in v else (PINK if "Halo" not in v and "Too" not in v and "Cold" not in v else GREY)
    txt(s, colx[5]+0.1, y+0.06, colw[5], 0.6, [[(v,9.5,vc,True)]], anchor=MSO_ANCHOR.MIDDLE, line_spacing=0.98)
    y+=0.74

# ---- packaging behaviour / recommendation
s = content_slide(prs, num(), "How the packaging should behave", kicker="3 · Packaging worlds")
divider(s)
txt(s, 0.5, 1.7, 12.3, 0.5, [[("Recommended world: ",12,CHAR),("“Clinical Warmth”",13,PINK,True,False,TITLE_FONT),
    (" — pharma-grade credibility carried with human calm. The structure itself becomes the mnemonic.",12,CHAR)]], line_spacing=1.15)
beh=[("What should DISAPPEAR","Fear language, crowded claims, busy florals, six competing icons, 'toxin-free' checklists.",GREY),
    ("What should DOMINATE","One outcome, one proof device, generous white space, a single signature colour per outcome.",PINK),
    ("Structure as mnemonic","A distinctive bottle silhouette + cap system recognised in silhouette — owned at 200px and on shelf.",BLUE),
    ("Packaging that teaches","A quiet 'barrier science' cue and a single 'what to expect' outcome ladder — educational, not loud.",GREEN),
    ("Signals safety by form","Tamper-evidence, refill architecture, soft-touch finish — safety felt in the hand, not just claimed.",VIOLET),
    ("One proof device","A single recurring 'Proven' mark (clinical/derm) replaces scattered trust seals across the range.",ORANGE)]
x=0.5
for i,(h,b,c) in enumerate(beh):
    col=i%3; row=i//3
    xx=0.5+col*4.12; yy=2.45+row*2.05
    card(s, xx, yy, 3.95, 1.88, fill=SOFT)
    rect(s, xx, yy, 3.95, 0.09, fill=c)
    txt(s, xx+0.22, yy+0.26, 3.5, 0.5, [[(h,12,c,True,False,TITLE_FONT)]], line_spacing=1.0)
    txt(s, xx+0.22, yy+0.78, 3.5, 1.0, [[(b,10.5,CHAR)]], line_spacing=1.12)

# ============================================================ SECTION 4
section_slide(prs, "4", "Brand-Element Selection", "Every existing element on trial: Keep · Modify · Replace · Delete · Invent.", num(), bg=PURPLE)

# ---- KMRDI table
s = content_slide(prs, num(), "Every element, judged", kicker="4 · Brand-element selection")
divider(s)
rect(s, 0.5, 1.7, 12.33, 0.42, fill=PURPLE)
h2=["ELEMENT","VERDICT","RATIONALE"]
cxx=[0.5,3.5,5.3]; cww=[3.0,1.8,7.4]
for h,cx,cw in zip(h2,cxx,cww):
    txt(s, cx+0.12, 1.77, cw, 0.35, [[(h,10,WHITE,True)]], anchor=MSO_ANCHOR.MIDDLE)
def vcol(v): return {"KEEP":GREEN,"MODIFY":BLUE,"REPLACE":ORANGE,"DELETE":PINK,"INVENT":PURPLE}[v]
rows=[("NikoMom name","KEEP","Real equity + cost to change. Keep the name — radically change what it stands for."),
    ("“Baby Care Expert” position","REPLACE","With “Baby Skin-Barrier Company.” Expertise talks down; barrier science empowers."),
    ("Four “-Nest” technologies","DELETE","HydraNest/TenderNest/DermaNest/HealNest → one master platform. Over-engineered."),
    ("Master technology platform","INVENT","BarrierNest™ — one signature science endorsement across the range."),
    ("“Safe / toxin-free” as lead","REPLACE","Table stakes. Lead with visible outcome + proof; safety becomes a given, not the pitch."),
    ("Panacea Biotec endorsement","KEEP","The single biggest asset — the pharma moat. Elevate it as the trust anchor."),
    ("Mother-and-child imagery","MODIFY","Shift hero to the baby's outcome; parent as confident winner, not anxious subject."),
    ("Multiple trust seals","MODIFY","Collapse to one recurring “Proven” proof device for instant recognition."),
    ("Confidence system / outcome ladder","INVENT","A “what to expect” ladder + parent companion (WhatsApp/app) — the new moat.")]
y=2.14
for i,(el,v,r) in enumerate(rows):
    fill = WHITE if i%2==0 else SOFT
    rect(s, 0.5, y, 12.33, 0.5, fill=fill)
    txt(s, cxx[0]+0.12, y+0.05, cww[0], 0.42, [[(el,10.5,PURPLE,True)]], anchor=MSO_ANCHOR.MIDDLE, line_spacing=0.95)
    chip(s, cxx[1]+0.05, y+0.09, 1.5, v, color=vcol(v), h=0.32, size=9)
    txt(s, cxx[2]+0.12, y+0.05, cww[2], 0.42, [[(r,10,CHAR)]], anchor=MSO_ANCHOR.MIDDLE, line_spacing=0.98)
    y+=0.505

# ---- technology system
s = content_slide(prs, num(), "The technology system is over-engineered", kicker="4 · Brand-element selection")
divider(s)
txt(s, 0.5, 1.7, 12.3, 0.55, [[("Four proprietary “-Nest” technologies for a young brand fragments equity, confuses parents, and demands an education budget the brand does not have. ",12,CHAR),
    ("Collapse four into one.",12,PINK,True)]], line_spacing=1.16)
# before
card(s, 0.5, 2.5, 5.9, 4.0, fill=SOFT)
txt(s, 0.75, 2.68, 5.4, 0.4, [[("BEFORE — four sub-technologies",11,GREY,True)]])
for i,nm in enumerate(["HydraNest","TenderNest","DermaNest","HealNest"]):
    yy=3.15+i*0.72
    card(s, 0.9, yy, 5.1, 0.58, fill=WHITE, line=LGREY)
    txt(s, 1.1, yy+0.13, 4.7, 0.35, [[(nm,12.5,CHAR,True)]])
txt(s, 0.75, 6.05, 5.4, 0.5, [[("4 names to explain · 4 badges · 4 equity pools · high confusion",10,PINK)]], line_spacing=1.05)
# arrow
a=rect(s, 6.5, 4.1, 0.4, 0.8, fill=PINK, shape=MSO_SHAPE.RIGHT_ARROW)
# after
card(s, 7.0, 2.5, 5.8, 4.0, fill=SOFTPK)
txt(s, 7.25, 2.68, 5.3, 0.4, [[("AFTER — one master platform",11,PINK,True)]])
card(s, 7.5, 3.2, 4.8, 1.5, fill=PURPLE)
txt(s, 7.7, 3.45, 4.4, 1.0, [[("BarrierNest™",24,WHITE,True,False,TITLE_FONT)],
    [("One protective science signature, across every product.",11,RGBColor(0xEB,0xDD,0xF3))]], space_after=4, line_spacing=1.1)
txt(s, 7.5, 4.9, 5.0, 1.5, [[("✓  Keeps the “Nest” equity (safe, warm, protective)",10.5,CHAR)],
    [("✓  Adds the “Barrier” science moat",10.5,CHAR)],
    [("✓  Ingredients & outcomes lead each pack; tech signs quietly",10.5,CHAR)],
    [("✓  One badge, one story, one equity pool",10.5,CHAR)]], space_after=6, line_spacing=1.05)

# ---- information architecture
s = content_slide(prs, num(), "What the parent should see first", kicker="4 · Brand-element selection")
divider(s)
txt(s, 0.5, 1.7, 12.3, 0.45, [[("Ranked information hierarchy — front of pack, Amazon thumbnail, and quick-commerce tile all obey this order.",12,CHAR)]], line_spacing=1.1)
ladder=[("1","OUTCOME","What visibly happens — “48h barrier protection”, “no rash”.",PINK),
    ("2","PROTECTION / CONFIDENCE","The emotional promise — your baby is protected; you've got this.",PURPLE),
    ("3","PROOF","Clinically / dermatologically tested; paediatrician-recommended stat.",BLUE),
    ("4","TECHNOLOGY","BarrierNest™ signature — small, quiet, consistent.",SKY),
    ("5","INGREDIENTS","Supporting reason-to-believe; hero actives named.",GREEN),
    ("6","PANACEA ENDORSEMENT","The trust anchor — corner-locked on every pack.",ORANGE),
    ("7","ROUTINE","When & how to use — back of pack and digital companion.",GREY)]
y=2.35
for nu,h,b,c in ladder:
    card(s, 0.5, y, 12.33, 0.585, fill=SOFT)
    rect(s, 0.5, y, 0.62, 0.585, fill=c, shape=MSO_SHAPE.ROUNDED_RECTANGLE).adjustments[0]=0.12
    rect(s, 0.85, y, 0.27, 0.585, fill=c)
    txt(s, 0.5, y+0.06, 0.62, 0.45, [[(nu,18,WHITE,True,False,TITLE_FONT)]], align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    txt(s, 1.35, y+0.05, 3.5, 0.5, [[(h,12.5,c,True,False,TITLE_FONT)]], anchor=MSO_ANCHOR.MIDDLE)
    txt(s, 4.9, y+0.05, 7.7, 0.5, [[(b,11,CHAR)]], anchor=MSO_ANCHOR.MIDDLE)
    y+=0.605
txt(s, 0.5, 6.65, 12.3, 0.35, [[("REJECTED AS LEAD:  ",10.5,PINK,True),("“Safe / toxin-free” (table stakes) · heavy technology (education cost) · “trust” as an adjective (unprovable).",10.5,CHAR)]])

# ============================================================ SECTION 5
section_slide(prs, "5", "Naming Philosophy", "Name, sub-brands, variants and technology — judged for equity, SEO, trademark and scale.", num(), bg=PINK)

# ---- name verdict
s = content_slide(prs, num(), "NikoMom: keep the name, replace its meaning", kicker="5 · Naming philosophy")
divider(s)
card(s, 0.5, 1.7, 5.9, 4.95, fill=SOFT)
txt(s, 0.75, 1.9, 5.4, 0.4, [[("THE HONEST CASE AGAINST",11,PINK,True)]])
neg=["“Mom” centres the mother — but the hero is the baby's outcome","Excludes fathers & modern shared parenting","“Niko” is warm but generic; limited science signal","Weaker standalone trademark & global distinctiveness"]
txt(s, 0.8, 2.35, 5.4, 2.2, [[("–  "+o,11.5,CHAR)] for o in neg], space_after=8, line_spacing=1.1)
txt(s, 0.75, 4.55, 5.4, 0.4, [[("THE CASE FOR KEEPING",11,GREEN,True)]])
pos=["Real, hard-won equity in market already","“Niko” = short, warm, globally pronounceable","Rebranding cost & risk are material","Meaning can be rebuilt without a rename"]
txt(s, 0.8, 4.95, 5.4, 1.7, [[("+  "+o,11.5,CHAR)] for o in pos], space_after=6, line_spacing=1.1)
# verdict
card(s, 6.7, 1.7, 6.1, 4.95, fill=PURPLE)
txt(s, 6.95, 1.95, 5.6, 0.4, [[("VERDICT",12,RGBColor(0xEB,0xDD,0xF3),True)]])
txt(s, 6.95, 2.35, 5.6, 1.9, [[("Keep ",18,WHITE,False,False,TITLE_FONT),("NikoMom",18,WHITE,True,False,TITLE_FONT),
    (". Radically change what it means — from “mom's little helper” to India's baby skin-barrier science company.",18,WHITE,False,False,TITLE_FONT)]], line_spacing=1.08)
txt(s, 6.95, 4.35, 5.6, 0.4, [[("HOW THE MEANING SHIFTS",11,PINK,True)]])
txt(s, 6.95, 4.75, 5.6, 1.8,
    [[("Niko",12,WHITE,True),(" — warmth, the human bond, “victory / good” resonance",11,RGBColor(0xEB,0xDD,0xF3))],
     [("+ a science endorsement signature (BarrierNest™ + Panacea)",11,RGBColor(0xEB,0xDD,0xF3))],
     [("= warm name, serious science. The tension is the brand.",12,WHITE,True)]], space_after=8, line_spacing=1.1)

# ---- naming system
s = content_slide(prs, num(), "One naming system, built for SEO and trust", kicker="5 · Naming philosophy")
divider(s)
rows=[("Master brand","Keep NikoMom","Endorsed by Panacea Biotec. Warm human name, serious science backer.","Ownable + equity retained",GREEN),
    ("Variant naming","Descriptive + outcome","“NikoMom Barrier Cream”, “Daily Protect Lotion” — not “DermaNest”.","Wins Amazon/Google search",BLUE),
    ("Sub-brand logic","Minimal / none","One master brand + descriptive ranges. Avoid sub-brand sprawl.","Cheaper to build, clearer",ORANGE),
    ("Technology naming","One platform","BarrierNest™ only. Benefit-led, not clinical jargon.","One equity pool",PINK),
    ("Range architecture","By outcome, not chemistry","Protect · Cleanse · Repair · Soothe — shopper language.","Intuitive on shelf",VIOLET)]
y=1.85
head=["DECISION","CHOICE","WHAT IT LOOKS LIKE","WHY",""]
rect(s, 0.5, 1.75, 12.33, 0.0, fill=WHITE)
for i,(d,ch,ex,why,c) in enumerate(rows):
    yy=1.9+i*0.96
    card(s, 0.5, yy, 12.33, 0.86, fill=(SOFT if i%2 else SOFTPK))
    rect(s, 0.5, yy, 0.09, 0.86, fill=c)
    txt(s, 0.75, yy+0.12, 2.3, 0.7, [[(d,11.5,PURPLE,True,False,TITLE_FONT)]], line_spacing=1.0)
    txt(s, 3.1, yy+0.12, 2.2, 0.7, [[(ch,11.5,c,True)]], line_spacing=1.0)
    txt(s, 5.4, yy+0.12, 4.3, 0.7, [[(ex,10.5,CHAR)]], line_spacing=1.06)
    txt(s, 9.85, yy+0.12, 2.85, 0.7, [[("→ "+why,10.5,CHAR,False,True)]], line_spacing=1.05)
txt(s, 0.5, 6.75, 12.3, 0.35, [[("PRINCIPLE   ",10.5,PINK,True),
    ("Proprietary names for the ONE thing worth owning (the technology). Descriptive, searchable names for everything a parent types into a search bar.",10.5,CHAR)]])

# ============================================================ SECTION 6
section_slide(prs, "6", "Decision Framework", "Six directions scored across fourteen board-level criteria. The matrix, not the opinion, decides.", num(), bg=SKY)

# ---- matrix
s = content_slide(prs, num(), "The decision matrix", kicker="6 · Decision framework")
divider(s, y=1.45)
crit=["Desirability","Distinctiveness","Memorability","Shelf impact","Amazon","Premium","Sci. credibility","Scalability","Portfolio flex","Future-proof","Ease exec.","Cost","Ownability","Int'l"]
dirs=[("Baby Care Expert (current)",[3,2,3,2,2,3,3,3,3,2,4,4,2,3]),
    ("Natural / Gentle",[3,1,2,2,3,2,2,3,3,2,4,3,1,3]),
    ("Skin-Barrier Company ★",[4,5,4,4,4,4,5,5,5,5,3,3,5,5]),
    ("First 1000 Days System",[4,4,3,3,3,4,4,5,5,5,2,2,4,4]),
    ("Daily Rituals / Calm",[4,3,4,3,3,4,2,3,3,3,3,3,3,4]),
    ("Indian Baby Science",[4,4,3,4,4,3,4,4,4,4,3,3,4,2])]
# header
x0=3.7; cw=(12.83-x0)/ (len(crit)+1)
rect(s, 0.5, 1.65, 12.33, 0.62, fill=PURPLE)
txt(s, 0.6, 1.72, 3.0, 0.5, [[("DIRECTION",8.5,WHITE,True)]], anchor=MSO_ANCHOR.MIDDLE)
for j,cr in enumerate(crit):
    cx=x0+j*cw
    tb=txt(s, cx, 1.66, cw, 0.6, [[(cr,6.6,WHITE,True)]], align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.BOTTOM, line_spacing=0.9)
txt(s, x0+len(crit)*cw, 1.72, cw+0.3, 0.5, [[("TOTAL",8,WHITE,True)]], align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
def scol(v): return {1:RGBColor(0xE9,0xC6,0xD9),2:RGBColor(0xE7,0xC9,0xE0),3:RGBColor(0xC9,0xD8,0xEE),4:RGBColor(0x9E,0xC7,0x8F),5:GREEN}[v]
y=2.29
for name,scores in dirs:
    star = "★" in name
    rect(s, 0.5, y, 12.33, 0.64, fill=(SOFTPK if star else (WHITE)))
    if star: rect(s, 0.5, y, 12.33, 0.64, fill=None, line=PINK, line_w=1.5)
    txt(s, 0.62, y+0.05, 3.05, 0.55, [[(name,8.6,(PINK if star else PURPLE),True)]], anchor=MSO_ANCHOR.MIDDLE, line_spacing=0.95)
    tot=sum(scores)
    for j,v in enumerate(scores):
        cx=x0+j*cw
        rect(s, cx+0.02, y+0.07, cw-0.04, 0.5, fill=scol(v))
        txt(s, cx, y+0.07, cw, 0.5, [[(str(v),8.5,CHAR,True)]], align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    cx=x0+len(crit)*cw
    txt(s, cx, y+0.05, cw+0.3, 0.55, [[(str(tot),12,(PINK if star else PURPLE),True,False,TITLE_FONT)]], align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    y+=0.66
txt(s, 0.5, 6.35, 8.0, 0.35, [[("Scale 1–5 (5 = strongest). ",9,GREY,True),("Skin-Barrier Company leads on 11 of 14 criteria — and every criterion that builds a moat.",9,CHAR)]])
# legend
lx=8.9
for v,lb in [(2,"Weak"),(3,"OK"),(4,"Strong"),(5,"Best")]:
    rect(s, lx, 6.32, 0.22, 0.22, fill=scol(v)); txt(s, lx+0.26, 6.31, 0.7, 0.25, [[(lb,8,CHAR)]]); lx+=0.95

# ---- rejections
s = content_slide(prs, num(), "Why the other directions were rejected", kicker="6 · Decision framework")
divider(s)
rej=[("Baby Care Expert (current)","36","Safe and executable, but undifferentiated and un-ownable. “Expert” is a posture every brand claims; it builds no moat and caps premium.",GREY),
    ("Natural / Gentle","35","Lowest distinctiveness and ownability. Directly into Mamaearth's teeth with none of its D2C cost advantage. A red-ocean fight.",GREEN),
    ("First 1000 Days System","52","Powerful and the natural extension — but too broad to launch on. Hard to execute now; adopted as the long-term runway, not the entry idea.",VIOLET),
    ("Daily Rituals / Calm","45","Warm and likeable, but sacrifices the science moat only Panacea can own. Emotionally soft against value-led competitors.",SKY),
    ("Indian Baby Science","50","Strong and defensible, but weak international relevance and better used as a proof pillar under the barrier story than as the whole brand.",ORANGE)]
y=1.8
for name,sc,why,c in rej:
    card(s, 0.5, y, 12.33, 0.92, fill=SOFT)
    rect(s, 0.5, y, 0.09, 0.92, fill=c)
    txt(s, 0.75, y+0.14, 3.4, 0.7, [[(name,12.5,PURPLE,True,False,TITLE_FONT)]], line_spacing=1.0)
    card(s, 4.15, y+0.24, 0.95, 0.46, fill=c)
    txt(s, 4.15, y+0.27, 0.95, 0.4, [[(sc,15,WHITE,True,False,TITLE_FONT)]], align=PP_ALIGN.CENTER)
    txt(s, 5.35, y+0.12, 7.25, 0.75, [[(why,11,CHAR)]], anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.08)
    y+=0.99
txt(s, 0.5, 6.85, 12.3, 0.3, [[("Winner: Baby Skin-Barrier Company — 62 / 70.",11,PINK,True)]])

# ============================================================ SECTION 7
section_slide(prs, "7", "Final Recommendation", "One direction. The reasoning, the trade-offs, and the inputs it locks for Workshops 2–5.", num(), bg=PURPLE)

# ---- the recommendation
s = content_slide(prs, num(), "The recommendation", kicker="7 · Final recommendation")
divider(s)
card(s, 0.5, 1.65, 12.33, 2.15, fill=PURPLE)
txt(s, 0.85, 1.85, 11.7, 1.9,
    [[("NikoMom becomes India's Baby Skin-Barrier Company.",21,WHITE,True,False,TITLE_FONT)],
     [("The pharma-backed brand — by Panacea Biotec — that protects and builds a baby's skin barrier, and turns anxious parents into confident ones through visible proof. ",13,RGBColor(0xEB,0xDD,0xF3)),
      ("We don't sell safety. We prove protection.",13,WHITE,True)],
     [("Signature idea:  “Protection, proven.”      Emotion owned: confidence.      Moat: pharma science + Indian barrier data.",12,RGBColor(0xD9,0xC4,0xE8),False,True)]],
    space_after=8, line_spacing=1.14)
piv=[("FROM","Baby Care Expert · reassurance · gentle & safe · four technologies · mother-hero · trust",GREY),
    ("TO","Baby Skin-Barrier Company · confidence · protection proven · one BarrierNest™ · baby-outcome hero · proof",PINK)]
y=4.05
for lb,b,c in piv:
    card(s, 0.5, y, 12.33, 1.25, fill=(SOFT if c==GREY else SOFTPK))
    chip(s, 0.75, y+0.42, 1.15, lb, color=c, h=0.4, size=12)
    txt(s, 2.15, y+0.2, 10.4, 0.9, [[(b,13,(CHAR if c==GREY else PURPLE),c!=GREY)]], anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.1)
    y+=1.35

# ---- system proof
s = content_slide(prs, num(), "One idea that works everywhere", kicker="7 · Final recommendation")
divider(s)
txt(s, 0.5, 1.7, 12.3, 0.4, [[("“Protection, proven” must survive every touchpoint. It does — because it is a system, not a slogan.",12,CHAR)]], line_spacing=1.1)
sys=[("Packaging","Outcome + one proof device + BarrierNest™ signature; structure as mnemonic.",PINK),
    ("Amazon / Q-commerce","Outcome-led thumbnails; A+ proof modules; searchable descriptive names.",BLUE),
    ("Doctors","Paediatrician & derm proof leads — pharma credibility is native here.",GREEN),
    ("Website / CRM","The barrier-science story + “what to expect” outcome ladder.",VIOLET),
    ("WhatsApp companion","A daily routine coach — the confidence engine and retention moat.",ORANGE),
    ("Subscriptions / refills","Barrier routine kits by growth stage; refills lower cost & waste.",SKY),
    ("Community / sampling","“Barrier Club” — proof shared parent-to-parent; UGC of real outcomes.",PINK),
    ("International","Barrier science travels; India-relevance localises without a rebrand.",PURPLE)]
x=0.5
for i,(h,b,c) in enumerate(sys):
    col=i%4; row=i//4
    xx=0.5+col*3.08; yy=2.35+row*2.15
    card(s, xx, yy, 2.92, 1.95, fill=SOFT)
    rect(s, xx, yy, 2.92, 0.09, fill=c)
    txt(s, xx+0.2, yy+0.24, 2.55, 0.5, [[(h,12,c,True,False,TITLE_FONT)]], line_spacing=1.0)
    txt(s, xx+0.2, yy+0.75, 2.55, 1.1, [[(b,10,CHAR)]], line_spacing=1.12)

# ---- tradeoffs
s = content_slide(prs, num(), "Trade-offs we accept, with eyes open", kicker="7 · Final recommendation")
divider(s)
tr=[("Higher proof burden","We must fund real clinical/derm substantiation. But it's exactly the moat competitors can't cross.",PINK),
    ("Slower, costlier than “natural”","Science credibility takes investment. Panacea's R&D makes it feasible where D2C cannot follow.",BLUE),
    ("Warmth risk (too clinical)","“Clinical Warmth” world + “Niko” name deliberately re-inject the human. Monitored in Workshop 4.",ORANGE),
    ("Name tension (Mom vs baby-hero)","We keep equity and reframe meaning — accepting a managed tension over a costly rename.",VIOLET),
    ("Education need for “barrier”","The barrier idea needs teaching — but that's the parent's exact unanswered question. Content is the product.",GREEN),
    ("Premium vs mass reach","Anchor premium via proof; ladder to accessible SKUs so credibility trickles down, not up.",SKY)]
x=0.5
for i,(h,b,c) in enumerate(tr):
    col=i%2; row=i//2
    xx=0.5+col*6.16; yy=1.9+row*1.55
    card(s, xx, yy, 6.0, 1.4, fill=SOFT)
    rect(s, xx, yy, 0.09, 1.4, fill=c)
    txt(s, xx+0.25, yy+0.16, 5.55, 0.5, [[("⚠  ",12,c,True),(h,12.5,PURPLE,True,False,TITLE_FONT)]], line_spacing=1.0)
    txt(s, xx+0.25, yy+0.62, 5.55, 0.7, [[(b,10.5,CHAR)]], line_spacing=1.1)
txt(s, 0.5, 6.65, 12.3, 0.35, [[("Net:  ",11,PINK,True),
    ("Every trade-off is on the side of the moat. The hard parts are exactly what makes the position ownable.",11,CHAR)]])

# ---- inputs locked
s = content_slide(prs, num(), "What this locks for Workshops 2–5", kicker="7 · Final recommendation")
divider(s)
txt(s, 0.5, 1.7, 12.3, 0.45, [[("Workshop 1 constrains everything downstream. These are the locked inputs the next four workshops must build within.",12,CHAR)]], line_spacing=1.12)
locks=[("W2 — Define","Claims ladder from OUTCOME → proof. BarrierNest™ is the single technology narrative. “What to expect” outcome ladder is the spine.",BLUE),
    ("W3 — Meaning","Purpose: confident parenting through proven protection. Voice: warm-but-precise (“clinical warmth”). Positioning: the Baby Skin-Barrier Company.",VIOLET),
    ("W4 — Translate","Visual world: Clinical Warmth. Structure as mnemonic. Outcome-coded colour. One proof device. Baby-outcome hero imagery.",PINK),
    ("W5 — Finalise","Pressure-test “Protection, proven” across pack, Amazon, doctor, WhatsApp companion, subscription and community without breaking.",GREEN)]
x=0.5
for i,(h,b,c) in enumerate(locks):
    col=i%2; row=i//2
    xx=0.5+col*6.16; yy=2.35+row*2.1
    card(s, xx, yy, 6.0, 1.95, fill=SOFT)
    rect(s, xx, yy, 6.0, 0.55, fill=c, shape=MSO_SHAPE.ROUNDED_RECTANGLE).adjustments[0]=0.08
    rect(s, xx, yy+0.28, 6.0, 0.27, fill=c)
    txt(s, xx+0.25, yy+0.09, 5.5, 0.45, [[(h,13,WHITE,True,False,TITLE_FONT)]], anchor=MSO_ANCHOR.MIDDLE)
    txt(s, xx+0.25, yy+0.72, 5.5, 1.1, [[(b,11,CHAR)]], line_spacing=1.14)

# ##################################################################
# WORKSHOP 2 — PRODUCT TRUTH & CLAIM ARCHITECTURE
# ##################################################################
workshop_opener(prs, 2, "Product Truth & Claim Architecture",
    "What exactly does each product solve — and what earns its place on pack?",
    ["The claim principle: outcome first, proof second","One technology platform: four barrier actions",
     "The outcome ladder as a proof engine","Per-product claim architecture (all six SKUs)",
     "Front-of-pack vs back-of-pack hierarchy","Trust & proof: the Panacea assurance system"],
    num(), accent=BLUE)

# product master data (reframed under barrier science, outcome-led)
PRODUCTS=[
 ("Baby Massage Oil","Nourish & Seal","HydraNest",ORANGE,
  "Fast-absorbing daily massage oil that locks moisture into the skin barrier",
  "+100% skin moisture in 30 min · 60%+ still held at 12 hrs",
  "10 cold-pressed oils + Vitamin E",
  "Day 1: soft, nourished  →  7 days: smoother, hydrated  →  Ongoing: lasting comfort",
  "Hydration that doesn't slip away."),
 ("Head-to-Toe Wash","Cleanse & Preserve","TenderNest",SKY,
  "3-in-1 wash that cleans without stripping the barrier — no tears, no dryness",
  "pH 5.5 · 100% of parents: tear-free, mild & leaves skin soft",
  "Triple-Sugar Complex (Aquaxyl), Oat, Neem, Aloe",
  "After bath: soft, calm  →  1–2 wks: less dry  →  Ongoing: healthy skin",
  "A gentle clean that protects."),
 ("Daily Lotion","Hydrate & Strengthen","DermaNest",VIOLET,
  "24-hour barrier hydration that cuts water loss and builds resilience",
  "+100% hydration in 30 min · 2× hydrated even at 6 hrs",
  "Ghee, Mango Butter, Coconut, Jojoba, Aloe",
  "Immediate: non-greasy soft  →  Daily: less flaky  →  Ongoing: stronger barrier",
  "24-hour barrier, all-day soft."),
 ("Diaper Rash Cream","Repair & Shield","HealNest",PINK,
  "Soothes and prevents rash by repairing and shielding the barrier",
  "50% improvement in 2 days · 100% in 7 days · no recurrence",
  "Oat Oil, Ghee, Coconut, Vetiver, Primrose",
  "Immediate: calmer  →  24–48h: redness down  →  5–7 days: clear",
  "Rescue today. Shield tomorrow."),
 ("Baby Diapers","Dry & Protect","ADL",GREEN,
  "Ultra-soft, breathable dryness that keeps the barrier calm day and night",
  "Dry after 5 wettings · up to 12 hrs · wetness indicator · aloe anti-rash",
  "ADL core + soft non-woven top-sheet",
  "Day 1: comfortable, no fuss  →  Ongoing: better sleep, less irritation",
  "Dry all day. Calm all night."),
 ("Wet Wipes","Purely Clean","Pure Water",BLUE,
  "99.9% pure-water wipes — safe from Day 1, with nothing to hide",
  "Paediatrician recommended · 100% biodegradable plant fabric",
  "99.9% pure water + soothing Aloe Vera",
  "Everyday, everywhere: gentle cleansing without irritation",
  "Pure water. Nothing to hide."),
]

# ---- 2.1 claim principle
s = content_slide(prs, num(), "Every claim must earn its place — and ladder up", kicker="Workshop 2 · Claim principle")
divider(s)
txt(s, 0.5, 1.7, 12.3, 0.55, [[("The current packs bury the outcome under ingredients and technology. We invert it. A parent decides in 8 seconds — so the ",12,CHAR),
    ("visible outcome leads, and everything below it exists only to prove that outcome.",12,PURPLE,True)]], line_spacing=1.16)
rungs=[("OUTCOME","What the parent sees & feels — the hero claim","“Skin stays soft and protected for 24 hours.”",PINK),
    ("PROOF","The evidence that makes it believable","“+100% hydration in 30 min · dermatologically tested”",BLUE),
    ("TECHNOLOGY","The named reason it works — one signature","“Powered by BarrierNest™”",VIOLET),
    ("INGREDIENTS","Supporting reason-to-believe","“Ghee, mango butter, jojoba, aloe”",GREEN),
    ("ASSURANCE","The trust anchor","“Assurance of Panacea Biotec”",ORANGE)]
y=2.45
for h,d,ex,c in rungs:
    card(s, 0.5, y, 12.33, 0.72, fill=SOFT)
    rect(s, 0.5, y, 0.12, 0.72, fill=c)
    txt(s, 0.8, y+0.04, 2.3, 0.65, [[(h,13,c,True,False,TITLE_FONT)]], anchor=MSO_ANCHOR.MIDDLE)
    txt(s, 3.2, y+0.04, 4.3, 0.65, [[(d,11,CHAR)]], anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.0)
    txt(s, 7.6, y+0.04, 5.0, 0.65, [[(ex,10.5,PURPLE,False,True)]], anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.0)
    y+=0.78
txt(s, 0.5, 6.55, 12.3, 0.4, [[("The ladder is identical on every SKU. ",11,PINK,True),
    ("That repetition is what turns six products into one recognisable system.",11,CHAR)]])

# ---- 2.2 technology architecture
s = content_slide(prs, num(), "Four technologies become one: BarrierNest™", kicker="Workshop 2 · Technology architecture")
divider(s)
txt(s, 0.5, 1.68, 12.3, 0.5, [[("We retire HydraNest, TenderNest, DermaNest & HealNest as separate brands. One master platform signs the science; ",12,CHAR),
    ("four plain-language barrier actions",12,PURPLE,True),(" tell each product's job.",12,CHAR)]], line_spacing=1.14)
card(s, 0.5, 2.35, 12.33, 1.15, fill=PURPLE)
txt(s, 0.8, 2.5, 4.0, 0.85, [[("BarrierNest™",24,WHITE,True,False,TITLE_FONT)],[("The protective science signature",10.5,RGBColor(0xEB,0xDD,0xF3))]], space_after=2, line_spacing=1.05)
acts=[("Cleanse",SKY),("Hydrate",VIOLET),("Repair",PINK),("Protect",GREEN)]
xx=5.0
for a,c in acts:
    chip(s, xx, 2.72, 1.7, a, color=c, h=0.5, size=13); xx+=1.85
txt(s, 0.5, 3.75, 12.3, 0.35, [[("HOW IT MAPS TO THE RANGE",11,BLUE,True)]])
y=4.15
for (nm,act,old,c,hero,proof,ing,ladder,pay) in PRODUCTS:
    card(s, 0.5, y, 12.33, 0.4, fill=(SOFT))
    rect(s, 0.5, y, 0.09, 0.4, fill=c)
    txt(s, 0.72, y+0.04, 3.0, 0.34, [[("NikoMom "+nm,10.5,PURPLE,True)]], anchor=MSO_ANCHOR.MIDDLE)
    txt(s, 3.8, y+0.04, 2.6, 0.34, [[("was ",8.5,GREY),(old+" Technology",9.5,GREY,False,True)]], anchor=MSO_ANCHOR.MIDDLE)
    txt(s, 6.5, y+0.04, 0.3, 0.34, [[("→",11,c,True)]], anchor=MSO_ANCHOR.MIDDLE)
    txt(s, 6.95, y+0.04, 3.0, 0.34, [[("BarrierNest™ · ",9.5,CHAR),(act,10.5,c,True)]], anchor=MSO_ANCHOR.MIDDLE)
    y+=0.415

# ---- 2.3 outcome ladder
s = content_slide(prs, num(), "The outcome ladder — our proof engine", kicker="Workshop 2 · Outcome ladder")
divider(s)
txt(s, 0.5, 1.7, 12.3, 0.5, [[("Every pack answers one question the category dodges: ",12,CHAR),
    ("“What will I actually see, and when?”",12,PINK,True),
    (" A three-step ladder turns science into a visible, time-bound promise.",12,CHAR)]], line_spacing=1.15)
steps3=[("FIRST USE","Immediate, sensory proof","Soft, calm, non-greasy skin from the very first day",PINK),
    ("7–14 DAYS","Visible change","Less dryness, less redness, smoother and calmer skin",VIOLET),
    ("CONTINUED USE","The real payoff","A stronger barrier and fewer flare-ups over time",GREEN)]
x=0.5
for i,(h,d,b,c) in enumerate(steps3):
    xx=0.5+i*4.12
    card(s, xx, 2.5, 3.95, 1.9, fill=SOFT)
    rect(s, xx, 2.5, 3.95, 0.09, fill=c)
    txt(s, xx+0.25, 2.7, 3.5, 0.4, [[(h,13,c,True,False,TITLE_FONT)]])
    txt(s, xx+0.25, 3.12, 3.5, 0.35, [[(d,11,PURPLE,True)]])
    txt(s, xx+0.25, 3.5, 3.5, 0.8, [[(b,10.5,CHAR)]], line_spacing=1.12)
    if i<2: txt(s, xx+3.85, 3.15, 0.4, 0.5, [[("›",26,LGREY,True)]])
txt(s, 0.5, 4.6, 12.3, 0.35, [[("PROVEN, PER PRODUCT — REAL PERFORMANCE DATA",11,BLUE,True)]])
y=5.0
for i,(nm,act,old,c,hero,proof,ing,ladder,pay) in enumerate(PRODUCTS[:4]):
    col=i%2; row=i//2
    xx=0.5+col*6.16; yy=5.0+row*0.78
    card(s, xx, yy, 6.0, 0.68, fill=SOFTPK if col==0 else SOFT)
    rect(s, xx, yy, 0.08, 0.68, fill=c)
    txt(s, xx+0.22, yy+0.06, 2.2, 0.56, [[(nm,10.5,PURPLE,True)]], anchor=MSO_ANCHOR.MIDDLE, line_spacing=0.95)
    txt(s, xx+2.4, yy+0.06, 3.5, 0.56, [[(proof,9.5,CHAR)]], anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.0)
    y+=0.78

# ---- 2.4 per-product claim architecture
s = content_slide(prs, num(), "Per-product claim architecture", kicker="Workshop 2 · The six SKUs")
divider(s, y=1.4)
rect(s, 0.5, 1.6, 12.33, 0.42, fill=PURPLE)
hd=[("PRODUCT",0.6,2.0),("HERO CLAIM (OUTCOME-LED)",2.7,4.9),("PROOF",7.65,3.0),("KEY INGREDIENTS",10.75,2.0)]
for t,cx,cw in hd: txt(s, cx, 1.67, cw, 0.35, [[(t,9,WHITE,True)]], anchor=MSO_ANCHOR.MIDDLE)
y=2.05
for (nm,act,old,c,hero,proof,ing,ladder,pay) in PRODUCTS:
    card(s, 0.5, y, 12.33, 0.78, fill=SOFT)
    rect(s, 0.5, y, 0.09, 0.78, fill=c)
    txt(s, 0.7, y+0.08, 2.0, 0.65, [[(nm,10,PURPLE,True)],[("BarrierNest · "+act,8,c,True)]], anchor=MSO_ANCHOR.MIDDLE, space_after=1, line_spacing=0.98)
    txt(s, 2.7, y+0.06, 4.85, 0.68, [[(hero,9.8,CHAR)]], anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.02)
    txt(s, 7.65, y+0.06, 3.0, 0.68, [[(proof,9,CHAR)]], anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.0)
    txt(s, 10.75, y+0.06, 2.05, 0.68, [[(ing,9,CHAR)]], anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.0)
    y+=0.8

# ---- 2.5 FOP / BOP
s = content_slide(prs, num(), "What goes on the front — and what waits on the back", kicker="Workshop 2 · Pack hierarchy")
divider(s)
txt(s, 0.5, 1.68, 12.3, 0.45, [[("The front sells the decision in 8 seconds. The back rewards the parent who turns it over. Nothing competes; everything ranks.",12,CHAR)]], line_spacing=1.12)
card(s, 0.5, 2.35, 5.95, 4.3, fill=SOFTPK)
txt(s, 0.78, 2.55, 5.4, 0.4, [[("FRONT OF PACK",13,PINK,True,False,TITLE_FONT)],[("The 8-second decision",10,GREY,False,True)]], space_after=1)
fop=["1  Hero OUTCOME claim","2  BarrierNest™ signature","3  One proof mark (derm / paediatrician)","4  Key ingredient or 3-in-1 descriptor","5  Assurance of Panacea Biotec + 7N","6  Net weight / variant colour"]
txt(s, 0.85, 3.35, 5.4, 3.1, [[(o,12,CHAR,True) if o[0] in "12" else (o,12,CHAR)] for o in fop], space_after=9, line_spacing=1.05)
card(s, 6.9, 2.35, 5.9, 4.3, fill=SOFT)
txt(s, 7.18, 2.55, 5.4, 0.4, [[("BACK OF PACK",13,PURPLE,True,False,TITLE_FONT)],[("The reward for turning over",10,GREY,False,True)]], space_after=1)
bop=["Barrier-science story (how it protects)","The outcome ladder — what to expect, when","Full ingredient story & hero actives","Directions & habit framing (daily ritual)","No-No ingredients + certifications","Regulatory, FSSAI, batch, Made-in-India","Other products from the NikoMom family"]
txt(s, 7.25, 3.35, 5.4, 3.1, [[("•  "+o,11.5,CHAR)] for o in bop], space_after=6, line_spacing=1.05)

# ---- 2.6 trust architecture
s = content_slide(prs, num(), "Trust & proof: the Panacea assurance system", kicker="Workshop 2 · Trust architecture")
divider(s)
txt(s, 0.5, 1.7, 12.3, 0.5, [[("The current packs list 10+ scattered assurances. We tier them into ",12,CHAR),
    ("one proof device and a single Panacea assurance seal",12,PURPLE,True),(" — the moat competitors can't copy.",12,CHAR)]], line_spacing=1.15)
tiers=[("THE ANCHOR","Assurance of Panacea Biotec","A pharma company stands behind every pack. 7N corporate endorsement + one “Assurance” seal, corner-locked.",PINK),
    ("THE PROOF","One recurring proof mark","“Paediatrician-recommended · Dermatologically tested.” One device, every SKU — instantly recognised.",BLUE),
    ("THE REASSURANCE","Simplified No-No list","From a wall of “free-froms” to a tight, tiered set: 100% safe actives · steroid & paraben free · allergen-free declaration.",GREEN)]
x=0.5
for h,t,b,c in tiers:
    card(s, x, 2.5, 3.94, 3.6, fill=SOFT)
    rect(s, x, 2.5, 3.94, 0.62, fill=c, shape=MSO_SHAPE.ROUNDED_RECTANGLE).adjustments[0]=0.08
    rect(s, x, 2.8, 3.94, 0.32, fill=c)
    txt(s, x+0.25, 2.6, 3.5, 0.45, [[(h,11.5,WHITE,True)]], anchor=MSO_ANCHOR.MIDDLE)
    txt(s, x+0.25, 3.28, 3.5, 0.7, [[(t,13.5,PURPLE,True,False,TITLE_FONT)]], line_spacing=1.0)
    txt(s, x+0.25, 4.15, 3.5, 1.8, [[(b,11,CHAR)]], line_spacing=1.16)
    x+=4.12
txt(s, 0.5, 6.25, 12.3, 0.4, [[("PRINCIPLE   ",11,PINK,True),
    ("Trust is not more badges — it is one badge nobody else can earn: a pharma company's name.",12,PURPLE,True)]])

# ##################################################################
# WORKSHOP 3 — BRAND MEANING, VOICE & PAYOFF SYSTEM
# ##################################################################
workshop_opener(prs, 3, "Brand Meaning, Voice & Payoff Lines",
    "What does NikoMom stand for — and how does it sound and sign off?",
    ["Purpose, promise & the positioning statement","Old foundation vs new foundation",
     "Personality & tone of voice: “clinical warmth”","The payoff-line system — master to product",
     "Naming architecture, cleaned up","Mnemonic & mascot — decisions resolved"],
    num(), accent=VIOLET)

# ---- 3.1 purpose & positioning
s = content_slide(prs, num(), "From reassurance to confidence", kicker="Workshop 3 · Purpose & positioning")
divider(s)
rows=[("Brand role","Remove fear, confusion & anxiety","Give parents proof and earned confidence"),
    ("Core emotion","“I don't need to overthink this.”","“I know I'm protecting my baby — and I can see it.”"),
    ("Promise","Protects what's still growing, gently, every day","Protects your baby's skin barrier — proven, every day"),
    ("Positioning","Baby Care Expert","India's Baby Skin-Barrier Company")]
txt(s, 0.5, 1.65, 6.0, 0.35, [[("CURRENT FOUNDATION",10.5,GREY,True)]])
txt(s, 6.85, 1.65, 6.0, 0.35, [[("EVOLVED FOUNDATION",10.5,PINK,True)]])
y=2.05
for lbl,old,new in rows:
    txt(s, 0.5, y+0.02, 2.0, 0.9, [[(lbl.upper(),9.5,PURPLE,True)]], anchor=MSO_ANCHOR.MIDDLE)
    card(s, 2.35, y, 4.1, 0.92, fill=SOFT)
    txt(s, 2.55, y+0.08, 3.75, 0.78, [[(old,10.5,GREY)]], anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.05)
    txt(s, 6.55, y+0.28, 0.3, 0.4, [[("→",15,PINK,True)]])
    card(s, 6.85, y, 5.95, 0.92, fill=SOFTPK)
    txt(s, 7.08, y+0.08, 5.5, 0.78, [[(new,11,PURPLE,True)]], anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.05)
    y+=1.0
card(s, 0.5, 6.15, 12.33, 0.75, fill=PURPLE)
txt(s, 0.8, 6.28, 11.8, 0.55, [[("POSITIONING STATEMENT   ",10,RGBColor(0xEB,0xDD,0xF3),True),
    ("For India's modern parents, NikoMom is the pharma-backed baby skin-barrier company that turns everyday care into proven protection — because only Panacea Biotec pairs real clinical science with formulations built for Indian skin.",11,WHITE)]], line_spacing=1.1)

# ---- 3.2 tone of voice
s = content_slide(prs, num(), "Tone of voice: clinical warmth", kicker="Workshop 3 · Voice & personality")
divider(s)
txt(s, 0.5, 1.7, 12.3, 0.5, [[("Warm enough to trust with a newborn; precise enough to believe with the science. ",12,CHAR),
    ("We sound like a calm expert friend — never a lab, never a hype machine.",12,PURPLE,True)]], line_spacing=1.15)
traits=[("Confident, not anxious","We state what's proven; we don't stoke fear.",PINK),
    ("Precise, not clinical","Plain words for real science. No jargon walls.",BLUE),
    ("Warm, not soft","Human and kind — but backed by evidence.",ORANGE),
    ("Proof, not promises","Every claim resolves to something visible.",GREEN)]
x=0.5
for i,(h,b,c) in enumerate(traits):
    col=i%2; row=i//2
    xx=0.5+col*3.1 if False else 0.5+i*3.09
    card(s, xx, 2.5, 2.92, 1.5, fill=SOFT)
    rect(s, xx, 2.5, 2.92, 0.09, fill=c)
    txt(s, xx+0.2, 2.7, 2.55, 0.6, [[(h,12,c,True,False,TITLE_FONT)]], line_spacing=1.0)
    txt(s, xx+0.2, 3.35, 2.55, 0.6, [[(b,10,CHAR)]], line_spacing=1.1)
card(s, 0.5, 4.25, 6.05, 2.4, fill=SOFTPK)
txt(s, 0.78, 4.45, 5.5, 0.4, [[("WORDS WE USE",12,GREEN,True)]])
txt(s, 0.82, 4.9, 5.5, 1.7, [[("✓  barrier · protect · proven · seal · calm",11.5,CHAR)],
    [("✓  visible · everyday · 24-hour · gentle-yet-effective",11.5,CHAR)],
    [("✓  dermatologically tested · paediatrician-recommended",11.5,CHAR)]], space_after=8, line_spacing=1.1)
card(s, 6.75, 4.25, 6.05, 2.4, fill=SOFT)
txt(s, 7.03, 4.45, 5.5, 0.4, [[("WORDS WE AVOID",12,PINK,True)]])
txt(s, 7.07, 4.9, 5.5, 1.7, [[("✕  fear framing · “chemicals” scare tactics",11.5,CHAR)],
    [("✕  empty superlatives · “miracle”, “#1”, hype",11.5,CHAR)],
    [("✕  jargon dumps · unexplained INCI names",11.5,CHAR)]], space_after=8, line_spacing=1.1)

# ---- 3.3 payoff-line system
s = content_slide(prs, num(), "The payoff-line system", kicker="Workshop 3 · Endlines that ladder")
divider(s)
txt(s, 0.5, 1.68, 12.3, 0.45, [[("One master line governs the brand; each product carries its own — but all resolve to the same idea: ",12,CHAR),
    ("protection you can see.",12,PINK,True)]], line_spacing=1.12)
card(s, 0.5, 2.3, 12.33, 1.0, fill=PURPLE)
txt(s, 0.8, 2.42, 8.0, 0.8, [[("MASTER PAYOFF",10,RGBColor(0xEB,0xDD,0xF3),True)],[("Protection, proven.",30,WHITE,True,False,TITLE_FONT)]], space_after=2)
txt(s, 8.7, 2.5, 4.0, 0.8, [[("SUPPORTING LINE",10,RGBColor(0xEB,0xDD,0xF3),True)],[("The science of a protected baby.",13,WHITE,False,True)]], anchor=MSO_ANCHOR.MIDDLE, space_after=2, line_spacing=1.05)
txt(s, 0.5, 3.5, 12.3, 0.35, [[("PRODUCT PAYOFF LINES",11,VIOLET,True)]])
y=3.9
for i,(nm,act,old,c,hero,proof,ing,ladder,pay) in enumerate(PRODUCTS):
    col=i%2; row=i//2
    xx=0.5+col*6.16; yy=3.9+row*0.9
    card(s, xx, yy, 6.0, 0.78, fill=SOFT)
    rect(s, xx, yy, 0.08, 0.78, fill=c)
    txt(s, xx+0.22, yy+0.1, 2.5, 0.6, [[(nm,10.5,PURPLE,True)]], anchor=MSO_ANCHOR.MIDDLE, line_spacing=0.95)
    txt(s, xx+2.7, yy+0.1, 3.2, 0.6, [[("“"+pay+"”",11,c,True,True)]], anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.0)
    y+=0.9

# ---- 3.4 naming architecture
s = content_slide(prs, num(), "Naming, cleaned up", kicker="Workshop 3 · Naming architecture")
divider(s)
txt(s, 0.5, 1.7, 12.3, 0.5, [[("The current names repeat “Baby” and run to three lines. We keep the ",12,CHAR),("NikoMom",12,PINK,True),
    (" equity, cut the clutter, and lead with the barrier action — searchable and shelf-legible.",12,CHAR)]], line_spacing=1.15)
txt(s, 0.5, 2.4, 6.0, 0.35, [[("BEFORE",10.5,GREY,True)]])
txt(s, 6.85, 2.4, 6.0, 0.35, [[("AFTER",10.5,PINK,True)]])
namepairs=[("NikoMom Baby Massage Oil","NikoMom Massage Oil · Nourish & Seal"),
    ("NikoMom Baby Head to Toe Wash","NikoMom 3-in-1 Wash · Cleanse & Preserve"),
    ("NikoMom Baby Daily Lotion","NikoMom Daily Lotion · Hydrate & Strengthen"),
    ("NikoMom Baby Diaper Rash Cream","NikoMom Rash Cream · Repair & Shield"),
    ("NikoMom Baby Premium Tape Diaper","NikoMom Diapers · Dry & Protect")]
y=2.8
for old,new in namepairs:
    card(s, 0.5, y, 5.95, 0.62, fill=SOFT)
    txt(s, 0.72, y+0.06, 5.6, 0.5, [[(old,10.5,GREY)]], anchor=MSO_ANCHOR.MIDDLE)
    txt(s, 6.5, y+0.11, 0.3, 0.4, [[("→",13,PINK,True)]])
    card(s, 6.85, y, 5.95, 0.62, fill=SOFTPK)
    txt(s, 7.07, y+0.06, 5.6, 0.5, [[(new,10.5,PURPLE,True)]], anchor=MSO_ANCHOR.MIDDLE)
    y+=0.72
txt(s, 0.5, 6.5, 12.3, 0.4, [[("RULES   ",11,VIOLET,True),
    ("Drop “Baby” (the brand already says it) · one line per name · barrier action as descriptor · drop “Premium” (let quality show) · BarrierNest™ is the only proprietary name.",10.5,CHAR)]], line_spacing=1.1)

# ---- 3.5 mnemonic & mascot
s = content_slide(prs, num(), "Mnemonic & mascot — decided", kicker="Workshop 3 · Sensory identity")
divider(s)
txt(s, 0.5, 1.7, 12.3, 0.45, [[("Two open questions from the current deck, now resolved against the strategy.",12,CHAR)]])
card(s, 0.5, 2.35, 6.05, 4.25, fill=SOFT)
chip(s, 0.78, 2.6, 1.7, "MASCOT", color=PINK, h=0.42, size=12)
txt(s, 2.7, 2.6, 3.6, 0.45, [[("Decision: NO mascot",15,PINK,True,False,TITLE_FONT)]], anchor=MSO_ANCHOR.MIDDLE)
txt(s, 0.82, 3.25, 5.5, 3.2, [[("A cartoon animal signals ",11.5,CHAR),("mass, not medicine",11.5,PURPLE,True),(".",11.5,CHAR)],
    [("Your own W1 decision agreed: avoid a mascot for premium positioning.",11.5,CHAR)],
    [("A science-backed barrier brand earns trust through restraint, not characters.",11.5,CHAR)],
    [("“Niko” stays the brand name — warm, human — not a teddy bear.",11.5,PURPLE,True)]], space_after=9, line_spacing=1.12)
card(s, 6.75, 2.35, 6.05, 4.25, fill=SOFTPK)
chip(s, 7.03, 2.6, 1.9, "MNEMONIC", color=VIOLET, h=0.42, size=12)
txt(s, 9.1, 2.6, 3.6, 0.45, [[("Evolve, don't drop",15,VIOLET,True,False,TITLE_FONT)]], anchor=MSO_ANCHOR.MIDDLE)
txt(s, 7.07, 3.25, 5.5, 3.2, [[("Retire the literal mother-&-child image (it centres the parent, not the outcome).",11.5,CHAR)],
    [("Invent a ",11.5,CHAR),("“smile-in-a-shield”",11.5,PURPLE,True),(" mark: the Niko smile held inside a protective barrier arc.",11.5,CHAR)],
    [("Owns both meanings at once — warmth (smile) and science (shield).",11.5,CHAR)],
    [("Works as a silent stamp at 200px, on pack, and as an app icon.",11.5,PURPLE,True)]], space_after=8, line_spacing=1.12)

# ##################################################################
# WORKSHOP 4 — VISUAL IDENTITY & PACKAGING SYSTEM
# ##################################################################
workshop_opener(prs, 4, "Visual Identity & Packaging System",
    "How does the strategy become something a parent can see and hold?",
    ["The “clinical warmth” execution principles","Packaging architecture: the front-of-pack zones",
     "Colour & SKU differentiation system","Structure & materials: bottles, pumps, feel",
     "Iconography, space & the proof device"],
    num(), accent=ORANGE)

# ---- 4.1 execution principles
s = content_slide(prs, num(), "Clinical warmth — the execution rules", kicker="Workshop 4 · Design principles")
divider(s)
txt(s, 0.5, 1.7, 12.3, 0.5, [[("The current packs use only ~40% of available space and read generic. Our fix isn't “add more” — it's ",12,CHAR),
    ("hierarchy, one owned colour field, and a technology-led minimalism that still feels human.",12,PURPLE,True)]], line_spacing=1.15)
princ=[("Technology-led, minimal","Clean, premium, uncluttered — your own W1 recommendation.",BLUE),
    ("Own a colour field","Retire plain white; a branded field lifts shelf stand-out.",PINK),
    ("Structure as mnemonic","A soft, rounded silhouette recognised before the label is read.",VIOLET),
    ("One outcome, one proof","A single hero claim + a single proof device — never a wall.",GREEN),
    ("Warmth in the detail","Soft-touch finish, rounded forms, human colour — not a lab.",ORANGE),
    ("Use the space with rank","Fill 70%+ of pack — but every element earns its position.",SKY)]
x=0.5
for i,(h,b,c) in enumerate(princ):
    col=i%3; row=i//3
    xx=0.5+col*4.12; yy=2.5+row*2.0
    card(s, xx, yy, 3.95, 1.82, fill=SOFT)
    rect(s, xx, yy, 3.95, 0.09, fill=c)
    txt(s, xx+0.22, yy+0.26, 3.5, 0.5, [[(h,12.5,c,True,False,TITLE_FONT)]], line_spacing=1.0)
    txt(s, xx+0.22, yy+0.8, 3.5, 0.9, [[(b,10.5,CHAR)]], line_spacing=1.14)

# ---- 4.2 packaging architecture
s = content_slide(prs, num(), "The front-of-pack architecture", kicker="Workshop 4 · Packaging hierarchy")
divider(s)
txt(s, 0.5, 1.7, 12.3, 0.45, [[("Six fixed zones, top to bottom. Same skeleton on every SKU — only the outcome and the colour change.",12,CHAR)]], line_spacing=1.1)
zones=[("Masterbrand + endorsement","NikoMom + 7N Panacea Biotec assurance",PURPLE),
    ("Variant + hero outcome","“24-hour barrier hydration” — the biggest thing on pack",PINK),
    ("BarrierNest™ signature","One technology badge, consistently placed",VIOLET),
    ("One proof mark","Paediatrician-recommended · Dermatologically tested",BLUE),
    ("Key ingredient / descriptor","Hero actives or 3-in-1 — the reason-to-believe",GREEN),
    ("Regulatory zone","Net weight, FSSAI, batch, Made-in-India",GREY)]
y=2.3
for i,(h,b,c) in enumerate(zones):
    card(s, 3.0, y, 9.8, 0.66, fill=SOFT)
    rect(s, 3.0, y, 0.5, 0.66, fill=c)
    txt(s, 3.0, y+0.06, 0.5, 0.54, [[(str(i+1),17,WHITE,True,False,TITLE_FONT)]], align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    txt(s, 3.7, y+0.08, 3.6, 0.5, [[(h,12,PURPLE,True)]], anchor=MSO_ANCHOR.MIDDLE, line_spacing=0.98)
    txt(s, 7.4, y+0.08, 5.3, 0.5, [[(b,10,CHAR)]], anchor=MSO_ANCHOR.MIDDLE, line_spacing=0.98)
    y+=0.72
# pack silhouette hint
card(s, 0.5, 2.3, 2.3, 4.28, fill=SOFTPK)
txt(s, 0.65, 2.45, 2.0, 0.5, [[("THE PACK",10,ORANGE,True)]])
rb=rect(s, 1.15, 3.0, 1.0, 3.2, fill=WHITE, line=ORANGE, line_w=1.5, shape=MSO_SHAPE.ROUNDED_RECTANGLE); rb.adjustments[0]=0.18
rect(s, 1.35, 2.75, 0.6, 0.4, fill=ORANGE, shape=MSO_SHAPE.ROUNDED_RECTANGLE).adjustments[0]=0.4
for zi,(zc) in enumerate([PURPLE,PINK,VIOLET,BLUE,GREEN,GREY]):
    rect(s, 1.28, 3.2+zi*0.44, 0.74, 0.32, fill=zc, shape=MSO_SHAPE.ROUNDED_RECTANGLE).adjustments[0]=0.3

# ---- 4.3 colour & SKU system
s = content_slide(prs, num(), "Colour & SKU differentiation", kicker="Workshop 4 · Colour system")
divider(s)
txt(s, 0.5, 1.7, 12.3, 0.5, [[("Purple is the master-brand spine. Each product owns one accent from the Panacea palette — so the range reads as ",12,CHAR),
    ("one family on the shelf, six clear choices in the hand.",12,PURPLE,True)]], line_spacing=1.15)
x=0.5
for i,(nm,act,old,c,hero,proof,ing,ladder,pay) in enumerate(PRODUCTS):
    xx=0.5+i*2.06
    card(s, xx, 2.55, 1.92, 2.5, fill=WHITE, line=LGREY)
    rect(s, xx, 2.55, 1.92, 1.15, fill=c, shape=MSO_SHAPE.ROUNDED_RECTANGLE).adjustments[0]=0.06
    rect(s, xx, 3.3, 1.92, 0.4, fill=c)
    txt(s, xx+0.12, 3.75, 1.7, 0.8, [[(nm,10,PURPLE,True)]], line_spacing=0.98)
    txt(s, xx+0.12, 4.55, 1.7, 0.4, [[(act,9,c,True)]], line_spacing=0.95)
card(s, 0.5, 5.3, 12.33, 1.3, fill=SOFT)
txt(s, 0.8, 5.48, 11.8, 0.4, [[("WHY IT WORKS",11,ORANGE,True)]])
txt(s, 0.8, 5.85, 11.8, 0.7, [[("Solves the current “white doesn't stand out” problem · lets a parent find “the orange one” by memory · keeps Amazon thumbnails distinct · and a shared purple spine + BarrierNest™ badge holds the six together as an unmistakable system.",11.5,CHAR)]], line_spacing=1.15)

# ---- 4.4 structure & materials
s = content_slide(prs, num(), "Structure & materials", kicker="Workshop 4 · Form & feel")
divider(s)
txt(s, 0.5, 1.7, 12.3, 0.45, [[("The bottle itself should communicate safety and premium before a word is read — and resolve the open cap decision.",12,CHAR)]], line_spacing=1.1)
dec=[("Dispensing: pump with on/off","Single-hand “no-slip” dispensing in a wet bathroom, spill-proof lock. Rejects the flip-on cap (tears away, feels cheap).",PINK),
    ("Silhouette: soft & rounded","A familiar, easy-hold form with no hard edges — safety felt in the hand, and a shape ownable as a mnemonic.",VIOLET),
    ("Finish: soft-touch, premium","Matte soft-touch with a branded colour field — reads clinical-warm, not glossy-mass.",ORANGE),
    ("Diapers & wipes: proof by feel","Ultra-soft breathable top-sheet, wetness indicator, aloe anti-rash; resealable biodegradable wipe pack.",GREEN)]
x=0.5
for i,(h,b,c) in enumerate(dec):
    col=i%2; row=i//2
    xx=0.5+col*6.16; yy=2.45+row*2.05
    card(s, xx, yy, 6.0, 1.88, fill=SOFT)
    rect(s, xx, yy, 0.09, 1.88, fill=c)
    txt(s, xx+0.25, yy+0.2, 5.5, 0.5, [[(h,13,c,True,False,TITLE_FONT)]], line_spacing=1.0)
    txt(s, xx+0.25, yy+0.75, 5.5, 1.0, [[(b,11,CHAR)]], line_spacing=1.16)

# ---- 4.5 iconography
s = content_slide(prs, num(), "Icons, space & the proof device", kicker="Workshop 4 · Information design")
divider(s)
ic=[("Max 4–6 icons","A tight, legible icon set — not a badge-storm. Each icon earns space.",BLUE),
    ("One proof device","A single, repeated “tested & recommended” mark across the whole range.",PINK),
    ("Fill 70%+, with hierarchy","Answer the current 40%-vs-75% gap — but through rank, never clutter.",GREEN),
    ("Design motif","A quiet barrier-arc motif ties pack, digital and comms into one language.",VIOLET)]
x=0.5
for i,(h,b,c) in enumerate(ic):
    xx=0.5+i*3.09
    card(s, xx, 2.4, 2.92, 2.3, fill=SOFT)
    rect(s, xx, 2.4, 2.92, 0.09, fill=c)
    txt(s, xx+0.2, 2.62, 2.55, 0.6, [[(h,12.5,c,True,False,TITLE_FONT)]], line_spacing=1.0)
    txt(s, xx+0.2, 3.3, 2.55, 1.3, [[(b,10.5,CHAR)]], line_spacing=1.16)
card(s, 0.5, 5.0, 12.33, 1.6, fill=SOFTPK)
txt(s, 0.8, 5.2, 11.8, 0.4, [[("THE 8-SECOND TEST — BUILT IN",12,PINK,True,False,TITLE_FONT)]])
txt(s, 0.8, 5.65, 11.8, 0.9, [[("A parent picks up the pack and, with no ad recall and no salesperson, reads in order: ",11.5,CHAR),
    ("what it is",11.5,PURPLE,True),(" (outcome) → ",11.5,CHAR),("why it's right",11.5,PURPLE,True),
    (" (BarrierNest + proof) → ",11.5,CHAR),("why to trust it",11.5,PURPLE,True),
    (" (Panacea). Decision made — in under eight seconds.",11.5,CHAR)]], line_spacing=1.16)

# ##################################################################
# WORKSHOP 5 — INTEGRATED BRAND & COMMUNICATION SYSTEM
# ##################################################################
workshop_opener(prs, 5, "Integrated Brand & Communication System",
    "Does the brand hold together — and flex — across every place a parent meets it?",
    ["Channel adaptation matrix (pack to WhatsApp)","Messaging adaptation by context",
     "The integrated brand-management cascade","Beyond the shelf: subscription & community",
     "Final output, governance & what's locked"],
    num(), accent=GREEN)

# ---- 5.1 channel matrix
s = content_slide(prs, num(), "One brand, every channel", kicker="Workshop 5 · Channel adaptation")
divider(s)
txt(s, 0.5, 1.7, 12.3, 0.45, [[("The system must flex without breaking. Each channel leads with a different rung of the same ladder — but it is always the same ladder.",12,CHAR)]], line_spacing=1.1)
ch=[("Amazon","Outcome thumbnail + A+ proof modules + reviews",BLUE),
    ("Quick commerce","One outcome + one proof, legible at tile size",SKY),
    ("Website / CRM","Barrier-science story + the outcome ladder",VIOLET),
    ("Retail shelf","SKU colour block + hero outcome at three feet",PINK),
    ("Doctors","Clinical proof + Panacea credibility leads",GREEN),
    ("Influencers","Real babies, real outcomes — authentic UGC",ORANGE),
    ("WhatsApp companion","A daily routine coach — the confidence engine",VIOLET),
    ("Subscription / refills","Barrier routine kits by growth stage",PINK)]
x=0.5
for i,(h,b,c) in enumerate(ch):
    col=i%4; row=i//4
    xx=0.5+col*3.08; yy=2.35+row*2.15
    card(s, xx, yy, 2.92, 1.95, fill=SOFT)
    rect(s, xx, yy, 2.92, 0.09, fill=c)
    txt(s, xx+0.2, yy+0.24, 2.55, 0.5, [[(h,12,c,True,False,TITLE_FONT)]], line_spacing=1.0)
    txt(s, xx+0.2, yy+0.75, 2.55, 1.1, [[(b,10,CHAR)]], line_spacing=1.14)

# ---- 5.2 messaging adaptation
s = content_slide(prs, num(), "Same brand, different job", kicker="Workshop 5 · Messaging by context")
divider(s)
txt(s, 0.5, 1.7, 12.3, 0.45, [[("Five contexts, five hierarchies — one voice. This is what stops an “integrated” brand from fragmenting into five different brands.",12,CHAR)]], line_spacing=1.1)
ctx=[("EDUCATE","Teach the barrier","Lead with the science: why the skin barrier matters and how NikoMom builds it.",BLUE),
    ("CONVERT","Close the sale","Lead with outcome + proof + offer. Least friction to “add to cart”.",PINK),
    ("EMOTION","Build the bond","Lead with the confident parent and the calm, protected baby.",ORANGE),
    ("RETAIL","Win at 3 feet","Lead with colour block + one outcome. Recognised, not read.",GREEN),
    ("MARKETPLACE","Get found & chosen","Lead with searchable descriptive names + proof + reviews.",VIOLET)]
y=2.35
for h,t,b,c in ctx:
    card(s, 0.5, y, 12.33, 0.78, fill=SOFT)
    rect(s, 0.5, y, 1.7, 0.78, fill=c, shape=MSO_SHAPE.ROUNDED_RECTANGLE).adjustments[0]=0.06
    rect(s, 1.1, y, 1.1, 0.78, fill=c)
    txt(s, 0.5, y+0.06, 1.7, 0.66, [[(h,12,WHITE,True,False,TITLE_FONT)]], align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    txt(s, 2.4, y+0.06, 3.0, 0.66, [[(t,12.5,PURPLE,True,False,TITLE_FONT)]], anchor=MSO_ANCHOR.MIDDLE)
    txt(s, 5.5, y+0.06, 7.1, 0.66, [[(b,11,CHAR)]], anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.05)
    y+=0.83

# ---- 5.3 integrated cascade
s = content_slide(prs, num(), "This is brand management, not a redesign", kicker="Workshop 5 · The integrated system")
divider(s)
txt(s, 0.5, 1.68, 12.3, 0.5, [[("Every layer is locked to the one above it. Change the strategy and everything moves; keep the strategy and nothing drifts. That single chain of custody — ",12,CHAR),
    ("strategy to shelf — is the deliverable.",12,PURPLE,True)]], line_spacing=1.15)
casc=[("W1","STRATEGY","Baby Skin-Barrier Company · “Protection, proven”",PINK),
    ("W2","CLAIMS","Outcome-led ladder · BarrierNest™ · proof architecture",BLUE),
    ("W3","MEANING & VOICE","Confidence · clinical warmth · payoff-line system",VIOLET),
    ("W4","DESIGN","Clinical-warmth pack · colour SKUs · 8-second front",ORANGE),
    ("W5","COMMUNICATION","Every channel & context, flexing without breaking",GREEN)]
y=2.45
for i,(w,h,b,c) in enumerate(casc):
    card(s, 0.5+i*0.25, y, 12.33-i*0.5, 0.66, fill=SOFT)
    rect(s, 0.5+i*0.25, y, 1.4, 0.66, fill=c, shape=MSO_SHAPE.ROUNDED_RECTANGLE).adjustments[0]=0.08
    rect(s, 1.2+i*0.25, y, 0.7, 0.66, fill=c)
    txt(s, 0.5+i*0.25, y+0.06, 1.4, 0.54, [[(w,15,WHITE,True,False,TITLE_FONT)]], align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    txt(s, 2.1+i*0.25, y+0.05, 3.2, 0.56, [[(h,12,c,True,False,TITLE_FONT)]], anchor=MSO_ANCHOR.MIDDLE)
    txt(s, 5.4+i*0.25, y+0.05, 6.7-i*0.5, 0.56, [[(b,10.5,CHAR)]], anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.0)
    if i<4: txt(s, 2.0+i*0.25, y+0.6, 0.6, 0.35, [[("▼",11,LGREY,True)]])
    y+=0.83

# ---- 5.4 final output & governance
s = content_slide(prs, num(), "Final output: three living documents", kicker="Workshop 5 · Governance")
divider(s)
txt(s, 0.5, 1.7, 12.3, 0.45, [[("The workshops resolve into three governing documents — so any team, agency or partner can execute NikoMom without it drifting.",12,CHAR)]], line_spacing=1.1)
docs=[("1  Brand Strategy","Purpose · positioning · audience · barrier-science narrative spine · payoff-line system",PINK),
    ("2  Identity Guidelines","Logo & endorsement · colour & SKU system · BarrierNest™ · pack architecture · mnemonic rules",VIOLET),
    ("3  Communication System","Claim & proof hierarchy · voice · channel & context playbooks · CTA principles",GREEN)]
x=0.5
for h,b,c in docs:
    card(s, x, 2.45, 3.94, 2.5, fill=SOFT)
    rect(s, x, 2.45, 3.94, 0.6, fill=c, shape=MSO_SHAPE.ROUNDED_RECTANGLE).adjustments[0]=0.08
    rect(s, x, 2.75, 3.94, 0.3, fill=c)
    txt(s, x+0.22, 2.53, 3.5, 0.45, [[(h,13,WHITE,True,False,TITLE_FONT)]], anchor=MSO_ANCHOR.MIDDLE)
    txt(s, x+0.22, 3.2, 3.5, 1.6, [[(b,11,CHAR)]], line_spacing=1.16)
    x+=4.12
card(s, 0.5, 5.15, 12.33, 1.45, fill=PURPLE)
txt(s, 0.8, 5.32, 11.8, 0.4, [[("LOCKED & NEXT",11,RGBColor(0xEB,0xDD,0xF3),True)]])
txt(s, 0.8, 5.7, 11.8, 0.8, [[("Locked:  ",12,WHITE,True),
    ("positioning · payoff system · BarrierNest™ · claim & proof hierarchy · colour/SKU system · voice.    ",11.5,RGBColor(0xEB,0xDD,0xF3)),
    ("Next:  ",12,WHITE,True),
    ("design execution of the six packs, the barrier-arc mnemonic, and the WhatsApp companion pilot.",11.5,RGBColor(0xEB,0xDD,0xF3))]], line_spacing=1.16)

# ---- closing
s = _blank(prs)
rect(s, 0, 0, 13.34, 7.5, fill=PURPLE)
rect(s, 0, 0, 13.34, 0.16, fill=PINK)
txt(s, 0.9, 1.5, 11.5, 0.5, [[("ONE STRATEGY, FIVE WORKSHOPS, ONE BRAND",13,RGBColor(0xEB,0xDD,0xF3),True)]], align=PP_ALIGN.CENTER)
txt(s, 0.9, 2.1, 11.5, 1.6, [[("Protection, proven.",52,WHITE,True,False,TITLE_FONT)],
    [("NikoMom — India's Baby Skin-Barrier Company.",20,RGBColor(0xEB,0xDD,0xF3),False,False,TITLE_FONT)]],
    align=PP_ALIGN.CENTER, space_after=8, line_spacing=1.05)
rect(s, 5.42, 4.2, 2.5, 0.05, fill=PINK)
txt(s, 0.9, 4.5, 11.5, 0.9, [[("From category strategy to what a parent reads on the shelf: a coherent,",14,RGBColor(0xE0,0xD0,0xEC))],
    [("differentiated, globally scalable brand system — integrated brand management, not a redesign.",14,RGBColor(0xE0,0xD0,0xEC))]],
    align=PP_ALIGN.CENTER, space_after=3, line_spacing=1.2)
# logo lockup bottom
lb=rect(s, 5.15, 5.75, 0.62, 0.62, fill=PINK, shape=MSO_SHAPE.ROUNDED_RECTANGLE); lb.adjustments[0]=0.28
tf=lb.text_frame; tf.vertical_anchor=MSO_ANCHOR.MIDDLE
for m in ('left','right','top','bottom'): setattr(tf,f'margin_{m}',0)
p=tf.paragraphs[0]; p.alignment=PP_ALIGN.CENTER; r=p.add_run(); r.text="7N"; _set_font(r,20,WHITE,True,False,TITLE_FONT)
txt(s, 5.9, 5.79, 3.2, 0.6, [[("Panacea Biotec",15,WHITE,True,False,TITLE_FONT)],[("BEST IN GOODNESS",8.5,RGBColor(0xD9,0xC4,0xE8),True)]], anchor=MSO_ANCHOR.MIDDLE, space_after=1)
txt(s, 0.9, 6.95, 11.5, 0.3, [[("July 2026   ·   Confidential. Circulation Restricted.",9,RGBColor(0xC9,0xB8,0xD8))]], align=PP_ALIGN.CENTER)

prs.save("/home/user/presentations/NikoMom_Workshop1_Reimagined.pptx")
print("Saved. Slides:", len(prs.slides.__iter__.__self__._sldIdLst))
