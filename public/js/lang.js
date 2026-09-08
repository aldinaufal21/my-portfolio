const translations = {
    en: {
        "nav.home": "Home",
        "nav.about": "About Me",
        "nav.client": "My Clients",
        "nav.contact": "Contact",

        "hero.greet": "Hello Everyone 👋, I am",
        "hero.role1": "I am a",
        "hero.role2": "Backend Developer!",
        "hero.desc": "Eat, Sleep, Code, Music, Repeat <span class=\"text-dark font-semibold\">;</span>",
        "hero.btn": "View my CV",

        "about.subtitle": "About Me",
        "about.title": "Let's get to know me better!",
        "about.desc": "I am a web developer specializing as a Backend Developer who loves crafting robust system architectures. I am highly familiar with server-side languages like Golang and PHP, as well as frameworks such as Laravel and frontend tools like Vue.js. I enjoy learning new cloud technologies, optimizing databases, and integrating AI-based services into my projects. I enjoy reading articles and listening to music in my free time.",
        "about.social": "My Social Media",
        "about.social_desc": "To know me is to love me, let's explore more!",

        "port.subtitle": "Portfolio",
        "port.title": "Latest Projects",
        "port.desc": "Some of the projects I have built during my time as a Web Developer!",
        "port.ekopz_desc": "Ekopz.id company profile web application using HTML, CSS, JS.",
        "port.startup_desc": "Startuphub.id company profile web application using HTML, CSS, JS, Wordpress.",
        "port.juki_desc": "Juki (Juragan Kios) e-commerce application using HTML, CSS, JS, Wordpress.",
        "port.smespos_desc": "Smespos.id e-commerce application using HTML, CSS, JS, Vue, and Laravel for the backend.",
        "port.puskesmas_title": "Puskesmas Activity Management Application",
        "port.puskesmas_desc": "Application for managing queue activities and examinations at a puskesmas using HTML, CSS, JS, and Laravel.",
        "port.koperasi_title": "Cooperative Accounting Application",
        "port.koperasi_desc": "Online cooperative accounting management application using HTML, CSS, JS, and Laravel.",
        "port.pengaduan_title": "Public Complaint Application",
        "port.pengaduan_desc": "Application for managing community reports or complaints using HTML, CSS, JS, and Laravel.",

        "client.subtitle": "Clients",
        "client.title": "Those who have collaborated",
        "client.desc": "Some companies or individuals who have worked with me to build and manage applications.",

        "contact.subtitle": "Contact",
        "contact.title": "Contact Me",
        "contact.desc": "Have an interesting project or want to collaborate? Don't hesitate to reach out!",
        "contact.name": "Name",
        "contact.email": "Email",
        "contact.msg": "Message",
        "contact.send": "Send Message",

        "footer.subtitle": "Web Developer",
        "footer.link_title": "Links",
        "footer.made_with": "Made with ❤️ by Aldy Naufal",
        "footer.used_framework": " use",
        "footer.framework_name": " Tailwind CSS",

        "cv.back": "&larr; Back",
        "cv.back_home": "Back to Home",
        "cv.download_pdf": "Download PDF"
    },
    id: {
        "nav.home": "Beranda",
        "nav.about": "Tentang Saya",
        "nav.client": "Klien Saya",
        "nav.contact": "Kontak",

        "hero.greet": "Hallo Semua 👋, saya",
        "hero.role1": "Saya",
        "hero.role2": "Backend Developer!",
        "hero.desc": "Eat, Sleep, Code, Music, Repeat <span class=\"text-dark font-semibold\">;</span>",
        "hero.btn": "Lihat CV saya",

        "about.subtitle": "Tentang Saya",
        "about.title": "Mari berkenalan dengan saya lebih dalam!",
        "about.desc": "Saya web developer spesialis di bagian backend yang hobi ngebangun arsitektur sistem yang robust. Keseharian saya lumayan akrab sama bahasa server-side kayak Golang dan PHP, framework Laravel, sampai frontend tools seperti Vue.js. Saya juga selalu excited buat belajar teknologi cloud terbaru, ngulik optimasi database, dan masangin fitur-fitur AI ke dalam project saya. Saya menikmati membaca artikel dan mendengarkan musik di waktu luang saya.",
        "about.social": "Sosial Media Saya",
        "about.social_desc": "Tak kenal maka tak sayang, mari lihat diri saya lebih jauh!",

        "port.subtitle": "Portofolio",
        "port.title": "Project Terbaru",
        "port.desc": "Beberapa project yang telah saya buat selama saya menjadi Web Developer!",
        "port.ekopz_desc": "Aplikasi web company profile Ekopz.id menggunakan html, css, js.",
        "port.startup_desc": "Aplikasi web company profile startuphub.id menggunakan html, css, js, wordpress.",
        "port.juki_desc": "Aplikasi e-commerce juki (Juragan Kios) menggunakan html, css, js, wordpress.",
        "port.smespos_desc": "Aplikasi e-commerce smespos.id menggunakan html, css, js, vue, dan laravel sebagai backend nya.",
        "port.puskesmas_title": "Aplikasi pengelolaan kegiatan puskesmas",
        "port.puskesmas_desc": "Aplikasi pengelolaan kegiatan antrian dan pemeriksaan pada puskesmas menggunakan html, css, js dan laravel.",
        "port.koperasi_title": "Aplikasi Pembukuan Koperasi",
        "port.koperasi_desc": "Aplikasi pengelolaan pembukuan koperasi secara online menggunakan html, css, js dan laravel.",
        "port.pengaduan_title": "Aplikasi Pengaduan Masyarakat",
        "port.pengaduan_desc": "Aplikasi untuk mengelola laporan atau keluhan masyarakat menggunakan html, css, js dan laravel.",

        "client.subtitle": "Klien",
        "client.title": "Yang Pernah Bekerjasama",
        "client.desc": "Beberapa perusahaan atau perorangan yang pernah bekerjasama dengan saya untuk membangun dan mengelola aplikasi.",

        "contact.subtitle": "Kontak",
        "contact.title": "Hubungi Saya",
        "contact.desc": "Punya project menarik atau ingin berkolaborasi? Jangan ragu untuk menghubungi saya!",
        "contact.name": "Nama",
        "contact.email": "Email",
        "contact.msg": "Pesan",
        "contact.send": "Kirim Pesan",

        "footer.subtitle": "Web Developer",
        "footer.link_title": "Tautan",
        "footer.made_with": "Dibuat dengan ❤️ oleh Aldy Naufal",
        "footer.used_framework": " menggunakan",
        "footer.framework_name": " Tailwind CSS",

        "cv.back": "&larr; Kembali",
        "cv.back_home": "Kembali ke Beranda",
        "cv.download_pdf": "Unduh PDF"
    }
};

