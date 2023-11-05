const sections = document.querySelectorAll("section[id]");

window.addEventListener("scroll", navHighlighter);

function navHighlighter() {

  let scrollY = window.pageYOffset;

  sections.forEach(current => {
    const sectionHeight = current.offsetHeight;
    const sectionTop = (current.getBoundingClientRect().top + window.pageYOffset) - 280;
    sectionId = current.getAttribute("id");

    if (scrollY > sectionTop && scrollY <= sectionTop + sectionHeight) {
      theone = document.querySelector('a.menu_item[href="#' + sectionId + '"]');
      theone.classList.add('active');
    } else {
      document.querySelector('a.menu_item[href="#' + sectionId + '"]').classList.remove('active');
    }
  });
  navScroll(theone);
}
function navScroll(item) {
  const menu = document.getElementById("menu");
  const menu_h = menu.offsetHeight;
  const item_h = item.offsetHeight;
  const item_y = item.offsetTop;
  menu.scrollTop = item_y - (menu_h/2) + (item_h/2);
}


function forceScroll(sectionID) {
  event.preventDefault();
  const section = document.getElementById(sectionID);
  window.scrollTo(0, section.offsetTop);
}

document.querySelector(".menu_button").addEventListener("click", Hide);

function Hide() {
  // document.querySelector(".info").display = "block";
  document.getElementById("main").style.display = "none";
  document.getElementById("body").style.display = "block";

}
document.querySelector("#back").addEventListener("click", Reveal);
function Reveal() {
  document.getElementById("main").style.display = "block";
  document.getElementById("body").style.display = "none";
  document.getElementById("phone").style.display = "none";
  document.getElementById("instagram").style.display = "none";
  document.getElementById("location").style.display = "none";
  document.querySelector(".inview")?.classList.remove("inview");
}
// const SocialLinks = document.querySelectorAll('span.social svg');
//
// SocialLinks.forEach(Sociallink => {
//   Sociallink.addEventListener('click', () => {
//     document.querySelector(".inview")?.classList.remove("inview");
//     Sociallink.classList.add("inview")
//   });
// });
document.querySelector("#insta").addEventListener("click", expand1);
document.querySelector("#loc").addEventListener("click", expand2);
document.querySelector("#phon").addEventListener("click", expand3);


function expand1() {
  const SocialLinks = document.querySelectorAll('span#insta svg');

  SocialLinks.forEach(Sociallink => {
    document.querySelector(".inview")?.classList.remove("inview");
    Sociallink.classList.add("inview")
  });
  document.getElementById("instagram").style.display = "block";
  document.getElementById("location").style.display = "none";
  document.getElementById("phone").style.display = "none";
}
function expand2() {
  const SocialLinks = document.querySelectorAll('span#loc svg');

  SocialLinks.forEach(Sociallink => {
    document.querySelector(".inview")?.classList.remove("inview");
    Sociallink.classList.add("inview")
  });

  document.getElementById("location").style.display = "block";
  document.getElementById("instagram").style.display = "none";
  document.getElementById("phone").style.display = "none";
}
function expand3() {
  const SocialLinks = document.querySelectorAll('span#phon svg');

  SocialLinks.forEach(Sociallink => {
    document.querySelector(".inview")?.classList.remove("inview");
    Sociallink.classList.add("inview")
  });

  document.getElementById("phone").style.display = "block";
  document.getElementById("instagram").style.display = "none";
  document.getElementById("location").style.display = "none";
}


