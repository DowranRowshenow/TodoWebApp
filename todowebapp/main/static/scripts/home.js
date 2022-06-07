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
        console.log("Cache Settings");
        settings = _settings;
    }
    else
    { 
        console.log("Create Settings");
        localStorage.setItem("settings", JSON.stringify(settings));
    }
    console.log("\nSETTINGS: " + settings);
    console.log("sort_by: " + settings.sort_by);
    console.log("filter_by: " + settings.filter_by);
    console.log("is_loaded: " + settings.is_loaded);
    console.log("is_searched: " + settings.is_searched);
    console.log("search_value: " + settings.search_value);
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
        console.log("First Open()");
    }
    _settings = null;
    console.log("\nSETTINGS: " + settings);
    console.log("sort_by: " + settings.sort_by);
    console.log("filter_by: " + settings.filter_by);
    console.log("is_loaded: " + settings.is_loaded);
    console.log("is_searched: " + settings.is_searched);
    console.log("search_value: " + settings.search_value);
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

// Update Item List
function update_items(update_items)
{
    current_items_list = update_items;
    for (i=0; i<current_items.length; i++)
    { current_items[i].remove(); }
    for (i=0; i<update_items.length; i++)
    {
        let item = document.createElement('div');
        item.id = "item_" + update_items[i].id;
        item.className = "item";
        container.appendChild(item);

        let input = document.createElement('input');
        if (update_items[i].is_completed == "True")
        { input.checked = true }
        else
        { input.checked = false }
        input.className = "checkbox";
        input.type = "checkbox";
        input.onclick = function(){return false};
        item.appendChild(input);

        let span = document.createElement('span');
        if (update_items[i].is_favorite == "True")
        { span.className = "fa fa-star checked"; }
        else
        { span.className = "fa fa-star"; }
        item.appendChild(span);
    
        let a = document.createElement('a');
        a.innerText = update_items[i].content;
        item.appendChild(a);

        let ad = document.createElement('a');
        ad.className = "created";
        ad.innerText = update_items[i].target_date;
        item.appendChild(ad);

        let options = document.createElement('div');
        options.id = "options_" + update_items[i].id;
        options.className = "options";
        item.appendChild(options);
        item.setAttribute("onclick", "on_item_click(" + options.id + ");");
    
        let favorite = document.createElement('a');
        favorite.className = "favorite";
        favorite.href = "favorite_item/" + update_items[i].id;
        if (update_items[i].is_favorite == "True") 
        { favorite.innerText = "Mark as Unfavorite";}
        else 
        { favorite.innerText = "Mark as Favorite"; }
        options.appendChild(favorite);

        let complete = document.createElement('a');
        complete.className = "complete";
        complete.href = "complete_item/" + update_items[i].id;
        if (update_items[i].is_completed == "True") 
        { complete.innerText = "Mark as Incomplete";}
        else 
        { complete.innerText = "Mark as Complete"; }
        options.appendChild(complete);
    
        let deleted = document.createElement('a');
        deleted.className = "delete";
        deleted.href = "delete_item/" + update_items[i].id;
        if (update_items[i].is_deleted == "True") 
        { deleted.innerText = "Delete Permanently";}
        else 
        { deleted.innerText = "Delete"; }
        options.appendChild(deleted);
        current_items.push(item);
    }
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
function dynamicSort(property) 
{
    var sortOrder = 1;
    if(property[0] === "-") 
    {
        sortOrder = -1;
        property = property.substr(1);
    }
    return function (a,b) 
    {
        var result = (a[property].toUpperCase() < b[property].toUpperCase()) ? -1 : (a[property].toUpperCase() > b[property].toUpperCase()) ? 1 : 0;
        return result * sortOrder;
    }
}
function compare(a, b) 
{
    if ( a.content.toUpperCase() < b.content.toUpperCase() )
    { return -1; }
    if ( a.content.toUpperCase() > b.content.toUpperCase() )
    { return 1; }
    return 0;
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
        { nav_a[i].style.fontSize = "1.5vw"; }
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