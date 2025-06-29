// VARIABLES
var root = document.querySelector(':root');
var rootStyle = getComputedStyle(root);
var today = document.getElementById('today');
var target_date_time = document.getElementById('target_date_time');
var add_section = document.getElementById('add_section');
var edit_section = document.getElementById('edit_section');
var edit_title = document.getElementById('edit_title');
var edit_content = document.getElementById('edit_content');
var edit_target_date_time = document.getElementById('edit_target_date_time');
var edit_form = document.getElementById('edit_form');

// MAIN 
Main();
function Main() {
    if (today) today.innerHTML = getCurrentDate();
    if (target_date_time) {
        const now = new Date();
        now.setMinutes(now.getMinutes() - now.getTimezoneOffset());
        target_date_time.value = now.toISOString().slice(0, 16);
    }
}

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
    if (add_section) {
        add_section.style.opacity = 1;
        add_section.style.visibility = 'visible';
    }
}
function on_edit_click(item_pk, target, url) {
    if (edit_section && edit_title && edit_content && edit_target_date_time && edit_form) {
        edit_section.style.opacity = 1;
        edit_section.style.visibility = 'visible';
        edit_title.value = document.getElementById('title_' + item_pk).innerHTML;
        edit_content.value = document.getElementById('content_' + item_pk).innerHTML;
        edit_target_date_time.value = target;
        edit_form.action = url;
    }
}
function on_close_click() {
    if (add_section) {
        add_section.style.opacity = 0;
        add_section.style.visibility = 'hidden';
    }
    if (edit_section) {
        edit_section.style.opacity = 0;
        edit_section.style.visibility = 'hidden';
    }
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