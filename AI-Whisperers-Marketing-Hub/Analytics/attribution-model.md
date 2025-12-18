# Lead Attribution Model

> Track where leads come from and which channels convert best
> **Model Type**: First-Touch Attribution (with multi-touch visibility)
> **Primary Tool**: UTM parameters + CRM Lead Source field

---

## Why Attribution Matters

| Without Attribution | With Attribution |
|---------------------|------------------|
| "We got 10 leads this month" | "We got 10 leads: 4 LinkedIn, 3 referral, 2 website, 1 email" |
| "Content seems to work" | "Educational posts convert 3x better than promotional" |
| "Keep doing everything" | "Double down on LinkedIn, reduce Twitter investment" |

---

## Attribution Model: First-Touch + Multi-Touch

### First-Touch (Primary)
**What**: The FIRST channel that brought them to us
**Why**: Tells us what's creating awareness
**Use**: Primary reporting metric

### Multi-Touch (Secondary)
**What**: ALL touchpoints before conversion
**Why**: Shows full journey
**Use**: Understanding, not primary decisions

### Example Journey

```
1. Saw LinkedIn post (First Touch ✓)
2. Visited website
3. Downloaded lead magnet
4. Received email sequence
5. Booked discovery call
6. Became client

Attribution: LinkedIn (organic)
Multi-touch: LinkedIn → Website → Lead Magnet → Email → Discovery
```

---

## Source Categories

### Primary Sources

| Source | Code | Description |
|--------|------|-------------|
| **LinkedIn Organic** | `linkedin-organic` | Posts, comments, profile views |
| **LinkedIn Outreach** | `linkedin-outreach` | Connection requests, DMs |
| **Website Organic** | `website-organic` | Direct/organic traffic |
| **Website Lead Magnet** | `website-leadmagnet` | Downloaded resource |
| **Referral** | `referral` | Client/partner referral |
| **Email Campaign** | `email-campaign` | Newsletter, sequence |
| **YouTube** | `youtube` | YouTube videos |
| **Cold Email** | `cold-email` | Outbound email |

### Secondary Sources

| Source | Code | Description |
|--------|------|-------------|
| Twitter/X | `twitter` | Tweets, threads |
| Webinar | `webinar` | Live events |
| Podcast | `podcast` | Guest appearances |
| Event | `event` | Conferences, meetups |
| Partner | `partner` | Partner referral |
| Paid Ads | `paid-[platform]` | LinkedIn/Google ads |

---

## UTM Parameter System

### UTM Structure

```
https://aiwhisperers.com/page?utm_source=X&utm_medium=Y&utm_campaign=Z&utm_content=W
```

| Parameter | Purpose | Examples |
|-----------|---------|----------|
| `utm_source` | Platform/channel | linkedin, youtube, email |
| `utm_medium` | Marketing medium | organic, paid, outreach |
| `utm_campaign` | Campaign name | q1-launch, lead-magnet |
| `utm_content` | Specific content | post-automation-tips, cta-button |

### Standard UTM Codes

#### LinkedIn

| Use Case | UTM Parameters |
|----------|---------------|
| Profile link | `?utm_source=linkedin&utm_medium=profile&utm_campaign=bio` |
| Post link | `?utm_source=linkedin&utm_medium=organic&utm_campaign=post&utm_content=[topic]` |
| DM link | `?utm_source=linkedin&utm_medium=outreach&utm_campaign=dm` |
| Article | `?utm_source=linkedin&utm_medium=organic&utm_campaign=article&utm_content=[title]` |

#### Email

| Use Case | UTM Parameters |
|----------|---------------|
| Newsletter | `?utm_source=email&utm_medium=newsletter&utm_campaign=weekly-[date]` |
| Nurture sequence | `?utm_source=email&utm_medium=nurture&utm_campaign=[sequence-name]&utm_content=email-[#]` |
| Cold outreach | `?utm_source=email&utm_medium=cold&utm_campaign=[campaign-name]` |

#### YouTube

| Use Case | UTM Parameters |
|----------|---------------|
| Video description | `?utm_source=youtube&utm_medium=organic&utm_campaign=video&utm_content=[video-title]` |
| Pinned comment | `?utm_source=youtube&utm_medium=organic&utm_campaign=comment&utm_content=[video-title]` |
| End screen | `?utm_source=youtube&utm_medium=organic&utm_campaign=endscreen` |

#### Other Channels

| Channel | UTM Parameters |
|---------|---------------|
| Twitter | `?utm_source=twitter&utm_medium=organic&utm_campaign=[topic]` |
| Webinar | `?utm_source=webinar&utm_medium=event&utm_campaign=[event-name]` |
| Partner | `?utm_source=partner&utm_medium=referral&utm_campaign=[partner-name]` |
| Podcast | `?utm_source=podcast&utm_medium=guest&utm_campaign=[show-name]` |

