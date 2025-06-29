// VARIABLES
var root = document.querySelector(':root');
var rootStyle = getComputedStyle(root);

// THEME MANAGEMENT
let currentTheme = localStorage.getItem('theme') || 'light';

// MAIN 
Main();
function Main() {
    // Initialize theme
    setTheme(currentTheme);

    const now = new Date();
    now.setMinutes(now.getMinutes() - now.getTimezoneOffset());
    target_date_time.value = now.toISOString().slice(0, 16);
}

// Theme Functions
function setTheme(theme) {
    const themeIcon = document.getElementById('theme-icon');
    const themeToggle = document.getElementById('theme-toggle');

    if (theme === 'dark') {
        document.body.classList.add('dark-theme');
        if (themeIcon) {
            themeIcon.className = 'fa fa-sun';
        }
        if (themeToggle) {
            themeToggle.title = 'Switch to light mode';
        }
    } else {
        document.body.classList.remove('dark-theme');
        if (themeIcon) {
            themeIcon.className = 'fa fa-moon';
        }
        if (themeToggle) {
            themeToggle.title = 'Switch to dark mode';
        }
    }

    currentTheme = theme;
    localStorage.setItem('theme', theme);
}

function toggleTheme() {
    const newTheme = currentTheme === 'light' ? 'dark' : 'light';
    setTheme(newTheme);
}

// Check for system preference
function checkSystemTheme() {
    if (localStorage.getItem('theme') === null) {
        const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
        setTheme(prefersDark ? 'dark' : 'light');
    }
}

// Listen for system theme changes
window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', e => {
    if (localStorage.getItem('theme') === null) {
        setTheme(e.matches ? 'dark' : 'light');
    }
});

// Initialize theme on page load
document.addEventListener('DOMContentLoaded', function () {
    checkSystemTheme();
});

// Static Functions
function getCurrentDate() {
    var date = new Date();
    var dd = String(date.getDate()).padStart(2, '0');
    var mm = String(date.getMonth() + 1).padStart(2, '0'); //January is 0!
    var yyyy = date.getFullYear();
    var today = mm + '/' + dd + '/' + yyyy;
    return today;
}

// On Click Events
function on_add_click() {
    add_section.style.opacity = 1;
    add_section.style.visibility = 'visible';
}
function on_edit_click(item_pk, target, url) {
    edit_section.style.opacity = 1;
    edit_section.style.visibility = 'visible';
    edit_title.value = document.getElementById('title_' + item_pk).innerHTML;
    edit_content.value = document.getElementById('content_' + item_pk).innerHTML;
    edit_target_date_time.value = target;
    edit_form.action = url;
}
function on_close_click() {
    add_section.style.opacity = 0;
    add_section.style.visibility = 'hidden';
    edit_section.style.opacity = 0;
    edit_section.style.visibility = 'hidden';
}
function on_item_click(item) {
    if (item.style.opacity != 0) {
        item.style.margin = 0;
        item.style.fontSize = 0;
        item.style.height = 0;
        item.style.opacity = 0;
        item.style.visibility = 'hidden';
    }
    else {
        item.style.opacity = 1;
        item.style.height = 'auto';
        item.style.fontSize = rootStyle.getPropertyValue('--expand_font');
        item.style.margin = rootStyle.getPropertyValue('--expand_margin');
        item.style.visibility = 'visible';
    }
}
function on_menu_click() {
    if (rootStyle.getPropertyValue('--nav_width') == rootStyle.getPropertyValue('--nav_width_max')) {
        root.style.setProperty('--nav_width', rootStyle.getPropertyValue('--nav_width_min'));
        root.style.setProperty('--nav_font_a', rootStyle.getPropertyValue('--nav_font_a_min'));
    }
    else {
        root.style.setProperty('--nav_width', rootStyle.getPropertyValue('--nav_width_max'));
        root.style.setProperty('--nav_font_a', rootStyle.getPropertyValue('--nav_font_a_max'));
    }
}