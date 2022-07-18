// DEFAULT VARIABLES
// const item_list = [];
var is_active = false;
var settings = {
    is_loaded: false,
    is_searched: false,
    search_value: "",
    sort_by: "id",
    filter_by: "none"
};

// MAIN 
Main();
function Main()
{
    settings_reader();
    ui_values();
}
function settings_reader()
{
    _settings = JSON.parse(localStorage.getItem("settings")); 
    if (_settings != null)
    {
        settings = _settings;
    }
    else
    { 
        localStorage.setItem("settings", JSON.stringify(settings));
    }
    if (settings.is_loaded)
    {
        settings.is_loaded = false;
        settings.is_searched = true;
        localStorage.setItem("settings", JSON.stringify(settings));
    }
    else if (settings.is_searched)
    {
        settings.saved_items = [];
        settings.is_searched = false;
        localStorage.setItem("settings", JSON.stringify(settings));
    }
    else
    {
        localStorage.clear();
    }
    _settings = null;
}
function ui_values()
{
    picker.valueAsDate = new Date(getCurrentDate_1());    
    today.innerHTML = getCurrentDate();
    search_value.value = settings.search_value;
    switch (settings.sort_by)
    {
        case "id":
            by_id.style.backgroundColor = "var(--green)";
            break;
        case "-id":
            by_id.style.backgroundColor = "var(--green)";
            by_id.innerText = "Id ⬆";
            break;
        case "content":
            alphabetical.style.backgroundColor = "var(--green)";
            break;
        case "-content":
            alphabetical.style.backgroundColor = "var(--green)";
            alphabetical.innerText = "Alphabetical ⬆";
            break;
        case "target_date":
            created_date.style.backgroundColor = "var(--green)";
            break;
        case "-target_date":
            created_date.style.backgroundColor = "var(--green)";
            created_date.innerText = "Target Date ⬆";
            break;
    }
    switch (settings.filter_by)
    {
        case "none":
            nones.style.backgroundColor = "var(--green)";
            break;
        case "favorites":
            favorites.style.backgroundColor = "var(--green)";
            break;
        case "-favorites":
            favorites.style.backgroundColor = "var(--green)";
            favorites.innerText = "Unfoavorites";
            break;
        case "completed":
            completed.style.backgroundColor = "var(--green)";
            break;
        case "-completed":
            completed.style.backgroundColor = "var(--green)";
            completed.innerText = "Incompleted";
            break;
    }
}

// Functions
function on_filter(val)
{
    if (settings.filter_by == val && val != "none")
    { val = "-" + val; }
	settings.filter_by = val;
	localStorage.setItem("settings", JSON.stringify(settings));
	filter_by.value = settings.filter_by;
	post_form.submit();
}
function on_sort(val)
{
    if (settings.sort_by == val)
    { val = "-" + val; }
    settings.sort_by = val;
    localStorage.setItem("settings", JSON.stringify(settings));
    sort_by.value = settings.sort_by;
    filter_by.value = settings.filter_by;
    post_form.submit();
}
function on_load_more()
{
    settings.saved_items = current_items_list;
    settings.is_loaded = true;
    localStorage.setItem("settings", JSON.stringify(settings));
    search_value.value = settings.search_value;
    load_value.value = settings.saved_items.length;
    sort_by.value = settings.sort_by;
    filter_by.value = settings.sort_by;
    post_form.submit();
}
function on_search()
{
    settings.search_value = search_value.value;
    settings.is_searched = true;
    localStorage.setItem("settings", JSON.stringify(settings));
    sort_by.value = settings.sort_by;
    filter_by.value = settings.filter_by;
    post_form.submit();
}

// Static Functions
function getCurrentDate()
{
    var date = new Date();
    var dd = String(date.getDate()).padStart(2, '0');
    var mm = String(date.getMonth() + 1).padStart(2, '0'); //January is 0!
    var yyyy = date.getFullYear();
    var today = mm + '/' + dd + '/' + yyyy;
    return today;
}
function getCurrentDate_1()
{
    var date = new Date();
    var dd = String(date.getDate()+1).padStart(2, '0');
    var mm = String(date.getMonth() + 1).padStart(2, '0'); //January is 0!
    var yyyy = date.getFullYear();
    var today = mm + '/' + dd + '/' + yyyy;
    return today;
}

// On Click Events
function on_menu_click()
{
    const nav_a = nav.getElementsByTagName("a");
    if (nav.style.width == "20vw")
    {
        nav.style.width = "8.5vw";
        main_obj.style.marginLeft = "8.5vw";
        for (i=0; i<nav_a.length; i++)
        { nav_a[i].style.fontSize = 0; }
    }
    else
    {
        for (i=0; i<nav_a.length; i++)
        { nav_a[i].style.fontSize = "1vw"; }
        nav.style.width = "20vw";
        main_obj.style.marginLeft = "20vw";
    }
    menu.style.fontSize = "3vw";
}
function on_menu_item_click(item_obj)
{
    active = document.getElementsByClassName("active");
    active[0].className = "";
    item_obj.className = "active"
}
function on_item_click(item_obj)
{
    if (!is_active)
    {
        setTimeout(function()
        {
            if (item_obj.style.visibility == "visible")
            {
                item_obj.style.visibility = "hidden";
                item_obj.style.opacity = 0;
            }
            else
            {
                item_obj.style.visibility = "visible";
                item_obj.style.opacity = 1;
                is_active = true;
            }
        });
    }
}

// Jquery on click event for mouse
$(document).on("click", function() 
{
    if (is_active)
    {
        is_active = false;
        sort_options.style.visibility = "hidden";
        sort_options.style.opacity = 0;
        filter_options.style.visibility = "hidden";
        filter_options.style.opacity = 0;
        const result = document.getElementsByClassName('options');
        for (i=0; i<result.length; i++)
        {
            result[i].style.visibility = "hidden";
            result[i].style.opacity = 0;
        }
    }
});