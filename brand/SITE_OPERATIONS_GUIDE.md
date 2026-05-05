# Be Audaciously You — Site Operations Guide

*Last updated: 5 May 2026 by Brian Leputu*

---

## Welcome to your live site

Your site is live at **https://beaudaciouslyyou.com**

What's working today:

- Your public website (hero, about, four service pillars, founder, events, mission, contact)
- Registration form that captures every signup to a Google Sheet and emails you a notification
- Custom email at `info@beaudaciouslyyou.com`
- Mobile-friendly across phones, tablets, and desktops

This guide is not a manual to read end-to-end. Skim the table of contents and jump to what you need.

---

## Where everything lives

| Thing | Where | How to access |
|---|---|---|
| The website | https://beaudaciouslyyou.com | Any browser |
| Your hosting control panel | https://da28.host-ww.net:2222 | Login in your credentials note |
| Your email mailbox | `info@beaudaciouslyyou.com` | Webmail link below, or phone client |
| Form registrations | Google Sheet "Be Audaciously You — Registrations" | Shared with you in your Drive |
| Brand assets | `/brand/` folder in the project | Sent to you separately |

**Important:** passwords and login URLs are NOT in this document. They were sent to you privately. Keep them in your password manager.

---

## Daily things you'll want to do

### Check new registrations

When someone fills in your registration form, two things happen automatically within 5 seconds:

1. A new row appears in your Google Sheet
2. A notification email lands in your `info@` inbox

**To see all registrations:** open the Google Sheet from your Drive (search "Be Audaciously You — Registrations"). Each row is one person.

**To export:** File → Download → Excel or CSV.

### Read your `info@` inbox

**On a browser (works immediately, no setup):**

Go to https://webmail.beaudaciouslyyou.com

Login:
- Username: `info@beaudaciouslyyou.com` (the full address, not just "info")
- Password: from your credentials note

If that URL doesn't load, the fallback that always works:
https://da28.host-ww.net:2222/webmail

**On your phone (Gmail, Outlook, Apple Mail):**

Add a new account. When asked to choose a provider, pick **"Other"** or **"Manual setup"**. Don't use auto-detect (it guesses wrong on this kind of mailbox).

Then enter:

| Field | Value |
|---|---|
| Email | `info@beaudaciouslyyou.com` |
| Password | from your credentials note |
| Incoming server (IMAP) | `mail.beaudaciouslyyou.com`, port 993, SSL/TLS |
| Outgoing server (SMTP) | `mail.beaudaciouslyyou.com`, port 587, STARTTLS |
| Username for both | the full email address |

If your phone keeps failing to connect, double-check that you picked "Manual" and not "Auto" or "IMAP only."

---

## When you need something changed

| You want to | You can do it | I handle it |
|---|---|---|
| Read registrations | ✅ | |
| Check the inbox | ✅ | |
| Reply to a registrant | ✅ | |
| Add real Instagram and Facebook URLs to the contact section | | ✅ |
| Swap a photo or change copy | | ✅ |
| Update the registration form fields | | ✅ |
| Add a new section or major feature | | ✅ separate scope |

For small edits, message me with what you want changed and I'll ship it. Most copy or image swaps take under a day.

For larger work (new sections, e-commerce, integrations) we'll have a separate conversation about scope and pricing.

---

## If something looks broken

| Symptom | First thing to try | Then |
|---|---|---|
| Site doesn't load at all | Try another browser or device | Message me |
| Layout looks broken or images missing | Hard refresh (Ctrl+F5 on Windows, Cmd+Shift+R on Mac) | Message me |
| Form says "Thank you!" but no row in the sheet | Send a second test from a different browser | Message me |
| Email not arriving in `info@` | Check the Spam folder | Message me |
| Webmail won't log you in | Confirm password. Try the fallback URL | Message me |

For anything urgent, message me directly. Ballpark response: same day for issues, next day for cosmetic stuff.

---

## Owning your stack long-term

This section is for if you ever want to be fully independent of me.

**Already 100% yours:**

- Your domain `beaudaciouslyyou.com` (registered and paid by you, lives at HostAfrica)
- Your hosting (HostAfrica account, your bill, your control panel login)
- Your mailbox `info@beaudaciouslyyou.com` (same HostAfrica account)
- Your brand assets (logos, photos, copy)

**Currently runs through my Google account:**

- The registrations Google Sheet lives in my Drive. You have Editor access, so you can read and edit, but ownership is mine.
- The piece of code that connects your form to the sheet runs through my Google account.

If you ever want to take both of these over fully (so nothing depends on me being available), it's a 30-minute handover. Ask whenever you're ready.

---

## Questions?

Message me on [WhatsApp / email — fill in your preferred channel].

I'll update this guide whenever something changes. The date at the top tells you when it was last touched.
