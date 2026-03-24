---
title: "How to Create a CNAME Record For Your Domain"
category: "general-linux"
tags: ["create", "cname", "record", "your", "domain"]
---

### How to Create a CNAME Record For Your Domain

<a id="article"></a>

The **CNAME** record will point your domain or subdomain to the IP address of the destination hostname. So, if the IP of the destination hostname changes, you won't need to change your DNS records as the CNAME will have the same IP.

You are welcome to use this video guide or follow the text instructions further in the article.

  

  
<br/>

**NOTE**: Please don't set up a CNAME record for a bare domain e.g., *yourdomain.tld* (@ hostname) since it may affect the operation of the domain's MX records and, consequently, the email service. In most cases you will need to create a CNAME record for *www* (or other subdomain) and URL Redirect for @ that will point to *http://www.yourdomain.tld/*  

  

It is possible to set up a CNAME record from Namecheap's side for [domains](https://www.namecheap.com/) that are using our [BasicDNS](https://www.namecheap.com/support/knowledgebase/article.aspx/782/10/how-do-i-set-my-domain-to-use-namecheaps-default-dns-servers), [PremiumDNS](https://www.namecheap.com/security/premiumdns/) or [FreeDNS](https://www.namecheap.com/support/knowledgebase/article.aspx/531/51/what-is-freedns).  

  

