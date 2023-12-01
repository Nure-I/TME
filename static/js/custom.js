$(document).ready(function () {
  $(".increement-btn").click(function (e) {
    e.preventDefault();
    var inc_value = $(this).closest(".a").find(".qty-input").val();
    var value = parseInt(inc_value, 10);
    value = isNaN(value) ? 0 : value;

    value++;
    $(this).closest(".a").find(".qty-input").val(value);
  });

  $(".decreement-btn").click(function (e) {
    e.preventDefault();
    var inc_value = $(this).closest(".a").find(".qty-input").val();
    var value = parseInt(inc_value, 10);
    value = isNaN(value) ? 0 : value;
    if (value > 1) {
      value--;
      $(this).closest(".a").find(".qty-input").val(value);
    }
  });

  $(".add_to_list").click(function (e) {
    e.preventDefault();
    var product_id = $(this).closest(".a").find(".product_id").val();
    var quantity = $(this).closest(".a").find(".qty-input").val();
    var unit = $(this).closest(".a").find(".unit").val();
    var grade = $(this).closest(".a").find(".grade").val();
    var page_number = $(this).closest(".a").find(".page_number").val();
    var unit_price = $(this).closest(".a").find(".unit_price").val();
    var product_type = $(this).closest(".a").find(".product_type").val();
    var token = $("input[name=csrfmiddlewaretoken]").val();
    console.log(product_id, quantity, product_type,page_number);
    $.ajax({
      method: "POST",
      url: "/requests/add_to_list",
      data: {
        product_id: product_id,
        quantity: quantity,
        product_type: product_type,
        unit: unit,
        grade: grade,
        page_number: page_number,
        unit_price: unit_price,
        csrfmiddlewaretoken: token,
      },

      success: function (response) {
        console.log(response);
        alertify.success(response.status);
      },
    });
  });

  $(".change_quantity").click(function (e) {
    e.preventDefault();
    var product_id = $(this).closest(".a").find(".product_id").val();
    var quantity = $(this).closest(".a").find(".qty-input").val();
    var price = $(this).closest(".aa").find(".price-input").val();
    console.log("sfsdf");
    var token = $("input[name=csrfmiddlewaretoken]").val();
    $.ajax({
      method: "POST",
      url: "/requests/update_list",
      data: {
        product_id: product_id,
        quantity: quantity,
        price: price,

        csrfmiddlewaretoken: token,
      },

      success: function (response) {
        console.log(response);
      },
    });
  });

  // $(".updaddte").click(function (e) {
  //   //Hide the menus if visible
  //   e.preventDefault();

  //   var product_id = $(this).closest(".a").find(".product_id").val();
  //   var price = $(this).closest(".a").find(".price-input").val();
  //   var token = $("input[name=csrfmiddlewaretoken]").val();
  //   $.ajax({
  //     method: "POST",
  //     url: "/requests/update_list_price",
  //     data: {
  //       product_id: product_id,
  //       price: price,
  //       csrfmiddlewaretoken: token,
  //     },

  //     success: function (response) {
  //       console.log(response);
  //     },
  //   });
  // });

  $(".remove_product").click(function (e) {
    //Hide the menus if visible
    e.preventDefault();

    var product_id = $(this).closest(".a").find(".product_id").val();
    var token = $("input[name=csrfmiddlewaretoken]").val();
    $.ajax({
      method: "POST",
      url: "/requests/remove_product",
      data: {
        product_id: product_id,
        csrfmiddlewaretoken: token,
      },

      success: function (response) {
        alertify.success(response.status);
        $('.list_data').load(location.href + " .list_data");
        console.log("adasdcasdcasdcadsc")
      }
    });
  });
});
