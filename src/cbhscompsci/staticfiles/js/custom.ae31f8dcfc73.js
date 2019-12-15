$(document).ready(function($) {
    $(".table-row").click(function() {
        window.location = $(this).data("href");
    });
});

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

// Gallery start *************************************************************

// external js: isotope.pkgd.js


// init Isotope
var $grid = $('.grid').isotope({
  itemSelector: '.element-item',
  layoutMode: 'fitRows',
});

// filter functions
var filterFns = {
  // show if number is greater than 50
  numberGreaterThan50: function() {
    var number = $(this).find('.number').text();
    return parseInt( number, 10 ) > 50;
  },
  // show if name ends with -ium
  ium: function() {
    var name = $(this).find('.name').text();
    return name.match( /ium$/ );
  }
};

// bind filter button click
$('#filters').on( 'click', 'button', function() {
  var filterValue = $( this ).attr('data-filter');
  // use filterFn if matches value
  filterValue = filterFns[ filterValue ] || filterValue;
  $grid.isotope({ filter: filterValue });
});

// change is-checked class on buttons
$('.button-group').each( function( i, buttonGroup ) {
  var $buttonGroup = $( buttonGroup );
  $buttonGroup.on( 'click', 'button', function() {
    $buttonGroup.find('.is-checked').removeClass('is-checked');
    $( this ).addClass('is-checked');
  });
});


// GALLERY END ****************************************************************




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

// Table search
function searchTable() {
  // Declare variables
  var input, filter, table, tr, td, td2, i, txtValue;
  input = $('.search')[0];
  filter = input.value.toUpperCase();
  table = $('#studentPoints')[0];
  tr = table.getElementsByTagName("tr");

  // Loop through all table rows, and hide those who don't match the search query
  for (i = 0; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td")[1];
    td2 = tr[i].getElementsByTagName("td")[2];

    if (td) {
      txtValue = td.innerText + " " + td2.innerText;
      console.log(txtValue)
      if (txtValue.toUpperCase().indexOf(filter) > -1) {
        tr[i].style.display = "";
      } else {
        tr[i].style.display = "none";
      }
    }
  }
}
