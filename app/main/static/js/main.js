$(document).ready(function() {

  // ON LOAD

  // This initializes the navigation tooltips
  $('[data-toggle="tooltip"]').tooltip()

  // This initializes the Date picker
  $(function () {
    var date = $("[name='date']").val()
    
    $("#datetimepicker").datetimepicker({
      date: new Date(date),
      format: 'DD/MM/YYYY',
    });

    $("[name='date']").val(date)
  });


  // EVENTS
  
  // This switches the chevron on collapse open/close
  $('.chevron').on('click', function (event) {
      $(this).children('.fas').toggleClass('fa-chevron-down fa-chevron-up');
  })

  // Fetches the relevant data when the modal is triggered
  $('#deleteModal').on('show.bs.modal', function (event) {
    var self  = $(this);
    var pk    = $(event.relatedTarget).data('id');
    var href = self.find('#delete a').attr('href')
    var splitHref = href.split("/")
    var replace = self.find('#delete a').attr('href').replace(splitHref[3], pk);

    self.find('#delete a').attr('href', replace);
  })

  // This manages the functions when the formset button add/delete is selected
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

  // This auto completes the end time field by +1 hour
  $(".start-time").on("change", function (event) {
    var id    = $(this).attr('id');
    var time  = moment(event.target.value, 'H:mm').add('1', 'hours').format('HH:mm');

    if(time != "Invalid date") {
      id = '#' + id.replace('start_time', 'end_time');
      $(id).val(time);
    }
  });

  // This manages the hidden formset fields to match the visible fields
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

  // This manages the select options to display the correct selected option
  $("select").on("change", function (event) {
    var self = $(this)
    var value = self.val();

    self.find('option').removeAttr('selected'),
    self.find("option[value='" + value + "']").attr('selected', 'selected')
  });

  // FUNCTIONS

  // This function extracts the prefix from the formset field
  function prefix( formset ) {
    var prefix = formset.children('input:first');

    prefix     = prefix[0].name.split('-');
    prefix     = prefix[0];

    return prefix;
  }

  // This function clones additional instances of the formset
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

    newElement.find('.remove-form').attr('href', '').attr('data-csrf', '');

    total++;
    $('#id_' + prefix + '-TOTAL_FORMS').val(total);
    
    if(hidden) {
      newElement.addClass('hidden');
      return newElement
    } else {
      $(selector).after(newElement);
    }
    
  }

  // This function deletes the relevant instance of the formset
  function deleteForm(self, formset, prefix) {
    var total = parseInt($('#id_' + prefix + '-TOTAL_FORMS').val());
    
    if (total > 1) {

      if (self.attr("href") && self.data("csrf")) {
        
        ajaxDeleteCustomerStatus(self);

      }

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

  // This function updates the formset index
  function updateElementIndex(el, prefix, ndx) {
    var id_regex = new RegExp('(' + prefix + '-\\d+)');
    var replacement = prefix + '-' + ndx;
    if ($(el).attr("for")) $(el).attr("for", $(el).attr("for").replace(id_regex, replacement));
    if (el.id) el.id = el.id.replace(id_regex, replacement);
    if (el.name) el.name = el.name.replace(id_regex, replacement);
  }

  // This Ajax call posts to the customer status delete url
  function ajaxDeleteCustomerStatus(self) {

    $.ajax({
      url: `${self.attr("href")}`,
      type: "POST",
      data: {
        csrfmiddlewaretoken: self.data("csrf"),
      },
      error: function(error) {
        console.log(error);
      }
    });

  }

});