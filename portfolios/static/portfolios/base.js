const btnOpen = document.querySelector('#btnOpen');
const btnClose = document.querySelector('#btnClose');
const topnavMenu = document.querySelector('#topNavMenu');
const media = window.matchMedia('(width < 640px)');


const openMobileMenu = () => {
    btnOpen.setAttribute('aria-expanded', 'true');
    topnavMenu.removeAttribute('style');
};


const closeMobileMenu = () => {
    btnOpen.setAttribute('aria-expanded', 'false');
};


const setupTopNav = (e) => {
    if (e.matches) {
        console.log('is mobile.');
        topnavMenu.style.transition = 'none';
        topnavMenu.style.overflowY = 'hidden';
    } else {
        console.log('is desktop');
        closeMobileMenu();
    }
}
setupTopNav(media);


btnOpen.addEventListener('click', openMobileMenu);
btnClose.addEventListener('click', closeMobileMenu);
media.addEventListener('change', (e) => {
    setupTopNav(e);
});