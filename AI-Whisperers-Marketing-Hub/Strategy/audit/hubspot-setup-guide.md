# HubSpot Setup Guide - Ai-Whisperers

## Step-by-Step Setup (30 minutes total)

---

## STEP 1: Initial Account Setup (5 min)

You're already logged in at: https://app.hubspot.com/global-home/50766796

### Complete Your Profile:
1. Click your **profile icon** (top right)
2. Go to **Profile & Preferences**
3. Fill in:
   - Full Name
   - Job Title: "Founder" or "AI Automation Consultant"
   - Phone number
   - Profile photo

---

## STEP 2: Create Your Contact List (5 min)

### Navigation:
1. Click **Contacts** in the top menu
2. Click **Lists** in the submenu
3. Click **Create list** (orange button, top right)

### Settings:
- **List name**: `AI Automation Leads`
- **List type**: Select **Active list** (auto-updates when contacts match criteria)
- For now, leave filters empty (we'll add contacts via forms)
- Click **Save list**

---

## STEP 3: Create Your Signup Form (10 min)

### Navigation:
1. Click **Marketing** in the top menu
2. Click **Forms** in the submenu
3. Click **Create form** (orange button)

### Form Setup:
1. Select **Embedded form**
2. Click **Next**
3. Choose **Blank template**
4. Click **Start**

### Add Form Fields:
Default fields to keep:
- Email (required) ✓
- First name ✓

Remove any other fields (keep it simple!)

### Form Settings (left sidebar):
1. Click **Options** tab:
   - **What should happen after someone submits**: Show thank you message
   - **Thank you message**:
   ```
   Thanks for signing up! Check your email for your free resource.
   ```

2. Click **Style & preview** to customize colors to match your brand

3. Click **Automation** tab:
   - Click **Create workflow**
   - This is where we'll connect the welcome email (Step 4)

### Save & Publish:
1. Click **Update** (top right)
2. Name your form: `Lead Magnet Signup Form`
3. Click **Publish**

### Get Embed Code:
1. After publishing, click **Share**
2. Copy the **Embed code**
3. Save this for your website

---

## STEP 4: Create Your Welcome Email (10 min)

### Navigation:
1. Click **Marketing** in the top menu
2. Click **Email** in the submenu
3. Click **Create email** (orange button)
4. Select **Regular**

### Choose Template:
1. Select **Simple** or **Plain** template
2. Click **Select**

### Email Content:

**Subject Line:**
```
Here's your AI Automation Opportunity Audit
```

**Preview Text:**
```
Plus a quick intro to how we can help you save 10+ hours per week
```

**Email Body (copy this):**

```
Hey {{contact.firstname}},

Thanks for downloading the AI Automation Opportunity Audit!

👉 Here's your link: [INSERT LINK TO YOUR PDF]

Quick intro: I'm [YOUR NAME] from Ai-Whisperers. We help businesses automate repetitive work using AI—cutting costs by 40% and saving 10+ hours per week.

What to expect from me:
• 1 email per week (no spam, ever)
• Practical automation tips you can use immediately
• Real case studies and results

Got questions? Just reply to this email—I read every one.

Talk soon,
[YOUR NAME]
Ai-Whisperers

P.S. Want faster results? Book a free 30-minute strategy call here: [CALENDLY LINK]
```

### Email Settings:
1. Click **Settings** tab
2. **From name**: Your Name
3. **From address**: your@email.com
4. **Reply-to**: same as from address

### Save:
1. Click **Save** (top left)
2. Name it: `Welcome Email - Lead Magnet`
3. Don't send yet - we'll automate it!

---

## STEP 5: Connect Form to Welcome Email (Automation)

### Navigation:
1. Click **Automation** in the top menu
2. Click **Workflows**
3. Click **Create workflow**
4. Select **From scratch**
5. Choose **Blank workflow**

### Build the Workflow:

**Step 1 - Set Trigger:**
1. Click **Set up triggers**
2. Select **Form submission**
3. Choose your form: `Lead Magnet Signup Form`
4. Click **Save**

**Step 2 - Add Action:**
1. Click the **+** button
2. Select **Send email**
3. Choose your email: `Welcome Email - Lead Magnet`
4. Click **Save**

**Step 3 - Add to List (optional but recommended):**
1. Click **+** after the email
2. Select **Add to static list** or use your active list
3. Choose: `AI Automation Leads`

### Activate:
1. Click **Review and publish** (top right)
2. Click **Turn on**

---

## STEP 6: Test Everything (5 min)

### Test Your Form:
1. Go to **Marketing** → **Forms**
2. Click your form
3. Click **Preview**
4. Fill in a test email (use yours + `+test`, e.g., `you+test@gmail.com`)
5. Submit

### Verify:
- [ ] Form submission works
- [ ] Thank you message appears
- [ ] Welcome email arrives in inbox
- [ ] Contact appears in your list

---

## QUICK REFERENCE: Where Things Are in HubSpot

| What | Where |
|------|-------|
| Contacts/Lists | Contacts → Lists |
| Forms | Marketing → Forms |
| Emails | Marketing → Email |
| Automations | Automation → Workflows |
| Analytics | Reporting → Dashboards |

---

## NEXT STEPS (After Basic Setup)

### This Week:
- [ ] Add form to your website
- [ ] Create your lead magnet PDF
- [ ] Test the full flow

### Next Week:
- [ ] Create email sequence (3-5 emails over 2 weeks)
- [ ] Set up lead scoring
- [ ] Connect to LinkedIn lead gen forms (if using)

---

## TROUBLESHOOTING

**Form not showing on website?**
- Make sure you copied the full embed code
- Check your website allows external scripts

**Email not sending?**
- Check workflow is turned ON
- Verify email is published (not draft)
- Check spam folder

**Contacts not appearing in list?**
- Refresh the page
- Check list filters aren't excluding them

---

## BONUS: Email Sequence to Add Later

After the welcome email, set up a nurture sequence:

**Email 2 (Day 3):** "The #1 mistake businesses make with automation"
**Email 3 (Day 7):** "Case study: How [Client] saved 15 hours/week"
**Email 4 (Day 10):** "5 processes you should automate this month"
**Email 5 (Day 14):** "Ready to automate? Here's how we can help"

I can help you write these when you're ready!

---

*Guide created for Ai-Whisperers HubSpot setup*
