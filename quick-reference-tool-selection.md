# Quick Reference: AI & Automation Tool Selection
## One-Page Guide for Client Recommendations

---

## AUTOMATION PLATFORM SELECTOR

### Choose Zapier If:
- Non-technical users need to build automation
- You want the easiest learning curve
- You have 8,000+ app integration needs
- Budget < $100/month (start small)
- You don't have DevOps staff

**Sweet Spot:** SMBs, teams < 10 people, non-technical workflows

---

### Choose Make If:
- You want better pricing than Zapier
- You need advanced automation features
- You have 50-200+ workflows planned
- Budget $100-1,000/month
- You want cost transparency (operations model)

**Sweet Spot:** Growing teams, marketing automation, data integration

---

### Choose n8n Cloud If:
- You want balance of ease and features
- You need moderate volume (< 50k executions/month)
- You want to avoid infrastructure management
- Budget $500-2,000/month
- You might migrate to self-hosted later

**Sweet Spot:** Mid-market companies, technical teams, future scaling

---

### Choose n8n Self-Hosted If:
- You have DevOps/technical capacity
- Volume > 2M operations/month (cost wins)
- Data privacy is critical (HIPAA, GDPR)
- You want complete infrastructure control
- Budget $3,000-5,000+/month for ops

**Sweet Spot:** Enterprises, healthcare, finance, high-volume automation

---

### Choose Power Automate If:
- Your company uses Microsoft M365
- You need RPA (desktop automation)
- You want tight Microsoft ecosystem integration
- You have 50+ Office 365 licenses
- You need enterprise SSO and audit logs

**Sweet Spot:** Microsoft-centric enterprises, RPA-heavy workloads

---

## LLM MODEL SELECTOR

### Cost-Sensitive (MVPs, Testing)
```
FIRST CHOICE: Gemini Flash-Lite
- Price: $0.0375/$0.15 per 1M tokens
- Context: 1M tokens (!)
- Speed: Fast
- Use for: POCs, MVP testing, cost validation
```

### Best Value (Production-Ready)
```
FIRST CHOICE: Claude Haiku 4.5 OR Gemini Flash
- Price: $1-5 per 1M tokens (Haiku) or $0.075-0.30 (Flash)
- Quality: 85-90% of premium models
- Speed: Fast to medium
- Use for: Customer chatbots, content generation
```

### Best Long-Context (Documents, Analysis)
```
FIRST CHOICE: Claude Sonnet 4.5
- Context: 1M tokens (150-200 pages)
- Price: $3/$15 per 1M tokens
- Quality: Excellent reasoning
- Use for: Document analysis, RAG, research
```

### Best All-Around (Production, Balanced)
```
FIRST CHOICE: GPT-4o
- Price: $2.50/$10 per 1M tokens
- Context: 128K tokens
- Quality: Excellent across all tasks
- Use for: Mission-critical applications
```

### Best Reasoning (Complex Problems)
```
FIRST CHOICE: Claude Opus 4.5
- Price: $5/$25 per 1M tokens
- Quality: Best reasoning, extended thinking
- Context: 200K tokens
- Use for: Complex analysis, research, problem-solving
```

### Best for Privacy (Regulated Data)
```
FIRST CHOICE: Claude (via API) OR Self-Hosted Llama/Mistral
- Claude: Privacy-first approach, no training on API data
- Self-Hosted: Complete data control
- Use for: Healthcare (HIPAA), Finance (PCI), Legal
```

### Best for Offline/Edge Deployment
```
FIRST CHOICE: Mistral 7B OR Llama 3.3 70B
- Price: $0 (self-hosted) + infrastructure
- Quality: Good to excellent
- Size: Fits on consumer GPUs
- Use for: On-premise deployment, offline
```

---

## DECISION MATRIX (Quick Version)

### By Monthly AI Budget

