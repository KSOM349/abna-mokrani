from flask import Flask, render_template_string, request

app = Flask(__name__)

def get_html(lang='ar'):
    if lang == 'en':
        return '''
        <!DOCTYPE html>
        <html lang="en" dir="ltr">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Abna Mokrani - Technology & Business</title>
            <style>
                /* نفس الاستايل السابق لكن بالإنجليزية */
                :root {
                    --gold: #FFD700;
                    --purple: #8A2BE2;
                    --blue: #1E90FF;
                    --dark: #0A0A0A;
                    --light: #FFFFFF;
                }
                
                * {
                    margin: 0;
                    padding: 0;
                    box-sizing: border-box;
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                }
                
                body {
                    background: var(--dark);
                    color: var(--light);
                    min-height: 100vh;
                    overflow-x: hidden;
                }

                /* تأثيرات تكنولوجية */
                body::before {
                    content: '';
                    position: fixed;
                    top: 0;
                    left: 0;
                    width: 100%;
                    height: 100%;
                    background: 
                        radial-gradient(circle at 20% 80%, rgba(138, 43, 226, 0.1) 0%, transparent 50%),
                        radial-gradient(circle at 80% 20%, rgba(30, 144, 255, 0.1) 0%, transparent 50%);
                    z-index: -1;
                }

                .container {
                    max-width: 1200px;
                    margin: 0 auto;
                    padding: 0 20px;
                }

                /* الهيدر */
                .header {
                    background: rgba(10, 10, 10, 0.95);
                    padding: 1rem 0;
                    border-bottom: 2px solid var(--gold);
                    position: fixed;
                    width: 100%;
                    top: 0;
                    z-index: 1000;
                }

                .nav-container {
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                }

                .logo {
                    font-size: 2rem;
                    font-weight: bold;
                    background: linear-gradient(45deg, var(--gold), var(--purple));
                    -webkit-background-clip: text;
                    -webkit-text-fill-color: transparent;
                }

                .nav-links {
                    display: flex;
                    list-style: none;
                    gap: 2rem;
                }

                .nav-links a {
                    color: var(--light);
                    text-decoration: none;
                    font-weight: 500;
                    transition: all 0.3s;
                    padding: 0.5rem 1rem;
                    border-radius: 5px;
                }

                .nav-links a:hover {
                    color: var(--gold);
                    background: rgba(255, 215, 0, 0.1);
                }

                .language-switcher {
                    background: rgba(255,255,255,0.1);
                    padding: 0.5rem 1rem;
                    border-radius: 5px;
                    color: var(--light);
                    text-decoration: none;
                    transition: all 0.3s;
                }

                .language-switcher:hover {
                    background: var(--gold);
                    color: var(--dark);
                }

                /* الهيرو مع صورتك */
                .hero {
                    padding: 200px 0 100px;
                    text-align: center;
                    background: linear-gradient(135deg, rgba(138, 43, 226, 0.2), rgba(30, 144, 255, 0.2));
                    position: relative;
                }

                .hero::before {
                    content: '';
                    position: absolute;
                    top: 0;
                    left: 0;
                    width: 100%;
                    height: 100%;
                    /* صورتك الحقيقية - تأكد من الرابط */
                    background: url('https://i.ibb.co/67yqYZkK/image.jpg') center/cover;
                    opacity: 0.3;
                    z-index: -1;
                }

                .hero h1 {
                    font-size: 3.5rem;
                    margin-bottom: 1rem;
                    background: linear-gradient(45deg, var(--gold), var(--blue));
                    -webkit-background-clip: text;
                    -webkit-text-fill-color: transparent;
                }

                .hero p {
                    font-size: 1.3rem;
                    margin-bottom: 2rem;
                    color: var(--light);
                    opacity: 0.9;
                }

                .btn {
                    background: linear-gradient(45deg, var(--purple), var(--blue));
                    color: white;
                    padding: 1rem 2rem;
                    border: none;
                    border-radius: 25px;
                    font-size: 1.1rem;
                    cursor: pointer;
                    transition: all 0.3s;
                    text-decoration: none;
                    display: inline-block;
                }

                .btn:hover {
                    transform: translateY(-3px);
                }

                /* الخدمات */
                .services {
                    padding: 100px 0;
                    background: rgba(10, 10, 10, 0.8);
                }

                .section-title {
                    text-align: center;
                    font-size: 2.5rem;
                    margin-bottom: 3rem;
                    color: var(--gold);
                }

                .services-grid {
                    display: grid;
                    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                    gap: 2rem;
                }

                .service-card {
                    background: rgba(255, 255, 255, 0.05);
                    padding: 2rem;
                    border-radius: 15px;
                    border: 1px solid rgba(255, 215, 0, 0.3);
                    transition: all 0.3s;
                }

                .service-card:hover {
                    transform: translateY(-10px);
                }

                .service-icon {
                    font-size: 3rem;
                    margin-bottom: 1rem;
                    color: var(--gold);
                }

                .service-card h3 {
                    font-size: 1.5rem;
                    margin-bottom: 1rem;
                }

                .service-card p {
                    color: rgba(255, 255, 255, 0.8);
                }
            </style>
        </head>
        <body>
            <header class="header">
                <div class="container nav-container">
                    <div class="logo">Abna Mokrani</div>
                    <ul class="nav-links">
                        <li><a href="#home">Home</a></li>
                        <li><a href="#services">Services</a></li>
                        <li><a href="#gallery">Gallery</a></li>
                        <li><a href="#contact">Contact</a></li>
                        <li><a href="/?lang=ar" class="language-switcher">العربية</a></li>
                    </ul>
                </div>
            </header>

            <section class="hero" id="home">
                <div class="container">
                    <h1>Abna Mokrani</h1>
                    <p>Technological Excellence Meets Craftsmanship - Future of Integrated Services</p>
                    <a href="#services" class="btn">Discover Our Services</a>
                </div>
            </section>

            <section class="services" id="services">
                <div class="container">
                    <h2 class="section-title">Our Integrated Services</h2>
                    <div class="services-grid">
                        <div class="service-card">
                            <div class="service-icon">🛋️</div>
                            <h3>Smart Furniture & Decor</h3>
                            <p>Design and manufacturing of custom furniture with luxury decorations</p>
                        </div>
                        <div class="service-card">
                            <div class="service-icon">❄️</div>
                            <h3>Refrigeration Systems</h3>
                            <p>Sales and maintenance of all cooling devices</p>
                        </div>
                        <div class="service-card">
                            <div class="service-icon">🚜</div>
                            <h3>Agricultural Equipment</h3>
                            <p>Modern agricultural equipment and spare parts</p>
                        </div>
                        <div class="service-card">
                            <div class="service-icon">🏘️</div>
                            <h3>Real Estate Rental</h3>
                            <p>Apartments, commercial shops, and warehouses</p>
                        </div>
                    </div>
                </div>
            </section>

            <section class="services" id="contact">
                <div class="container">
                    <h2 class="section-title">Contact Us</h2>
                    <div style="text-align: center; padding: 2rem;">
                        <p>📞 <strong>Phone:</strong> 05X-XXX-XXXX</p>
                        <p>📍 <strong>Location:</strong> Saudi Arabia</p>
                        <p>⏰ <strong>Working Hours:</strong> 8 AM - 10 PM</p>
                    </div>
                </div>
            </section>
        </body>
        </html>
        '''
    else:
        return '''
        <!DOCTYPE html>
        <html lang="ar" dir="rtl">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>أبناء مقراني - للتكنولوجيا والأعمال</title>
            <style>
                :root {
                    --gold: #FFD700;
                    --purple: #8A2BE2;
                    --blue: #1E90FF;
                    --dark: #0A0A0A;
                    --light: #FFFFFF;
                }
                
                * {
                    margin: 0;
                    padding: 0;
                    box-sizing: border-box;
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                }
                
                body {
                    background: var(--dark);
                    color: var(--light);
                    min-height: 100vh;
                    overflow-x: hidden;
                }

                body::before {
                    content: '';
                    position: fixed;
                    top: 0;
                    left: 0;
                    width: 100%;
                    height: 100%;
                    background: 
                        radial-gradient(circle at 20% 80%, rgba(138, 43, 226, 0.1) 0%, transparent 50%),
                        radial-gradient(circle at 80% 20%, rgba(30, 144, 255, 0.1) 0%, transparent 50%);
                    z-index: -1;
                }

                .container {
                    max-width: 1200px;
                    margin: 0 auto;
                    padding: 0 20px;
                }

                .header {
                    background: rgba(10, 10, 10, 0.95);
                    padding: 1rem 0;
                    border-bottom: 2px solid var(--gold);
                    position: fixed;
                    width: 100%;
                    top: 0;
                    z-index: 1000;
                }

                .nav-container {
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                }

                .logo {
                    font-size: 2rem;
                    font-weight: bold;
                    background: linear-gradient(45deg, var(--gold), var(--purple));
                    -webkit-background-clip: text;
                    -webkit-text-fill-color: transparent;
                }

                .nav-links {
                    display: flex;
                    list-style: none;
                    gap: 2rem;
                }

                .nav-links a {
                    color: var(--light);
                    text-decoration: none;
                    font-weight: 500;
                    transition: all 0.3s;
                    padding: 0.5rem 1rem;
                    border-radius: 5px;
                }

                .nav-links a:hover {
                    color: var(--gold);
                    background: rgba(255, 215, 0, 0.1);
                }

                .language-switcher {
                    background: rgba(255,255,255,0.1);
                    padding: 0.5rem 1rem;
                    border-radius: 5px;
                    color: var(--light);
                    text-decoration: none;
                    transition: all 0.3s;
                }

                .language-switcher:hover {
                    background: var(--gold);
                    color: var(--dark);
                }

                /* الهيرو مع صورتك */
                .hero {
                    padding: 200px 0 100px;
                    text-align: center;
                    background: linear-gradient(135deg, rgba(138, 43, 226, 0.2), rgba(30, 144, 255, 0.2));
                    position: relative;
                }

                .hero::before {
                    content: '';
                    position: absolute;
                    top: 0;
                    left: 0;
                    width: 100%;
                    height: 100%;
                    /* صورتك الحقيقية */
                    background: url('https://i.ibb.co/67yqYZkK/image.jpg') center/cover;
                    opacity: 0.3;
                    z-index: -1;
                }

                .hero h1 {
                    font-size: 3.5rem;
                    margin-bottom: 1rem;
                    background: linear-gradient(45deg, var(--gold), var(--blue));
                    -webkit-background-clip: text;
                    -webkit-text-fill-color: transparent;
                }

                .hero p {
                    font-size: 1.3rem;
                    margin-bottom: 2rem;
                    color: var(--light);
                    opacity: 0.9;
                }

                .btn {
                    background: linear-gradient(45deg, var(--purple), var(--blue));
                    color: white;
                    padding: 1rem 2rem;
                    border: none;
                    border-radius: 25px;
                    font-size: 1.1rem;
                    cursor: pointer;
                    transition: all 0.3s;
                    text-decoration: none;
                    display: inline-block;
                }

                .btn:hover {
                    transform: translateY(-3px);
                }

                .services {
                    padding: 100px 0;
                    background: rgba(10, 10, 10, 0.8);
                }

                .section-title {
                    text-align: center;
                    font-size: 2.5rem;
                    margin-bottom: 3rem;
                    color: var(--gold);
                }

                .services-grid {
                    display: grid;
                    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                    gap: 2rem;
                }

                .service-card {
                    background: rgba(255, 255, 255, 0.05);
                    padding: 2rem;
                    border-radius: 15px;
                    border: 1px solid rgba(255, 215, 0, 0.3);
                    transition: all 0.3s;
                }

                .service-card:hover {
                    transform: translateY(-10px);
                }

                .service-icon {
                    font-size: 3rem;
                    margin-bottom: 1rem;
                    color: var(--gold);
                }

                .service-card h3 {
                    font-size: 1.5rem;
                    margin-bottom: 1rem;
                }

                .service-card p {
                    color: rgba(255, 255, 255, 0.8);
                }
            </style>
        </head>
        <body>
            <header class="header">
                <div class="container nav-container">
                    <div class="logo">أبناء مقراني</div>
                    <ul class="nav-links">
                        <li><a href="#home">الرئيسية</a></li>
                        <li><a href="#services">خدماتنا</a></li>
                        <li><a href="#gallery">معرض الأعمال</a></li>
                        <li><a href="#contact">اتصل بنا</a></li>
                        <li><a href="/?lang=en" class="language-switcher">English</a></li>
                    </ul>
                </div>
            </header>

            <section class="hero" id="home">
                <div class="container">
                    <h1>أبناء مقراني</h1>
                    <p>التميز التكنولوجي يلتقي بالحرفية اليدوية - مستقبل الخدمات المتكاملة</p>
                    <a href="#services" class="btn">اكتشف خدماتنا</a>
                </div>
            </section>

            <section class="services" id="services">
                <div class="container">
                    <h2 class="section-title">خدماتنا المتكاملة</h2>
                    <div class="services-grid">
                        <div class="service-card">
                            <div class="service-icon">🛋️</div>
                            <h3>الأثاث الذكي والديكور</h3>
                            <p>تصميم وتصنيع أثاث مدمج بتقنيات ذكية بديكورات فاخرة</p>
                        </div>
                        <div class="service-card">
                            <div class="service-icon">❄️</div>
                            <h3>أنظمة التبريد المتطورة</h3>
                            <p>أحدث حلول التبريد الذكية والرقمية</p>
                        </div>
                        <div class="service-card">
                            <div class="service-icon">🚜</div>
                            <h3>التكنولوجيا الزراعية</h3>
                            <p>معدات زراعية ذكية وأنظمة رقمية متكاملة</p>
                        </div>
                        <div class="service-card">
                            <div class="service-icon">🏘️</div>
                            <h3>الحلول العقارية الرقمية</h3>
                            <p>منصات ذكية لإدارة وتأجير العقارات</p>
                        </div>
                    </div>
                </div>
            </section>

            <section class="services" id="contact">
                <div class="container">
                    <h2 class="section-title">اتصل بنا</h2>
                    <div style="text-align: center; padding: 2rem;">
                        <p>📞 <strong>الجوال:</strong> 05X-XXX-XXXX</p>
                        <p>📍 <strong>الموقع:</strong> المملكة العربية السعودية</p>
                        <p>⏰ <strong>أوقات العمل:</strong> 8 صباحاً - 10 مساءً</p>
                    </div>
                </div>
            </section>
        </body>
        </html>
        '''

@app.route('/')
def home():
    lang = request.args.get('lang', 'ar')
    return get_html(lang)

if __name__ == '__main__':
    app.run(debug=True)
