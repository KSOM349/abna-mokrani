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

        /* باقي الكود CSS... */
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

    <!-- باقي كود HTML... -->
</body>
</html>
'''

@app.route('/')
def home():
    return html_code

if __name__ == '__main__':
    app.run(debug=True)