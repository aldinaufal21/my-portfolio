import re
import codecs

def update_file():
    with codecs.open('public/index.html', 'r', 'utf-8') as f:
        content = f.read()

    # 1. Update cv link
    content = content.replace('href="cv.html"', 'href="/public/cv.html"')

    # 2. Add language toggle to header
    header_toggle = """<div class="hidden lg:flex mr-6 items-center bg-slate-100 rounded-full px-3 py-1 border border-slate-200">
                    <button id="btn-lang-en" class="font-bold text-primary text-sm focus:outline-none">EN</button>
                    <span class="mx-2 text-slate-300">|</span>
                    <button id="btn-lang-id" class="text-secondary font-medium text-sm focus:outline-none hover:text-primary transition-colors">ID</button>
                </div>"""
    
    hamburger_tag = '<button id="hamburger"'
    content = content.replace(hamburger_tag, header_toggle + '\n                ' + hamburger_tag)

    # 3. Add mobile toggle to nav
    mobile_toggle = """<li class="group lg:hidden flex justify-center mb-4">
                            <!-- Mobile Language Toggle -->
                            <div class="flex items-center bg-slate-100 rounded-full px-3 py-1 border border-slate-200">
                                <button id="btn-lang-en-mob" class="font-bold text-primary text-sm focus:outline-none">EN</button>
                                <span class="mx-2 text-slate-300">|</span>
                                <button id="btn-lang-id-mob" class="text-secondary font-medium text-sm focus:outline-none hover:text-primary transition-colors">ID</button>
                            </div>
                        </li>"""
    
    ul_tag = '<ul class="block lg:flex">'
    content = content.replace(ul_tag, ul_tag + '\n                        ' + mobile_toggle)

    # 4. Include lang.js at the end
    script_tag = '<script src="../src/js/script.js">'
    content = content.replace(script_tag, '<script src="/public/js/lang.js"></script>\n\n    ' + script_tag)

    # Now let's carefully add data-i18n tags and change text
    
    replacements = [
        # Nav
        (r'<a href="#home"\s*class="text-base text-dark py-2 mx-6 flex group-hover:text-primary">Beranda</a>',
         r'<a href="#home" class="text-base text-dark py-2 mx-6 flex group-hover:text-primary" data-i18n="nav.home">Home</a>'),
        (r'<a href="#about" class="text-base text-dark py-2 mx-6 flex group-hover:text-primary">Tentang Saya</a>',
         r'<a href="#about" class="text-base text-dark py-2 mx-6 flex group-hover:text-primary" data-i18n="nav.about">About Me</a>'),
        (r'<a href="#client" class="text-base text-dark py-2 mx-6 flex group-hover:text-primary">Klien Saya</a>',
         r'<a href="#client" class="text-base text-dark py-2 mx-6 flex group-hover:text-primary" data-i18n="nav.client">My Clients</a>'),
        (r'<a href="#contact"\s*class="text-base text-dark py-2 mx-6 flex group-hover:text-primary">Kontak</a>',
         r'<a href="#contact" class="text-base text-dark py-2 mx-6 flex group-hover:text-primary" data-i18n="nav.contact">Contact</a>'),

        # Hero
        (r'Halo Semua 👋, Saya', r'<span data-i18n="hero.greet">Hello Everyone 👋, I am</span>'),
        (r'Saya Seorang', r'<span data-i18n="hero.role1">I am a</span>'),
        (r'<span class="text-dark">Web Developer!</span>', r'<span class="text-dark" data-i18n="hero.role2">Web Developer!</span>'),
        (r'Makan, Tidur, Ngoding, Musik, Ulangi', r'<span data-i18n="hero.desc">Eat, Sleep, Code, Music, Repeat</span>'),
        (r'class="text-base font-semibold text-white bg-primary py-3 px-8 rounded-full hover:shadow-lg hover:opacity-80 transition duration-300 ease-in-out">Lihat CV Saya</a>',
         r'class="text-base font-semibold text-white bg-primary py-3 px-8 rounded-full hover:shadow-lg hover:opacity-80 transition duration-300 ease-in-out" data-i18n="hero.btn">View my CV</a>'),

        # About
        (r'<h4 class="font-bold uppercase text-primary text-lg mb-3">Tentang Saya</h4>',
         r'<h4 class="font-bold uppercase text-primary text-lg mb-3" data-i18n="about.subtitle">About Me</h4>'),
        (r'<h2 class="font-bold text-dark text-3xl mb-5 max-w-md lg:text-4xl">Mari kenal saya lebih dekat!</h2>',
         r'<h2 class="font-bold text-dark text-3xl mb-5 max-w-md lg:text-4xl" data-i18n="about.title">Let\'s get to know me better!</h2>'),
        (r'<p class="font-medium text-base text-secondary max-w-xl lg:text-lg">Saya merupakan seorang web developer dengan spesialisasi sebagai fullstack developer yang memiliki minat besar dalam mempelajari hal-hal baru. Saya familiar dengan beberapa framework PHP seperti Laravel dan juga framework javascript seperti Vue Js. Saya menikmati membaca artikel dan mendengarkan musik di waktu luang.</p>',
         r'<p class="font-medium text-base text-secondary max-w-xl lg:text-lg" data-i18n="about.desc">I am a web developer specializing as a fullstack developer with a strong passion for learning new things. I am familiar with several PHP frameworks including Laravel and also javascript frameworks like Vue Js. I enjoy reading articles and listening to music in my free time.</p>'),
        (r'<h3 class="font-semibold text-dark text-2xl mb-4 lg:pt-12">Sosial Media Saya</h3>',
         r'<h3 class="font-semibold text-dark text-2xl mb-4 lg:pt-12" data-i18n="about.social">My Social Media</h3>'),
        (r'<p class="font-medium text-base text-secondary mb-6 lg:text-lg">Tak kenal maka tak sayang, mari eksplor lebih jauh</p>',
         r'<p class="font-medium text-base text-secondary mb-6 lg:text-lg" data-i18n="about.social_desc">To know me is to love me, let\'s explore more!</p>'),

        # Portfolio
        (r'<h4 class="font-semibold text-lg text-primary mb-2">Portofolio</h4>',
         r'<h4 class="font-semibold text-lg text-primary mb-2" data-i18n="port.subtitle">Portfolio</h4>'),
        (r'<h2 class="font-bold text-dark text-3xl mb-4 sm:text-4xl lg:text-5xl">Proyek Terbaru</h2>',
         r'<h2 class="font-bold text-dark text-3xl mb-4 sm:text-4xl lg:text-5xl" data-i18n="port.title">Latest Projects</h2>'),
        (r'<p class="font-medium px-3 pb-3 text-md text-secondary md:text-lg">Beberapa poyek yang telah saya bangun selama saya menjadi Web Developer!</p>',
         r'<p class="font-medium px-3 pb-3 text-md text-secondary md:text-lg" data-i18n="port.desc">Some of the projects I have built during my time as a Web Developer!</p>'),
        
        (r'<p class="font-medium px-3 pb-3 text-base text-secondary">Aplikasi web company profile Ekopz.id menggunakan HTML, CSS, JS.</p>',
         r'<p class="font-medium px-3 pb-3 text-base text-secondary" data-i18n="port.ekopz_desc">Ekopz.id company profile web application using HTML, CSS, JS.</p>'),
        
        (r'<p class="font-medium px-3 pb-3 text-base text-secondary">Aplikasi web company profile startuphub.id menggunakan HTML, CSS, JS, Wordpress.</p>',
         r'<p class="font-medium px-3 pb-3 text-base text-secondary" data-i18n="port.startup_desc">Startuphub.id company profile web application using HTML, CSS, JS, Wordpress.</p>'),
         
        (r'<a href="#" target="_blank">Aplikasi E-commerce Juki</a>',
         r'<a href="#" target="_blank" data-i18n="port.juki_title">Juki E-commerce Application</a>'),
        (r'<p class="font-medium px-3 pb-3 text-base text-secondary">Aplikasi e-commerce Juki \(Juragan Kios\) menggunakan HTML, CSS, JS, Wordpress.</p>',
         r'<p class="font-medium px-3 pb-3 text-base text-secondary" data-i18n="port.juki_desc">Juki (Juragan Kios) e-commerce application using HTML, CSS, JS, Wordpress.</p>'),
         
        (r'<a href="#" target="_blank">Aplikasi E-commerce Smespos.id</a>',
         r'<a href="#" target="_blank" data-i18n="port.smespos_title">Smespos.id E-commerce Application</a>'),
        (r'<p class="font-medium px-3 pb-3 text-base text-secondary">Aplikasi e-commerce Smespos.id menggunakan HTML, CSS, JS, vue dan laravel untuk backendnya.</p>',
         r'<p class="font-medium px-3 pb-3 text-base text-secondary" data-i18n="port.smespos_desc">Smespos.id e-commerce application using HTML, CSS, JS, Vue, and Laravel for the backend.</p>'),
         
        (r'<a href="#" target="_blank">Aplikasi Manajemen Kegiatan Puskesmas</a>',
         r'<a href="#" target="_blank" data-i18n="port.puskesmas_title">Puskesmas Activity Management Application</a>'),
        (r'<p class="font-medium px-3 pb-3 text-base text-secondary">Aplikasi pengelolaan kegiatan antrean hingga pemeriksaan pada puskesmas menggunakan HTML, CSS, JS dan Laravel.</p>',
         r'<p class="font-medium px-3 pb-3 text-base text-secondary" data-i18n="port.puskesmas_desc">Application for managing queue activities and examinations at a puskesmas using HTML, CSS, JS, and Laravel.</p>'),
         
        (r'<a href="#" target="_blank">Aplikasi Akuntansi Koperasi</a>',
         r'<a href="#" target="_blank" data-i18n="port.koperasi_title">Cooperative Accounting Application</a>'),
        (r'<p class="font-medium px-3 pb-3 text-base text-secondary">Aplikasi manajemen akuntansi koperasi online menggunakan HTML, CSS, JS dan Laravel.</p>',
         r'<p class="font-medium px-3 pb-3 text-base text-secondary" data-i18n="port.koperasi_desc">Online cooperative accounting management application using HTML, CSS, JS, and Laravel.</p>'),

        # Clients
        (r'<h4 class="font-semibold text-lg text-primary mb-2">Klien</h4>',
         r'<h4 class="font-semibold text-lg text-primary mb-2" data-i18n="client.subtitle">Clients</h4>'),
        (r'<h2 class="font-bold text-white text-3xl mb-4 sm:text-4xl lg:text-5xl">Yang Pernah Bekerjasama</h2>',
         r'<h2 class="font-bold text-white text-3xl mb-4 sm:text-4xl lg:text-5xl" data-i18n="client.title">Those who have collaborated</h2>'),
        (r'<p class="font-medium px-3 pb-3 text-md text-secondary md:text-lg">Beberapa perusahaan atau individu yang pernah bekerjasama dengan saya untuk membangun dan mengelola aplikasi</p>',
         r'<p class="font-medium px-3 pb-3 text-md text-secondary md:text-lg" data-i18n="client.desc">Some companies or individuals who have worked with me to build and manage applications.</p>'),

        # Contact
        (r'<h4 class="font-semibold text-lg text-primary mb-2">Kontak</h4>',
         r'<h4 class="font-semibold text-lg text-primary mb-2" data-i18n="contact.subtitle">Contact</h4>'),
        (r'<h2 class="font-bold text-dark text-3xl mb-4 sm:text-4xl lg:text-5xl">Hubungi Saya</h2>',
         r'<h2 class="font-bold text-dark text-3xl mb-4 sm:text-4xl lg:text-5xl" data-i18n="contact.title">Contact Me</h2>'),
        (r'<p class="font-medium px-3 pb-3 text-md text-secondary md:text-lg">Punya proyek menarik atau ingin berkolaborasi? jangan ragu untuk menghubungi!</p>',
         r'<p class="font-medium px-3 pb-3 text-md text-secondary md:text-lg" data-i18n="contact.desc">Have an interesting project or want to collaborate? Don\'t hesitate to reach out!</p>'),
        
        (r'<label for="name" class="text-base text-primary font-bold">Nama</label>',
         r'<label for="name" class="text-base text-primary font-bold" data-i18n="contact.name">Name</label>'),
        (r'<label for="message" class="text-base text-primary font-bold">Pesan</label>',
         r'<label for="message" class="text-base text-primary font-bold" data-i18n="contact.msg">Message</label>'),
        (r'Kirim Pesan</button>',
         r'Send Message</button>'),
        (r'class="text-base font-semibold text-white bg-primary py-3 px-8 rounded-full w-full hover:opacity-80 hover:shadow-lg transition duration-500">Send Message',
         r'class="text-base font-semibold text-white bg-primary py-3 px-8 rounded-full w-full hover:opacity-80 hover:shadow-lg transition duration-500" data-i18n="contact.send">Send Message'),

        # Footer
        (r'<h3 class="font-bold text-2xl mb-2">Hubungi Kami</h3>',
         r'<h3 class="font-bold text-2xl mb-2" data-i18n="contact.title">Contact Me</h3>'),
        (r'<h3 class="font-semibold text-xl text-white mb-5 ">Tautan</h3>',
         r'<h3 class="font-semibold text-xl text-white mb-5 " data-i18n="footer.link_title">Links</h3>'),
        (r'<li><a href="#home" class="inline-block text-base hover:text-primary mb-3">Beranda</a></li>',
         r'<li><a href="#home" class="inline-block text-base hover:text-primary mb-3" data-i18n="nav.home">Home</a></li>'),
        (r'<li><a href="#about" class="inline-block text-base hover:text-primary mb-3">Tentang Saya</a>',
         r'<li><a href="#about" class="inline-block text-base hover:text-primary mb-3" data-i18n="nav.about">About Me</a>'),
        (r'<li><a href="#portofolio" class="inline-block text-base hover:text-primary mb-3">Portofolio</a>',
         r'<li><a href="#portofolio" class="inline-block text-base hover:text-primary mb-3" data-i18n="port.subtitle">Portfolio</a>'),
        (r'<li><a href="#client" class="inline-block text-base hover:text-primary mb-3">Klien Saya</a></li>',
         r'<li><a href="#client" class="inline-block text-base hover:text-primary mb-3" data-i18n="client.subtitle">Clients</a></li>'),
        (r'<li><a href="#contact" class="inline-block text-base hover:text-primary mb-3">Kontak</a></li>',
         r'<li><a href="#contact" class="inline-block text-base hover:text-primary mb-3" data-i18n="contact.subtitle">Contact</a></li>'),
         
        (r'Dibuat dengan ❤️ oleh',
         r'<span data-i18n="footer.made_with">Made with ❤️ by</span>'),
    ]

    for old, new in replacements:
        content = re.sub(old, new, content)
        
    with codecs.open('public/index.html', 'w', 'utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    update_file()
