# Team Section

## Purpose

Put faces to the name, build trust, showcase expertise.

**Key message**: We're real people with real skills, not a faceless agency.

---

## Section Placement

**Option 1**: On `/about` page (recommended)  
**Option 2**: Dedicated `/team` page  
**Option 3**: Brief section on homepage

---

## Team Section Structure

### SECTION HEADLINE
```
Meet the Team
```

**Alternatives**:
- "The People Behind the Code"
- "Meet Your AI Automation Partners"
- "Who We Are"

---

### SECTION SUBHEADLINE
```
A team of engineers, automation specialists, and problem-solvers 
committed to delivering results.
```

---

## Team Member Profile Template

### Profile Structure for Each Team Member:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[PHOTO - Professional headshot, 400x400px]

[NAME]
[Role/Title]

[BIO - 2-3 sentences]
[Background/expertise/what they bring to the team]

Specializes in:
• [Expertise area 1]
• [Expertise area 2]
• [Expertise area 3]

[LinkedIn Icon] [GitHub Icon] [Twitter Icon]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Example Team Member Profiles

### FOUNDER/CEO Profile Example

```html
<div class="team-member">
  <div class="member-photo">
    <img src="/team/founder.jpg" alt="[Founder Name]">
  </div>
  <div class="member-info">
    <h3>[Founder Name]</h3>
    <p class="member-role">Founder & CEO</p>
    
    <p class="member-bio">
      [Founder Name] started AI Whisperers after years of helping businesses 
      struggle with inefficient processes. With a background in software 
      engineering and enterprise automation, [he/she] leads the team in 
      delivering practical AI solutions that actually work.
    </p>
    
    <div class="member-specialties">
      <h4>Specializes in:</h4>
      <ul>
        <li>Enterprise AI architecture</li>
        <li>Process optimization</li>
        <li>Strategic automation planning</li>
      </ul>
    </div>
    
    <div class="member-contributions">
      <p><strong>GitHub Contributions:</strong> 500+ commits across 7 repos</p>
      <p><strong>Projects Led:</strong> 30+ successful implementations</p>
    </div>
    
    <div class="member-social">
      <a href="[LinkedIn URL]" target="_blank">
        <img src="/icons/linkedin.svg" alt="LinkedIn">
      </a>
      <a href="https://github.com/[username]" target="_blank">
        <img src="/icons/github.svg" alt="GitHub">
      </a>
      <a href="[Twitter URL]" target="_blank">
        <img src="/icons/twitter.svg" alt="Twitter">
      </a>
    </div>
  </div>
</div>
```

---

### TECHNICAL LEAD Profile Example

```html
<div class="team-member">
  <div class="member-photo">
    <img src="/team/tech-lead.jpg" alt="[Tech Lead Name]">
  </div>
  <div class="member-info">
    <h3>[Tech Lead Name]</h3>
    <p class="member-role">Lead Automation Engineer</p>
    
    <p class="member-bio">
      [Name] brings 8+ years of experience building scalable automation systems. 
      Passionate about clean code and practical solutions, [he/she] leads our 
      implementation team and contributes heavily to our open-source projects.
    </p>
    
    <div class="member-specialties">
      <h4>Specializes in:</h4>
      <ul>
        <li>Python & TypeScript automation</li>
        <li>API integrations</li>
        <li>AI agent development</li>
      </ul>
    </div>
    
    <div class="member-tech">
      <p><strong>Tech Stack:</strong> Python, TypeScript, Node.js, React, PostgreSQL</p>
      <p><strong>Open Source:</strong> Contributor to agentic-schemas, yt-transcript-headless</p>
    </div>
    
    <div class="member-social">
      <a href="[LinkedIn URL]" target="_blank">
        <img src="/icons/linkedin.svg" alt="LinkedIn">
      </a>
      <a href="https://github.com/[username]" target="_blank">
        <img src="/icons/github.svg" alt="GitHub">
      </a>
    </div>
  </div>
</div>
```

---

### CLIENT SUCCESS MANAGER Profile Example

