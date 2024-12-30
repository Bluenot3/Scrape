<html lang="en">
<base href="https://ZENai.biz/">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ZEN AI Pioneer Program - 26 Week Journey</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

        :root {
            --primary-color: #00b4d8;
            --secondary-color: #90e0ef;
            --accent-color: #ffd60a;
            --bg-color: #03045e;
            --text-color: #ffffff;
            --light-text-color: #caf0f8;
            --card-bg-color: rgba(255, 255, 255, 0.1);
            --card-hover-bg: rgba(255, 255, 255, 0.2);
        }

        body, html {
            margin: 0;
            padding: 0;
            font-family: 'Poppins', sans-serif;
            background-color: var(--bg-color);
            color: var(--text-color);
            scroll-behavior: smooth;
            overflow-x: hidden;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
            position: relative;
            z-index: 2;
        }

        /* Background elements covering the entire page */
        #particles-js, #animated-bg, #svg-animation {
            position: fixed;
            width: 100%;
            height: 100%;
            top: 0;
            left: 0;
            z-index: 0;
            pointer-events: none;
        }

        header {
            position: relative;
            text-align: center;
            padding: 150px 20px;
            color: var(--light-text-color);
        }

        h1 {
            font-size: 4em;
            margin-bottom: 20px;
            text-transform: uppercase;
            letter-spacing: 4px;
            color: #fff;
            text-shadow: 0 0 20px var(--accent-color), 0 0 30px var(--accent-color), 0 0 40px var(--accent-color), 
                         0 0 50px var(--accent-color), 0 0 60px var(--accent-color);
            animation: glow 2s ease-in-out infinite alternate;
        }

        @keyframes glow {
            from {
                text-shadow: 0 0 10px var(--accent-color), 0 0 20px var(--accent-color), 0 0 30px var(--accent-color), 
                             0 0 40px var(--accent-color), 0 0 50px var(--accent-color);
            }
            to {
                text-shadow: 0 0 20px var(--accent-color), 0 0 30px var(--accent-color), 0 0 40px var(--accent-color), 
                             0 0 50px var(--accent-color), 0 0 60px var(--accent-color);
            }
        }

        .tagline {
            font-size: 1.5em;
            margin-bottom: 40px;
        }

        .cta-button {
            display: inline-block;
            padding: 15px 40px;
            background-color: var(--accent-color);
            color: var(--bg-color);
            text-decoration: none;
            border-radius: 50px;
            font-weight: bold;
            position: relative;
            overflow: hidden;
        }

        .cta-button::after {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: var(--primary-color);
            transition: left 0.5s ease;
        }

        .cta-button:hover::after {
            left: 0;
        }

        .cta-button:hover {
            color: var(--text-color);
        }

        .section {
            padding: 80px 0;
            opacity: 0;
            transform: translateY(50px);
            transition: all 1s ease;
        }

        .section.visible {
            opacity: 1;
            transform: translateY(0);
        }

        h2 {
            text-align: center;
            margin-bottom: 60px;
            font-size: 2.5em;
            position: relative;
        }

        h2::after {
            content: '';
            width: 80px;
            height: 4px;
            background: var(--accent-color);
            position: absolute;
            bottom: -15px;
            left: 50%;
            transform: translateX(-50%);
        }

        p {
            font-size: 1.1em;
            line-height: 1.8em;
        }

        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 40px;
        }

        .card {
            background-color: var(--card-bg-color);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 40px 30px;
            text-align: center;
            position: relative;
            overflow: hidden;
            transition: transform 0.5s ease, background 0.5s ease;
        }

        .card:hover {
            transform: translateY(-15px);
            background: var(--card-hover-bg);
        }

        .card-icon {
            font-size: 3em;
            margin-bottom: 20px;
            color: var(--accent-color);
            animation: floatIcon 3s ease-in-out infinite;
        }

        @keyframes floatIcon {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-10px); }
        }

        .module-selector {
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            margin-bottom: 50px;
        }

        .module-button {
            padding: 15px 30px;
            margin: 10px;
            background-color: var(--primary-color);
            color: var(--bg-color);
            border: none;
            border-radius: 30px;
            cursor: pointer;
            position: relative;
            overflow: hidden;
            transition: color 0.5s ease;
        }

        .module-button.active, .module-button:hover {
            color: var(--text-color);
        }

        .module-button::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: var(--accent-color);
            transition: left 0.5s ease;
            z-index: -1;
        }

        .module-button.active::before, .module-button:hover::before {
            left: 0;
        }

        .module-content {
            animation: fadeIn 1s ease;
            background-color: var(--card-bg-color);
            padding: 40px;
            border-radius: 20px;
        }

        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }

        .testimonial {
            background-color: var(--card-bg-color);
            border-radius: 20px;
            padding: 30px;
            margin-bottom: 30px;
            position: relative;
            overflow: hidden;
            color: var(--light-text-color);
            backdrop-filter: blur(10px);
        }

        .testimonial::before {
            content: '“';
            font-family: serif;
            font-size: 8em;
            position: absolute;
            top: -20px;
            left: 20px;
            color: var(--accent-color);
            opacity: 0.2;
        }

        footer {
            text-align: center;
            padding: 40px 0;
            background-color: rgba(0, 0, 0, 0.5);
            position: relative;
            z-index: 2;
        }

        .clubhouse-section {
            background-color: var(--secondary-color);
            color: var(--bg-color);
            padding: 60px 40px;
            border-radius: 30px;
            margin-top: 80px;
            position: relative;
            overflow: hidden;
        }

        .clubhouse-section::before {
            content: '';
            position: absolute;
            top: -10%;
            left: -10%;
            width: 120%;
            height: 120%;
            background: radial-gradient(circle at center, rgba(255, 255, 255, 0.2), transparent);
            animation: pulse 5s infinite;
            z-index: -1;
        }

        @keyframes pulse {
            0%, 100% { transform: scale(1); opacity: 1; }
            50% { transform: scale(1.1); opacity: 0.7; }
        }

        .clubhouse-icon {
            font-size: 5em;
            margin-bottom: 20px;
            color: var(--accent-color);
        }

        ul {
            list-style: none;
            padding-left: 0;
        }

        ul li {
            font-size: 1.1em;
            margin-bottom: 10px;
            position: relative;
            padding-left: 25px;
        }

        ul li::before {
            content: '✓';
            position: absolute;
            left: 0;
            color: var(--accent-color);
        }

        @media (max-width: 768px) {
            h1 {
                font-size: 2.5em;
            }

            .cta-button {
                padding: 12px 25px;
            }

            h2 {
                font-size: 2em;
            }
        }

        @media (max-width: 480px) {
            h1 {
                font-size: 2em;
            }

            .tagline {
                font-size: 1.2em;
            }
        }

        main, footer {
            position: relative;
            z-index: 2;
        }

        /* New background animation */
        @keyframes bgAnimation {
            0% {
                background-position: 0% 50%;
            }
            50% {
                background-position: 100% 50%;
            }
            100% {
                background-position: 0% 50%;
            }
        }

        #animated-bg {
            background: linear-gradient(-45deg, #03045e, #00b4d8, #ffd60a, #023e8a);
            background-size: 400% 400%;
            animation: bgAnimation 30s ease infinite;
            opacity: 0.5;
        }

    </style>
