// DEFAULT VARIABLES
var is_active = false;

// MAIN 
Main();
function Main()
{
    picker.valueAsDate = new Date(getCurrentDate_1());    
    today.innerHTML = getCurrentDate();
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
        nav.style.width = "5.5vw";
        main_obj.style.marginLeft = "5.5vw";
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
    menu.style.fontSize = "2vw";
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