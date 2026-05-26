# Lead Capture Sections

## The Problem

**Current site**: Only has "Get in Touch" contact form  
**Issue**: You're losing 95%+ of interested visitors who aren't ready to contact you yet

**Solution**: Multiple lead capture points with varying levels of commitment

---

## Lead Capture Strategy

### The Funnel:
```
100 visitors
  ↓
  10 would consider your services (10%)
  ↓
  1 is ready to contact you now (1%)
  ↓
  YOU LOSE THE OTHER 9
```

### With Lead Magnets:
```
100 visitors
  ↓
  30 download free resource (30%)
  ↓
  10 book strategy call over time (10%)
  ↓
  YOU CAPTURE 10X MORE LEADS
```

---

## Lead Magnet: AI Automation Opportunity Audit

### What It Is:
A free, customized report showing visitors:
- Which processes they should automate first
- Expected ROI and time savings
- Recommended tools and approach
- 30-60-90 day roadmap

### Why It Works:
- ✅ High perceived value
- ✅ Addresses their specific situation
- ✅ No commitment required
- ✅ Demonstrates your expertise
- ✅ Natural lead into your services

### Delivery:
**Option 1 (Automated)**: Form → Thank you page with instant PDF download  
**Option 2 (Personalized)**: Form → You email custom 1-pager within 24 hours  
**Recommended**: Start with Option 1, upgrade to Option 2 as you scale

---

## 1. Exit Intent Popup

### When It Appears:
- User moves cursor toward browser back button
- User attempts to close tab
- User scrolls to bottom of page and hesitates

### Popup Content:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WAIT! Before You Go...

Get Your Free AI Automation Opportunity Audit

Discover which processes you should automate first—
and how much time and money you could save.

[First Name]  [Email Address]

[Send Me the Free Audit]

✓ No credit card required
✓ Instant delivery
✓ Unsubscribe anytime

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Design Notes:
- **Size**: 500px wide, centered overlay
- **Background**: Semi-transparent dark overlay
- **Close button**: Top-right corner (X)
- **No annoying**: Only triggers once per visitor (use cookies)

---

## 2. Timed Popup (45-60 seconds)

### When It Appears:
After visitor has been on page for 45-60 seconds (engaged behavior)

### Popup Content:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Enjoying What You're Reading?

Get weekly AI automation insights, case studies, 
and actionable tips—delivered to your inbox.

[Your Email Address]

[Subscribe for Free]

Join 500+ professionals already subscribed.
No spam. Unsubscribe anytime.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Design Notes:
- **Appearance**: Slide in from bottom-right (less intrusive)
- **Size**: 400px wide
- **Frequency**: Once per session
- **Alternative trigger**: After 2 page views

---

## 3. Hero Section CTA (Primary)

### Already Covered in 01-hero-section.md

```html
<a href="/free-ai-audit" class="btn btn-primary btn-large">
  Get Your Free AI Audit
</a>
```

**Links to**: Dedicated landing page (see Section 7 below)

---

## 4. Mid-Page Content Upgrade

### Placement:
Between "Projects" and "Why Partner With Us" sections

### Content:

```html
<section class="lead-capture-banner">
  <div class="container">
    <div class="banner-content">
      <div class="banner-text">
        <h3>Not Ready to Talk Yet? Start Here.</h3>
        <p>
          Get our free "AI Automation Opportunity Audit" and discover 
          which processes you should automate first.
        </p>
        <ul class="checkmarks">
          <li>✓ Customized to your business</li>
          <li>✓ Expected ROI calculations</li>
          <li>✓ Tool recommendations</li>
          <li>✓ 30-60-90 day roadmap</li>
        </ul>
      </div>
      <div class="banner-form">
        <form class="inline-lead-form">
          <input type="text" placeholder="First Name" required>
          <input type="email" placeholder="Email Address" required>
          <button type="submit" class="btn btn-primary">
            Get Free Audit
          </button>
        </form>
        <p class="form-disclaimer">
          No credit card required. Instant delivery.
        </p>
      </div>
    </div>
  </div>
</section>
```

