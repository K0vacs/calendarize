$(document).ready(function(){

  $('#exampleModal').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget)
    var pk = button.data('id')
    var modal = $(this)
    var href = modal.find('#delete a').attr('href').replace('0', pk)
    modal.find('#delete a').attr('href', href)
  })

  $(document).on('click', '.add-service-price', function(e){
    e.preventDefault();
    cloneMore('.formset-form:last', 'form');
    return false;
  });

  $(document).on('click', '.remove-service-price', function(e){
    // e.preventDefault();
    deleteForm('form', $(this));
    return false;
  });

  function cloneMore(selector, prefix) {
    var newElement = $(selector).clone(true);
    // $('.formset').find('.formset-form:last').after(newElement)
    
    var total = $('#id_' + prefix + '-TOTAL_FORMS').val();
    newElement.find(':input:not([type=button]):not([type=submit]):not([type=reset])').each(function() {
      var name = $(this).attr('name').replace('-' + (total-1) + '-', '-' + total + '-');
      var id = 'id_' + name;
      $(this).attr({'name': name, 'id': id}).val('').removeAttr('checked');
    });

    newElement.find('label').each(function() {
        var forValue = $(this).attr('for');
        if (forValue) {
          forValue = forValue.replace('-' + (total-1) + '-', '-' + total + '-');
          $(this).attr({'for': forValue});
        }
    });
    total++;
    $('#id_' + prefix + '-TOTAL_FORMS').val(total);
    $(selector).after(newElement);
    // var conditionRow = $('.form-row:not(:last)');
    // conditionRow.find('.btn.add-form-row')
    // .removeClass('btn-success').addClass('btn-danger')
    // .removeClass('add-form-row').addClass('remove-form-row')
    // .html('<span class="glyphicon glyphicon-minus" aria-hidden="true"></span>');
    // return false;
  }

  function deleteForm(prefix, btn) {
    var total = parseInt($('#id_' + prefix + '-TOTAL_FORMS').val());
    if (total > 1) {
        btn.parents('.formset-form').remove();
        var forms = $('.formset-form');
        $('#id_' + prefix + '-TOTAL_FORMS').val(forms.length);
        for (var i=0, formCount=forms.length; i<formCount; i++) {
            $(forms.get(i)).find(':input').each(function() {
                updateElementIndex(this, prefix, i);
            });
        }
    }
    return false;
  }

})