| Budget | LLM Choice | Framework | Automation |
|--------|-----------|-----------|-----------|
| < $50 | Flash-Lite | None (simple) | Zapier Free |
| $50-500 | Haiku 4.5 | CrewAI | Zapier Pro |
| $500-2,000 | Sonnet 4.5 | CrewAI/LangChain | Make Pro |
| $2,000-5,000 | Opus 4.5 | LangChain | n8n Cloud |
| $5,000+ | Opus 4.5 + GPT-4o | LangChain | n8n Self |

---

### By Use Case

| Use Case | Platform | Model | Cost |
|----------|----------|-------|------|
| Customer chatbot | Zapier + CrewAI | Haiku 4.5 | $500-1,500/mo |
| Content generation | Make | Flash-Lite/Haiku | $200-800/mo |
| Document processing | n8n | Sonnet 4.5 | $100-500/mo |
| Complex research | LangChain | Opus 4.5 | $1,000-3,000/mo |
| Healthcare automation | n8n Self | Claude + Llama | $3,000-5,000/mo |
| Marketing automation | Zapier/Make | Haiku 4.5 | $300-1,200/mo |
| Data analysis at scale | n8n | Sonnet 4.5 | $500-2,000/mo |
| AI pair programming | LangChain | GPT-4o | $800-1,500/mo |

---

## AGENT FRAMEWORK QUICK GUIDE

### Choose CrewAI If:
- Team is new to agents
- Need to launch in weeks, not months
- Don't need 600+ integrations
- Budget is tight
- **Cost:** Free, LLM-only
- **Learning time:** 1-2 weeks

### Choose LangChain If:
- Building production systems
- Need 600+ integrations
- Have experienced dev team
- Long-term maintainability matters
- **Cost:** Free, LLM-only
- **Learning time:** 3-4 weeks

### Choose AutoGen If:
- Building multi-agent conversations
- Need peer review/debate patterns
- Have coding expertise
- Complex problem decomposition
- **Cost:** Free, LLM-only
- **Learning time:** 2-3 weeks

### Build Custom If:
- Unique competitive advantage
- Willing to invest $50K+
- Have AI engineering team
- Need proprietary behavior
- **Cost:** $50K-200K+, ongoing
- **Time:** 3-6 months

---

## PRICING QUICK REFERENCE

### Annual Costs (Typical Setup)

| Setup | Automation | LLM | Framework | Total/Year |
|------|-----------|-----|-----------|------------|
| Startup MVP | $200 | $500 | Free | $700 |
| Growing SMB | $1,200 | $3,000 | Free | $4,200 |
| Mid-Market | $6,000 | $12,000 | Free | $18,000 |
| Enterprise | $30,000 | $50,000 | Free | $80,000 |

---

## RED FLAGS & GOTCHAS

### Automation Platforms
- [ ] Zapier: Watch overage costs (1.25x multiplier)
- [ ] Make: Auto-purchase can surprise bill (30% markup)
- [ ] n8n Self: Infrastructure often 2-3x initial estimate
- [ ] Power Automate: Premium connectors add cost
- [ ] All: Monitor task/operation growth monthly

### LLM Platforms
- [ ] Token counting: Prompts + context + function defs cost money
- [ ] Rate limits: Spikes can exceed quota instantly
- [ ] Vision tasks: More expensive per token
- [ ] Batch vs. real-time: Different pricing tiers
- [ ] Context length: Bigger windows = higher cost

### Agent Systems
- [ ] LLM costs scale 3-5x with agents (multiple API calls)
- [ ] Tool use adds latency and cost
- [ ] Conversation memory grows unbounded (cache it!)
- [ ] Multi-agent debugging expensive (test carefully)

---

## MIGRATION PATH (Typical)

