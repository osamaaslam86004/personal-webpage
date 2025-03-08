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

## 📩 Contact
📧 Email: osama.aslam.86004@gmail.com  
🔗 LinkedIn: [osamaaslam86004](https://www.linkedin.com/in/osama-aslam-86004/)  

---

## 🏆 Next Steps
- Add **structured data (`JSON-LD`)** for richer Google search results.