### Design:
- **Background**: Light colored box (stands out from white page)
- **Layout**: Text left, form right (stack on mobile)
- **Visibility**: Clearly separated from surrounding content

---

## 5. Footer Newsletter Signup

### Placement:
In footer, above standard footer links

### Content:

```html
<section class="footer-newsletter">
  <div class="container">
    <div class="newsletter-content">
      <h3>Get Weekly AI Automation Insights</h3>
      <p>
        Join 500+ professionals receiving practical tips, case studies, 
        and automation strategies every week.
      </p>
      <form class="newsletter-form">
        <input type="email" 
               placeholder="Your email address" 
               required>
        <button type="submit" class="btn btn-secondary">
          Subscribe
        </button>
      </form>
      <p class="small-text">
        No spam. Unsubscribe anytime. We respect your privacy.
      </p>
    </div>
  </div>
</section>
```

---

## 6. Sidebar Sticky CTA (Optional)

### Placement:
Right sidebar that follows scroll on desktop (hidden on mobile)

### Content:

```html
<div class="sticky-sidebar-cta">
  <div class="cta-box">
    <h4>Ready to Automate?</h4>
    <p>Get your free audit</p>
    <a href="/free-ai-audit" class="btn btn-primary btn-block">
      Download Now
    </a>
    <p class="small-text">Or</p>
    <a href="/contact" class="btn btn-outline btn-block">
      Book a Call
    </a>
  </div>
</div>
```

### Behavior:
- Appears after user scrolls past hero
- Stays visible until footer
- Doesn't obstruct content

---

## 7. Dedicated Lead Magnet Landing Page

### URL:
`/free-ai-audit` or `/automation-assessment`

### Complete Page Structure:

```html
<!DOCTYPE html>
<html>
<head>
  <title>Free AI Automation Opportunity Audit | AI Whisperers</title>
  <meta name="description" content="Discover which processes you should automate first. Get a free, customized AI automation opportunity report.">
</head>
<body>
  <section class="lead-page-hero">
    <div class="container-narrow">
      <h1>Discover Which Processes You Should Automate First</h1>
      <p class="lead-subtitle">
        Get a custom AI automation opportunity report—showing you exactly 
        where you're losing time and money (and how to fix it)
      </p>
      <p class="trust-bar">
        ✓ No credit card required | ✓ Instant delivery | ✓ Completely free
      </p>
    </div>
  </section>
  
  <section class="lead-page-what-you-get">
    <div class="container-narrow">
      <h2>What You'll Get:</h2>
      <ul class="benefit-list">
        <li>
          <strong>Process Efficiency Analysis</strong><br>
          Identify which processes are wasting the most time
        </li>
        <li>
          <strong>ROI Calculations</strong><br>
          Expected time and cost savings for each automation opportunity
        </li>
        <li>
          <strong>Tool Recommendations</strong><br>
          Specific tools matched to your use cases (many are free)
        </li>
        <li>
          <strong>Implementation Roadmap</strong><br>
          Prioritized 30-60-90 day plan you can start today
        </li>
        <li>
          <strong>Getting Started Guide</strong><br>
          First steps, common pitfalls, and resources
        </li>
      </ul>
    </div>
  </section>
  
  <section class="lead-page-form">
    <div class="container-narrow">
      <div class="form-box">
        <h2>Get Your Free Audit</h2>
        <p>Takes 2 minutes. Results delivered instantly.</p>
        
        <form id="lead-magnet-form">
          <!-- Personal Info -->
          <div class="form-group">
            <label>First Name *</label>
            <input type="text" name="first_name" required>
          </div>
          
          <div class="form-group">
            <label>Email Address *</label>
            <input type="email" name="email" required>
          </div>
          
          <div class="form-group">
            <label>Company Name *</label>
            <input type="text" name="company" required>
          </div>
          
          <!-- Business Context -->
          <div class="form-group">
            <label>Industry *</label>
            <select name="industry" required>
              <option value="">Select your industry...</option>
              <option value="saas">SaaS / Software</option>
              <option value="ecommerce">E-commerce</option>
              <option value="consulting">Consulting</option>
              <option value="agency">Agency / Marketing</option>
              <option value="finance">Finance / Banking</option>
              <option value="healthcare">Healthcare</option>
              <option value="manufacturing">Manufacturing</option>
              <option value="other">Other</option>
            </select>
          </div>
          
          <div class="form-group">
            <label>Company Size *</label>
            <select name="company_size" required>
              <option value="">Select size...</option>
              <option value="solo">Solo / 1 person</option>
              <option value="2-10">2-10 employees</option>
              <option value="11-50">11-50 employees</option>
              <option value="51-200">51-200 employees</option>
              <option value="200+">200+ employees</option>
            </select>
          </div>
          
          <!-- Pain Points -->
          <div class="form-group">
            <label>What's your biggest operational challenge? *</label>
            <textarea name="challenge" rows="3" required></textarea>
          </div>
          
          <div class="form-group">
            <label>Hours per week spent on repetitive tasks *</label>
            <select name="hours_wasted" required>
              <option value="">Select range...</option>
              <option value="0-5">Less than 5 hours</option>
              <option value="5-10">5-10 hours</option>
              <option value="10-20">10-20 hours</option>
              <option value="20+">20+ hours (send help!)</option>
            </select>
          </div>
          
          <!-- Submit -->
          <div class="form-group">
            <button type="submit" class="btn btn-primary btn-large btn-block">
              Get My Free Audit Report →
            </button>
          </div>
          
          <p class="form-disclaimer">
            We respect your privacy. Your information will never be shared. 
            Unsubscribe anytime.
          </p>
        </form>
      </div>
    </div>
  </section>
  
  <section class="lead-page-faq">
    <div class="container-narrow">
      <h2>Frequently Asked Questions</h2>
      
      <div class="faq-item">
        <h3>Is this really free?</h3>
        <p>Yes! No credit card required, no catch. We provide value first to earn your trust.</p>
      </div>
      
      <div class="faq-item">
        <h3>How long does it take?</h3>
        <p>The assessment takes 2 minutes. You'll receive your custom report via email within 24 hours.</p>
      </div>
      
      <div class="faq-item">
        <h3>What happens after I get the audit?</h3>
        <p>That's up to you! Implement the recommendations yourself, or if you want help, we offer implementation services. No pressure either way.</p>
      </div>
      
      <div class="faq-item">
        <h3>Will I be spammed with sales calls?</h3>
        <p>No. We'll send your report and one follow-up email asking if you have questions. That's it.</p>
      </div>
    </div>
  </section>
</body>
</html>
```

