# 08 - Operations

> Tools, training, design, and internal operations
> **Total Time**: ~6 hours
> **Priority**: 🟣 Lower (Week 4)

---

## Overview

| Task | Time | Output |
|------|------|--------|
| Tool Setup Guides | 1.5 hrs | Integration documentation |
| Design Templates | 1.5 hrs | Visual asset guidelines |
| Team Training Guide | 2 hrs | Onboarding documentation |
| Partnership Materials | 1 hr | Contracts and processes |

---

## Task 1: Tool Setup Guides
**Location**: `08-Tools/tool-setup-guides.md` (NEW)
**Time**: 1.5 hours
**Priority**: 🟣 Lower

### Structure:

```markdown
# Tool Setup Guides

## Our Tech Stack

### Core Tools

| Tool | Purpose | Cost |
|------|---------|------|
| HubSpot Free | CRM + Email tracking | Free |
| Calendly | Meeting scheduling | $12/mo |
| Loom | Video messages | $15/mo |
| Notion | Internal wiki | $10/mo |
| Slack | Communication | Free |
| ConvertKit | Email marketing | $29/mo |
| Canva | Design | $13/mo |

**Total Monthly**: ~$80

### Automation Tools (for client work)
- Make (Integromat)
- Zapier
- n8n (self-hosted)
- Custom APIs

---

## Integration Map

```
LinkedIn → HubSpot (manual entry or automation)
    ↓
HubSpot ← → ConvertKit (sync subscribers)
    ↓
Calendly → HubSpot (meeting booked trigger)
    ↓
Notion (internal tracking)
```

---

## Setup Guides

### HubSpot Setup
See: `06-Analytics/crm-setup-guide.md`

### Calendly Setup
1. Create account at calendly.com
2. Connect calendar (Google/Outlook)
3. Create event types:
   - "30-Min Discovery Call"
   - "15-Min Quick Chat"
4. Set availability (buffer times, working hours)
5. Add to email signature and LinkedIn
6. Connect to HubSpot

### ConvertKit Setup
1. Create account
2. Verify domain (for deliverability)
3. Create segments (by ICP)
4. Build welcome sequence
5. Create landing page for lead magnet
6. Connect forms to website

### Notion Setup
1. Create workspace
2. Create databases:
   - Content Calendar
   - Meeting Notes
   - Project Tracker
   - SOPs
3. Set up templates for recurring content

---

## Automation Workflows We Use

### Lead Capture → CRM
**Trigger**: Form submission
**Actions**:
1. Add to HubSpot as contact
2. Add to ConvertKit with tag
3. Send internal Slack notification
4. Trigger welcome sequence

### Meeting Booked → Follow-up
**Trigger**: Calendly booking
**Actions**:
1. Add meeting to HubSpot
2. Send prep email (automated)
3. Create Notion meeting note template
4. Send reminder 1 hour before

### Proposal Sent → Follow-up
**Trigger**: Manual (mark in HubSpot)
**Actions**:
1. Schedule follow-up task (Day 3)
2. Add to "Proposal Follow-up" sequence
3. Alert if no response in 7 days
```

### Checklist:
- [ ] Document tech stack
- [ ] Create integration map
- [ ] Write setup guides for each tool
- [ ] Document automation workflows

---

## Task 2: Design Templates
**Location**: `07-Assets/design/social-templates.md` (NEW)
**Time**: 1.5 hours
**Priority**: 🟣 Lower

### Structure:

```markdown
# Design Templates & Guidelines

## Brand Colors

### Primary
- **Navy Blue**: #1a365d (trust, professionalism)
- **White**: #ffffff (clean, modern)

### Secondary
- **Orange**: #ed8936 (energy, action)
- **Light Gray**: #f7fafc (backgrounds)

### Usage
- Navy: Headlines, CTAs, key elements
- Orange: Accents, buttons, highlights
- White: Backgrounds, text on dark
- Gray: Secondary backgrounds

---

## Typography

### Headlines
- Font: Inter Bold (or system -apple-system)
- Size: 24-48px depending on context

### Body
- Font: Inter Regular
- Size: 16-18px
- Line height: 1.5-1.7

### LinkedIn Posts
- No custom fonts (platform-dependent)
- Use line breaks for readability
- Emojis sparingly (1-2 per post max)

---

## LinkedIn Post Dimensions

### Image Posts
- Square: 1080 x 1080px
- Landscape: 1200 x 627px
- Portrait: 1080 x 1350px

### Carousel Posts
- Dimensions: 1080 x 1080px per slide
- Max slides: 10
- File format: PDF (best) or images

### Video
- Dimensions: 1920 x 1080px (landscape) or 1080 x 1920px (portrait)
- Max length: 10 minutes
- File size: Max 5GB

---

## Content Templates (Canva)

### LinkedIn Post Template
[Link to Canva template]
- Headline area
- Body text area
- Logo placement
- CTA area

### Carousel Template
[Link to Canva template]
- Cover slide
- Content slides
- CTA slide

### Quote Graphic Template
[Link to Canva template]
- Testimonial text
- Client name/title
- Logo

### Stats Graphic Template
[Link to Canva template]
- Large number
- Context text
- Branding

---

## Image Guidelines

### Do:
- Use real photos when possible
- Show people (faces increase engagement)
- High contrast, clear text
- Consistent filter/style

### Don't:
- Cheesy stock photos
- Too much text on images
- Low resolution images
- Overly busy backgrounds

### Free Image Sources:
- Unsplash.com
- Pexels.com
- Generated AI images (carefully)

---

## Video Thumbnail Guidelines

### Elements:
- Face (yours or speaker's)
- 3-5 word headline
- Bright, contrasting colors
- Consistent style across videos

### Dimensions:
- YouTube: 1280 x 720px
- LinkedIn: 1200 x 627px

### Template:
[Link to Canva template]
```

### Checklist:
- [ ] Define brand colors
- [ ] Document typography
- [ ] Add dimension specs
- [ ] Create Canva template links
- [ ] Write image guidelines

---

## Task 3: Team Training Guide
**Location**: `TODO/team-training-guide.md` (NEW)
**Time**: 2 hours
**Priority**: 🟣 Lower

### Structure:

```markdown
# Team Training Guide

> How to onboard new team members to the Marketing Hub

---

## Week 1: Foundation

### Day 1: Orientation
- [ ] Read this guide completely
- [ ] Access all tools (HubSpot, Slack, etc.)
- [ ] Review `01-Strategy/positioning/positioning-strategy.md`
- [ ] Review all 3 ICP personas in `02-Audience/personas/`

### Day 2: Sales Training
- [ ] Read `TODO/book-insights-and-applications.md` (focus on sales sections)
- [ ] Read `05-Sales/sales-playbook.md`
- [ ] Shadow 2 discovery calls
- [ ] Review `05-Sales/email-sequences/`

### Day 3: Content Training
- [ ] Review `03-Content/ready-to-use/10-post-ideas.md`
- [ ] Review `04-Channels/linkedin/daily-playbook.md`
- [ ] Understand content calendar
- [ ] Post first LinkedIn content (with approval)

### Day 4: Tools Training
- [ ] HubSpot walkthrough
- [ ] Calendly setup
- [ ] Email tool training
- [ ] Notion workspace orientation

### Day 5: Practice
- [ ] Write 3 outreach messages for feedback
- [ ] Draft 2 LinkedIn posts for feedback
- [ ] Role-play discovery call
- [ ] Q&A session

---

## Week 2: Execution

### Sales Activities
- [ ] Make first 10 outreach attempts
- [ ] Book first discovery call
- [ ] Observe proposal presentation
- [ ] Handle first objections with support

### Content Activities
- [ ] Post daily on LinkedIn
- [ ] Engage per playbook
- [ ] Contribute to content calendar
- [ ] Draft first email newsletter

---

## Key Documents to Know

### Must Read (Priority 1):
1. `01-Strategy/positioning/positioning-strategy.md`
2. `02-Audience/personas/` (all 3)
3. `05-Sales/sales-playbook.md`
4. `TODO/book-insights-and-applications.md`
5. `04-Channels/linkedin/daily-playbook.md`

### Should Read (Priority 2):
1. `01-Strategy/messaging/messaging-framework.md`
2. `03-Content/lead-magnets/ai-automation-audit/`
3. `05-Sales/battle-cards/`
4. `06-Analytics/dashboards/weekly-kpi-dashboard.md`

### Reference (Priority 3):
Everything else as needed

---

## Role-Specific Training

### Sales Role
**Focus Areas**:
- Discovery call methodology
- Proposal writing
- Objection handling
- CRM discipline

**KPIs**:
- Outreach volume
- Call booking rate
- Proposal close rate

### Marketing Role
**Focus Areas**:
- LinkedIn execution
- Content creation
- Email marketing
- Analytics tracking

**KPIs**:
- Content published
- Engagement rates
- Lead magnet downloads
- List growth

---

## Common Questions

### "What do we actually do?"
We help businesses automate repetitive work using AI tools. We implement the automations, train teams to use them, and provide ongoing support.

### "Who do we sell to?"
Three main types:
1. Solopreneurs drowning in admin work
2. SME operations managers with growth pressure
3. Corporate innovation leads proving AI ROI

### "How do we differentiate?"
Speed (days not months), accessibility (built for non-technical), and comprehensiveness (education + implementation + support).

### "What's our sales process?"
Discovery call (Gap Selling) → Proposal → Close → Onboarding

---

## 30-60-90 Day Goals

### Day 30:
- [ ] Can articulate positioning confidently
- [ ] Can run discovery calls independently
- [ ] Posting LinkedIn content daily
- [ ] CRM habits established

### Day 60:
- [ ] Closed first deal (with support)
- [ ] Writing proposals independently
- [ ] Contributing content ideas
- [ ] Handling objections confidently

### Day 90:
- [ ] Fully independent in role
- [ ] Contributing to improvement of materials
- [ ] Training others on specific topics
- [ ] Hitting KPIs consistently
```

