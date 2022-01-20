// Stripe - code taken from Boutique Ado videos

let stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
let client_secret = $('#id_client_secret').text().slice(1, -1);
let stripe = Stripe(stripe_public_key);
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