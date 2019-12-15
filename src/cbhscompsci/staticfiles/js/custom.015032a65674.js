$(document).ready(function($) {
    $(".table-row").click(function() {
        window.location = $(this).data("href");
    });
});
// Gallery start
$( function() {
  var $grid = $('.grid').isotope({
    itemSelector: 'article'
  });

  // filter buttons
  $('.filters-button-group').on( 'click', 'button', function() {
    var filterValue = $( this ).attr('data-filter');
    $grid.isotope({ filter: filterValue });
  });
  $('.button-group').each( function( i, buttonGroup ) {
    var $buttonGroup = $( buttonGroup );
    $buttonGroup.on( 'click', 'button', function() {
      $buttonGroup.find('.is-checked').removeClass('is-checked');
      $( this ).addClass('is-checked');
    });
  });
});

// debounce so filtering doesn't happen every millisecond
function debounce( fn, threshold ) {
  var timeout;
  return function debounced() {
    if ( timeout ) {
      clearTimeout( timeout );
    }
    function delayed() {
      fn();
      timeout = null;
    }
    timeout = setTimeout( delayed, threshold || 100 );
  }
}

$(window).bind("load", function() {
  $('#all').click();
});
// Gallery end

// Breakdown begin

var __OBJECTS = [];
$(".lineage").each(function(index){
  $( this ).addClass("hidden")
  __OBJECTS.push( $(this) );
});
var seconds = 0;

function changeLineage(){
  var $object = __OBJECTS.shift();
  $object.addClass("animated fadeInUp").removeClass("lineage hidden")
  if(__OBJECTS.length){
    setTimeout(changeLineage, 100)
  }
}
$(document).ready(changeLineage());
// Brakdown endblock

// Counting animation

// header
// <span class="sr-only">Home</span>
var gallery = true
if (document.URL.includes("points/entry")) {
  document.getElementById('entryPage').innerHTML='<li class="nav-item active"><a class="nav-link" href="/points/entry">Entry Form</a></li>';
} else if (document.URL.includes("points")) {
  document.getElementById('pointsPage').innerHTML='<li class="nav-item active"><a class="nav-link" href="/points/">View Points</a></li>';
} else if (document.URL.includes("gallery")) {
  gallery = false
  console.log(gallery)
} else if (document.URL.includes("meetings")) {
  document.getElementById('meetingsPage').innerHTML='<li class="nav-item active"><a class="nav-link" href="/meetings/">Meetings</a></li>'
} else {
  document.getElementById('homePage').innerHTML='<li class="nav-item active"><a class="nav-link" href="/">Home</a></li>';
}

if (gallery) {
  document.getElementById('galleryPage').innerHTML='<li class="nav-item"><a class="nav-link" href="/gallery/">Gallery</a></li>'
}