```
MONTH 1-2: MVP
├─ Automation: Zapier Free + Make Free
├─ LLM: Gemini Flash-Lite ($50-200)
├─ Framework: CrewAI
└─ Total: $100-500/month

MONTH 3-6: VALIDATION
├─ Automation: Zapier Pro ($50-100)
├─ LLM: Claude Haiku 4.5 ($300-800)
├─ Framework: CrewAI → LangChain (if needed)
└─ Total: $500-2,000/month

MONTH 7-12: GROWTH
├─ Automation: Make Pro ($500-1,000)
├─ LLM: Claude Sonnet 4.5 ($1,000-3,000)
├─ Framework: LangChain production
└─ Total: $2,000-5,000/month

MONTH 12+: SCALE
├─ Automation: n8n Self ($3,000+) OR Power Automate
├─ LLM: Multi-model (Sonnet 4.5 + GPT-4o)
├─ Framework: Custom or LangChain enterprise
└─ Total: $5,000-15,000+/month
```

---

## CONVERSATION STARTERS FOR CLIENTS

### "What's your timeline?"
- < 2 weeks: Zapier/Make + Gemini Flash
- 1 month: n8n Cloud + Claude Haiku
- 3+ months: LangChain + custom architecture

### "What's your budget?"
- < $100/month: Zapier Free + Flash-Lite
- $100-1,000: Make + Haiku 4.5
- $1,000-5,000: n8n + Sonnet 4.5
- $5,000+: n8n Self + Opus 4.5

### "Do you have technical staff?"
- No: Zapier, never n8n Self
- Yes, small team: Make or n8n Cloud
- Yes, large team: n8n Self + custom agents

### "How much data?"
- < 1GB: Any SaaS platform
- 1-100GB: Zapier/Make + cloud LLM
- > 100GB: n8n Self + consider self-hosted LLM

### "Data privacy critical?"
- Yes: Claude API + n8n Self + open-source LLM
- No: Any platform acceptable

---

## SAMPLE CLIENT PROPOSALS (Cost Estimates)

### Proposal A: Content Marketing Automation
```
Customer Service Chatbot + Content Generation

Tools:
- Automation: Zapier Professional ($30/month)
- LLM: Claude Haiku 4.5 ($500/month estimated)
- Framework: CrewAI (free)

Monthly: $530
Annual: $6,360
ROI: Reduces customer service 40%
```

### Proposal B: Enterprise Data Integration
```
50+ Workflow Automation + Document Analysis

Tools:
- Automation: Make Team Plan ($1,000/month)
- LLM: Claude Sonnet 4.5 ($2,000/month)
- Framework: LangChain (free)

Monthly: $3,000
Annual: $36,000
ROI: Reduces manual work 60%, improves accuracy
```

### Proposal C: Healthcare Compliance System
```
HIPAA-Compliant Automation + Private LLM

Tools:
- Automation: n8n Self-Hosted ($4,000/month ops)
- LLM: Claude API (on-premise) ($1,500/month)
- Framework: LangChain (free)

Monthly: $5,500
Annual: $66,000
ROI: Maintains compliance, reduces breach risk
```

---

## COMPARISON TABLE (One-Liner)

| Tool | Cost | Ease | Power | Best For |
|------|------|------|-------|----------|
| **Zapier** | Medium | ★★★★★ | ★★★ | SMBs |
| **Make** | Low | ★★★★ | ★★★★ | Growing teams |
| **n8n Cloud** | Medium | ★★★ | ★★★★ | Technical teams |
| **n8n Self** | High* | ★★ | ★★★★★ | Enterprises |
| **Power Automate** | Medium | ★★★ | ★★★★ | Microsoft orgs |
| **GPT-4o** | Medium | - | ★★★★★ | All uses |
| **Claude Sonnet** | Low | - | ★★★★ | Long documents |
| **Gemini Flash** | Very Low | - | ★★★ | MVPs |
| **LangChain** | Free | ★★★ | ★★★★★ | Complex agents |
| **CrewAI** | Free | ★★★★ | ★★★★ | New to agents |

*High due to infrastructure, not licensing

---

