# CRM Setup Guide

> HubSpot Free CRM configuration for AI-Whisperers
> **Recommended Tool**: HubSpot Free (upgradeable as we scale)
> **Alternative**: Pipedrive, Salesforce Essentials

---

## Why HubSpot Free?

| Feature | HubSpot Free | Notes |
|---------|--------------|-------|
| Contact management | Unlimited | No per-contact fees |
| Deal pipeline | 1 pipeline | Enough for our model |
| Email tracking | Yes | Opens, clicks |
| Meeting scheduler | Yes | Calendly alternative |
| Forms | Yes | Lead capture |
| Live chat | Yes | Website widget |
| Reporting | Basic | Upgrade for advanced |
| **Cost** | **$0** | Upgrade when >$50K MRR |

---

## Account Setup (30 minutes)

### Step 1: Create Account
1. Go to hubspot.com/products/free
2. Sign up with company email
3. Verify email
4. Complete company profile

### Step 2: Company Settings
- **Company name**: Ai-Whisperers
- **Industry**: Consulting Services
- **Company size**: 1-10
- **Currency**: USD
- **Timezone**: Your primary timezone

### Step 3: Connect Email
1. Settings → Integrations → Email
2. Connect Gmail or Outlook
3. Enable email tracking (opens, clicks)
4. Set up email signature

### Step 4: Calendar Integration
1. Settings → Integrations → Calendar
2. Connect Google Calendar or Outlook
3. Set meeting availability
4. Create meeting link (alternative to Calendly)

---

## Pipeline Configuration

### Our 8-Stage Pipeline

| Stage | Definition | Expected Duration |
|-------|------------|-------------------|
| **1. Lead** | New contact, not yet qualified | 1-3 days |
| **2. Contacted** | First outreach made | 1-7 days |
| **3. Engaged** | Replied or showed interest | 3-7 days |
| **4. Discovery Scheduled** | Meeting booked | 1-7 days |
| **5. Discovery Complete** | Call completed, needs identified | 1-3 days |
| **6. Proposal Sent** | Formal proposal delivered | 3-14 days |
| **7. Negotiation** | Active discussion on terms | 1-14 days |
| **8. Closed Won** | Contract signed | - |
| **8b. Closed Lost** | Did not convert | - |

### Setup in HubSpot
1. Sales → Deals → Pipeline settings
2. Create custom pipeline "Sales Pipeline"
3. Add stages in order above
4. Set probability for each stage:
   - Lead: 5%
   - Contacted: 10%
   - Engaged: 20%
   - Discovery Scheduled: 30%
   - Discovery Complete: 50%
   - Proposal Sent: 70%
   - Negotiation: 80%
   - Closed Won: 100%
   - Closed Lost: 0%

---

## Custom Properties

### Contact Properties

| Property | Type | Options | Why |
|----------|------|---------|-----|
| **ICP Type** | Dropdown | Solopreneur, SME, Corporate | Segment by buyer type |
| **Lead Source** | Dropdown | See list below | Attribution |
| **Pain Points** | Multi-checkbox | Time waste, Errors, Scaling, Costs, Team | Discovery insights |
| **Budget Range** | Dropdown | <$5K, $5-15K, $15-50K, $50K+ | Qualification |
| **Timeline** | Dropdown | Immediate, 1-3 months, 3-6 months, Exploring | Urgency |
| **Decision Maker** | Checkbox | Yes/No | Qualification |
| **Referral Source** | Text | Free text | Track referrals |

### Lead Source Options
- LinkedIn (organic)
- LinkedIn (outreach)
- Website (organic)
- Website (lead magnet)
- Referral
- Email campaign
- YouTube
- Twitter/X
- Webinar
- Event
- Cold email
- Partner referral
- Other

### Deal Properties

| Property | Type | Why |
|----------|------|-----|
| **Service Type** | Dropdown: Course, DWY, DFY, Retainer | Track service mix |
| **Initial Quote** | Currency | Compare to final |
| **Final Amount** | Currency | Revenue tracking |
| **Lost Reason** | Dropdown | See list below | Learn from losses |

### Lost Reason Options
- Price too high
- Chose competitor
- Went DIY
- Timeline mismatch
- No budget
- Ghosted
- Not a fit
- Internal changes
- Other

---

## Contact Views (Lists)

### Create These Saved Views

| View Name | Filter | Purpose |
|-----------|--------|---------|
| **Hot Leads** | Stage = Discovery Scheduled OR Proposal Sent | Daily focus |
| **Follow-Up Needed** | Last activity > 7 days, not Closed | Re-engage |
| **Solopreneurs** | ICP Type = Solopreneur | Segment outreach |
| **SME Leads** | ICP Type = SME | Segment outreach |
| **Corporate Leads** | ICP Type = Corporate | Segment outreach |
| **High Budget** | Budget Range = $15-50K OR $50K+ | Prioritize |
| **This Week's Meetings** | Meeting scheduled this week | Prep |
| **Referrals** | Lead Source = Referral | Track program |

---

## Daily CRM Habits (15 minutes)

### Morning Routine

```
□ Check "Hot Leads" view - any updates needed?
□ Review today's scheduled meetings (prep notes)
□ Check for new leads overnight
□ Update any deal stages from yesterday
```

### After Each Interaction

```
□ Log activity (call, email, meeting)
□ Add notes from conversation
□ Update deal stage if changed
□ Set next task/reminder
□ Update contact properties if learned new info
```

