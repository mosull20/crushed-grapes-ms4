// Stripe - code taken from Boutique Ado videos

let stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
let clientSecret = $('#id_client_secret').text().slice(1, -1);
let stripe = Stripe(stripePublicKey);
let elements = stripe.elements({
    // solution to use google font in stripe card element found in stack overflow 
    // https://stackoverflow.com/questions/44915511/stripe-elements-google-web-font-not-working/47468682
    fonts: [
      {
        cssSrc: 'https://fonts.googleapis.com/css?family=Reem+Kufi:wght@400;500;600;700'
      }
    ]
  });
let style = {
    base: {
        color: '#000',
        fontFamily: '"Reem Kufi", sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};
let card = elements.create('card', {style: style});
card.mount('#card-element');

// Handle realtime validation errors on the card element
card.addEventListener('change', function (event) {
  let errorDiv = document.getElementById('card-errors');
  if (event.error) {
    let html = `
        <span class="icon mr-2" role="alert">
          <i class="fas fa-times"></i>
        </span>
        <span>${event.error.message}</span>
        `;
    $(errorDiv).html(html);
  } else {
      errorDiv.textContent = '';
  }
});

// Handle submit payment to Stripe

let form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
  ev.preventDefault();
  card.update({ 'disabled': true});
  $('#payment-button').attr('disabled', true);
  stripe.confirmCardPayment(clientSecret, {
    payment_method: {
      card: card,
    }
  }).then(function(result) {
    if (result.error) {
        let errorDiv = document.getElementById('card-errors');
        let html = `
          <span class="icon mr-2" role="alert">
            <i class="fas fa-times"></i>
          </span>
          <span>${result.error.message}</span>`;
        $(errorDiv).html(html);
        card.update({ 'disabled': false});
        $('#payment-button').attr('disabled', false);
    } else {
      if (result.paymentIntent.status === 'succeeded') {
        form.submit();
      }
    }
  });
});
