# 04 - Analytics & Tracking

> Everything needed to measure what's working
> **Total Time**: ~7 hours
> **Priority**: 🔴 Critical (Week 1)

---

## Overview

Current state: Dashboard template exists but no actual tracking, no attribution, no setup guide.

| Task | Time | Output |
|------|------|--------|
| CRM Setup Guide | 2 hrs | Tool recommendation + setup |
| Attribution Model | 1 hr | How we track sources |
| Weekly Dashboard | 2 hrs | Filled with real targets |
| Monthly Report Template | 1 hr | Complete template |
| A/B Test Framework | 1 hr | Test log + process |

---

## Task 1: Create CRM Setup Guide
**Location**: `06-Analytics/crm-setup-guide.md` (NEW)
**Time**: 2 hours
**Priority**: 🔴 Critical

### Structure:

```markdown
# CRM Setup Guide

## Recommended Tool: HubSpot Free CRM

### Why HubSpot Free:
- Free for unlimited contacts
- Email tracking built-in
- Pipeline management
- Meeting scheduler
- Integrates with most tools

### Alternatives:
| Tool | Best For | Cost |
|------|----------|------|
| HubSpot Free | Starting out | Free |
| Pipedrive | Sales-focused teams | $15/user/mo |
| Notion | Simple tracking | Free/$10/mo |
| Airtable | Customization | Free/$20/mo |

---

## Setup Instructions

### Step 1: Create Account
[Link + instructions]

### Step 2: Configure Pipeline Stages
Create these stages:
1. **Lead** - New contact, not qualified
2. **Qualified** - Fits ICP, has budget/authority
3. **Discovery Scheduled** - Call booked
4. **Discovery Complete** - Call done, proposal pending
5. **Proposal Sent** - Waiting for decision
6. **Negotiation** - Discussing terms
7. **Closed Won** - Deal signed
8. **Closed Lost** - Did not proceed

### Step 3: Create Custom Fields
Required fields:
- ICP Type (Solopreneur / SME Ops / Corporate)
- Lead Source (LinkedIn / Email / Referral / Content / Paid)
- First Touch Date
- Services Interested In
- Budget Range
- Timeline
- Decision Maker (Y/N)

### Step 4: Set Up Email Tracking
[Instructions for email integration]

### Step 5: Connect Calendar
[Instructions for meeting scheduler]

---

## Daily CRM Habits

### Morning (5 min):
- Check for new leads overnight
- Review today's scheduled calls
- Check for overdue follow-ups

### After Every Call:
- Log call notes immediately
- Update pipeline stage
- Set next action + date
- Add any new contacts

### End of Day (5 min):
- Ensure all activities logged
- Set tomorrow's priorities
- Check nothing is stuck

---

## Weekly CRM Review

Every Friday:
- [ ] All leads have next action date
- [ ] Pipeline stages are current
- [ ] No deals stuck >14 days
- [ ] Lead sources are tagged
- [ ] Notes are complete
```

### Checklist:
- [ ] Write tool recommendation section
- [ ] Write setup instructions (step-by-step)
- [ ] Define pipeline stages
- [ ] Define custom fields
- [ ] Write daily/weekly habits
- [ ] Add screenshots if helpful

---

## Task 2: Create Attribution Model
**Location**: `06-Analytics/attribution-model.md` (NEW)
**Time**: 1 hour
**Priority**: 🔴 Critical

### Structure:

```markdown
# Attribution Model

## How We Track Lead Sources

### Primary Question:
"How did you hear about us?"

### Source Categories:

| Source | How to Identify | UTM Parameter |
|--------|-----------------|---------------|
| LinkedIn Organic | Profile visit → DM | utm_source=linkedin&utm_medium=organic |
| LinkedIn Content | Commented/engaged | utm_source=linkedin&utm_medium=content |
| LinkedIn Outreach | We reached out first | utm_source=linkedin&utm_medium=outreach |
| Email Campaign | Clicked email link | utm_source=email&utm_campaign=[name] |
| Referral | Someone referred them | Ask: "Who referred you?" |
| Website Organic | Found via Google | utm_source=google&utm_medium=organic |
| Lead Magnet | Downloaded audit | utm_source=leadmagnet&utm_campaign=audit |
| Paid Ads | Clicked ad | utm_source=linkedin&utm_medium=paid |

---

## UTM Parameter System

### Structure:
`?utm_source=[source]&utm_medium=[medium]&utm_campaign=[campaign]`

### Examples:
- LinkedIn bio link: `?utm_source=linkedin&utm_medium=profile`
- Email signature: `?utm_source=email&utm_medium=signature`
- Newsletter CTA: `?utm_source=email&utm_campaign=newsletter-dec`
- LinkedIn post: `?utm_source=linkedin&utm_medium=post&utm_campaign=automation-tips`

### Where to Use:
- [ ] LinkedIn profile link
- [ ] Email signature links
- [ ] All email CTAs
- [ ] All social post links
- [ ] Lead magnet landing page (as final destination)

---

## Attribution Type: First Touch

We use **first-touch attribution**:
- The FIRST source that brought them to us gets credit
- Simpler to track and explain
- Better for understanding acquisition

### In CRM:
- "Lead Source" = First touch
- "Lead Source Detail" = Specific campaign/post

---

## Monthly Attribution Review

Questions to answer:
1. Which source brought the most leads?
2. Which source brought the most QUALIFIED leads?
3. Which source has the best conversion rate?
4. Which source has the highest deal value?
5. What's our cost per lead by source?

### Report Format:
| Source | Leads | SQLs | Deals | Revenue | CAC |
|--------|-------|------|-------|---------|-----|
| LinkedIn Organic | | | | | |
| LinkedIn Outreach | | | | | |
| Email | | | | | |
| Referral | | | | | |
| Lead Magnet | | | | | |
```

### Checklist:
- [ ] Define source categories
- [ ] Create UTM parameter system
- [ ] Document where to use UTMs
- [ ] Explain attribution type choice
- [ ] Create monthly review template

---

## Task 3: Complete Weekly KPI Dashboard
**Location**: `06-Analytics/dashboards/weekly-kpi-dashboard.md`
**Time**: 2 hours
**Priority**: 🔴 Critical

### What to Add:

1. **Realistic Targets** (based on current capacity):

```markdown
## Weekly Targets

### Traffic & Reach
| Metric | Target | Actual | Trend |
|--------|--------|--------|-------|
| LinkedIn profile views | 100 | | |
| LinkedIn post impressions | 2,000 | | |
| Website visits | 50 | | |
| Email list growth | 10 | | |

### Engagement
| Metric | Target | Actual | Trend |
|--------|--------|--------|-------|
| LinkedIn connection accepts | 25 | | |
| LinkedIn comments received | 20 | | |
| Email open rate | 25% | | |
| Email click rate | 3% | | |

### Leads
| Metric | Target | Actual | Trend |
|--------|--------|--------|-------|
| New leads (any source) | 10 | | |
| Qualified leads (SQLs) | 4 | | |
| Discovery calls booked | 2 | | |
| Proposals sent | 1 | | |

### Revenue
| Metric | Target | Actual | Trend |
|--------|--------|--------|-------|
| Deals closed | 0.5 | | |
| Revenue | $2,500 | | |
| Pipeline value | $15,000 | | |
```

2. **Tracking Instructions**:
```markdown
## How to Fill This Dashboard

### Every Monday:
1. Open Google Analytics → Get website visits
2. Open LinkedIn Analytics → Get profile views, impressions
3. Open HubSpot → Get leads, SQLs, pipeline
4. Open email tool → Get open/click rates
5. Calculate trends (⬆️ ➡️ ⬇️)

### Data Sources:
| Metric | Where to Find |
|--------|---------------|
| LinkedIn stats | LinkedIn → Analytics |
| Website visits | Google Analytics → Audience |
| Email stats | [Email tool] → Reports |
| Lead stats | HubSpot → Reports |
| Revenue | HubSpot → Deals |
```

3. **Revenue Connection**:
```markdown
## Revenue Math

### The Funnel:
- 10 leads/week
- 40% qualify → 4 SQLs/week
- 50% book call → 2 calls/week
- 50% get proposal → 1 proposal/week
- 50% close → 0.5 deals/week
- Average deal: $5,000
- **Weekly revenue: $2,500**
- **Monthly revenue: $10,000**

### If We Want $20K/month:
- Need 1 deal/week
- Need 2 proposals/week
- Need 4 calls/week
- Need 8 SQLs/week
- Need 20 leads/week
```