### End of Day

```
□ Review "Follow-Up Needed" view
□ Schedule tomorrow's tasks
□ Update any stale deals
□ Log any new contacts
```

---

## Weekly CRM Review (30 minutes)

### Every Friday

| Check | Action |
|-------|--------|
| **Pipeline health** | Any deals stuck? Move or close. |
| **Lead sources** | Which sources producing quality? |
| **Velocity** | Average time in each stage? |
| **Follow-ups** | Anyone waiting >7 days? |
| **Data quality** | Any contacts missing key fields? |

### Weekly Report Template

```
Week of: [DATE]

NEW LEADS: [#]
- LinkedIn: [#]
- Website: [#]
- Referral: [#]
- Other: [#]

PIPELINE MOVEMENT:
- Leads → Contacted: [#]
- Contacted → Engaged: [#]
- Engaged → Discovery: [#]
- Discovery → Proposal: [#]
- Proposal → Closed: [#]

DEALS CLOSED: [$]
DEALS LOST: [#] (reasons: [])

PIPELINE VALUE: [$]
WEIGHTED PIPELINE: [$]

NEXT WEEK FOCUS:
1. [Priority 1]
2. [Priority 2]
3. [Priority 3]
```

---

## Automation Setup (HubSpot Workflows)

### Workflow 1: New Lead Notification
- **Trigger**: New contact created
- **Action**: Send internal email notification
- **Purpose**: Never miss a new lead

### Workflow 2: Lead Assignment
- **Trigger**: New contact from [source]
- **Action**: Assign to specific owner
- **Purpose**: Route leads to right person

### Workflow 3: Follow-Up Reminder
- **Trigger**: No activity in 7 days, stage not Closed
- **Action**: Create task "Follow up with [contact]"
- **Purpose**: Never let leads go cold

### Workflow 4: Post-Meeting Task
- **Trigger**: Meeting completed
- **Action**: Create task "Send follow-up email"
- **Purpose**: Consistent follow-through

### Workflow 5: Deal Stage Alerts
- **Trigger**: Deal moves to Proposal Sent
- **Action**: Send Slack/email notification
- **Purpose**: Team visibility on hot deals

---

## Integration Setup

### Must-Have Integrations

| Tool | Integration | Purpose |
|------|-------------|---------|
| Gmail/Outlook | Native | Email sync, tracking |
| Calendar | Native | Meeting scheduling |
| Slack | HubSpot app | Deal notifications |
| Zoom | Native | Auto-log meetings |

### Nice-to-Have Integrations

| Tool | Integration | Purpose |
|------|-------------|---------|
| LinkedIn Sales Navigator | HubSpot app | Lead enrichment |
| Calendly | Zapier | If using Calendly |
| Stripe | Native | Payment tracking |
| Typeform | Native | Form submissions |

---

## Reporting Dashboard

### Create These Reports

| Report | Type | Frequency |
|--------|------|-----------|
| Pipeline by Stage | Funnel | Daily view |
| Deals by Lead Source | Pie chart | Weekly review |
| Revenue by Month | Bar chart | Monthly |
| Win Rate by ICP | Table | Monthly |
| Average Deal Size | Single value | Monthly |
| Time in Stage | Avg by stage | Monthly |
| Lost Reason Analysis | Pie chart | Monthly |

### Dashboard Setup
1. Reports → Create dashboard
2. Name: "Sales Dashboard"
3. Add all reports above
4. Set as default dashboard
5. Review weekly

---

## Data Entry Standards

### Contact Naming
- First name: Capitalize properly (John, not john or JOHN)
- Last name: Capitalize properly
- Company: Official company name
- Email: Lowercase

### Notes Format
```
[DATE] - [INTERACTION TYPE]
Summary: [1-2 sentence summary]
Key points:
- [Point 1]
- [Point 2]
Next steps: [Action item]
```

### Deal Naming
```
[Company Name] - [Service Type] - [Month/Year]
Example: "Acme Corp - DFY Implementation - Dec 2025"
```

---

## Common Mistakes to Avoid

| Mistake | Why It Hurts | Solution |
|---------|--------------|----------|
| Not logging activities | Can't track what works | Log everything |
| Skipping properties | Poor segmentation | Fill key fields |
| Leaving deals stale | False pipeline value | Weekly cleanup |
| No lost reason | Can't improve | Always capture |
| Duplicate contacts | Confusing reports | Search before create |
| No next task | Leads fall through | Always set next action |

---

## Upgrade Path

### When to Upgrade to HubSpot Starter ($20/mo)

- Need multiple pipelines
- Need more automation
- Need ad management
- Team grows to 3+ sales people

### When to Upgrade to Professional ($500/mo)

- Need advanced reporting
- Need sequences (automated emails)
- Need sales analytics
- $100K+ in pipeline

---

## Quick Reference Card

```
DAILY (15 min):
□ Check Hot Leads
□ Prep for meetings
□ Log activities
□ Update stages
□ Set next tasks

WEEKLY (30 min):
□ Review pipeline health
□ Check follow-up needed
□ Update stale deals
□ Complete weekly report

AFTER EVERY CALL:
□ Log activity
□ Add notes
□ Update stage
□ Set next task
□ Update properties
```

---

*Set up once, maintain daily. Your CRM is only as good as the data in it.*
