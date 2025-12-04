# A/B Test Log

> Document every test. Learn from every result.

---

## Why Track Tests?

Without documentation:
- You repeat failed experiments
- You forget what worked
- You can't build on learnings
- Everything stays random

With documentation:
- Compound your learnings
- Make data-driven decisions
- Build a playbook of what works
- Continuously improve

---

## Test Template

```markdown
## Test #[NUMBER]: [NAME]

**Date**: [Start] - [End]
**Channel**: [LinkedIn / Email / Website / Ads]
**Type**: [Subject line / CTA / Copy / Design / Timing]

### Hypothesis
[If we do X, then Y will happen, because Z]

### Variants
**Control (A)**: [Description]
**Variant (B)**: [Description]

### Sample Size
- Control: [n]
- Variant: [n]
- Total: [n]

### Results
| Metric | Control | Variant | Difference | Significant? |
|--------|---------|---------|------------|--------------|
| [Primary metric] | | | | |
| [Secondary metric] | | | | |

### Winner
[A / B / Inconclusive]

### Learning
[What did we learn? How will this change what we do?]

### Next Steps
[What will we test next based on this?]
```

---

## Active Tests

### Test #001: [Name]

**Status**: 🟡 Running

[Use template above]

---

## Completed Tests

### Test #001: LinkedIn Subject Line - Question vs Statement

**Date**: [Date] - [Date]
**Channel**: LinkedIn InMail / Connection Messages
**Type**: Opening line

#### Hypothesis
Questions get more responses than statements because they prompt engagement.

#### Variants
**Control (A)**: "I help [industry] companies automate their operations..."
**Variant (B)**: "Quick question - how much time does your team spend on [task]?"

#### Sample Size
- Control: 50
- Variant: 50
- Total: 100

#### Results
| Metric | Control | Variant | Difference | Significant? |
|--------|---------|---------|------------|--------------|
| Response rate | X% | Y% | +Z% | Yes/No |
| Positive responses | X% | Y% | +Z% | Yes/No |

#### Winner
[A / B / Inconclusive]

#### Learning
[What we learned]

#### Next Steps
[What we'll do next]

---

### Test #002: Email Subject Line - Personalization

**Date**: [Date] - [Date]
**Channel**: Cold Email
**Type**: Subject line

#### Hypothesis
Including the company name in subject lines increases open rates because it feels less like mass email.

#### Variants
**Control (A)**: "Quick question about customer feedback"
**Variant (B)**: "Quick question about [Company]'s customer feedback"

#### Sample Size
- Control: 100
- Variant: 100
- Total: 200

#### Results
| Metric | Control | Variant | Difference | Significant? |
|--------|---------|---------|------------|--------------|
| Open rate | X% | Y% | +Z% | Yes/No |
| Reply rate | X% | Y% | +Z% | Yes/No |

#### Winner
[A / B / Inconclusive]

#### Learning
[What we learned]

---

### Test #003: CTA Button Text

**Date**: [Date] - [Date]
**Channel**: Landing Page
**Type**: CTA

#### Hypothesis
Action-oriented CTAs ("Get My Audit") outperform generic CTAs ("Download") because they're more specific and personal.

#### Variants
**Control (A)**: "Download Now"
**Variant (B)**: "Get My Free Audit"

#### Sample Size
- Control: 200 visitors
- Variant: 200 visitors

#### Results
| Metric | Control | Variant | Difference | Significant? |
|--------|---------|---------|------------|--------------|
| Click rate | X% | Y% | +Z% | Yes/No |
| Conversion rate | X% | Y% | +Z% | Yes/No |

#### Winner
[A / B / Inconclusive]

#### Learning
[What we learned]

---

## Test Ideas Backlog

| Priority | Test Idea | Channel | Hypothesis |
|----------|-----------|---------|------------|
| High | LinkedIn post timing (morning vs afternoon) | LinkedIn | Morning posts get more engagement |
| High | Email length (short vs detailed) | Email | Shorter emails get more replies |
| Medium | With emoji vs without emoji in subject | Email | Emojis increase open rates |
| Medium | Social proof in CTA area | Landing Page | Testimonials near CTA increase conversion |
| Low | Video thumbnail style | YouTube | Faces get more clicks than text |
| Low | Post format (carousel vs single image) | LinkedIn | Carousels get more engagement |

---

## Learnings Summary

### What We Know Works
1. [Learning from tests]
2. [Learning from tests]
3. [Learning from tests]

### What We Know Doesn't Work
1. [Learning from tests]
2. [Learning from tests]

### Inconclusive (Need More Data)
1. [Topic needing more testing]
2. [Topic needing more testing]

---

## Testing Best Practices

### Before Testing
- [ ] Clear hypothesis documented
- [ ] Single variable being tested
- [ ] Success metric defined
- [ ] Sample size calculated
- [ ] Test duration planned

### During Testing
- [ ] Don't peek too early
- [ ] Don't change mid-test
- [ ] Track both variants equally
- [ ] Document any anomalies

### After Testing
- [ ] Analyze with statistical significance
- [ ] Document learnings (win or lose)
- [ ] Implement winner
- [ ] Plan follow-up test
- [ ] Share with team

### Statistical Significance
For most marketing tests:
- Need 100+ data points per variant minimum
- Look for 95% confidence (p < 0.05)
- Tools: [AB Test Calculator](https://www.abtestcalculator.com/)

---

## Test Calendar

| Week | Test Running | Status |
|------|--------------|--------|
| [Date] | | |
| [Date] | | |
| [Date] | | |
| [Date] | | |