### Checklist:
- [ ] Set realistic targets for each metric
- [ ] Add tracking instructions
- [ ] Connect metrics to revenue
- [ ] Add data source references
- [ ] Add trend tracking method

---

## Task 4: Create Monthly Report Template
**Location**: `06-Analytics/dashboards/monthly-report-template.md`
**Time**: 1 hour
**Priority**: 🟠 High

### Structure:

```markdown
# Monthly Marketing Report - [Month Year]

## Executive Summary
[2-3 sentence overview of the month]

## Key Metrics

### vs. Last Month
| Metric | Last Month | This Month | Change |
|--------|------------|------------|--------|
| Leads | | | |
| SQLs | | | |
| Deals | | | |
| Revenue | | | |

### vs. Target
| Metric | Target | Actual | % of Target |
|--------|--------|--------|-------------|
| Leads | | | |
| SQLs | | | |
| Revenue | | | |

## Channel Performance

### LinkedIn
- Profile views:
- Connection requests sent:
- Accepts:
- Messages sent:
- Responses:
- Calls booked from LinkedIn:

### Email
- Emails sent:
- Open rate:
- Click rate:
- Leads from email:

### Content
- Posts published:
- Total impressions:
- Top performing post:
- Lead magnet downloads:

## What Worked
1.
2.
3.

## What Didn't Work
1.
2.
3.

## Learnings
1.
2.

## Next Month Priorities
1.
2.
3.

## Revenue Attribution
| Source | Leads | Deals | Revenue |
|--------|-------|-------|---------|
| LinkedIn | | | |
| Email | | | |
| Referral | | | |
| Other | | | |
```

### Checklist:
- [ ] Create template structure
- [ ] Add all key metrics
- [ ] Add channel breakdown
- [ ] Add reflection sections
- [ ] Add revenue attribution

---

## Task 5: Create A/B Test Framework
**Location**: `06-Analytics/tests/ab-test-log.md`
**Time**: 1 hour
**Priority**: 🟡 Medium

### Structure:

```markdown
# A/B Test Log

## How to Run Tests

### Step 1: Form Hypothesis
"If we [change], then [metric] will [improve] because [reason]."

### Step 2: Design Test
- Control (A): Current version
- Variant (B): New version
- Sample size needed: Minimum 100 per variant
- Duration: Minimum 1 week

### Step 3: Run Test
- Split traffic 50/50
- Don't change anything else
- Track daily

### Step 4: Analyze Results
- Is difference statistically significant?
- What did we learn?
- What's the next test?

---

## Test Log

### Test #1: [Name]
**Date**:
**Hypothesis**: If we [change], then [metric] will [improve] because [reason].

**What we tested**:
- A (Control):
- B (Variant):

**Results**:
| Version | Sample | [Metric] | Conversion |
|---------|--------|----------|------------|
| A | | | |
| B | | | |

**Winner**: A / B / Inconclusive

**Learnings**:

**Next Test**:

---

### Test #2: [Name]
[Same format]

---

## Test Ideas Backlog

| Test | Hypothesis | Priority |
|------|------------|----------|
| LinkedIn headline variations | Different hooks = higher engagement | High |
| Email subject lines | Question vs statement | High |
| CTA button text | "Book Call" vs "Get Assessment" | Medium |
| Landing page headline | Pain vs aspiration | Medium |
| Outreach message length | Short vs detailed | Medium |
```

### Checklist:
- [ ] Create testing process
- [ ] Create test log template
- [ ] Add 3-5 test ideas
- [ ] Add analysis framework

---

## Completion Checklist

| # | Task | Time | Status | Date |
|---|------|------|--------|------|
| 1 | CRM Setup Guide | 2 hrs | ⬜ | |
| 2 | Attribution Model | 1 hr | ⬜ | |
| 3 | Weekly Dashboard | 2 hrs | ⬜ | |
| 4 | Monthly Report | 1 hr | ⬜ | |
| 5 | A/B Test Framework | 1 hr | ⬜ | |

**All Analytics Tasks Complete**: ⬜

---

*When done, update [00-INDEX.md](00-INDEX.md) progress dashboard*
