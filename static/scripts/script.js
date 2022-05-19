document.addEventListener('DOMContentLoaded', function() {
  const sidenav = document.querySelectorAll('.sidenav');
  M.Sidenav.init(sidenav);

  document.getElementById('rent-intro-toggle').addEventListener('click', toggleRentIntro);
});

function toggleRentIntro() {
  let e = document.getElementById("rent-intro");
  e.classList.toggle('hide')
}
