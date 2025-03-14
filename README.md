# 🚀 Django-Based Portfolio Website

A personal portfolio website built with **Django** and **HTML/CSS**, implementing best practices for **SEO, security, performance, and accessibility**.

## 📌 What I Learned

- Implement **lazy loading (`loading="lazy"`)** for performance improvements.

### 🔹 Frontend (HTML & CSS)
#### 1️⃣ Meta Tags for SEO Optimization
- Implemented essential `<meta>` tags to improve search ranking and social media sharing.
- Used **Open Graph (OG) & Twitter Cards** for better previews when sharing the website.
- Applied `canonical` links to avoid duplicate content issues.

#### 2️⃣ Optimized `<a>` Tags for SEO, Security & Accessibility
- **LinkedIn, GitHub, and Vercel links** were enhanced with:
  - **`noopener noreferrer`** → Improves security by preventing tab hijacking.
  - **`nofollow`** → Used when needed to prevent passing SEO authority.
  - **`hreflang="en"`** → Helps search engines understand the language.
  - **`aria-label`** → Improves accessibility for screen readers.
  - **`referrerpolicy="strict-origin-when-cross-origin"`** → Limits referrer data exposure.

#### 3️⃣ Fixed Styling & Layout Issues
- Fixed unintended **bold text issue** by debugging CSS rules (`font-weight: bold;`).
- Ensured proper `robots.txt` configuration for **SEO** to prevent indexing of unnecessary URLs.

---

### 🔹 Backend (Django)
#### 1️⃣ Creating a Basic Sitemap for the Portfolio
- Built a **dynamic sitemap** using `django.contrib.sitemaps`, helping search engines crawl important pages.
- Registered `sitemap.xml` in `robots.txt` to assist search engines in indexing the site.

#### 2️⃣ Adding Content Security Policy (CSP) using `django-csp`
- Implemented **CSP headers** to mitigate risks of XSS (Cross-Site Scripting) attacks.
- Used **`script-src`, `style-src`, `img-src`, `font-src` directives** to allow only trusted resources.
- Enabled **error logging** for CSP violations (`error_logged.txt`).

#### 3️⃣ Configured `robots.txt` to Control Indexing
- Allowed indexing of **important pages** while blocking unnecessary ones (`admin/`, `csp-violation-report/`).

---

## 📌 JSON-LD for SEO Optimization  

To enhance **Google Search visibility** and enable **rich results**, I implemented **JSON-LD structured data** in my portfolio.  

### 🔹 Features of JSON-LD Integration  
- 📌 **Personal Profile Schema (`@type: Person`)** → Helps Google recognize me as a **Python Django Developer**.  
- 🔗 **Social & Professional Links (`sameAs`)** → Added **LinkedIn, GitHub, and Twitter** for credibility.  
- 🎓 **Certifications & Education (`alumniOf`)** → Listed multiple **online courses & certifications** from Coursera, Google Cloud, etc.  
- 📩 **Contact Information (`email`)** → Helps with professional outreach.  

### 🛠️ **Implementation Details**  
- The **JSON-LD script** is placed inside the `<head>` section of `base.html`.  
- Verified with **Google Rich Results Test** and submitted via **Google Search Console**.  

🔍 **[Test JSON-LD Structured Data](https://search.google.com/test/rich-results)**  


## 🌍 Live Demo
- **Portfolio Website:** [personalwebpage.pythonanywhere.com](https://personalwebpage.pythonanywhere.com/)  
- **GitHub Repo:** [Portfolio Repository](https://github.com/osamaaslam86004/personal-webpage.git)  

---

## 🔧 Technologies Used
- **Frontend:** HTML5, CSS3, Bootstrap  
- **Backend:** Django, Django REST Framework  
- **Security Enhancements:** `django-csp`, `robots.txt`, `sitemap.xml`  
- **Hosting:** PythonAnywhere  

---


## Update: 1 

### ✅ Added `srcset` for SEO and Performance
- Implemented the `srcset` attribute for responsive images.
- Improves SEO by providing better image resolution based on device capabilities.
- Enhances website performance by loading the optimal image size.

### ✅ Implemented Cache Header + ETag Header
- Added `Cache-Control` headers to improve page load speed.
- Implemented ETag headers by fetching the last modified time of the HTML file from the OS.
- Ensures efficient caching and reduces unnecessary data transfers.


## 📩 Contact
📧 Email: osama.aslam.86004@gmail.com  
🔗 LinkedIn: [osamaaslam86004](https://www.linkedin.com/in/osama-aslam-86004/)  

---