```html
<div class="team-member">
  <div class="member-photo">
    <img src="/team/csm.jpg" alt="[CSM Name]">
  </div>
  <div class="member-info">
    <h3>[CSM Name]</h3>
    <p class="member-role">Client Success Manager</p>
    
    <p class="member-bio">
      [Name] ensures every client sees real results. With a background in 
      operations and project management, [he/she] guides implementations 
      from kickoff to optimization, making sure everything runs smoothly.
    </p>
    
    <div class="member-specialties">
      <h4>Specializes in:</h4>
      <ul>
        <li>Project management</li>
        <li>Client training and onboarding</li>
        <li>Process documentation</li>
      </ul>
    </div>
    
    <div class="member-impact">
      <p><strong>Client NPS:</strong> 9.2/10</p>
      <p><strong>Projects Managed:</strong> 25+ successful deliveries</p>
    </div>
    
    <div class="member-social">
      <a href="[LinkedIn URL]" target="_blank">
        <img src="/icons/linkedin.svg" alt="LinkedIn">
      </a>
    </div>
  </div>
</div>
```

---

## Team Section - Complete HTML

```html
<section class="team-section">
  <div class="container">
    <!-- Section Header -->
    <div class="section-header text-center">
      <h2>Meet the Team</h2>
      <p class="section-subheadline">
        A team of engineers, automation specialists, and problem-solvers 
        committed to delivering results.
      </p>
    </div>
    
    <!-- Team Grid -->
    <div class="team-grid">
      <!-- Team Member 1 -->
      <div class="team-member-card">
        <div class="member-photo-wrapper">
          <img src="/images/team/member1.jpg" 
               alt="Team Member Name" 
               class="member-photo">
          <div class="member-github-link">
            <a href="https://github.com/[username]" target="_blank">
              View GitHub →
            </a>
          </div>
        </div>
        <div class="member-content">
          <h3 class="member-name">[Name]</h3>
          <p class="member-role">Founder & CEO</p>
          <p class="member-bio">
            [2-3 sentence bio about background, expertise, and passion]
          </p>
          <div class="member-specialties">
            <strong>Specializes in:</strong>
            <span class="specialty-tag">Enterprise AI</span>
            <span class="specialty-tag">Process Optimization</span>
            <span class="specialty-tag">Strategy</span>
          </div>
          <div class="member-stats">
            <div class="stat">
              <strong>30+</strong>
              <span>Projects Led</span>
            </div>
            <div class="stat">
              <strong>500+</strong>
              <span>GitHub Commits</span>
            </div>
          </div>
          <div class="member-social-links">
            <a href="[LinkedIn]" target="_blank" aria-label="LinkedIn">
              <i class="icon-linkedin"></i>
            </a>
            <a href="[GitHub]" target="_blank" aria-label="GitHub">
              <i class="icon-github"></i>
            </a>
            <a href="[Twitter]" target="_blank" aria-label="Twitter">
              <i class="icon-twitter"></i>
            </a>
          </div>
        </div>
      </div>
      
      <!-- Repeat for additional team members -->
      
    </div>
    
    <!-- Team Values/Culture -->
    <div class="team-culture">
      <h3>How We Work Together</h3>
      <div class="culture-points">
        <div class="culture-point">
          <h4>🤝 Collaborative</h4>
          <p>We believe the best solutions come from diverse perspectives and open communication.</p>
        </div>
        <div class="culture-point">
          <h4>🎓 Always Learning</h4>
          <p>AI moves fast. We dedicate time each week to learning new tools and techniques.</p>
        </div>
        <div class="culture-point">
          <h4>🔓 Transparent</h4>
          <p>We share what we learn—through open source, blogs, and community contributions.</p>
        </div>
        <div class="culture-point">
          <h4>🎯 Results-Focused</h4>
          <p>We care about outcomes, not just outputs. Client success is our success.</p>
        </div>
      </div>
    </div>
    
    <!-- Join Team CTA (optional) -->
    <div class="join-team-cta text-center">
      <h3>Want to Join Our Team?</h3>
      <p>We're always looking for talented automation engineers and problem-solvers.</p>
      <a href="/careers" class="btn btn-outline">
        View Open Positions
      </a>
    </div>
  </div>
</section>
```

---

## Alternative: Compact Team Section (Homepage)

For homepage, use a more compact version:

```html
<section class="team-preview">
  <div class="container">
    <h2>Built by Practitioners, Not Just Consultants</h2>
    <p>Our team of engineers and automation specialists ship real code, not just advice.</p>
    
    <div class="team-photos-row">
      <div class="team-photo">
        <img src="/team/member1.jpg" alt="Team Member 1">
        <p class="name">[Name]</p>
        <p class="role">Founder</p>
      </div>
      <div class="team-photo">
        <img src="/team/member2.jpg" alt="Team Member 2">
        <p class="name">[Name]</p>
        <p class="role">Lead Engineer</p>
      </div>
      <div class="team-photo">
        <img src="/team/member3.jpg" alt="Team Member 3">
        <p class="name">[Name]</p>
        <p class="role">Client Success</p>
      </div>
      <!-- Add more as needed -->
    </div>
    
    <div class="team-stats">
      <div class="stat">
        <strong>8+ years</strong>
        <span>Combined experience</span>
      </div>
      <div class="stat">
        <strong>50+ projects</strong>
        <span>Successfully delivered</span>
      </div>
      <div class="stat">
        <strong>100%</strong>
        <span>Client satisfaction</span>
      </div>
    </div>
    
    <a href="/about" class="btn btn-outline">Meet the Full Team →</a>
  </div>
</section>
```