### Checklist:
- [ ] Write week 1 orientation
- [ ] Create key documents list
- [ ] Add role-specific training
- [ ] Write FAQ section
- [ ] Add 30-60-90 day goals

---

## Task 4: Partnership Materials
**Location**: `07-Assets/growth/partnership-agreement.md` (NEW)
**Time**: 1 hour
**Priority**: 🟣 Lower

### Structure:

```markdown
# Partnership Agreement Template

## REFERRAL PARTNER AGREEMENT

**Between**: Ai-Whisperers ("Company")
**And**: [Partner Name] ("Partner")
**Effective Date**: [Date]

---

### 1. Partnership Type

☐ Referral Partner (commission on referred clients)
☐ Strategic Partner (co-marketing, revenue share)
☐ Affiliate Partner (link-based tracking)

---

### 2. Commission Structure

#### For Referral Partners:
- **First project**: 10% of project value
- **Ongoing services**: 5% for first 12 months
- **Payment terms**: Within 30 days of client payment

#### Qualifying Referrals:
- Must be new client (not in our CRM)
- Client must mention partner by name
- Must close within 90 days of introduction

---

### 3. Partner Responsibilities

Partner agrees to:
- Only refer qualified prospects (fit our ICP)
- Not make guarantees on our behalf
- Disclose partnership relationship when relevant
- Maintain professional standards

---

### 4. Company Responsibilities

Company agrees to:
- Pay commissions as outlined
- Keep partner informed of referral status
- Provide marketing materials as needed
- Handle all client delivery

---

### 5. Term and Termination

- Initial term: 12 months
- Renewal: Automatic unless 30-day notice
- Either party may terminate with 30-day notice
- Commissions for closed deals honored after termination

---

### 6. Confidentiality

Both parties agree to keep confidential:
- Client information
- Pricing and commission details
- Business strategies

---

### Signatures

**Company**: ___________________ Date: _______
**Partner**: ___________________ Date: _______
```

### Checklist:
- [ ] Create agreement template
- [ ] Define commission structure
- [ ] Add partner responsibilities
- [ ] Include termination terms

---

## Completion Checklist

| # | Task | Time | Status | Date |
|---|------|------|--------|------|
| 1 | Tool Setup Guides | 1.5 hrs | ⬜ | |
| 2 | Design Templates | 1.5 hrs | ⬜ | |
| 3 | Team Training Guide | 2 hrs | ⬜ | |
| 4 | Partnership Materials | 1 hr | ⬜ | |

**All Operations Tasks Complete**: ⬜

---

*When done, update [00-INDEX.md](00-INDEX.md) progress dashboard*