---

## Implementation

### Step 1: Set Up Link Tracking

#### Option A: URL Builder (Manual)
1. Use Google Campaign URL Builder
2. Enter base URL + UTM parameters
3. Copy full URL
4. Use in content

#### Option B: Link Shortener (Better)
1. Use Bitly or Rebrandly
2. Create branded short domain (e.g., go.aiwhisperers.com)
3. Create short links with UTMs built in
4. Easier to share, looks cleaner

### Step 2: Capture in Forms

All website forms should capture:
- Hidden UTM fields (auto-populated from URL)
- "How did you hear about us?" dropdown (backup)

### Step 3: Sync to CRM

When lead enters CRM:
1. UTM parameters → Lead Source field
2. If no UTM → Use form dropdown response
3. If neither → Mark as "Unknown" + investigate

---

## Where to Use UTMs

### Always Use UTMs

| Location | Link Destination |
|----------|-----------------|
| LinkedIn bio | Main website |
| LinkedIn post CTAs | Landing pages |
| YouTube descriptions | Website/landing pages |
| Email CTAs | All external links |
| Webinar registrations | Registration page |

### Don't Need UTMs

| Location | Why |
|----------|-----|
| Internal website links | Already on site |
| Email signature (to your site) | Low tracking value |
| PDF downloads | Can't track easily |

---

## Monthly Attribution Review

### Report Template

```
MONTH: [Month Year]

LEAD SOURCES:
| Source            | Leads | % of Total | Conversion Rate |
|-------------------|-------|------------|-----------------|
| LinkedIn Organic  |       |            |                 |
| LinkedIn Outreach |       |            |                 |
| Website Organic   |       |            |                 |
| Website Lead Mag  |       |            |                 |
| Referral          |       |            |                 |
| Email Campaign    |       |            |                 |
| YouTube           |       |            |                 |
| Cold Email        |       |            |                 |
| Other             |       |            |                 |
| Unknown           |       |            |                 |
| TOTAL             |       | 100%       |                 |

TOP PERFORMING:
1. [Source]: [#] leads, [%] conversion
2. [Source]: [#] leads, [%] conversion
3. [Source]: [#] leads, [%] conversion

UNDERPERFORMING:
1. [Source]: [#] leads, [%] conversion - Action: [decision]

REVENUE BY SOURCE:
| Source            | Closed Deals | Revenue |
|-------------------|--------------|---------|
|                   |              |         |

INSIGHTS:
-
-
-

ACTIONS FOR NEXT MONTH:
- Increase: [source]
- Decrease: [source]
- Test: [new source]
```

### Questions to Answer Monthly

1. **Which source drives most leads?**
2. **Which source has highest conversion rate?**
3. **Which source drives highest revenue?**
4. **What's the cost per lead by source?** (if applicable)
5. **Are any sources not worth the effort?**

---

## Attribution Best Practices

### Do's

- Use UTMs consistently on ALL external links
- Train team on attribution importance
- Review monthly, not daily
- Act on data (cut underperformers, double down on winners)
- Keep source list manageable (<15 categories)

### Don'ts

- Over-complicate (keep it simple first)
- Change UTM structure mid-campaign
- Ignore "unknown" sources (investigate them)
- Make decisions on small sample sizes (<30 leads)
- Forget to track offline sources (events, calls)

---

## Quick Reference: UTM Cheat Sheet

```
LINKEDIN POST:
aiwhisperers.com/page?utm_source=linkedin&utm_medium=organic&utm_campaign=post&utm_content=TOPIC

LINKEDIN DM:
aiwhisperers.com/page?utm_source=linkedin&utm_medium=outreach&utm_campaign=dm

EMAIL NEWSLETTER:
aiwhisperers.com/page?utm_source=email&utm_medium=newsletter&utm_campaign=weekly-DATE

YOUTUBE VIDEO:
aiwhisperers.com/page?utm_source=youtube&utm_medium=organic&utm_campaign=video&utm_content=VIDEO-TITLE

COLD EMAIL:
aiwhisperers.com/page?utm_source=email&utm_medium=cold&utm_campaign=CAMPAIGN-NAME

PARTNER REFERRAL:
aiwhisperers.com/page?utm_source=partner&utm_medium=referral&utm_campaign=PARTNER-NAME
```

---

## Tools & Resources

| Tool | Use | Cost |
|------|-----|------|
| Google Campaign URL Builder | Create UTMs | Free |
| Bitly | Short links with tracking | Free tier |
| HubSpot | CRM attribution | Free tier |
| Google Analytics | Website attribution | Free |
| Notion/Sheets | Monthly tracking | Free |

---

*Start simple. Track consistently. Review monthly. Optimize quarterly.*