</head>
<body>
    <div id="particles-js"></div>
    <div id="animated-bg"></div>
    <svg id="svg-animation" class="svg-background" viewBox="0 0 800 600" preserveAspectRatio="xMidYMid slice">
        <defs>
            <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="0%">
                <stop offset="0%" style="stop-color:#00b4d8;stop-opacity:1" />
                <stop offset="100%" style="stop-color:#ffd60a;stop-opacity:1" />
            </linearGradient>
        </defs>
        <circle id="circle1" cx="400" cy="300" r="200" fill="url(#grad1)" opacity="0.2">
            <animate attributeName="r" from="150" to="250" dur="10s" repeatCount="indefinite" />
            <animate attributeName="cx" from="200" to="600" dur="20s" repeatCount="indefinite" />
        </circle>
        <polygon id="polygon1" points="400,50 450,150 550,150 475,225 500,325 400,275 300,325 325,225 250,150 350,150" fill="#90e0ef" opacity="0.1">
            <animateTransform attributeName="transform" type="rotate" from="0 400 300" to="360 400 300" dur="40s" repeatCount="indefinite" />
        </polygon>
    </svg>
    <div class="container">
        <header>
            <h1>ZEN AI Pioneer Program</h1>
            <p class="tagline">A 26-Week Journey to AI Mastery</p>
            <a href="https://ZENai.biz/challenge-page/309f3381-40ca-41c6-9b5f-37c5bbeb1b52?programId=309f3381-40ca-41c6-9b5f-37c5bbeb1b52" class="cta-button">Embark on Your AI Adventure</a>
        </header>

        <main>
            <section id="about" class="section">
                <h2>About Our 26-Week Program</h2>
                <p>The ZEN AI Pioneer Program is an intensive, 26-week journey designed to transform beginners into AI professionals. Our comprehensive curriculum spans 14 modules, each carefully crafted to build upon the previous, ensuring a solid foundation and steady progression in AI literacy and skills.</p>
            </section>

            <section id="core-principles" class="section">
                <h2>Core Principles</h2>
                <div class="grid">
                    <div class="card">
                        <div class="card-icon">🤖</div>
                        <h3>Immersive Learning</h3>
                        <p>Dive deep into AI with hands-on projects and real-world applications</p>
                    </div>
                    <div class="card">
                        <div class="card-icon">⚖️</div>
                        <h3>Ethical AI Development</h3>
                        <p>Understand the importance of responsible AI practices and bias mitigation</p>
                    </div>
                    <div class="card">
                        <div class="card-icon">🔄</div>
                        <h3>Continuous Adaptation</h3>
                        <p>Stay current with rapidly evolving AI technologies and methodologies</p>
                    </div>
                    <div class="card">
                        <div class="card-icon">🌍</div>
                        <h3>Global Perspective</h3>
                        <p>Explore AI's impact across industries and cultures worldwide</p>
                    </div>
                </div>
            </section>

            <section id="program-structure" class="section">
                <h2>Program Structure: 14 Comprehensive Modules</h2>
                <p>Our 26-week program is divided into 14 in-depth modules, each designed to build your AI expertise step by step.</p>
                <div class="module-selector">
                    <button class="module-button" onclick="showModule(1)">Module 1-2</button>
                    <button class="module-button" onclick="showModule(2)">Module 3-4</button>
                    <button class="module-button" onclick="showModule(3)">Module 5-6</button>
                    <button class="module-button" onclick="showModule(4)">Module 7-8</button>
                    <button class="module-button" onclick="showModule(5)">Module 9-10</button>
                    <button class="module-button" onclick="showModule(6)">Module 11-12</button>
                    <button class="module-button" onclick="showModule(7)">Module 13-14</button>
                </div>
                <div id="moduleContent">
                    <!-- Module content will be dynamically inserted here -->
                </div>
            </section>

            <section id="clubhouse" class="section clubhouse-section">
                <div class="clubhouse-icon">🏠</div>
                <h2>Clubhouse at Your House</h2>
                <p>Experience the unique ZEN AI Clubhouse atmosphere right in your own home! Our virtual clubhouse creates a collaborative and supportive environment where you can interact with fellow learners, mentors, and AI enthusiasts from around the globe.</p>
                <ul>
                    <li>Weekly virtual meetups and coding sessions</li>
                    <li>AI project showcases and peer reviews</li>
                    <li>Guest lectures from industry experts</li>
                    <li>Networking opportunities with AI professionals</li>
                </ul>
            </section>

        </