---

## Team Member Information to Collect

For each team member, gather:

### Essential:
- [ ] Full name
- [ ] Role/title
- [ ] Professional headshot (400x400px minimum)
- [ ] 2-3 sentence bio
- [ ] 3-5 areas of expertise
- [ ] LinkedIn profile URL

### Nice to Have:
- [ ] GitHub username
- [ ] Twitter/X handle
- [ ] Notable projects or contributions
- [ ] GitHub commit count
- [ ] Years of experience
- [ ] Certifications or education
- [ ] Personal interests (optional)
- [ ] Fun fact (optional)

---

## Photography Guidelines

### Professional Headshots:
- **Size**: 400x400px minimum (square format)
- **Background**: Clean, consistent across team
- **Lighting**: Professional, well-lit
- **Expression**: Friendly, approachable
- **Attire**: Professional but not overly formal
- **Consistency**: Similar style for all team members

### DIY Photo Tips:
- Use natural light (near window)
- Plain background (wall or backdrop)
- Eye-level camera angle
- Smile naturally
- Use portrait mode if available

---

## Design Specifications

### Layout Options:

**Option 1: Grid Layout**
- 3 columns on desktop
- 2 columns on tablet
- 1 column on mobile
- Equal height cards

**Option 2: Staggered Layout**
- Alternating photo left/right
- More visual interest
- Better for long bios

**Option 3: Carousel**
- Swipeable on mobile
- Featured team member highlighted
- Good for many team members

### Card Design:
- **Photo**: Top or left side
- **Name**: Large, bold
- **Role**: Smaller, gray
- **Bio**: Readable size (16-18px)
- **Specialties**: Tagged chips/pills
- **Social icons**: Bottom of card
- **Hover effect**: Subtle lift or glow

---

## Team Stats Section

Add credibility with aggregate stats:

```html
<div class="team-stats-section">
  <h3>Our Team by the Numbers</h3>
  <div class="stats-grid">
    <div class="stat">
      <div class="stat-number">15+</div>
      <div class="stat-label">Years Combined Experience</div>
    </div>
    <div class="stat">
      <div class="stat-number">1,000+</div>
      <div class="stat-label">GitHub Contributions</div>
    </div>
    <div class="stat">
      <div class="stat-number">7</div>
      <div class="stat-label">Open Source Projects</div>
    </div>
    <div class="stat">
      <div class="stat-number">50+</div>
      <div class="stat-label">Successful Projects</div>
    </div>
  </div>
</div>
```

---

## Implementation Checklist

### Content:
- [ ] Collect team member information (use template above)
- [ ] Get professional headshots (or schedule photoshoot)
- [ ] Write bios for each team member
- [ ] Get social media links
- [ ] Calculate team stats

### Design:
- [ ] Choose layout style (grid, staggered, or carousel)
- [ ] Design team member cards
- [ ] Add social media icons
- [ ] Make mobile responsive
- [ ] Test on all devices

### Technical:
- [ ] Optimize images for web
- [ ] Add alt text to all photos
- [ ] Ensure social links open in new tabs
- [ ] Add schema markup for team members (SEO)
- [ ] Test loading speed

---

## If You Don't Have Team Photos Yet

### Temporary Solutions:

**Option 1**: Use professional illustrations or avatars  
**Option 2**: Wait to launch team section until photos ready  
**Option 3**: Use company/office photos instead of individuals  
**Option 4**: Start with just founder, add team later

**Recommendation**: Don't launch with bad photos. Wait for good ones or skip this section temporarily.

---

## Next Steps

1. ✅ **Collect team information** using template
2. ✅ **Schedule professional photoshoot** (or DIY with good lighting)
3. ✅ **Write team bios** (2-3 sentences each)
4. ✅ **Add to About page** (primary location)
5. ✅ **Link from homepage** ("Meet the Team")
6. ✅ **Update as team grows**

---

**People buy from people. Show your team, build trust, close more deals. 🚀**