## QUESTIONS TO ASK CLIENTS

1. **Timeline:** When do you need this live? (affects tech choice)
2. **Volume:** How many transactions/requests per month? (affects cost model)
3. **Integrations:** What apps must connect? (affects platform choice)
4. **Privacy:** Any compliance requirements? (HIPAA, GDPR, PCI) (affects hosting)
5. **Team:** Do you have developers on staff? (affects self-hosting vs SaaS)
6. **Budget:** Total monthly/annual spend? (affects all choices)
7. **Growth:** Expected growth trajectory? (affects migration path)
8. **Maintenance:** Who maintains this after launch? (affects support needs)
9. **Accuracy:** How important is output accuracy? (affects model choice)
10. **Languages:** Multi-language support needed? (affects model choice)

---

## KEY METRICS TO TRACK

### For Automation Platforms
- Tasks/operations per month (watch for overgrowth)
- Error rates (indicates workflow quality)
- Cost per workflow (monitor for efficiency)
- Execution time (affects customer experience)

### For LLM Platforms
- Tokens used per month (monitor costs)
- Latency (p50, p95, p99)
- Cost per request (optimize with batching)
- Error/timeout rates (quality indicator)

### For Agent Systems
- Cost per agent interaction (LLM calls)
- Success rate (first-call resolution)
- Conversation length (watch memory growth)
- Tool call accuracy (integration health)

---

## FINAL DECISION TREE (60-Second Version)

```
1. Budget > $5K/month?
   YES → n8n Self OR Power Automate Enterprise
   NO → Skip to question 2

2. Data privacy critical?
   YES → Claude + n8n Self + open-source LLM
   NO → Skip to question 3

3. Lots of integrations (1000+)?
   YES → Zapier or LangChain
   NO → Skip to question 4

4. Need long documents (100+ pages)?
   YES → Claude Sonnet 4.5 + Batch API
   NO → Skip to question 5

5. Have DevOps team?
   YES → n8n Self if volume > 2M/month
   NO → Use SaaS (Zapier, Make, or n8n Cloud)

6. Building agents?
   YES → CrewAI (easy) or LangChain (production)
   NO → Simple automation sufficient

RESULT: You now have your recommendation
```

---

## WHEN TO SAY "NO" (Red Flags for Clients)

- ❌ "We need this live in 2 days" (unrealistic unless simple)
- ❌ "We have zero budget" (you can't do it well)
- ❌ "We want enterprise features for $10/month" (math doesn't work)
- ❌ "We need 99.9% uptime but won't pay for it" (impossible)
- ❌ "Build us an AI agent, figure it out" (scope creep hazard)
- ❌ "We'll migrate to our own server later" (rarely happens, costs double)

---

## TEMPLATES FOR PROPOSALS

### Template 1: Simple Automation + ChatBot

**Project:** [Name] Customer Experience Automation

**Solution:**
- Tool: Zapier + CrewAI + Claude Haiku 4.5
- Scope: Customer inquiry routing + chatbot
- Timeline: 2-3 weeks
- Cost: $30/mo automation + $500/mo LLM = $530/month

**Expected ROI:**
- Reduce support response time: 24h → 2 minutes
- Reduce support headcount: 2 FTE → 1 FTE ($60K saving)
- Payback period: 1 month

---

### Template 2: Enterprise Integration

**Project:** [Name] Workflow Automation Platform

**Solution:**
- Tool: Make Team Plan + LangChain + Claude Sonnet 4.5
- Scope: 25 core workflows + data pipeline + analysis
- Timeline: 6-8 weeks
- Cost: $1,000/mo + $2,000/mo + support = $3,500/month

**Expected ROI:**
- Eliminate manual data entry: 40 hours/week saved
- Improve accuracy: 95% → 99.5% (error reduction)
- Payback period: 3 months

---

**Last Updated:** December 2025
**For Internal Use By:** AI Consultants, Solution Architects