---

## 8. Thank You Page

### URL:
`/free-ai-audit/thank-you`

### Content:

```html
<section class="thank-you-page">
  <div class="container-narrow text-center">
    <div class="success-icon">✓</div>
    <h1>Check Your Email!</h1>
    <p class="lead">
      Your AI Automation Opportunity Audit is on its way.
    </p>
    <p>
      We've sent it to <strong>[email@address.com]</strong><br>
      (Check your spam folder if you don't see it in 5 minutes)
    </p>
    
    <hr>
    
    <h2>While You Wait...</h2>
    
    <div class="next-steps">
      <div class="next-step-card">
        <h3>📊 Explore Our GitHub</h3>
        <p>See real automation projects and open-source tools</p>
        <a href="https://github.com/orgs/Ai-Whisperers/repositories" 
           class="btn btn-outline">
          View on GitHub →
        </a>
      </div>
      
      <div class="next-step-card">
        <h3>📚 Read Case Studies</h3>
        <p>See how we've helped companies like yours</p>
        <a href="/clients" class="btn btn-outline">
          View Case Studies →
        </a>
      </div>
      
      <div class="next-step-card">
        <h3>📞 Book a Strategy Call</h3>
        <p>Want to discuss your situation? Let's talk.</p>
        <a href="/contact" class="btn btn-primary">
          Schedule Call →
        </a>
      </div>
    </div>
    
    <hr>
    
    <h3>Follow Us for More Insights</h3>
    <div class="social-links">
      <a href="[LinkedIn URL]">LinkedIn</a>
      <a href="[Twitter URL]">Twitter</a>
      <a href="[GitHub URL]">GitHub</a>
    </div>
  </div>
</section>
```

