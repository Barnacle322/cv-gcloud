// check for saved 'lightMode' in localStorage
let lightMode = localStorage.getItem('lightMode');

console.log(localStorage)

const enableLightMode = () => {

    var body = document.getElementsByClassName('body')[0];
    body.classList.add("light");
    var cv = document.getElementsByClassName('cv')[0];
    cv.classList.add("cv-light");
    try {
        var langswitch = document.getElementsByClassName('langswitch');
        (Array.from(langswitch)).forEach(element => {
            element.classList.add("langswitch-light");
        });
    } catch (error) {
        //pass
    }

    try {
        var linedivider = document.getElementsByClassName('linedivider');
        (Array.from(linedivider)).forEach(element => {
            element.classList.add("linedivider-light");
        });
    } catch (error) {
        //pass
    }

    try {
        var contacthref = document.getElementsByClassName('contact-href');
        (Array.from(contacthref)).forEach(element => {
            element.classList.add("contact-href-light");
        });
    } catch (error) {
        //pass
    }

    localStorage.setItem('lightMode', 'enabled');
}

const disableLightMode = () => {
    var body = document.getElementsByClassName('body')[0];
    body.classList.remove("light");
    var cv = document.getElementsByClassName('cv')[0];
    cv.classList.remove("cv-light");
    try {
        var langswitch = document.getElementsByClassName('langswitch');
        (Array.from(langswitch)).forEach(element => {
            element.classList.remove("langswitch-light");
        });
    } catch (error) {
        //pass
    }

    try {
        var linedivider = document.getElementsByClassName('linedivider');
        (Array.from(linedivider)).forEach(element => {
            element.classList.remove("linedivider-light");
        });
    } catch (error) {
        //pass
    }

    try {
        var contacthref = document.getElementsByClassName('contact-href');
        (Array.from(contacthref)).forEach(element => {
            element.classList.remove("contact-href-light");
        });
    } catch (error) {
        //pass
    }
    localStorage.setItem('lightMode', null);
}

// If the user already visited and enabled lightMode
// start things off with it on
if (lightMode === 'enabled') {
    // console.log(lightMode);
    var button = document.getElementById('switch-button');
    button.checked = true;
    enableLightMode();

}

function myFunction() {
    lightMode = localStorage.getItem('lightMode');
    // console.log(lightMode);

    // if it not current enabled, enable it
    if (lightMode !== 'enabled') {
        enableLightMode();
        // if it has been enabled, turn it off  
    } else {
        disableLightMode();
    }
}