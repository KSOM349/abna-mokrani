from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>أبناء مقراني - قمة التكنولوجيا والتميز</title>
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

            /* تأثيرات تكنولوجية متطورة */
            body::before {
                content: '';
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background: 
                    radial-gradient(circle at 20% 80%, rgba(138, 43, 226, 0.1) 0%, transparent 50%),
                    radial-gradient(circle at 80% 20%, rgba(30, 144, 255, 0.1) 0%, transparent 50%),
                    radial-gradient(circle at 40% 40%, rgba(255, 215, 0, 0.05) 0%, transparent 50%);
                animation: pulse 4s ease-in-out infinite;
                z-index: -1;
            }

            @keyframes pulse {
                0%, 100% { opacity: 0.5; }
                50% { opacity: 0.8; }
            }

            .container {
                max-width: 1200px;
                margin: 0 auto;
                padding: 0 20px;
            }

            /* الهيدر التكنولوجي */
            .header {
                background: rgba(10, 10, 10, 0.95);
                backdrop-filter: blur(20px);
                padding: 1rem 0;
                border-bottom: 3px solid transparent;
                border-image: linear-gradient(45deg, var(--gold), var(--purple), var(--blue)) 1;
                position: fixed;
                width: 100%;
                top: 0;
                z-index: 1000;
                box-shadow: 0 0 30px rgba(138, 43, 226, 0.3);
            }

            .nav-container {
                display: flex;
                justify-content: space-between;
                align-items: center;
            }

            .logo {
                font-size: 2.2rem;
                font-weight: bold;
                background: linear-gradient(45deg, var(--gold), var(--purple), var(--blue));
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                text-shadow: 0 0 20px rgba(255, 215, 0, 0.5);
                animation: glow 2s ease-in-out infinite alternate;
            }

            @keyframes glow {
                from { text-shadow: 0 0 20px rgba(255, 215, 0, 0.5); }
                to { text-shadow: 0 0 30px rgba(255, 215, 0, 0.8), 0 0 40px rgba(138, 43, 226, 0.6); }
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
                border-radius: 8px;
                position: relative;
                overflow: hidden;
            }

            .nav-links a::before {
                content: '';
                position: absolute;
                top: 0;
                left: -100%;
                width: 100%;
                height: 100%;
                background: linear-gradient(90deg, transparent, rgba(255, 215, 0, 0.2), transparent);
                transition: left 0.5s;
            }

            .nav-links a:hover::before {
                left: 100%;
            }

            .nav-links a:hover {
                color: var(--gold);
                background: rgba(255, 215, 0, 0.1);
                box-shadow: 0 0 15px rgba(255, 215, 0, 0.3);
            }

            /* الهيرو مع صورتك */
            .hero {
                padding: 200px 0 100px;
                text-align: center;
                background: linear-gradient(135deg, 
                    rgba(138, 43, 226, 0.2), 
                    rgba(30, 144, 255, 0.2),
                    rgba(255, 215, 0, 0.1));
                position: relative;
                overflow: hidden;
            }

            .hero::before {
                content: '';
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                /* صورتك هنا */
                background: url('https://i.ibb.co/67yqYZkK/image.jpg') center/cover;
                opacity: 0.3;
                z-index: -1;
                filter: brightness(0.7) contrast(1.2);
            }

            .hero::after {
                content: '';
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background: linear-gradient(45deg, 
                    rgba(138, 43, 226, 0.3), 
                    transparent 30%,
                    transparent 70%,
                    rgba(30, 144, 255, 0.3));
                z-index: -1;
            }

            .hero h1 {
                font-size: 4rem;
                margin-bottom: 1.5rem;
                background: linear-gradient(45deg, var(--gold), var(--blue), var(--purple));
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                text-shadow: 0 0 30px rgba(255, 215, 0, 0.5);
                animation: titleGlow 3s ease-in-out infinite alternate;
            }

            @keyframes titleGlow {
                from { 
                    text-shadow: 0 0 30px rgba(255, 215, 0, 0.5);
                    transform: scale(1);
                }
                to { 
                    text-shadow: 0 0 50px rgba(255, 215, 0, 0.8), 0 0 60px rgba(138, 43, 226, 0.6);
                    transform: scale(1.02);
                }
            }

            .hero p {
                font-size: 1.5rem;
                margin-bottom: 2.5rem;
                color: var(--light);
                opacity: 0.9;
                text-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
            }

            .btn {
                background: linear-gradient(45deg, var(--purple), var(--blue));
                color: white;
                padding: 1.2rem 2.5rem;
                border: none;
                border-radius: 30px;
                font-size: 1.2rem;
                cursor: pointer;
                transition: all 0.3s;
                text-decoration: none;
                display: inline-block;
                position: relative;
                overflow: hidden;
                box-shadow: 0 0 20px rgba(138, 43, 226, 0.4);
            }

            .btn::before {
                content: '';
                position: absolute;
                top: -2px;
                left: -2px;
                right: -2px;
                bottom: -2px;
                background: linear-gradient(45deg, var(--gold), var(--purple), var(--blue), var(--gold));
                z-index: -1;
                border-radius: 32px;
                animation: btnRotate 3s linear infinite;
            }

            @keyframes btnRotate {
                0% { transform: rotate(0deg); }
                100% { transform: rotate(360deg); }
            }

            .btn:hover {
                transform: translateY(-5px);
                box-shadow: 0 10px 30px rgba(138, 43, 226, 0.6);
            }

            /* الخدمات بتصميم تكنولوجي */
            .services {
                padding: 120px 0;
                background: rgba(10, 10, 10, 0.9);
                position: relative;
            }

            .services::before {
                content: '';
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 2px;
                background: linear-gradient(90deg, transparent, var(--gold), var(--purple), var(--blue), transparent);
            }

            .section-title {
                text-align: center;
                font-size: 3rem;
                margin-bottom: 4rem;
                color: transparent;
                background: linear-gradient(45deg, var(--gold), var(--purple));
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                text-shadow: 0 0 20px rgba(255, 215, 0, 0.3);
            }

            .services-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
                gap: 2.5rem;
            }

            .service-card {
                background: rgba(255, 255, 255, 0.05);
                padding: 2.5rem;
                border-radius: 20px;
                border: 1px solid transparent;
                background-clip: padding-box;
                position: relative;
                transition: all 0.4s;
                backdrop-filter: blur(15px);
            }

            .service-card::before {
                content: '';
                position: absolute;
                top: -2px;
                left: -2px;
                right: -2px;
                bottom: -2px;
                background: linear-gradient(45deg, var(--gold), var(--purple), var(--blue), var(--gold));
                border-radius: 22px;
                z-index: -1;
                opacity: 0;
                transition: opacity 0.4s;
            }

            .service-card:hover::before {
                opacity: 1;
                animation: cardGlow 2s ease-in-out infinite;
            }

            @keyframes cardGlow {
                0%, 100% { opacity: 0.7; }
                50% { opacity: 1; }
            }

            .service-card:hover {
                transform: translateY(-15px) scale(1.05);
                box-shadow: 0 20px 40px rgba(0, 0, 0, 0.5);
            }

            .service-icon {
                font-size: 4rem;
                margin-bottom: 1.5rem;
                color: var(--gold);
                text-shadow: 0 0 20px currentColor;
                animation: iconFloat 3s ease-in-out infinite;
            }

            @keyframes iconFloat {
                0%, 100% { transform: translateY(0px); }
                50% { transform: translateY(-10px); }
            }

            .service-card h3 {
                font-size: 1.8rem;
                margin-bottom: 1rem;
                color: var(--light);
            }

            .service-card p {
                color: rgba(255, 255, 255, 0.8);
                line-height: 1.6;
            }

            /* بقية الأقسام بنفس المستوى التكنولوجي */
            .gallery {
                padding: 120px 0;
                background: rgba(10, 10, 10, 0.8);
            }

            .gallery-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
                gap: 2rem;
            }

            .gallery-item {
                background: rgba(255, 255, 255, 0.05);
                padding: 2rem;
                border-radius: 15px;
                text-align: center;
                border: 1px solid rgba(30, 144, 255, 0.3);
                transition: all 0.4s;
                backdrop-filter: blur(10px);
                position: relative;
                overflow: hidden;
            }

            .gallery-item::before {
                content: '';
                position: absolute;
                top: 0;
                left: -100%;
                width: 100%;
                height: 100%;
                background: linear-gradient(90deg, transparent, rgba(30, 144, 255, 0.2), transparent);
                transition: left 0.6s;
            }

            .gallery-item:hover::before {
                left: 100%;
            }

            .gallery-item:hover {
                border-color: var(--blue);
                transform: scale(1.08) rotate(2deg);
                box-shadow: 0 15px 30px rgba(30, 144, 255, 0.3);
            }

            .footer {
                background: rgba(10, 10, 10, 0.95);
                padding: 4rem 0;
                text-align: center;
                border-top: 3px solid transparent;
                border-image: linear-gradient(45deg, var(--purple), var(--blue)) 1;
                position: relative;
            }

            .footer::before {
                content: '';
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background: radial-gradient(circle at center, rgba(138, 43, 226, 0.1) 0%, transparent 70%);
            }
        </style>
    </head>
    <body>
        <!-- الهيدر -->
        <header class="header">
            <div class="container nav-container">
                <div class="logo">أبناء مقراني</div>
                <ul class="nav-links">
                    <li><a href="#home">الرئيسية</a></li>
                    <li><a href="#services">خدماتنا</a></li>
                    <li><a href="#gallery">معرض الأعمال</a></li>
                    <li><a href="#contact">اتصل بنا</a></li>
                </ul>
            </div>
        </header>

        <!-- الهيرو مع صورتك -->
        <section class="hero" id="home">
            <div class="container">
                <h1>أبناء مقراني</h1>
                <p>التميز التكنولوجي meets الحرفية اليدوية - مستقبل الخدمات المتكاملة</p>
                <a href="#services" class="btn">اكتشف عالمنا التكنولوجي</a>
            </div>
        </section>

        <!-- الخدمات -->
        <section class="services" id="services">
            <div class="container">
                <h2 class="section-title">خدماتنا التكنولوجية المتكاملة</h2>
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

        <!-- معرض الأعمال -->
        <section class="gallery" id="gallery">
            <div class="container">
                <h2 class="section-title">إبداعاتنا التكنولوجية</h2>
                <div class="gallery-grid">
                    <div class="gallery-item">🛏️ ديكور ذكي لغرف النوم</div>
                    <div class="gallery-item">🍽️ مطابخ ذكية متكاملة</div>
                    <div class="gallery-item">📚 أنظمة تخزين ذكية</div>
                    <div class="gallery-item">🚪 حلول أمنية تكنولوجية</div>
                    <div class="gallery-item">🛋️ أثاث ذكي متفاعل</div>
                    <div class="gallery-item">🎨 تحف فنية رقمية</div>
                </div>
            </div>
        </section>

        <!-- اتصل بنا -->
        <section class="services" id="contact">
            <div class="container">
                <h2 class="section-title">التواصل التكنولوجي</h2>
                <div style="text-align: center; padding: 3rem; background: rgba(255,255,255,0.05); border-radius: 20px; backdrop-filter: blur(10px);">
                    <p style="font-size: 1.3rem; margin-bottom: 1.5rem;">📞 <strong>الخط الساخن:</strong> 05X-XXX-XXXX</p>
                    <p style="font-size: 1.3rem; margin-bottom: 1.5rem;">📍 <strong>المركز التكنولوجي:</strong> المملكة العربية السعودية</p>
                    <p style="font-size: 1.3rem; margin-bottom: 1.5rem;">⏰ <strong>الدعم الفني:</strong> 24/7</p>
                </div>
            </div>
        </section>

        <!-- الفوتر -->
        <footer class="footer">
            <div class="container">
                <p style="font-size: 1.2rem;">© 2024 أبناء مقراني - قمة التميز التكنولوجي - جميع الحقوق محفوظة</p>
            </div>
        </footer>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
