$(document).ready(function() {
    $('#example2').on("click",".modalHardware",function() {
      var id = $(this).data('id');
      var serial_no = $(this).data('serial_no');
      var display_name = $(this).data('display_name');
      var stock_room = $(this).data('stock_room');

      // Set the data in the modal fields
      $('#item_id').val(id);
      $('#serial_no').val(serial_no);
      $('#display_name').val(display_name);

      $('#editItemForm').attr('action', '{% url "edit_item" 0 %}'.replace('0', id));

        $.ajax({
              type: 'GET',
              url: '/get_all_stockroom/',  // Use the correct URL for fetching all locations
              success: function(data) {
                  var stockRoomSelect = $('.stock_room');
                  stockRoomSelect.empty();
                  
                  if (data.length > 0) {
                      for (var i = 0; i < data.length; i++) {
                          stockRoomSelect.append($('<option>', {
                              value: data[i],
                              text: data[i]
                          }));
                      }
                  } else {
                      stockRoomSelect.append($('<option>', {
                          value: '',
                          text: 'No stock rooms available'
                      }));
                  }
                  
                  $('#hardwareModal').modal('show');
              },
              error: function() {
                  console.log('Error fetching locations.');
              }
          });


  
    });
  });