// ===== ТЁМНАЯ/СВЕТЛАЯ ТЕМА =====
function toggleTheme() {
    const body = document.body;
    const icon = document.getElementById('themeIcon');
    
    if (body.classList.contains('dark-mode')) {
        body.classList.remove('dark-mode');
        body.classList.add('light-mode');
        icon.className = 'fas fa-moon';
        localStorage.setItem('theme', 'light');
    } else {
        body.classList.remove('light-mode');
        body.classList.add('dark-mode');
        icon.className = 'fas fa-sun';
        localStorage.setItem('theme', 'dark');
    }
}

// Применяем сохранённую тему
const savedTheme = localStorage.getItem('theme');
if (savedTheme === 'dark') {
    document.body.classList.add('dark-mode');
    document.body.classList.remove('light-mode');
    const icon = document.getElementById('themeIcon');
    if (icon) icon.className = 'fas fa-sun';
}

// ===== ПЕРЕКЛЮЧАТЕЛЬ ЯЗЫКА =====
function toggleLang() {
    const dropdown = document.getElementById('langDropdown');
    dropdown.classList.toggle('show');
}

// Закрыть dropdown если кликнули вне
document.addEventListener('click', function(e) {
    const switcher = document.querySelector('.lang-switcher');
    if (switcher && !switcher.contains(e.target)) {
        document.getElementById('langDropdown').classList.remove('show');
    }
});