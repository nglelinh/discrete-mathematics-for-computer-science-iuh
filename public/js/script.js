(function(document) {
  var toggle = document.querySelector('.sidebar-toggle');
  var sidebar = document.querySelector('#sidebar');
  var checkbox = document.querySelector('#sidebar-checkbox');

  if (window.innerWidth > 1480)
    checkbox.checked = true;

  var activeLesson = sidebar.querySelector('.sidebar-lesson.active');
  if (activeLesson) {
    var lessonRect = activeLesson.getBoundingClientRect();
    var sideRect = sidebar.getBoundingClientRect();
    sidebar.scrollTop += lessonRect.top - sideRect.top - Math.min(sideRect.height / 3, 120);
  }

  document.addEventListener('click', function(e) {
    var target = e.target;

    if(!checkbox.checked ||
       sidebar.contains(target) ||
       (target === checkbox || target === toggle)) return;

    checkbox.checked = false;
  }, false);
})(document);
