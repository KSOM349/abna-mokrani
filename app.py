from flask import Flask, render_template_string

app = Flask(__name__)

html_code = '''
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

        /* تأثير الخطوط العنكبوتية */
        body::before {
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: 
                linear-gradient(90deg, var(--dark) 21px, transparent 1%) center,
                linear-gradient(var(--dark) 21px, transparent 1%) center,
                var(--purple);
            background-size: 22px 22px;
            opacity: 0.1;
            z-index: -1;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }

        /* الهيدر */
        .header {
            background: rgba(10, 10, 10, 0.9);
            backdrop-filter: blur(10px);
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
            text-shadow: 0 0 10px rgba(255, 215, 0, 0.3);
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
            text-shadow: 0 0 10px var(--gold);
        }

        /* الهيرو */
        .hero {
            padding: 200px 0 100px;
            text-align: center;
            background: linear-gradient(135deg, rgba(138, 43, 226, 0.1), rgba(30, 144, 255, 0.1));
            position: relative;
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
            box-shadow: 0 5px 15px rgba(138, 43, 226, 0.4);
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
            backdrop-filter: blur(10px);
        }

        .service-card:hover {
            transform: translateY(-10px);
            border-color: var(--gold);
            box-shadow: 0 10px 30px rgba(255, 215, 0, 0.2);
        }

        .service-icon {
            font-size: 3rem;
            margin-bottom: 1rem;
            color: var(--gold);
        }

        /* معرض الصور */
        .gallery {
            padding: 100px 0;
        }

        .gallery-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 1rem;
        }

        .gallery-item {
            background: rgba(255, 255, 255, 0.05);
            padding: 2rem;
            border-radius: 10px;
            text-align: center;
            border: 1px solid rgba(30, 144, 255, 0.3);
            transition: all 0.3s;
        }

        .gallery-item:hover {
            border-color: var(--blue);
            transform: scale(1.05);
        }

        /* الفوتر */
        .footer {
            background: rgba(10, 10, 10, 0.9);
            padding: 3rem 0;
            text-align: center;
            border-top: 2px solid var(--purple);
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

    <!-- الهيرو -->
    <section class="hero" id="home">
        <div class="container">
            <h1>أبناء مقراني</h1>
            <p>نحو مستقبل تقني متطور - جودة لا تضاهى</p>
            <a href="#services" class="btn">اكتشف خدماتنا</a>
        </div>
    </section>

    <!-- الخدمات -->
    <section class="services" id="services">
        <div class="container">
            <h2 class="section-title">خدماتنا المتكاملة</h2>
            <div class="services-grid">
                <div class="service-card">
                    <div class="service-icon">🛋️</div>
                    <h3>الأثاث والديكور</h3>
                    <p>تصميم وتصنيع أثاث مخصص بديكورات فاخرة</p>
                </div>
                <div class="service-card">
                    <div class="service-icon">❄️</div>
                    <h3>الثلاجات والتبريد</h3>
                    <p>بيع وصيانة جميع أجهزة التبريد</p>
                </div>
                <div class="service-card">
                    <div class="service-icon">🚜</div>
                    <h3>المعدات الزراعية</h3>
                    <p>معدات زراعية حديثة وقطع غيار</p>
                </div>
                <div class="service-card">
                    <div class="service-icon">🏘️</div>
                    <h3>تأجير العقارات</h3>
                    <p>شقق ومحلات تجارية ومستودعات</p>
                </div>
            </div>
        </div>
    </section>

    <!-- معرض الأعمال -->
    <section class="gallery" id="gallery">
        <div class="container">
            <h2 class="section-title">معرض أعمالنا</h2>
            <div class="gallery-grid">
                <div class="gallery-item">🛏️ ديكور غرف نوم</div>
                <div class="gallery-item">🍽️ مطابخ مخصصة</div>
                <div class="gallery-item">📚 مكتبات خشبية</div>
                <div class="gallery-item">🚪 أبواب ونوافذ</div>
                <div class="gallery-item">🛋️ كراسي وطاولات</div>
                <div class="gallery-item">🎨 أعمال فنية</div>
            </div>
        </div>
    </section>

    <!-- اتصل بنا -->
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

    <!-- الفوتر -->
    <footer class="footer">
        <div class="container">
            <p>© 2024 أبناء مقراني - جميع الحقوق محفوظة</p>
        </div>
    </footer>
</body>
</html>
'''

@app.route('/')
def home():
    return html_code

if __name__ == '__main__':
    app.run(debug=True)
