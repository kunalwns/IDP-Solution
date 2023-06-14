function getPageList(totalPages, page, maxLength) {
    if (maxLength < 5) throw "maxLength must be at least 5";

    function range(start, end) {
        return Array.from(Array(end - start + 1), (_, i) => i + start);
    }

    var sideWidth = maxLength < 9 ? 1 : 2;
    var leftWidth = (maxLength - sideWidth*2 - 3) >> 1;
    var rightWidth = (maxLength - sideWidth*2 - 2) >> 1;
	
	
    if (totalPages <= maxLength) {
        // no breaks in list
        return range(1, totalPages);
    }
    if (page <= maxLength - sideWidth - 1 - rightWidth) {
        // no break on left of page
        return range(1, maxLength - sideWidth - 1)
            .concat(0, range(totalPages - sideWidth + 1, totalPages));
    }
    if (page >= totalPages - sideWidth - 1 - rightWidth) {
        // no break on right of page
        return range(1, sideWidth)
            .concat(0, range(totalPages - sideWidth - 1 - rightWidth - leftWidth, totalPages));
    }
    // Breaks on both sides
	
    return range(1, sideWidth)
        .concat(0, range(page - leftWidth, page + rightWidth),
                0, range(totalPages - sideWidth + 1, totalPages));
}

$(function () {
    // Number of items and limits the number of items per page
    var numberOfItems = $("#jar .content").length;
    var limitPerPage = 1;
    var totalPages = Math.ceil(numberOfItems / limitPerPage);
    var paginationSize = 7; 
    var currentPage;

    function showPage(whichPage) {
		if(whichPage == totalPages){
				$('.billing').removeAttr("disabled").addClass('goforspliting');
                $('.goforspliting').click(function(){
                    setTimeout(function() {
                        $('.billing').attr('disabled', 'disabled').removeClass('goforspliting');
                        // if($('.billing').hasClass('Treatmentandbilling')){
                        //     $('.billing').removeClass('Treatmentandbilling')
                        // }
                    },1000);
                })
             
		}else{
			$('.billing').prop('disabled', true);
			$('.billing').removeClass('goforspliting');
            $(".right-content").removeClass('hideelement');
            $(".spliting").addClass('hideelement');  
		}
        $(".goforspliting").click(function(){
            $("html, body").animate({ scrollTop: 0 }, "fast");
            $(".spliting").removeClass('hideelement');
            $(".right-content").addClass('hideelement');
        })
        if (whichPage < 1 || whichPage > totalPages) return false;
        currentPage = whichPage;
        $("#jar .content").hide()
            .slice((currentPage-1) * limitPerPage, 
                    currentPage * limitPerPage).show();
        // Replace the navigation items (not prev/next):            
        $(".pagination li").slice(1, -1).remove();
        getPageList(totalPages, currentPage, paginationSize).forEach( item => {
            $("<li>").addClass("page-item")
                     .addClass(item ? "current-page" : "disabled")
                     .toggleClass("active", item === currentPage).append(
                $("<a>").addClass("page-link").attr({
                    href: "javascript:void(0)"}).text(item || "...")
            ).insertBefore("#next-page");
        });
        // Disable prev/next when at first/last page:
        $("#previous-page").toggleClass("disabled", currentPage === 1);
        $("#next-page").toggleClass("disabled", currentPage === totalPages);
        return true;
    }

    // Include the prev/next buttons:
    $(".pagination").append(
        $("<li>").addClass("page-item").attr({ id: "previous-page" }).append(
            $("<a>").addClass("page-link").attr({
                href: "javascript:void(0)"}).text("Prev")
        ),
        $("<li>").addClass("page-item").attr({ id: "next-page" }).append(
            $("<a>").addClass("page-link").attr({
                href: "javascript:void(0)"}).text("Next")
        )
    );
    // Show the page links
    $("#jar").show();
    showPage(1);

    // Use event delegation, as these items are recreated later    
    $(document).on("click", ".pagination li.current-page:not(.active)", function () {
        return showPage(+$(this).text());
    });
    $("#next-page").on("click", function () {
        return showPage(currentPage+1);
    });

    $("#previous-page").on("click", function () {
        return showPage(currentPage-1);
    });
	
	// Set current Date
		var now = new Date();

		var day = ("0" + now.getDate()).slice(-2);
		var month = ("0" + (now.getMonth() + 1)).slice(-2);

		var today = now.getFullYear()+"-"+(month)+"-"+(day) ;

		$('.datePicker').val(today);
});
// increment and decrement 

function increaseValue() {
  var value = parseInt(document.getElementById('numberincrement').value, 10);
  value = isNaN(value) ? 0 : value;
  value = value + 10;
  document.getElementById('numberincrement').value = value;
  $(".content").each(function () {
	  if($(this).hasClass('reduceimage')){
		   $(this).removeClass('reduceimage')
		}
		if($(this).hasClass('zoomimage')){
		   $(this).removeClass('zoomimage')
		}
        if ($(this).css("display") == "none") { $(this).addClass("reduceimage"); }
        if ($(this).css("display") == "block") { $(this).addClass("zoomimage"); }
    })
}

function decreaseValue() {
  var value = parseInt(document.getElementById('numberincrement').value, 10);
  value = isNaN(value) ? 0 : value;
  value < 1 ? value = 1 : '';
  value = value - 10;
  document.getElementById('numberincrement').value = value;
  $(".content").each(function () {
	  if($(this).hasClass('reduceimage')){
		   $(this).removeClass('reduceimage')
		}
		if($(this).hasClass('zoomimage')){
		   $(this).removeClass('zoomimage')
		}
        if ($(this).css("display") == "none") { $(this).addClass("reduceimage"); }
        if ($(this).css("display") == "block") { $(this).addClass("zoomimage"); }
    })
}
$(function () {
    var accordinlength = $('.accordion-item').length ;
    $('.totalaccordion').text(accordinlength)
})

$(function () {
    $('.getsplitlastelement .accordion-item').click(function(){
        if($(this).is(':last-child')){
            $('.billing').removeAttr("disabled").addClass('Treatmentandbilling');
            $(this).removeClass('goforspliting');
        }
    })
    // $('.Treatmentandbilling').click(function(){
    //     $('.Treatmentandbilling').removeClass('hideelement')
    //     $('.spliting').addClass('hideelement');
    // })

});