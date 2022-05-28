document.addEventListener('DOMContentLoaded', function() {
  const sidenav = document.querySelectorAll('.sidenav');
  M.Sidenav.init(sidenav);

  const rentIntro = document.getElementById('rent-intro-toggle')
  if (rentIntro) rentIntro.addEventListener('click', toggleRentIntro);
});

function toggleRentIntro() {
  let e = document.getElementById("rent-intro");
  e.classList.toggle('hide')
}
