$(document).ready(function() {


  // EVENTS

  $('#deleteModal').on('show.bs.modal', function (event) {
    var self  = $(this);
    var pk    = $(event.relatedTarget).data('id');
    var href  = self.find('#delete a').attr('href').replace('0', pk);

    self.find('#delete a').attr('href', href)
  })

  $('.formset').on('click', '.add-form, .remove-form', function(event) {
    event.preventDefault();
    
    var self        = $(this);
    var formset     = self.parents('.formset');
    
    $(".formset:last").find(".hidden").each(function() {
      self = $(this).find(".remove-form");
      formset = self.parents('.formset');

      deleteForm(self, formset, prefix(formset));
    });

    if(self.hasClass('add-form')) {
      var lastForm = formset.children('.formset-form:last');
      cloneMore(lastForm, prefix(formset), false);
    } else if(self.hasClass('remove-form')) {
      deleteForm(self, formset, prefix(formset));
    }
    
    return false;
  });

  $(".start-time").on("change", function (event) {
    var id    = $(this).attr('id');
    var time  = moment(event.target.value, 'H:mm').add('1', 'hours').format('HH:mm');

    if(time != "Invalid date") {
      id = '#' + id.replace('starttime', 'endtime');
      $(id).val(time);
    }
  });

  $("#submit").on("submit", function (event) {
    var dates = $('.formset:first').find('.formset-form').length - 1;
    var statuses = $('.formset:last').find('.formset-form').length;
    var forms = []
    var factor = (dates * statuses) - statuses
    
    lastFormset = $('.formset:last')
    formsetForms = $('.formset:last .formset-form')

    for (i = 0; i < dates; i++) {
      $(lastFormset).find('.formset-form').each(function() {
        forms.push(cloneMore($(this), prefix(lastFormset), true))
      });
    }

    for (form of forms) {
      $('.formset-form:last').after(form);
    }

  });

  $("select").on("change", function (event) {
    var self = $(this)
    var value = self.val();

    self.find('option').removeAttr('selected'),
    self.find("option[value='" + value + "']").attr('selected', 'selected')
  });

  // FUNCTIONS

  function prefix( formset ) {
    var prefix = formset.children('input:first');

    prefix     = prefix[0].name.split('-');
    prefix     = prefix[0];

    return prefix;
  }

  function cloneMore( selector, prefix, hidden ) {
    var newElement = $(selector).clone(true);
    var total = $('#id_' + prefix + '-TOTAL_FORMS').val();
    
    newElement.find(':input:not([type=button]):not([type=submit]):not([type=reset])').each(function() {
      var self = $(this);
      var i = self.attr('name').split("-");
      var name = self.attr('name').replace('-' + i[1] + '-', '-' + total + '-');
      var id = 'id_' + name;

      self.attr({'name': name, 'id': id});
    });

    total++;
    $('#id_' + prefix + '-TOTAL_FORMS').val(total);
    
    if(hidden) {
      newElement.addClass('hidden');
      return newElement
    } else {
      $(selector).after(newElement);
    }
    
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

});