let currentLang = localStorage.getItem('lang') || 'en';

function applyTranslations(lang) {
    document.querySelectorAll('[data-i18n]').forEach(el => {
        const key = el.getAttribute('data-i18n');
        if (translations[lang] && translations[lang][key]) {
            el.innerHTML = translations[lang][key];
        }
    });

    // Handle language toggle button states if they exist
    const btnEn = document.getElementById('btn-lang-en');
    const btnId = document.getElementById('btn-lang-id');

    if (btnEn && btnId) {
        if (lang === 'en') {
            btnEn.classList.add('font-bold', 'text-primary');
            btnEn.classList.remove('text-secondary', 'font-medium');
            btnId.classList.remove('font-bold', 'text-primary');
            btnId.classList.add('text-secondary', 'font-medium');
        } else {
            btnId.classList.add('font-bold', 'text-primary');
            btnId.classList.remove('text-secondary', 'font-medium');
            btnEn.classList.remove('font-bold', 'text-primary');
            btnEn.classList.add('text-secondary', 'font-medium');
        }
    }
}

function setLanguage(lang) {
    currentLang = lang;
    localStorage.setItem('lang', lang);
    applyTranslations(lang);

    // Custom event to notify other scripts (like CV loader)
    document.dispatchEvent(new CustomEvent('languageChanged', { detail: lang }));
}

document.addEventListener('DOMContentLoaded', () => {
    applyTranslations(currentLang);

    const btnEn = document.getElementById('btn-lang-en');
    const btnId = document.getElementById('btn-lang-id');

    if (btnEn) {
        btnEn.addEventListener('click', (e) => {
            e.preventDefault();
            setLanguage('en');
        });
    }

    if (btnId) {
        btnId.addEventListener('click', (e) => {
            e.preventDefault();
            setLanguage('id');
        });
    }
});