If your domain is pointed to the Namecheap Web Hosting DNS, you can set the CNAME record in your cPanel with the help of [this tutorial](https://www.namecheap.com/support/knowledgebase/article.aspx/10277/2255/video-how-to-set-up-a-cname-record-in-cpanel).

  

### **Follow these steps to create a CNAME record for your domain**

  

(1) Sign into your **Namecheap account** (The "Sign In" option is available in the header of the page):  

  

  
![](../_resources/sign_in_349d2536ff804208a3bcacbbefe29eca.png)  
<br/>

(2) Select **Domain List** from the left side menu and (3) click the **Manage** button next to your domain:  

  

  

<img width="844" height="309" src="../_resources/domain_list_manage_a7153d139813471194561d8a8c803c6.png"/>

  

(4) Navigate to the **Advanced DNS** tab and (5) click the **Add New Record** button (*[not able to edit Host Records?](https://www.namecheap.com/support/knowledgebase/article.aspx/323/46/why-cant-i-modify-email-domain-redirect-and-host-records-in-my-namecheap-account/)*) in the **Host Records** section:  

  

  
<img width="844" height="302" src="../_resources/advanced_new_record_8e21cb10799c42b0b48661aa96c652.png"/>  
<br/>

(6) Select **CNAME Record** from the drop-down menu for **Type**, put your desired host (e.g. *www*) for **Host** and enter the record itself (e.g. *ghs.googlehosted.com*) into **Value**:  

  

  

<img width="844" height="118" src="../_resources/cname_record_2d2e0ff507bb4279b8940ca6a6e8fac5.png"/>  
<br/>

***Note**: **Namecheap DNS system** automatically adds the domain name to the values submitted during record creation. Please make sure that your domain name is not duplicated in the values (e.g., that you enter your subdomain  just like mysubdomain and not like mysubdomain.domain.tld). If your domain is using Namecheap Basic nameservers or PremiumDNS, remove the "domain.tld" part of the provided Host value before adding it to the validation record for the domain. Copy the Host and Target values and paste them into the corresponding fields in your DNS provider account. Set the minimum possible TTL value.*

  

More details on hosts you can use can be found in the "*[How do I create a subdomain for my domain?](https://www.namecheap.com/support/knowledgebase/article.aspx/9776/2237/how-do-i-create-a-subdomain-for-my-domain)*" article.  

  

Please note that the target value should be a [fully qualified domain name](https://en.wikipedia.org/wiki/Fully_qualified_domain_name) - a valid (sub)domain, not just a random string of symbols. Otherwise, you will get the "*Please enter a fully qualified domain name.*" warning.  

  

(7) Click on the **Save All Changes** button each time you need to save the record:  

  

  
<img width="844" height="128" src="../_resources/cname_record2_8d465b95478549dca544c6253044f07f.png"/>  
<br/>Please check if there are any CNAME, URL Redirect (*Unmasked/Masked/Permanent*), ALIAS or A records set for the same **Host**. Such records can conflict with each other and they should be removed. CNAME record blocks any other records created for the same Host.  
<br/>

Here is a CNAME Example with conflicting records:

  

  

<img width="844" height="127" src="../_resources/conflict2_b9162c00c4f749d09de64ee26c4de658.png"/>  
<br/>Once you've done this, wait for 30 minutes for the host records to be accepted.  
<br/>That's it!  
<br/>

If you have any questions, feel free to contact our [Support Team](https://www.namecheap.com//support/live-chat/domains/).

### Associated articles

[Which record type option should I choose for the information I’m about to enter?](https://www.namecheap.com/support/knowledgebase/article.aspx/579/2237/which-record-type-option-should-i-choose-for-the-information-im-about-to-enter/)

Comments

We welcome your comments, questions, corrections and additional information relating to this article. Your comments may take some time to appear. Please be aware that off-topic comments will be deleted.

If you need specific help with your account, feel free to contact our [Support Team](https://www.namecheap.com/help-centre/). Thank you.

Updated

**9/23/2024**

Viewed

**177324** times

[](http://www.facebook.com/sharer.php?u=https://www.namecheap.com/support/knowledgebase/article.aspx/9646/2237/how-to-create-a-cname-record-for-your-domain/&t=How%20to%20Create%20a%20CNAME%20Record%20For%20Your%20Domain%20-%20Host%20records%20setup%20-%20Namecheap.com&display=popup "Share on Facebook")[](http://twitter.com/share?url=https://www.namecheap.com/support/knowledgebase/article.aspx/9646/2237/how-to-create-a-cname-record-for-your-domain/&text=How%20to%20Create%20a%20CNAME%20Record%20For%20Your%20Domain%20-%20Host%20records%20setup%20-%20Namecheap.com&via=namecheap "Tweet This")[](http://pinterest.com/pin/create/button/?url=https://www.namecheap.com/support/knowledgebase/article.aspx/9646/2237/how-to-create-a-cname-record-for-your-domain/&description=How%20to%20Create%20a%20CNAME%20Record%20For%20Your%20Domain%20-%20Host%20records%20setup%20-%20Namecheap.com "Pin on Pinterest")

Need help? We're always here for you.

[Go to Live Chat page](https://www.namecheap.com/help-centre/live-chat?loc=)

<img width="30" height="20" src="../_resources/34735a65a0c63bd007fa4c32f67dab4c_ba6f9464f70c46d89.svg"/>We ❤️ Ukraine. Namecheap is a US based registrar. Many of our colleagues originate from or are located within Ukraine. To support Ukraine in their time of need visit this [page](https://war.ukraine.ua/support-ukraine/).

<img width="219" height="43" src="../_resources/26ddc5044470a6aa832e4f370a6b7804_d2472c13452f41429.png"/>](https://www.namecheap.com/)

We make registering, hosting, and managing domains for yourself or others easy and affordable, because the internet needs people.

- [About Namecheap](https://www.namecheap.com/about/)
- [Read our blog](https://www.namecheap.com/blog/)

**Join Our Newsletter & Marketing Communication**  
We'll send you news and offers.

- [](https://twitter.com/namecheap "Twitter")
- [](https://www.facebook.com/NameCheap "Facebook")
- [](https://www.instagram.com/namecheap/ "Instagram")
- [](https://www.pinterest.com/namecheap/ "Pinterest")

**[Domains](https://www.namecheap.com/domains/)**

- [Domain Name Search](https://www.namecheap.com/domains/domain-name-search/)
- [Domain Transfer](https://www.namecheap.com/domains/transfer/)
- [New TLDs](https://www.namecheap.com/domains/new-tlds/explore/)
- [Handshake domainsNEW](https://www.namecheap.com/domains/handshake-domains/)
- [Personal Domain](https://www.namecheap.com/domains/personal/)
- [Namecheap Market](https://www.namecheap.com/market/)
- [Whois Lookup](https://www.namecheap.com/domains/whois/)
- [PremiumDNS](https://www.namecheap.com/security/premiumdns/)
- [FreeDNS](https://www.namecheap.com/domains/freedns/)

**[Hosting](https://www.namecheap.com/hosting/)**

- [Shared Hosting](https://www.namecheap.com/hosting/shared/)
- [WordPress Hosting](https://www.namecheap.com/wordpress/)
- [Reseller Hosting](https://www.namecheap.com/hosting/reseller/)
- [VPS Hosting](https://www.namecheap.com/hosting/vps/)
- [Dedicated Servers](https://www.namecheap.com/hosting/dedicated-servers/)
- [Private Email Hosting](https://www.namecheap.com/hosting/email/)
- [Migrate to Namecheap](https://www.namecheap.com/hosting/hosting-migrate-to-namecheap/)

**[WordPress](https://www.namecheap.com/wordpress/)**

- [Shared Hosting](https://www.namecheap.com/hosting/shared/)
- [WordPress Hosting](https://www.namecheap.com/wordpress/)
- [Migrate WordPress](https://www.namecheap.com/wordpress/migrate/)

**[Security](https://www.namecheap.com/security/)**

- [Domain Privacy](https://www.namecheap.com/security/domain-privacy-service/)
- [Website SecurityNEW](https://www.namecheap.com/security/protect-website/)
- [Fix Hacked WebsiteSOS](https://www.namecheap.com/security/fix-hacked-website/)
- [Domain VaultNEW](https://www.namecheap.com/security/domain-vault/)
- [PremiumDNS](https://www.namecheap.com/security/premiumdns/)
- [CDN](https://www.namecheap.com/supersonic-cdn/)
- [FastVPNUPDATED](https://www.namecheap.com/vpn/)
- [Cyber InsuranceNEW](https://www.namecheap.com/cyber-insurance/)
- [2FA](https://www.namecheap.com/security/2fa-two-factor-authentication/)
- [Public DNS](https://www.namecheap.com/dns/free-public-dns/)
- [Anti-Spam ProtectionNEW](https://www.namecheap.com/security/anti-spam-protection/)

**[Transfer to UsTRY ME](https://www.namecheap.com/domains/transfer/)**

- [Domain Transfer](https://www.namecheap.com/domains/transfer/)
- [Migrate Hosting](https://www.namecheap.com/hosting/hosting-migrate-to-namecheap/)
- [Migrate WordPress](https://www.namecheap.com/wordpress/migrate/)
- [Migrate Email](https://www.namecheap.com/hosting/email/migrate-email/)

**[SSL Certificates](https://www.namecheap.com/security/ssl-certificates/)**

- [Comodo](https://www.namecheap.com/security/ssl-certificates/comodo/)
- [Organisation Validation](https://www.namecheap.com/security/ssl-certificates/organisation-validation/)
- [Domain Validation](https://www.namecheap.com/security/ssl-certificates/domain-validation/)
- [Extended Validation](https://www.namecheap.com/security/ssl-certificates/extended-validation/)
- [Single Domain](https://www.namecheap.com/security/ssl-certificates/single-domain/)
- [Wildcard](https://www.namecheap.com/security/ssl-certificates/wildcard/)
- [Multi-Domain](https://www.namecheap.com/security/ssl-certificates/multi-domain/)

**[Resellers](https://www.namecheap.com/resellers/ssl-certificates/join-the-program/)**

- [SSL Certificates](https://www.namecheap.com/resellers/ssl-certificates/join-the-program/)
- [Reseller Hosting](https://www.namecheap.com/hosting/reseller/)

**[Promos](https://www.namecheap.com/promos/)**

**[Guru Guides](https://www.namecheap.com/guru-guides/)**

**[Help centre](https://www.namecheap.com/help-centre/)**

- [Status Updates](https://www.namecheap.com/status-updates/)
- [Knowledgebase](https://www.namecheap.com/support/knowledgebase/)
- [How-To Videos](https://www.namecheap.com/support/knowledgebase/category/2253/howto-videos/)
- [Submit Ticket](https://support.namecheap.com/index.php?/Tickets/Submit)
- [Live Chat](https://www.namecheap.com/help-centre/live-chat/)
- [Report Abuse](https://www.namecheap.com/support/knowledgebase/article.aspx/9196/5/how-and-where-can-i-file-abuse-complaints/)

**[Marketing Tools](https://www.namecheap.com/apps/)**

- [Marketplace](https://www.namecheap.com/apps/)
- [How to Get StartedNEW](https://www.namecheap.com/build-and-grow-hub/)
- [Business FormationFREE](https://www.namecheap.com/apps/business-formation/)
- [Relate](https://www.namecheap.com/relate/)
- [RelateSocialAI](https://www.namecheap.com/relate/social/)
- [RelateReviewsAI](https://www.namecheap.com/relate/reviews/)
- [RelateLocalNEWAI](https://www.namecheap.com/relate/local/)
- [RelateSEONEWAI](https://www.namecheap.com/relate/seo/)
- [RelateAdsNEWAI](https://www.namecheap.com/relate/ads/)
- [Brand MonitoringNEWAI](https://www.namecheap.com/relate/radar/)
- [Visual](https://www.namecheap.com/visual/)
- [Site MakerNEW](https://www.namecheap.com/visual/site-maker/)
- [Font MakerNEW](https://www.namecheap.com/visual/font-generator/)
- [Logo MakerAI](https://www.namecheap.com/logo-maker/)
- [Business Name Generator](https://www.namecheap.com/visual/business-name-generator/)
- [Stencil Graphics](https://www.namecheap.com/visual/stencil/)
- [Business Card Maker](https://www.namecheap.com/visual/card-maker/)

**[Careers](https://www.namecheap.com/careers/)**

**[Affiliates](https://www.namecheap.com/affiliates/)**

**[Send us Feedback](mailto:feedback@namecheap.com?subject=Send%20us%20Feedback)**

The entirety of this site is protected by copyright © 2000–2024 Namecheap, Inc.

4600 East Washington Street, Suite 300, Phoenix, AZ 85034, USA

- [Terms and Conditions](https://www.namecheap.com/legal/)
- [Privacy Policy](https://www.namecheap.com/legal/general/privacy-policy/)
- [UDRP](https://www.namecheap.com/legal/domains/udrp/)
- Cookie Preferences

**WE SUPPORT**

*Electronic Frontier Foundation*

*Fight For The Future*

We are an ICANN accredited registrar.  
Serving customers since 2001.

Payment Options

- *American Express*
- *Bitcoin*
- *MasterCard*
- *PayPal*
- *Visa*
- *Discover*
- *UnionPay*
- *JCB*
- *Diners Club*

- [![Sectigo](../_resources/7911bedb11d7caa2db368f7b8e1bf9a8_35975705882e4a439.png)](https://secure.trust-provider.com/ttb_searcher/trustlogo?v_querytype=W&v_shortname=SECEV&v_search=http://www.namecheap.com/&x=6&y=5)
- [*Android app on google play*](https://nc1.app.link/W1qV0gjLZG "Android app on google play")
- [*iOS App Store*](https://nc1.app.link/W1qV0gjLZG "iOS App Store")