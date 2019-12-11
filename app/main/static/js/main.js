$(document).ready(function(){

  $('#exampleModal').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget)
    var pk = button.data('id')
    var modal = $(this)
    var href = modal.find('#delete a').attr('href').replace('0', pk)
    modal.find('#delete a').attr('href', href)
  })

  $('.formset').on('click', '.add-form', function(e) {
    e.preventDefault();
    var self        = $(this);
    var formset     = self.parents('.formset');
    var lastForm    = formset.children('.formset-form:last');

    cloneMore(lastForm, prefix(formset));
    return false;
  });

  $('.formset').on('click', '.remove-form', function(e) {
    var self    = $(this);
    var formset = self.parents('.formset');
    
    deleteForm(self, formset, prefix(formset));
    return false;
  });

  function prefix(formset) {
    var hiddenInput = formset.children('input:first');
    var splitName   = hiddenInput[0].name.split('-');
    var prefix      = splitName[0];

    return prefix;
  }

  function cloneMore(selector, prefix) {
    var newElement = $(selector).clone(true);
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
  }

  function deleteForm(self, formset, prefix) {
    var total = parseInt($('#id_' + prefix + '-TOTAL_FORMS').val());
    
    if (total > 1) {
        self.parents('.formset-form').remove();
        var forms = formset.children('.formset-form');
        
        $('#id_' + prefix + '-TOTAL_FORMS').val(forms.length);
        for (var i=0, formCount=forms.length; i<formCount; i++) {
            $(forms.get(i)).find(':input').each(function() {
              updateElementIndex(this, prefix, i);
            });
        }
    }
    return false;
  }

  function updateElementIndex(el, prefix, ndx) {
    var id_regex = new RegExp('(' + prefix + '-\\d+)');
    var replacement = prefix + '-' + ndx;
    if ($(el).attr("for")) $(el).attr("for", $(el).attr("for").replace(id_regex, replacement));
    if (el.id) el.id = el.id.replace(id_regex, replacement);
    if (el.name) el.name = el.name.replace(id_regex, replacement);
  }

  $('.date').datetimepicker({
      format: 'YYYY-MM-DD'
  });
  $('.time').datetimepicker({
    format: 'H:mm',
    useCurrent: true,
    disabled: true,
  });








  $("#id_starttime").on("change.datetimepicker", function (e) {
      var time = moment(e.target.value, 'H:mm').add('1', 'hours').format('HH:mm');
      $('#id_endtime').val(time);
      console.log("change");
  });

  $("#id_starttime").on("input", function (e) {
    var time = moment(e.target.value, 'H:mm').add('1', 'hours').format('HH:mm');
    $('#id_endtime').val(time);
    console.log("input");
  });

})