---

## Email Tool Setup

### Recommended Tools:

**Option 1: HubSpot (Free)**
- ✅ Free CRM + Email
- ✅ Form builder included
- ✅ Simple automation
- ✅ Good for startups
- 👉 **Best for**: Getting started quickly

**Option 2: Mailchimp (Free up to 500)**
- ✅ Easy to use
- ✅ Good templates
- ✅ Basic automation
- ⚠️ Limited on free tier
- 👉 **Best for**: Simple newsletter

**Option 3: ConvertKit**
- ✅ Built for creators
- ✅ Great automation
- ✅ Tag-based segmentation
- 💰 $29/mo (1,000 subscribers)
- 👉 **Best for**: Content-focused

### Setup Steps (HubSpot):

1. **Create Account**: hubspot.com/products/get-started
2. **Create Form**:
   - Marketing → Forms → Create Form
   - Add fields from landing page spec above
   - Customize thank you page redirect

3. **Create Email Template**:
   ```
   Subject: Here's Your AI Automation Opportunity Audit

   Hi [First Name],

   Thanks for requesting your AI Automation Opportunity Audit!

   Based on your responses, here are your top automation opportunities:

   [Customize based on their answers, or send general PDF]

   Attached is your full report with:
   • Process efficiency analysis
   • ROI calculations  
   • Tool recommendations
   • 30-60-90 day roadmap

   Questions? Just reply to this email.

   Best,
   [Your Name]
   AI Whisperers

   P.S. Want help implementing these? Book a free strategy call: [link]
   ```

4. **Set Up Automation**:
   - Trigger: Form submission
   - Action: Send email with PDF attachment
   - Delay: Immediate

5. **Add to Website**:
   - Copy embed code
   - Paste into landing page or use popup tool

---

## Popup Tool Setup

### Recommended: OptinMonster or Sumo

**OptinMonster** ($9/mo):
- Exit intent
- Timed popups
- A/B testing
- Advanced targeting

**Sumo** (Free):
- Basic popups
- Email capture
- Social sharing
- Limited on free tier

**Custom React Component** (If building yourself):
```javascript
// Simple exit intent detection
useEffect(() => {
  const handleMouseLeave = (e) => {
    if (e.clientY <= 0) {
      // User moving to close tab
      showPopup();
    }
  };
  
  document.addEventListener('mouseleave', handleMouseLeave);
  return () => document.removeEventListener('mouseleave', handleMouseLeave);
}, []);
```

---

## Implementation Checklist

### Week 1: Core Setup
- [ ] Choose email tool (HubSpot recommended)
- [ ] Create lead magnet PDF or template
- [ ] Build `/free-ai-audit` landing page
- [ ] Set up form and automation
- [ ] Create thank you page
- [ ] Test entire flow

### Week 2: Optimization
- [ ] Add exit intent popup
- [ ] Add timed popup (45-60 sec)
- [ ] Add mid-page content upgrade
- [ ] Add footer newsletter signup
- [ ] Set up analytics tracking

### Week 3: Testing
- [ ] Test on all devices
- [ ] Test email delivery
- [ ] Check spam scores
- [ ] A/B test popup copy
- [ ] Monitor conversion rates

---

## Expected Results

### Conservative (Month 1):
- 1,000 visitors → 50-100 email captures (5-10%)
- 50 leads → 10 strategy calls (20%)
- 10 calls → 2-3 clients (20-30%)

### Optimized (Month 3):
- 2,000 visitors → 200-300 email captures (10-15%)
- 200 leads → 30-40 strategy calls (15-20%)
- 30 calls → 6-10 clients (20-30%)

---

## Next Steps

1. ✅ **Choose email tool** and create account
2. ✅ **Create lead magnet** (use template from parent folder)
3. ✅ **Build landing page** using structure above
4. ✅ **Set up automation** in email tool
5. ✅ **Add popups** to homepage
6. ✅ **Test everything** before launch
7. ✅ **Monitor and optimize** weekly

---

**Lead capture is THE most important addition to your site. This alone could 10x your pipeline. Implement this first! 🚀**

